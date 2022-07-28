import awkward as ak
from coffea import hist, processor
import uproot
from coffea.nanoevents import NanoEventsFactory, BaseSchema
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import uproot
import pickle

#outhists = [
#"HT1500_0",
#"HT1500_1",
#"HT1000_0",
#"HT1000_1",
#"HT1000_2",
#"HT700_0",
#"HT700_1",
#"HT700_2",
#"HT500_0",
#"HT500_1",
#"HT500_2",
#"HT300_0",
#"HT300_1",
#"HT300_2",
#"HT200_0",
#"HT200_1",
#"HT200_2",
#]
outhists = [
"HT2000_1"
,"HT2000_2"
,"HT1500_0"
,"HT1500_1"
,"HT1500_2"
,"HT1500_3"
,"HT1500_4"
,"HT1500_5"
,"HT1500_6"
,"HT1000_0"
,"HT1000_1"
,"HT1000_2"
,"HT1000_3"
,"HT1000_4"
,"HT1000_5"
,"HT1000_6"
,"HT1000_7"
,"HT1000_8"
,"HT700_0"
,"HT700_1"
,"HT700_2"
,"HT700_3"
,"HT700_4"
,"HT700_5"
,"HT700_6"
,"HT700_7"
,"HT700_8"
,"HT700_9"
,"HT700_10" 
,"HT700_11"
,"HT700_12"
,"HT700_13"
,"HT700_14"
,"HT700_15"
,"HT700_16"
,"HT700_17"
,"HT700_18"
,"HT700_19"
,"HT700_20"
,"HT700_21"
,"HT700_22"
,"HT700_23"
,"HT700_24"
,"HT700_25"
,"HT700_26"
,"HT500_0"
,"HT500_1"
,"HT500_2"
,"HT500_3"
,"HT500_4"
,"HT500_5"
,"HT500_6"
,"HT500_7"
,"HT500_8"
,"HT500_9"
,"HT500_10"
,"HT500_11"
,"HT500_12"
,"HT500_13"
,"HT500_14"
,"HT500_15"
,"HT500_16"
,"HT500_17"
,"HT500_18"
,"HT500_19"
,"HT500_20"
,"HT500_21"
,"HT500_22"
,"HT500_23"
,"HT500_24"
,"HT500_25"
,"HT500_26"
,"HT500_27"
,"HT300_0"
,"HT300_1"
,"HT300_2"
,"HT300_3"
,"HT300_4"
,"HT300_5"
,"HT300_6"
,"HT300_7"
,"HT300_8"
,"HT300_9"
,"HT300_10"
,"HT300_11"
,"HT300_12"
,"HT300_13"
,"HT300_14"
,"HT300_15"
,"HT300_16"
,"HT300_17"
,"HT300_18"
,"HT300_19"
,"HT300_20"
,"HT300_21"
,"HT300_22"
,"HT300_23"
,"HT300_24"
,"HT300_25"
,"HT300_26"
,"HT300_27"
,"HT300_28"
,"HT200_0"
,"HT200_1"
,"HT200_2"
,"HT200_3"
,"HT200_4"
,"HT200_5"
,"HT200_6"
,"HT200_7"
,"HT200_8"
,"HT200_9"
,"HT200_10"
,"HT200_11"
#,"HT200_12"
,"HT200_13"
,"HT200_14"
,"HT200_15"
,"HT200_16"
,"HT200_17"
,"HT200_18"
,"HT200_19"
,"HT200_20"
,"HT200_21"
,"HT200_22"
,"HT200_23"
,"HT200_24"
,"HT200_25"
,"HT200_26"
,"HT200_27"
,"HT200_28"
,"HT200_29"
]
neventsHT= {"HT200":0,"HT300":0,"HT500":0,"HT700":0,"HT1000":0,"HT1500":0,"HT2000":0}
for ohist in ["HT2000_0"]+outhists:
  with open("outhists/myhistos_%s.p"%(ohist), "rb") as pkl_file:
      qcd_samp = ohist.split("_")[0]
      print(ohist)
      out = pickle.load(pkl_file)
      #print(out)
      #xsec = xsecs[qcd_samp]
      #nevents = out["sumw"]["sig400"]
      neventsHT[qcd_samp] = neventsHT[qcd_samp] + out["sumw"][qcd_samp]
      #print(qcd_samp,nevents[qcd_samp])

lumi = 1# no luminosity. set to nEvents from data. #59.74*1000
scaled = {}
#xsecs = {"HT200":1735000,"HT300":366800,"HT500":29370,"HT700":6524,"HT1000":1064*3,"HT1500":121.5*3,"HT2000":25.42*6}
#xsecs = {"HT200":1735000,"HT300":366800,"HT500":29370,"HT700":6524,"HT1000":1064,"HT1500":121.5,"HT2000":25.42}
#xsecs = {"HT200":1559000,"HT300":347700,"HT500":32100,"HT700":6831,"HT1000":1207,"HT1500":119.9,"HT2000":25.24}
xsecs = {"HT200":1551000.0,"HT300":323400.0,"HT500":30140.0,"HT700":6344.0,"HT1000":1092.0,"HT1500":99.76,"HT2000":20.35}
with open("outhists/myhistos_HT2000_0.p", "rb") as pkl_file:
    out = pickle.load(pkl_file)
    print(out)
    xsec = xsecs["HT2000"]
    #nevents = out["sumw"]["sig400"]
    nevents = neventsHT["HT2000"] #out["sumw"]["HT2000"]
    print("nevents ",nevents)
    #fout = uproot.recreate("output.root")
    for name, h in out.items():
      if "PFcand_dR" in name or "res" in name or "gen" in name or "alldR" in name or "scalar" in name:
        continue
      if isinstance(h, hist.Hist):
        #print(name)
        scaled[name] = h.copy()
        scaled[name].scale(lumi*xsec/nevents)
    #h1 = scaled["dist_ht"].integrate("cut",slice(2,3))
    #scaled["nEvents"] = sum(h1.values(sumw2=True)[()][0])

for ohist in outhists:
  with open("outhists/myhistos_%s.p"%(ohist), "rb") as pkl_file:
      qcd_samp = ohist.split("_")[0]
      print(ohist)
      out = pickle.load(pkl_file)
      print(out)
      xsec = xsecs[qcd_samp]
      #nevents = out["sumw"]["sig400"]
      nevents = neventsHT[qcd_samp] #out["sumw"][qcd_samp]
      print("nevents ",nevents)
      #fout = uproot.recreate("output.root")
      for name, h in out.items():
        if "PFcand_dR" in name or "res" in name or "gen" in name or "alldR" in name or "scalar" in name:
          continue
        if isinstance(h, hist.Hist):
          print(name)
          temphist = h.copy()
          temphist.scale(lumi*xsec/nevents)
          #h1 = temphist["dist_ht"].integrate("cut",slice(2,3))
          #scaled["nEvents"] = scaled["nEvents"]+sum(h1.values(sumw2=True)[()][0])
          scaled[name] = scaled[name]+temphist
      #h1 = scaled["dist_ht"].integrate("cut",slice(2,3))
      #scaled["nEvents"] = scaled["nEvents"]+sum(h1.values(sumw2=True)[()][0])
with open("outhists/myhistos_QCD.p", "wb") as pkl_file:
        pickle.dump(scaled, pkl_file)
