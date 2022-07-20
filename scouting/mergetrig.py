import awkward as ak
from coffea import hist, processor
import uproot
from coffea.nanoevents import NanoEventsFactory, BaseSchema
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import uproot
import pickle

lumi = 1#59.74*1000
scaled = {}
with open("outhists/myhistos_Trigger_0.p", "rb") as pkl_file:
    out = pickle.load(pkl_file)
    for name, h in out.items():
      if "PFcand_dR" in name or "res" in name or "gen" in name or "alldR" in name:
        continue
      if isinstance(h, hist.Hist):
        scaled[name] = h.copy()
outhists = [
"Trigger_1",
"Trigger_2",
"Trigger_3",
#"Trigger_4",
"Trigger_5",
"Trigger_6",
"Trigger_7",
"Trigger_8",
#"Trigger_9",
"Trigger_10",
"Trigger_11",
#"Trigger_12",
"Trigger_13",
#"Trigger_14",
"Trigger_15",
"Trigger_16",
"Trigger_17",
"Trigger_18",
#"Trigger_19",
"Trigger_20",
"Trigger_21",
"Trigger_22",
"Trigger_23",
"Trigger_24",
"Trigger_25",
"Trigger_26",
"Trigger_27",
"Trigger_28",
"Trigger_29",
"Trigger_30",
#"Trigger_31",
#"Trigger_32",
"Trigger_33",
#"Trigger_34",
#"Trigger_35",
#"Trigger_36",
]
#outhists = ["RunA_%s"%x for x in range(1,50)]
#outhists = ["Trigger_%s"%x for x in range(1,2)]
#outhists = outhists+ ["Trigger_%s"%x for x in range(3,24)]
#outhists = outhists+ ["Trigger_%s"%x for x in range(25,59)]
#outhists = outhists+ ["Trigger_%s"%x for x in range(60,67)]
#outhists = outhists+ ["Trigger_%s"%x for x in range(68,70)]
#outhists = outhists+ ["Trigger_%s"%x for x in range(71,73)]
for ohist in outhists:
  with open("outhists/myhistos_%s.p"%(ohist), "rb") as pkl_file:
      print(ohist)
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if "PFcand_dR" in name or "res" in name or "gen" in name or "alldR" in name:
          continue
        if isinstance(h, hist.Hist):
          temphist = h.copy()
          scaled[name] = scaled[name]+temphist
with open("outhists/myhistos_Trigger.p", "wb") as pkl_file:
        pickle.dump(scaled, pkl_file)
