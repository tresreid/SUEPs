import awkward as ak
from coffea import hist, processor, nanoevents
import uproot
from coffea.nanoevents import NanoEventsFactory, BaseSchema
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import uproot
import pickle
import time
from distributed import Client
from lpcjobqueue import LPCCondorCluster
import sys

# register our candidate behaviors
from coffea.nanoevents.methods import candidate
ak.behavior.update(candidate.behavior)
def packtrig(output,vals,var):
        output["trigdist_%s"%(var)].fill(cut="cut 0:No cut", v1=vals[0][var])
        output["trigdist_%s"%(var)].fill(cut="cut 1:Mu Trig", v1=vals[1][var]) 
        output["trigdist_%s"%(var)].fill(cut="cut 2:HT Trig", v1=vals[2][var]) 
        return output
def packdist(output,vals,var):
        output["dist_%s"%(var)].fill(cut="cut 0:No cut", v1=vals[0][var])
        output["dist_%s"%(var)].fill(cut="cut 1:HT Trig", v1=vals[1][var]) 
        output["dist_%s"%(var)].fill(cut="cut 2:Ht>=600", v1=vals[2][var])
        output["dist_%s"%(var)].fill(cut="cut 3:fj>=2", v1=vals[3][var])
        output["dist_%s"%(var)].fill(cut="cut 4:nPFCand>=100", v1=vals[4][var]) 
        return output
def packdistflat(output,vals,var):
        output["dist_%s"%(var)].fill(cut="cut 0:No cut",       v1=ak.flatten(vals[0][var]))
        output["dist_%s"%(var)].fill(cut="cut 1:HT Trig",      v1=ak.flatten(vals[1][var])) 
        output["dist_%s"%(var)].fill(cut="cut 2:Ht>=600",      v1=ak.flatten(vals[2][var]))
        output["dist_%s"%(var)].fill(cut="cut 3:fj>=2",        v1=ak.flatten(vals[3][var]))
        output["dist_%s"%(var)].fill(cut="cut 4:nPFCand>=100", v1=ak.flatten(vals[4][var])) 
        return output
def mupackdist(output,vals,var):
        output["mudist_%s"%(var)].fill(cut="cut 0:No cut", v1=vals[0][var])
        output["mudist_%s"%(var)].fill(cut="cut 1:Mu Trig", v1=vals[1][var]) 
        output["mudist_%s"%(var)].fill(cut="cut 2:nPFMu>=4", v1=vals[2][var])
        output["mudist_%s"%(var)].fill(cut="cut 3:fj>=2", v1=vals[3][var])
        output["mudist_%s"%(var)].fill(cut="cut 4:nPFCand>=100", v1=vals[4][var]) 
        return output
def mupackdistflat(output,vals,var):
        output["mudist_%s"%(var)].fill(cut="cut 0:No cut",       v1=ak.flatten(vals[0][var]))
        output["mudist_%s"%(var)].fill(cut="cut 1:Mu Trig",      v1=ak.flatten(vals[1][var])) 
        output["mudist_%s"%(var)].fill(cut="cut 2:nPFMu>=4",      v1=ak.flatten(vals[2][var]))
        output["mudist_%s"%(var)].fill(cut="cut 3:fj>=2",        v1=ak.flatten(vals[3][var]))
        output["mudist_%s"%(var)].fill(cut="cut 4:nPFCand>=100", v1=ak.flatten(vals[4][var])) 
        return output
pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50])
eta_bins = np.array(range(-250,250,25))/100.
phi_bins = np.array(range(-31,31,5))/10.
class MyProcessor(processor.ProcessorABC):
    def __init__(self):
        self._accumulator = processor.dict_accumulator({
            "sumw": processor.defaultdict_accumulator(float),
            "trigdist_ht": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ht",100,0,1500)
            ),
            "dist_ht": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ht",100,0,1500)
            ),
            "dist_event_sphericity": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","spericity",50,0,1)
            ),
            "dist_eventBoosted_sphericity": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Boosted Sphericity",50,0,1)
            ),
            "dist_n_pfcand": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand",50,0,300)
            ),
            "dist_n_jet": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nJet",20,0,20)
            ),
            "dist_n_fatjet": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nFatJet",10,0,10)
            ),
            "dist_Jet_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Jet_pt",100,0,300)
            ),
            "dist_Jet_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Jet_eta",eta_bins)
            ),
            "dist_Jet_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Jet_phi",phi_bins)
            ),
            "dist_FatJet_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_pt",100,0,300)
            ),
            "dist_FatJet_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_eta",eta_bins)
            ),
            "dist_FatJet_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_phi",phi_bins)
            ),
            "dist_PFcand_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_pt",pt_bins)
            ),
            "dist_PFcand_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_eta",eta_bins)
            ),
            "dist_PFcand_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_phi",phi_bins)
            ),
#            "dist_n_pfMu": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","n_pfMuons",15,0,15)
#            ),
#            "dist_n_pfEl": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","n_pfElectrons",20,0,20)
#            ),
#            "mudist_ht": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","ht",100,0,1500)
#            ),
#            "mudist_event_sphericity": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","spericity",50,0,1)
#            ),
#            "mudist_eventBoosted_sphericity": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","Boosted Sphericity",50,0,1)
#            ),
#            "mudist_n_pfcand": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","nPFCand",50,0,300)
#            ),
#            "mudist_n_jet": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","nJet",20,0,20)
#            ),
#            "mudist_n_fatjet": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","nFatJet",10,0,10)
#            ),
#            "mudist_Jet_pt": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","Jet_pt",100,0,300)
#            ),
#            "mudist_Jet_eta": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","Jet_eta",eta_bins)
#            ),
#            "mudist_Jet_phi": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","Jet_phi",phi_bins)
#            ),
#            "mudist_FatJet_pt": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","FatJet_pt",100,0,300)
#            ),
#            "mudist_FatJet_eta": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","FatJet_eta",eta_bins)
#            ),
#            "mudist_FatJet_phi": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","FatJet_phi",phi_bins)
#            ),
#            "mudist_PFcand_pt": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","PFcand_pt",pt_bins)
#            ),
#            "mudist_PFcand_eta": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","PFcand_eta",eta_bins)
#            ),
#            "mudist_PFcand_phi": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","PFcand_phi",phi_bins)
#            ),
#            "mudist_n_pfMu": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","n_pfMuons",15,0,15)
#            ),
#            "mudist_n_pfEl": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","n_pfElectrons",20,0,20)
#            ),
        })

    @property
    def accumulator(self):
        return self._accumulator

    def process(self, arrays):
        output = self.accumulator.identity()
        #print(events)
        dataset = arrays.metadata['dataset']
        #arrays = {k: v for k,v in events.arrays(how=dict).items()}
        output["sumw"][dataset] += len(arrays) # get number of events
        tright = [item[7] for item in arrays["hltResult"]]
        trigmu = [item[2] for item in arrays["hltResult"]]
        vals0 = ak.zip({
               'ht': arrays["ht"],
               'n_pfcand': arrays["n_pfcand"],
               'event_sphericity': arrays["event_sphericity"],
               'eventBoosted_sphericity': arrays["eventBoosted_sphericity"],
               'n_fatjet': arrays["n_fatjet"],
               'n_jet': arrays["n_jet"],
#               'n_pfMu': arrays["n_pfMu"],
#               'n_pfEl': arrays["n_pfEl"],
               'triggerHt': tright,
               'triggerMu': trigmu,
        })

        vals_jet0 = ak.zip({
                       'Jet_pt' : arrays["Jet_pt"],
                       'Jet_eta': arrays["Jet_eta"],
                       'Jet_phi': arrays["Jet_phi"],
        })
        print("loaded jet")
        vals_fatjet0 = ak.zip({
                       'FatJet_pt' : arrays["FatJet_pt"],
                       'FatJet_eta': arrays["FatJet_eta"],
                       'FatJet_phi': arrays["FatJet_phi"],
        })
        print("loaded fatjet")
        vals_tracks0 = ak.zip({
                       'PFcand_pt' : arrays["PFcand_pt"],
                       'PFcand_eta': arrays["PFcand_eta"],
                       'PFcand_phi': arrays["PFcand_phi"],
        })

        #cutflow Ht
        vals1 = vals0[vals0.triggerHt >= 1]
        vals2 = vals1[vals1.ht >= 600]
        vals3 = vals2[vals2.n_fatjet >= 2]
        vals4 = vals3[vals3.n_pfcand >= 100]

        vals_jet1 = vals_jet0[vals0.triggerHt >= 1]
        vals_jet2 = vals_jet1[vals1.ht >= 600]
        vals_jet3 = vals_jet2[vals2.n_fatjet >= 2]
        vals_jet4 = vals_jet3[vals3.n_pfcand >= 100]
        
        vals_fatjet1 = vals_fatjet0[vals0.triggerHt >= 1]
        vals_fatjet2 = vals_fatjet1[vals1.ht >= 600]
        vals_fatjet3 = vals_fatjet2[vals2.n_fatjet >= 2]
        vals_fatjet4 = vals_fatjet3[vals3.n_pfcand >= 100]
        
        vals_tracks1 = vals_tracks0[vals0.triggerHt >= 1]
        vals_tracks2 = vals_tracks1[vals1.ht >= 600]
        vals_tracks3 = vals_tracks2[vals2.n_fatjet >= 2]
        vals_tracks4 = vals_tracks3[vals3.n_pfcand >= 100]
        vals = [vals0,vals1,vals2,vals3,vals4]
        vals_jet = [vals_jet0,vals_jet1,vals_jet2,vals_jet3,vals_jet4]
        vals_fatjet = [vals_fatjet0,vals_fatjet1,vals_fatjet2,vals_fatjet3,vals_fatjet4]
        vals_tracks = [vals_tracks0,vals_tracks1,vals_tracks2,vals_tracks3,vals_tracks4]

#        #cutflow Mu
#        mu_vals1 = vals0[vals0.triggerMu >= 1]
#        mu_vals2 = mu_vals1[mu_vals1.n_pfMu >= 4]
#        mu_vals3 = mu_vals2[mu_vals2.n_fatjet >= 2]
#        mu_vals4 = mu_vals3[mu_vals3.n_pfcand >= 100]
#
#        mu_vals_jet1 = vals_jet0[vals0.triggerMu >= 1]
#        mu_vals_jet2 = mu_vals_jet1[mu_vals1.n_pfMu >= 4]
#        mu_vals_jet3 = mu_vals_jet2[mu_vals2.n_fatjet >= 2]
#        mu_vals_jet4 = mu_vals_jet3[mu_vals3.n_pfcand >= 100]
#
#        mu_vals_fatjet1 = vals_fatjet0[vals0.triggerMu >= 1]
#        mu_vals_fatjet2 = mu_vals_fatjet1[mu_vals1.n_pfMu >= 4]
#        mu_vals_fatjet3 = mu_vals_fatjet2[mu_vals2.n_fatjet >= 2]
#        mu_vals_fatjet4 = mu_vals_fatjet3[mu_vals3.n_pfcand >= 100]
#
#        mu_vals_tracks1 = vals_tracks0[vals0.triggerMu >= 1]
#        mu_vals_tracks2 = mu_vals_tracks1[mu_vals1.n_pfMu >= 4]
#        mu_vals_tracks3 = mu_vals_tracks2[mu_vals2.n_fatjet >= 2]
#        mu_vals_tracks4 = mu_vals_tracks3[mu_vals3.n_pfcand >= 100]
#        mu_vals = [vals0,mu_vals1,mu_vals2,mu_vals3,mu_vals4]
#        mu_vals_jet = [vals_jet0,mu_vals_jet1,mu_vals_jet2,mu_vals_jet3,mu_vals_jet4]
#        mu_vals_fatjet = [vals_fatjet0,mu_vals_fatjet1,mu_vals_fatjet2,mu_vals_fatjet3,mu_vals_fatjet4]
#        mu_vals_tracks = [vals_tracks0,mu_vals_tracks1,mu_vals_tracks2,mu_vals_tracks3,mu_vals_tracks4]

        #trig cutflow
        trig1 = vals0[vals0.triggerMu >=1]
        trig2 = trig1[trig1.triggerHt >=1]
        trigs = [vals0,trig1,trig2]

        output = packtrig(output,trigs,"ht")
        #fill hists
        output = packdist(output,vals,"ht")
        output = packdist(output,vals,"n_pfcand")
        output = packdist(output,vals,"event_sphericity")
        output = packdist(output,vals,"eventBoosted_sphericity")
        output = packdist(output,vals,"n_fatjet")
        output = packdist(output,vals,"n_jet")
#        output = packdist(output,vals,"n_pfMu")
#        output = packdist(output,vals,"n_pfEl")
        
        output = packdistflat(output,vals_jet,"Jet_pt")
        output = packdistflat(output,vals_jet,"Jet_eta")
        output = packdistflat(output,vals_jet,"Jet_phi")
        output = packdistflat(output,vals_fatjet,"FatJet_pt")
        output = packdistflat(output,vals_fatjet,"FatJet_eta")
        output = packdistflat(output,vals_fatjet,"FatJet_phi")
        output = packdistflat(output,vals_tracks,"PFcand_pt")
        output = packdistflat(output,vals_tracks,"PFcand_eta")
        output = packdistflat(output,vals_tracks,"PFcand_phi")

#        #fill mu hists
#        output = mupackdist(output,mu_vals,"ht")
#        output = mupackdist(output,mu_vals,"n_pfcand")
#        output = mupackdist(output,mu_vals,"event_sphericity")
#        output = mupackdist(output,mu_vals,"eventBoosted_sphericity")
#        output = mupackdist(output,mu_vals,"n_fatjet")
#        output = mupackdist(output,mu_vals,"n_jet")
#        output = mupackdist(output,mu_vals,"n_pfMu")
#        output = mupackdist(output,mu_vals,"n_pfEl")
#        
#        output = mupackdistflat(output,mu_vals_jet,"Jet_pt")
#        output = mupackdistflat(output,mu_vals_jet,"Jet_eta")
#        output = mupackdistflat(output,mu_vals_jet,"Jet_phi")
#        output = mupackdistflat(output,mu_vals_fatjet,"FatJet_pt")
#        output = mupackdistflat(output,mu_vals_fatjet,"FatJet_eta")
#        output = mupackdistflat(output,mu_vals_fatjet,"FatJet_phi")
#        output = mupackdistflat(output,mu_vals_tracks,"PFcand_pt")
#        output = mupackdistflat(output,mu_vals_tracks,"PFcand_eta")
#        output = mupackdistflat(output,mu_vals_tracks,"PFcand_phi")

        return output

    def postprocess(self, accumulator):
        return accumulator


# https://github.com/scikit-hep/uproot4/issues/122
uproot.open.defaults["xrootd_handler"] = uproot.source.xrootd.MultithreadedXRootDSource


fin = "HT2000"
batch = 0
if len(sys.argv) >= 2:
  fin = sys.argv[1]
#fin = "sig400"
if len(sys.argv) >= 3:
  batch = int(sys.argv[2])
if "HT" in fin:
  fs = np.loadtxt("rootfiles/%s.txt"%(fin),dtype=str)
  fs=fs[400*batch:400*(batch+1)]
  fileset = {
           fin : ["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCD/%s/%s"%(fin,f) for f in fs],
           #'HT700' : ["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCD/HT700/%s"%(f) for f in fs_sub],
#            fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Signal/%s_darkPho_ntrack.root"%fin]
#            'sig400_darkPho':["/uscms/home/mreid/nobackup/sueps/analysis/CMSSW_10_6_0/src/PhysicsTools/newData_ntrack/sig400_darkPho_ntrack.root"],
#            'sig300_darkPho':["/uscms/home/mreid/nobackup/sueps/analysis/CMSSW_10_6_0/src/PhysicsTools/newData_ntrack/sig300_darkPho_ntrack.root"],
#            'sig200_darkPho':["/uscms/home/mreid/nobackup/sueps/analysis/CMSSW_10_6_0/src/PhysicsTools/newData_ntrack/sig200_darkPho_ntrack.root"],
  }
else:
  decays = ["darkPho","darkPhoHad","generic"]
  fileset = {
            fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Signal/%s_%s_ntrackboost.root"%(fin,decays[batch])]
  }  


if __name__ == "__main__":
    tic = time.time()
    #print(sys.argv)
    cluster = LPCCondorCluster()
    # minimum > 0: https://github.com/CoffeaTeam/coffea/issues/465
    cluster.adapt(minimum=1, maximum=10)
    client = Client(cluster)

    exe_args = {
        "client": client,
        "savemetrics": True,
        "schema": BaseSchema, #nanoevents.NanoAODSchema,
        "align_clusters": True,
    }

    proc = MyProcessor()

    print("Waiting for at least one worker...")
    client.wait_for_workers(1)
    #hists, metrics = processor.run_uproot_job(
    out,metrics = processor.run_uproot_job(
        fileset,
        treename="mmtree/tree",
        processor_instance=proc,
        executor=processor.dask_executor,
        executor_args=exe_args,
        # remove this to run on the whole fileset:
        #maxchunks=10,
    )

    elapsed = time.time() - tic
    print(f"Output: {out}")
    print(f"Metrics: {metrics}")
    print(f"Finished in {elapsed:.1f}s")
    print(f"Events/s: {metrics['entries'] / elapsed:.0f}")
#out = processor.run_uproot_job(
#      fileset,
#      treename="mmtree/tree",
#      processor_instance=MyProcessor(),
#      executor=processor.iterative_executor,
#      executor_args={
#          "schema": BaseSchema,
#      },
#      maxchunks=4,
#)
    print(out)

    with open("outhists/myhistos_%s_%s.p"%(fin,batch), "wb") as pkl_file:
        pickle.dump(out, pkl_file)
