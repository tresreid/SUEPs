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
               #'Jet_pt' : arrays.pop("Jet_pt"),
               #'Jet_eta': arrays.pop("Jet_eta"),
               #'Jet_phi': arrays.pop("Jet_phi"),
               #'FatJet_pt' : arrays.pop("FatJet_pt"),
               #'FatJet_eta': arrays.pop("FatJet_eta"),
               #'FatJet_phi': arrays.pop("FatJet_phi"),
               'PFcand_pt' : arrays.pop("PFcand_pt"),
               'PFcand_eta': arrays.pop("PFcand_eta"),
               'PFcand_phi': arrays.pop("PFcand_phi"),
#               'triggerMu': trigmu,
              # 'triggerMu': arrays.pop("hltResult")[:][2],
              })
print(vals.ht)

#vals_jet = ak.zip({
#               'Jet_pt': arrays.pop("Jet_pt"),
#               'Jet_eta': arrays.pop("Jet_eta"),
#               'Jet_phi': arrays.pop("Jet_phi"),
#})
#vals_fatjet = ak.zip({
#               'FatJet_pt' : ak.flatten(arrays.pop("FatJet_pt")),
#               'FatJet_eta': ak.flatten(arrays.pop("FatJet_eta")),
#               'FatJet_phi': ak.flatten(arrays.pop("FatJet_phi")),
#})

#cutflow Ht
vals1 = vals[vals.triggerHt >= 1]
vals2 = vals1[vals1.ht >= 600]
vals3 = vals2[vals2.n_fatjet >= 2]
vals4 = vals3[vals3.n_pfcand >= 200]

rang = range(0,1500,10)

def make_dist(var,bins,log=False):
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
  
  dist.fill(cut="cut 0:no cut",        v1=ak.flatten(vals[var]))
  dist.fill(cut="cut 1:TrigHt",        v1=ak.flatten(vals1[var]))
  dist.fill(cut="cut 2:ht >= 600",     v1=ak.flatten(vals2[var]))
  dist.fill(cut="cut 3:fj >= 2",       v1=ak.flatten(vals3[var]))
  dist.fill(cut="cut 4:n_PfCand >=200",v1=ak.flatten(vals4[var]))
  
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

pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50,200])
eta_bins = np.array(range(-250,250,25))/100.
phi_bins = np.array(range(-31,31,5))/10.

make_dist("ht",[150,0,1500])
make_dist("n_pfcand",[50,0,500])
make_dist("event_sphericity",[100,0,1])
make_dist("eventBoosted_sphericity",[100,0,1])
make_dist("n_fatjet",[10,0,10])
make_dist("n_jet",[20,0,20])
make_dist("n_pfMu",[10,0,10])
make_dist("n_pfEl",[10,0,10])
#make_dist("Jet_pt",[300,0,300])
#make_dist("Jet_eta",eta_bins)
#make_dist("Jet_phi",phi_bins)
#make_dist("FatJet_pt",[300,0,300])
#make_dist("FatJet_eta",eta_bins)
#make_dist("FatJet_phi",phi_bins)
make_dist("PFcand_pt",pt_bins)
make_dist("PFcand_eta",eta_bins)
make_dist("PFcand_phi",phi_bins)

