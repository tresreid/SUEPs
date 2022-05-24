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
#outhists = ["HT500_0","HT500_1","HT500_2","HT500_3","HT700_0","HT700_1","HT700_2","HT1000_0","HT1000_1","HT1500_0","HT1500_1"]
outhists = ["HT200_0","HT200_1","HT200_2","HT200_3","HT200_4","HT200_5","HT200_6","HT200_7","HT200_8","HT300_0","HT300_1","HT300_2","HT300_3","HT300_4","HT300_5","HT300_7","HT500_0","HT500_1","HT500_2","HT500_3","HT500_4","HT500_5","HT500_6", "HT700_0","HT700_1","HT700_2","HT700_3","HT700_4","HT700_5","HT700_6","HT700_7","HT1000_0","HT1000_1","HT1500_0","HT1500_1"]
#outhists = ["HT50_0","HT50_1","HT50_2","HT100_0","HT100_1","HT100_2","HT100_3","HT100_4","HT100_5","HT100_6","HT100_7","HT100_8","HT100_9","HT100_10","HT100_11","HT100_12","HT100_13","HT100_14","HT100_15","HT200_0","HT200_1","HT200_2","HT200_3","HT200_4","HT200_5","HT200_6","HT200_7" ,"HT300_0","HT300_1","HT300_2","HT300_3","HT300_4","HT300_5","HT500_0","HT500_1","HT500_2","HT500_3", "HT700_0","HT700_1","HT700_2","HT700_3","HT1000_0","HT1000_1","HT1000_2","HT1500_0","HT1500_1"]
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
