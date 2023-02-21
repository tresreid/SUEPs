import awkward as ak
from coffea import hist, processor
import uproot
from coffea.nanoevents import NanoEventsFactory, BaseSchema
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import uproot
import pickle
import pandas as pd
from numpy import unravel_index
import heapq
from scipy.optimize import curve_fit
import scipy
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from matplotlib.offsetbox import AnchoredText
from matplotlib.colors import LogNorm
from root_numpy import array2hist, hist2array
import ROOT
from utils import *

#offline = {}
scouting = {} 
lumi = 1
#directory = "../../outhists/"
#ext="png"
#year=2018
#with open(directory+"%s.p"%("myhistos_QCD_2018_offline_nodrop"), "rb") as pkl_file:
#     out = pickle.load(pkl_file)
#     for name, h in out.items():
#       if isinstance(h, hist.Hist):
#         offline[name] = h.copy()
#         offline[name].scale(lumi)
with open(directory+"%s.p"%("myhistos_QCD_2018_offline"), "rb") as pkl_file:
     out = pickle.load(pkl_file)
     for name, h in out.items():
       if isinstance(h, hist.Hist):
         scouting[name] = h.copy()
         scouting[name].scale(lumi)


def make_plots(var="ht"):

  fig, (ax,ax1) = plt.subplots(
  nrows=2,
  ncols=1,
  figsize=(7,7),
  gridspec_kw={"height_ratios": (3, 1)},
  sharex=True
  )
  if(var=="event_sphericity"):
    xs = np.linspace(0,1,100)
    ax1.set_xlabel("Event Sphericity (unbooosted)")
  elif(var=="FatJet_nconst"):
    xs = np.linspace(0,300,100)
    ax1.set_xlabel("SUEP Jet Track Multiplicity")
  else:
    xs = np.linspace(0,1500,100)
    ax1.set_xlabel("Ht [GeV]")
  fig.subplots_adjust(hspace=.07)


  b = scouting["dist_offlinetrk_%s"%var].integrate("cut",slice(2,3))#.to_hist().to_numpy()

  d = scouting["dist_PFcand_%s"%var].integrate("cut",slice(2,3))#.to_hist().to_numpy()
  hx1 = hist.plotratio(
      d,b,
      ax=ax,
      error_opts={'color': 'r', 'marker': '.'},
      unc='clopper-pearson'
  )

  ax1.axhline(y=1,color="grey",ls="--")
  ax.set_ylim(0,1.1)
  ax1.set_ylabel("Data/QCD")
  ax1.set_ylim(0.5,1.5)
  ax.set_xlabel("")
  ax.set_ylabel("Efficiency")
  ax.legend(loc="lower right")
  fig.suptitle("HT Trigger Efficiency DoubleMu3 Reference: Data")
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
  fig.savefig("Plots/offline_scouting_compare_%s.%s"%(var,ext))
  plt.close()

make_plots("pt")
make_plots("eta")
make_plots("phi")
