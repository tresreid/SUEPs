import awkward as ak
from coffea import hist, processor
import uproot
from coffea.nanoevents import NanoEventsFactory, BaseSchema
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import uproot
import pickle

with open("myhistos.p", "rb") as pkl_file:
    out = pickle.load(pkl_file)
    print(out)
    lumi = 59.74*1000
    xsec = 5962
    nevents = out["sumw"]["HT700"]
    print("nevents ",nevents)
    scaled = {}
    #fout = uproot.recreate("output.root")
    for name, h in out.items():
      if isinstance(h, hist.Hist):
        #xsec = xsecs[name]
        scaled[name] = h.copy()
        scaled[name].scale(lumi*xsec/nevents)
    
    
        fig, ax1 = plt.subplots()
    
        hx = hist.plot1d(
            scaled[name],
            ax=ax1,
            overlay="cut",
            stack=False,
            fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
        )
        hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
        fig.savefig("Plots/proccess_%s"%(name))
        plt.close()

