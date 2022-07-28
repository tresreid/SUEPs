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
with open("outhists/myhistos_RunA_0.p", "rb") as pkl_file:
    out = pickle.load(pkl_file)
    for name, h in out.items():
      if "PFcand_dR" in name or "res" in name or "gen" in name or "alldR" in name or "scalar" in name:
        continue
      if isinstance(h, hist.Hist):
        #print(name)
        scaled[name] = h.copy()
outhists = ["RunA_%s"%x for x in range(1,6)]
outhists = outhists + ["RunA_%s"%x for x in range(7,20)]
outhists = outhists+ ["RunA_%s"%x for x in range(21,22)]
outhists = outhists+ ["RunA_%s"%x for x in range(24,47)]
outhists = outhists+ ["RunA_%s"%x for x in range(48,49)]
outhists = outhists+ ["RunA_%s"%x for x in range(50,90)]
outhists = outhists+ ["RunA_%s"%x for x in range(91,99)]
#outhists = outhists+ ["RunA_%s"%x for x in range(70,82)]
#outhists = outhists+ ["RunA_%s"%x for x in range(84,97)]
#outhists = outhists+ ["RunA_%s"%x for x in range(98,99)]
#print(outhists)

for ohist in outhists:
  with open("outhists/myhistos_%s.p"%(ohist), "rb") as pkl_file:
      print(ohist)
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if "PFcand_dR" in name or "res" in name or "gen" in name or "alldR" in name or "scalar" in name:
          continue
        if isinstance(h, hist.Hist):
          temphist = h.copy()
          scaled[name] = scaled[name]+temphist
with open("outhists/myhistos_Data.p", "wb") as pkl_file:
        pickle.dump(scaled, pkl_file)
