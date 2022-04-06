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
lumi = 59.74*1000
scaled = {}
xsecs = {"HT200":1559000,"HT300":347700,"HT500":32100,"HT700":6831,"HT1000":1207,"HT1500":119.9,"HT2000":25.24}
with open("outhists/myhistos_HT2000_0.p", "rb") as pkl_file:
    out = pickle.load(pkl_file)
    print(out)
    xsec = xsecs["HT2000"]
    #nevents = out["sumw"]["sig400"]
    nevents = out["sumw"]["HT2000"]
    print("nevents ",nevents)
    #fout = uproot.recreate("output.root")
    for name, h in out.items():
      if isinstance(h, hist.Hist):
        #print(name)
        scaled[name] = h.copy()
        scaled[name].scale(lumi*xsec/nevents)
outhists = ["HT500_0","HT500_1","HT500_2","HT500_3","HT500_4","HT500_5","HT500_6", "HT700_0","HT700_1","HT700_2","HT700_3","HT700_4","HT700_5","HT700_6","HT1000_0","HT1000_1","HT1000_2","HT1500_0","HT1500_1"]
#outhists = ["HT700_0","HT700_1","HT700_2","HT700_3","HT700_4","HT700_5","HT700_6","HT1000_0","HT1000_1","HT1000_2","HT1500_0","HT1500_1"]
for ohist in outhists:
  with open("outhists/myhistos_%s.p"%(ohist), "rb") as pkl_file:
      qcd_samp = ohist.split("_")[0]
      print(qcd_samp)
      out = pickle.load(pkl_file)
      print(out)
      xsec = xsecs[qcd_samp]
      #nevents = out["sumw"]["sig400"]
      nevents = out["sumw"][qcd_samp]
      print("nevents ",nevents)
      #fout = uproot.recreate("output.root")
      for name, h in out.items():
        if isinstance(h, hist.Hist):
          print(name)
          temphist = h.copy()
          temphist.scale(lumi*xsec/nevents)
          scaled[name] = scaled[name]+temphist
with open("outhists/myhistos_QCD.p", "wb") as pkl_file:
        pickle.dump(scaled, pkl_file)
