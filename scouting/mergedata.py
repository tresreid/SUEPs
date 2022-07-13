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
      if "PFcand_dR" in name or "res" in name or "gen" in name:
        continue
      if isinstance(h, hist.Hist):
        #print(name)
        scaled[name] = h.copy()
outhists = ["RunA_%s"%x for x in range(1,15)]
#outhists = outhists+ ["RunA_%s"%x for x in range(7,23)]
#outhists = outhists+ ["RunA_%s"%x for x in range(25,27)]
#outhists = outhists+ ["RunA_%s"%x for x in range(28,54)]
#outhists = outhists+ ["RunA_%s"%x for x in range(55,57)]
#outhists = outhists+ ["RunA_%s"%x for x in range(59,62)]
#outhists = outhists+ ["RunA_%s"%x for x in range(63,69)]
#outhists = outhists+ ["RunA_%s"%x for x in range(70,82)]
#outhists = outhists+ ["RunA_%s"%x for x in range(84,97)]
#outhists = outhists+ ["RunA_%s"%x for x in range(98,99)]
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
      for name, h in out.items():
        if "PFcand_dR" in name or "res" in name or "gen" in name:
          continue
        if isinstance(h, hist.Hist):
          temphist = h.copy()
          scaled[name] = scaled[name]+temphist
with open("outhists/myhistos_RunA.p", "wb") as pkl_file:
        pickle.dump(scaled, pkl_file)
