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
with open("myhistos_HT2000_0.p", "rb") as pkl_file:
    out = pickle.load(pkl_file)
    print(out)
    lumi = 59.74*1000
    xsec = 5962
    #nevents = out["sumw"]["sig400"]
    nevents = out["sumw"]["HT2000"]
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

    fig, ax1 = plt.subplots()
    
    hx = hist.plotratio(
        out["trigdist_ht"].integrate("cut",slice(2,3)),out["trigdist_ht"].integrate("cut",slice(0,1)),
        ax=ax1,
        error_opts={'color': 'k', 'marker': '.'},
        unc='clopper-pearson'
        #overlay="cut",
        #stack=False,
        #fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
    )
    ax1.set_ylim(0,1.1)
    hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
    fig.savefig("Plots/trigHtnoref_%s"%("ht"))
    plt.close()
    fig, ax1 = plt.subplots()
    
    hx = hist.plotratio(
        out["trigdist_ht"].integrate("cut",slice(1,2)),out["trigdist_ht"].integrate("cut",slice(0,1)),
        ax=ax1,
        error_opts={'color': 'k', 'marker': '.'},
        unc='clopper-pearson'
        #overlay="cut",
        #stack=False,
        #fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
    )
    ax1.set_ylim(0,1.1)
    hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
    fig.savefig("Plots/trigMunoref_%s"%("ht"))
    plt.close()
    fig, ax1 = plt.subplots()
    
    hx = hist.plotratio(
        out["trigdist_ht"].integrate("cut",slice(2,3)),out["trigdist_ht"].integrate("cut",slice(1,2)),
        ax=ax1,
        error_opts={'color': 'k', 'marker': '.'},
        unc='clopper-pearson'
        #overlay="cut",
        #stack=False,
        #fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
    )
    ax1.set_ylim(0,1.1)
    hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
    fig.savefig("Plots/trigHtMu_%s"%("ht"))
    plt.close()
#    print(out["trigdist_ht"].to_hist().to_numpy())    
#    fig, ax1 = plt.subplots()
#    
#    hx = hist.plot2d(
#        out["trigdist_ht"],
#        ax=ax1,
#        xaxis="cut",
#        #overlay="cut",
#        #stack=False,
#        #fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
#    )
#    ax1.set_ylim(0,1.1)
#    hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
#    fig.savefig("Plots/trigproccess2d_%s"%("ht"))
#    plt.close()

