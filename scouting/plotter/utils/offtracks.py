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

pt_bins = np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50])
eta_bins = np.array(range(-250,275,25))/100.
phi_bins = np.array(range(-31,31,5))/10.
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
with open(directory+"%s.p"%("myhistos_QCD_2018"), "rb") as pkl_file:
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
  if(var=="eta"):
    ax1.set_xlabel("Eta")
  elif(var=="phi"):
    ax1.set_xlabel("Phi")
  else:
    ax1.set_xlabel("pt [GeV]")
  fig.subplots_adjust(hspace=.07)


  b = scouting["dist_offlinetrk_%s"%var].integrate("cut",slice(2,3))#.to_hist().to_numpy()

  d = scouting["dist_PFcand_%s"%var].integrate("cut",slice(2,3))#.to_hist().to_numpy()

  hx1 = hist.plotratio(
      d,b,
      ax=ax1,
      error_opts={'color': 'r', 'marker': '.'},
      unc='clopper-pearson'
  )

  #fig.savefig("Plots/offline_scouting_compare_%s.%s"%(var,ext))
  #plt.close()
  #fig, ax1 = plt.subplots()
  hx = hist.plot1d(
        b,
        ax=ax,
        #overlay="cut",
        stack=False,
        fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
    )
  #fig.savefig("Plots/offline_scouting_pfcand_%s.%s"%(var,ext))
  #plt.close()
  #fig, ax1 = plt.subplots()
  hx = hist.plot1d(
        d,
        ax=ax,
        #overlay="cut",
        stack=False,
        clear=False,
        fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
    )
  label_list=[]
  for t in ax.get_legend_handles_labels():
    label_list.append(t)

  ax.legend(handles=label_list[0], labels=["Offline","Scouting"])
  #ax.legend(labels=["Offline","Scouting"])
  ax1.axhline(y=1,color="grey",ls="--")
  #ax.set_ylim(0,1.1)
  ax1.set_ylabel("Scouting/Offline")
  ax1.set_ylim(0.0,1.1)
  ax.set_xlabel("")
  fig.suptitle("Offline vs Scouting: %s"%(var))
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
  fig.savefig("Plots/offline_scouting_compare_%s.%s"%(var,ext))
  plt.close()
def make_plots2d(var1="pt",var2="eta"):

  fig, (ax) = plt.subplots(
  )
  ax.set_ylabel("pt [GeV]")
  ax.set_xlabel("eta")


  off = scouting["dist_offlinetrk_%s_%s"%(var1,var2)].integrate("cut",slice(2,3))#.to_hist().to_numpy()

  scout = scouting["dist_PFcand_%s_%s"%(var1,var2)].integrate("cut",slice(2,3))#.to_hist().to_numpy()

  off_vals = off.to_hist().to_numpy()[0]
  scout_vals = scout.to_hist().to_numpy()[0]
  rat_vals = np.divide(scout_vals,off_vals)
  print(off_vals)
  print(scout_vals)
  print(rat_vals)

  X,Y = np.meshgrid(off.to_hist().to_numpy()[2],off.to_hist().to_numpy()[1])
  h3 = ax.pcolor(X,Y,rat_vals)

  fig.colorbar(h3)
  fig.suptitle("Offline vs Scouting Track Ratio Map")
  np.savetxt("../systematics/triggers/track_drop_full_2018.txt",np.nan_to_num(rat_vals), delimiter=",")
  fig.savefig("Plots/trackhist2dratio_%s_%s.png"%(var1,var2))
  plt.close()


make_plots("pt")
make_plots("eta")
make_plots("phi")
make_plots2d("pt","eta")
