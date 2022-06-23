import awkward as ak
from coffea import hist, processor
import uproot
from coffea.nanoevents import NanoEventsFactory, BaseSchema
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import uproot
import pickle

#with open("myhistos_sig400_0.p", "rb") as pkl_file:
lumi = 1#59.74*1000
scaled = {}
#xsecs = {"HT200":1559000,"HT300":347700,"HT500":32100,"HT700":6831,"HT1000":1207,"HT1500":119.9,"HT2000":25.24}
with open("outhists/myhistos_RunA_0.p", "rb") as pkl_file:
    out = pickle.load(pkl_file)
    #print(out)
    #xsec = 1#xsecs["HT2000"]
    #nevents = out["sumw"]["sig400"]
    #nevents = 1#out["sumw"]["RunA"]
    #print("nevents ",nevents)
    #scaled["nEvents"] = out["sumw"]["RunA"]
    #fout = uproot.recreate("output.root")
    for name, h in out.items():
      if "PFcand_dR" in name or "res" in name or "gen" in name:
        continue
      if isinstance(h, hist.Hist):
        #print(name)
        scaled[name] = h.copy()
        #scaled[name].scale(lumi*xsec/nevents)
    #h1 = scaled["dist_ht"].integrate("cut",slice(2,3))
    #scaled["nEvents"] = sum(h1.values(sumw2=True)[()][0])
#outhists = [
#"RunA_1",
#"RunA_2",
#"RunA_3",
#"RunA_4",
#"RunA_5",
#"RunA_6",
#"RunA_7",
#"RunA_8"
#]
#outhists = ["RunA_%s"%x for x in range(1,50)]
outhists = ["RunA_%s"%x for x in range(1,7)]
outhists = outhists+ ["RunA_%s"%x for x in range(7,23)]
outhists = outhists+ ["RunA_%s"%x for x in range(25,27)]
outhists = outhists+ ["RunA_%s"%x for x in range(28,54)]
outhists = outhists+ ["RunA_%s"%x for x in range(55,57)]
outhists = outhists+ ["RunA_%s"%x for x in range(59,62)]
outhists = outhists+ ["RunA_%s"%x for x in range(63,69)]
outhists = outhists+ ["RunA_%s"%x for x in range(70,82)]
outhists = outhists+ ["RunA_%s"%x for x in range(84,97)]
outhists = outhists+ ["RunA_%s"%x for x in range(98,99)]
#outhists = outhists+ ["RunA_%s"%x for x in range(58,62)]
#outhists = outhists+ ["RunA_%s"%x for x in range(65,68)]
#outhists = outhists+ ["RunA_%s"%x for x in range(69,79)]
#outhists = outhists+ ["RunA_%s"%x for x in range(82,83)]
#outhists = outhists+ ["RunA_%s"%x for x in range(84,88)]
#outhists = outhists+ ["RunA_%s"%x for x in range(89,92)]
#outhists = outhists+ ["RunA_%s"%x for x in range(93,97)]
#outhists = outhists+ ["RunA_%s"%x for x in range(98,99)]
#outhists = outhists+ ["RunA_%s"%x for x in range(100,101)]
#print(outhists)

for ohist in outhists:
  with open("outhists/myhistos_%s.p"%(ohist), "rb") as pkl_file:
      print(ohist)
      out = pickle.load(pkl_file)
      #print(out)
      #xsec = 1
      #nevents = 1
      #scaled["nEvents"] = scaled["nEvents"] + out["sumw"]["RunA"]
      for name, h in out.items():
        if "PFcand_dR" in name or "res" in name or "gen" in name:
          continue
        if isinstance(h, hist.Hist):
          temphist = h.copy()
          scaled[name] = scaled[name]+temphist
with open("outhists/myhistos_RunA.p", "wb") as pkl_file:
        pickle.dump(scaled, pkl_file)
