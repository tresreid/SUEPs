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

# register our candidate behaviors
from coffea.nanoevents.methods import candidate
ak.behavior.update(candidate.behavior)
def packdist(output,vals,var):
        output["dist_%s"%(var)].fill(cut="cut 0:No cut", v1=vals[0][var])
        output["dist_%s"%(var)].fill(cut="cut 1:HT Trig", v1=vals[1][var]) 
        output["dist_%s"%(var)].fill(cut="cut 2:Ht>=600", v1=vals[2][var])
        output["dist_%s"%(var)].fill(cut="cut 3:fj>=2", v1=vals[3][var])
        output["dist_%s"%(var)].fill(cut="cut 4:nPFCand>=200", v1=vals[4][var]) 
        return output
def packdistflat(output,vals,var):
        output["dist_%s"%(var)].fill(cut="cut 0:No cut",       v1=ak.flatten(vals[0][var]))
        output["dist_%s"%(var)].fill(cut="cut 1:HT Trig",      v1=ak.flatten(vals[1][var])) 
        output["dist_%s"%(var)].fill(cut="cut 2:Ht>=600",      v1=ak.flatten(vals[2][var]))
        output["dist_%s"%(var)].fill(cut="cut 3:fj>=2",        v1=ak.flatten(vals[3][var]))
        output["dist_%s"%(var)].fill(cut="cut 4:nPFCand>=200", v1=ak.flatten(vals[4][var])) 
        return output
pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50])
eta_bins = np.array(range(-250,250,25))/100.
phi_bins = np.array(range(-31,31,5))/10.
class MyProcessor(processor.ProcessorABC):
    def __init__(self):
        self._accumulator = processor.dict_accumulator({
            "sumw": processor.defaultdict_accumulator(float),
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
        vals0 = ak.zip({
               'ht': arrays["ht"],
               'n_pfcand': arrays["n_pfcand"],
               'event_sphericity': arrays["event_sphericity"],
               'eventBoosted_sphericity': arrays["eventBoosted_sphericity"],
               'n_fatjet': arrays["n_fatjet"],
               'n_jet': arrays["n_jet"],
#               'n_pfMu': arrays.pop("n_pfMu"),
#               'n_pfEl': arrays.pop("n_pfEl"),
               'triggerHt': tright,
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

        #cut = (ak.num(muons) == 2) & (ak.sum(muons.charge) == 0)
        # add first and second muon in every event together
        #dimuon = muons[cut][:, 0] + muons[cut][:, 1]

        #cutflow Ht
        vals1 = vals0[vals0.triggerHt >= 1]
        vals2 = vals1[vals1.ht >= 600]
        vals3 = vals2[vals2.n_fatjet >= 2]
        vals4 = vals3[vals3.n_pfcand >= 200]

        vals_jet1 = vals_jet0[vals0.triggerHt >= 1]
        vals_jet2 = vals_jet1[vals1.ht >= 600]
        vals_jet3 = vals_jet2[vals2.n_fatjet >= 2]
        vals_jet4 = vals_jet3[vals3.n_pfcand >= 200]
        
        vals_fatjet1 = vals_fatjet0[vals0.triggerHt >= 1]
        vals_fatjet2 = vals_fatjet1[vals1.ht >= 600]
        vals_fatjet3 = vals_fatjet2[vals2.n_fatjet >= 2]
        vals_fatjet4 = vals_fatjet3[vals3.n_pfcand >= 200]
        
        vals_tracks1 = vals_tracks0[vals0.triggerHt >= 1]
        vals_tracks2 = vals_tracks1[vals1.ht >= 600]
        vals_tracks3 = vals_tracks2[vals2.n_fatjet >= 2]
        vals_tracks4 = vals_tracks3[vals3.n_pfcand >= 200]
        vals = [vals0,vals1,vals2,vals3,vals4]
        vals_jet = [vals_jet0,vals_jet1,vals_jet2,vals_jet3,vals_jet4]
        vals_fatjet = [vals_fatjet0,vals_fatjet1,vals_fatjet2,vals_fatjet3,vals_fatjet4]
        vals_tracks = [vals_tracks0,vals_tracks1,vals_tracks2,vals_tracks3,vals_tracks4]
        #fill hists
        output = packdist(output,vals,"ht")
        output = packdist(output,vals,"n_pfcand")
        output = packdist(output,vals,"event_sphericity")
        output = packdist(output,vals,"eventBoosted_sphericity")
        output = packdist(output,vals,"n_fatjet")
        output = packdist(output,vals,"n_jet")
        
        output = packdistflat(output,vals_jet,"Jet_pt")
        output = packdistflat(output,vals_jet,"Jet_eta")
        output = packdistflat(output,vals_jet,"Jet_phi")
        output = packdistflat(output,vals_fatjet,"FatJet_pt")
        output = packdistflat(output,vals_fatjet,"FatJet_eta")
        output = packdistflat(output,vals_fatjet,"FatJet_phi")
        output = packdistflat(output,vals_tracks,"PFcand_pt")
        output = packdistflat(output,vals_tracks,"PFcand_eta")
        output = packdistflat(output,vals_tracks,"PFcand_phi")

        return output

    def postprocess(self, accumulator):
        return accumulator


# https://github.com/scikit-hep/uproot4/issues/122
uproot.open.defaults["xrootd_handler"] = uproot.source.xrootd.MultithreadedXRootDSource

fs = np.loadtxt("rootfiles/%s.txt"%("HT700"),dtype=str)
#fs_sub = ["F980E45B-3E04-C64B-B9EB-87DD0E1E8783.root",
#            "F9838A6B-DA97-B24D-91FC-D8453D7618BA.root",
#            "F9CE0AD2-252B-CB4E-8F3A-9488DAF84A3C.root",
#            "F9D04630-B90B-0A41-89B6-4960B86187C6.root",
#            "F9D7DE16-1658-9043-9471-E1D77545A0AF.root",
#            "F9DD1443-8504-0A49-8CF0-AC8AE55FF6B8.root",
#]
fileset = {
           'HT700' : ["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCD/HT700/%s"%(f) for f in fs],
           #'HT700' : ["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCD/HT700/%s"%(f) for f in fs_sub],
#            'sig400_darkPho':["/uscms/home/mreid/nobackup/sueps/analysis/CMSSW_10_6_0/src/PhysicsTools/newData_ntrack/sig400_darkPho_ntrack.root"],
#            'sig300_darkPho':["/uscms/home/mreid/nobackup/sueps/analysis/CMSSW_10_6_0/src/PhysicsTools/newData_ntrack/sig300_darkPho_ntrack.root"],
#            'sig200_darkPho':["/uscms/home/mreid/nobackup/sueps/analysis/CMSSW_10_6_0/src/PhysicsTools/newData_ntrack/sig200_darkPho_ntrack.root"],
}


if __name__ == "__main__":
    tic = time.time()
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

    with open("myhistos.p", "wb") as pkl_file:
        pickle.dump(out, pkl_file)
