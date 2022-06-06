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
    print(out)
    xsec = 1#xsecs["HT2000"]
    #nevents = out["sumw"]["sig400"]
    nevents = 1#out["sumw"]["RunA"]
    print("nevents ",nevents)
    #fout = uproot.recreate("output.root")
    for name, h in out.items():
      if "PFcand_dR" in name or "res" in name or "gen" in name:
        continue
      if "spher" in name:
        continue
      if isinstance(h, hist.Hist):
        #print(name)
        scaled[name] = h.copy()
        scaled[name].scale(lumi*xsec/nevents)
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
outhists = ["RunA_%s"%x for x in range(1,100)]
#outhists = outhists+ ["RunA_%s"%x for x in range(22,41)]
#print(outhists)

for ohist in outhists:
  with open("outhists/myhistos_%s.p"%(ohist), "rb") as pkl_file:
      print(ohist)
      out = pickle.load(pkl_file)
      print(out)
      xsec = 1
      nevents = 1
      for name, h in out.items():
        if "PFcand_dR" in name or "res" in name or "gen" in name:
          continue
        if "spher" in name:
          continue
        if isinstance(h, hist.Hist):
          print(name)
          temphist = h.copy()
          temphist.scale(lumi*xsec/nevents)
          scaled[name] = scaled[name]+temphist
with open("outhists/myhistos_RunA.p", "wb") as pkl_file:
        pickle.dump(scaled, pkl_file)
