import uproot
import awkward as ak
from coffea.nanoevents.methods import vector
import coffea.hist as hist
import matplotlib.pyplot as plt
import numpy as np
ak.behavior.update(vector.behavior)
import mplhep as hep
plt.style.use(hep.style.ROOT)



dir1 = "/uscms/home/mreid/nobackup/sueps/analysis/CMSSW_10_6_0/src/PhysicsTools/"
fin = uproot.open("%s/newData_ntrack/%s_ntrack.root"%(dir1,"sig400_darkPho"))
tree = fin["mmtree/tree"]
print(fin)
print(tree)

# let's build the lepton arrays back into objects
# in the future, some of this verbosity can be reduced
arrays = {k: v for k,v in tree.arrays(how=dict).items()}
tright = [item[7] for item in arrays.pop("hltResult")]
#trigmu = [item[7] for item in arrays.pop("hltResult")]
vals = ak.zip({
               'ht': arrays.pop("ht"),
               'n_pfcand': arrays.pop("n_pfcand"),
               'event_sphericity': arrays.pop("event_sphericity"),
               'eventBoosted_sphericity': arrays.pop("eventBoosted_sphericity"),
               'n_fatjet': arrays.pop("n_fatjet"),
               'n_jet': arrays.pop("n_jet"),
               'n_pfMu': arrays.pop("n_pfMu"),
               'n_pfEl': arrays.pop("n_pfEl"),
               'triggerHt': tright, 
#               'triggerMu': trigmu,
              # 'triggerMu': arrays.pop("hltResult")[:][2],
              })
print("loaded main")

vals_jet = ak.zip({
               'Jet_pt': arrays.pop("Jet_pt"),
               'Jet_eta': arrays.pop("Jet_eta"),
               'Jet_phi': arrays.pop("Jet_phi"),
})
print("loaded jet")
vals_fatjet = ak.zip({
               'FatJet_pt' : arrays.pop("FatJet_pt"),
               'FatJet_eta': arrays.pop("FatJet_eta"),
               'FatJet_phi': arrays.pop("FatJet_phi"),
})
print("loaded fatjet")
vals_tracks = ak.zip({
               'PFcand_pt' : arrays.pop("PFcand_pt"),
               'PFcand_eta': arrays.pop("PFcand_eta"),
               'PFcand_phi': arrays.pop("PFcand_phi"),
})
print("loaded tracks")

#cutflow Ht
vals1 = vals[vals.triggerHt >= 1]
vals2 = vals1[vals1.ht >= 600]
vals3 = vals2[vals2.n_fatjet >= 2]
vals4 = vals3[vals3.n_pfcand >= 200]

vals_jet1 = vals_jet[vals.triggerHt >= 1]
vals_jet2 = vals_jet1[vals1.ht >= 600]
vals_jet3 = vals_jet2[vals2.n_fatjet >= 2]
vals_jet4 = vals_jet3[vals3.n_pfcand >= 200]

vals_fatjet1 = vals_fatjet[vals.triggerHt >= 1]
vals_fatjet2 = vals_fatjet1[vals1.ht >= 600]
vals_fatjet3 = vals_fatjet2[vals2.n_fatjet >= 2]
vals_fatjet4 = vals_fatjet3[vals3.n_pfcand >= 200]

vals_tracks1 = vals_tracks[vals.triggerHt >= 1]
vals_tracks2 = vals_tracks1[vals1.ht >= 600]
vals_tracks3 = vals_tracks2[vals2.n_fatjet >= 2]
vals_tracks4 = vals_tracks3[vals3.n_pfcand >= 200]
valx1 = [vals,vals1,vals2,vals3,vals4]
valx2 = [vals_jet,vals_jet1,vals_jet2,vals_jet3,vals_jet4]
valx3 = [vals_fatjet,vals_fatjet1,vals_fatjet2,vals_fatjet3,vals_fatjet4]
valx4 = [vals_tracks,vals_tracks1,vals_tracks2,vals_tracks3,vals_tracks4]

print("set cutflow")
rang = range(0,1500,10)

def make_dist(valx,var,bins,flatten,log=False):
  if len(bins) ==3:
    dist = hist.Hist(
      "Events",
      hist.Cat("cut","Cutflow"),
      hist.Bin("v1",var,bins[0],bins[1],bins[2])
      )
  else:
    dist = hist.Hist(
      "Events",
      hist.Cat("cut","Cutflow"),
      hist.Bin("v1",var,bins)
      )
  if flatten: 
    dist.fill(cut="cut 0:no cut",        v1=ak.flatten(valx[0][var]))
    dist.fill(cut="cut 1:TrigHt",        v1=ak.flatten(valx[1][var]))
    dist.fill(cut="cut 2:ht >= 600",     v1=ak.flatten(valx[2][var]))
    dist.fill(cut="cut 3:fj >= 2",       v1=ak.flatten(valx[3][var]))
    dist.fill(cut="cut 4:n_PfCand >=200",v1=ak.flatten(valx[4][var]))
  else:
    dist.fill(cut="cut 0:no cut",        v1=valx[0][var])
    dist.fill(cut="cut 1:TrigHt",        v1=valx[1][var])
    dist.fill(cut="cut 2:ht >= 600",     v1=valx[2][var])
    dist.fill(cut="cut 3:fj >= 2",       v1=valx[3][var])
    dist.fill(cut="cut 4:n_PfCand >=200",v1=valx[4][var])
  
  fig, ax1 = plt.subplots()
  
  hist.plot1d(
      dist,
      ax=ax1,
      overlay="cut",
      stack=False,
      fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
  )
  if log:
    ax1.set_yscale('log') 
  #hep.cms.label(loc=2)
  hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
  fig.savefig("Plots/dist_%s"%(var))
  plt.close()

pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50])
eta_bins = np.array(range(-250,250,25))/100.
phi_bins = np.array(range(-31,31,5))/10.


print("making distributions")
make_dist(valx1,"ht",[150,0,1500],False)
make_dist(valx1,"n_pfcand",[50,0,300],False)
make_dist(valx1,"event_sphericity",[50,0,1],False)
make_dist(valx1,"eventBoosted_sphericity",[50,0,1],False)
make_dist(valx1,"n_fatjet",[10,0,10],False)
make_dist(valx1,"n_jet",[20,0,20],False)
make_dist(valx1,"n_pfMu",[10,0,10],False)
make_dist(valx1,"n_pfEl",[10,0,10],False)
make_dist(valx2,"Jet_pt",[100,0,300],True,True)
make_dist(valx2,"Jet_eta",eta_bins,True)
make_dist(valx2,"Jet_phi",phi_bins,True)
make_dist(valx3,"FatJet_pt",[100,0,300],True,True)
make_dist(valx3,"FatJet_eta",eta_bins,True)
make_dist(valx3,"FatJet_phi",phi_bins,True)
make_dist(valx4,"PFcand_pt",pt_bins,True)
make_dist(valx4,"PFcand_eta",eta_bins,True)
make_dist(valx4,"PFcand_phi",phi_bins,True)

