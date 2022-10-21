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

#year = 2018
year = 2017
#ext="png"
ext="pdf"
pd.set_option("precision",2)

parameters = {'axes.labelsize': 20,
          'axes.titlesize': 20,
          'legend.fontsize':10
          }
plt.rcParams.update(parameters)
if year == 2018:
  lumi = 59.69*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
if year == 2017:
  lumi = 36.74*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
if year == 2016:
  lumi = 35.48*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
if year == "Run3":
  lumi = 131.91*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
xsecs = {"RunA_0":0,"RunA":0,"QCD":lumi,"sig1000":0.185,"sig700":0.621,"sig400":3.16,"sig300":6.59,"sig200":16.9,"sig125":45.2,"HT2000":25.24} #1000-200
#xsecs = {"RunA_0":0,"RunA":0,"QCD":lumi,"sig1000":0.17,"sig700":0.5,"sig400":5.9,"sig300":8.9,"sig200":13.6,"HT2000":25.24} #1000-200
colors = ["black","red","green","orange","blue","magenta","cyan","yellow","brown","grey","indigo"]
cuts=["0:None","1:HTTrig","2:HT>=560","3:FJ>=2","4:nPFCand>=140"]
sigcolors = {"sig1000":"green","sig700":"cyan","sig400":"blue","sig300":"orange","sig200":"magenta","sig125":"saddlebrown","RunA":"black","QCD":"wheat"}
labels = {"sig1000":r"$m_{\phi}$ = 1000 GeV","sig700":r"$m_{\phi}$ = 700 GeV","sig400":r"$m_{\phi}$ = 400 GeV","sig300":r"$m_{\phi}$ = 300 GeV","sig200":r"$m_{\phi}$ = 200 GeV","sig125":r"$m_{\phi}$ = 125 GeV","RunA":"Data(1%)","QCD":"QCD","Data":"Data(100% RunA)","Trigger":"Trigger Data (100%)"}

selection = ["Selection:\n None","Selection:\nTrigger","Selection:\nTrigger\n %s>560 GeV"%(r"$H_{t}$"),"Selection:\nTrigger\n %s>560 GeV\n 2+ AK15 Jets"%(r"$H_{t}$"),"Selection:\n Trigger\n %s>560 GeV\n 2+ AK15 Jets\n nPFcands>70"%(r"$H_{t}$")]

region_cuts_tracks = [70,85,90,105] #gap, R1,R2,R3
region_cuts_sphere = [50,80,65,50]
inner_tracks = 20
inner_sphere = 38

directory = "../outhists/"
qcdscaled = {}
qcddatascaled = {}
qcddatafullscaled = {}
datascaled = {}
datafullscaled = {}
trigscaled = {}
datafulllumi = 0
with open(directory+"myhistos_Data_%s.p"%year, "rb") as pkl_file:
    out = pickle.load(pkl_file)
    for name, h in out.items():
      if isinstance(h, hist.Hist):
        datafullscaled[name] = h.copy()
    h1 = datafullscaled["dist_ht"].integrate("cut",slice(2,3))
    datafulllumi = sum(h1.values(sumw2=True)[()][0])
with open(directory+"myhistos_RunA.p", "rb") as pkl_file:
    out = pickle.load(pkl_file)
    for name, h in out.items():
      if isinstance(h, hist.Hist):
        datascaled[name] = h.copy()
    h1 = datascaled["dist_ht"].integrate("cut",slice(2,3))
    datalumi = sum(h1.values(sumw2=True)[()][0])
#with open(directory+"myhistos_Trigger_%s.p"%year, "rb") as pkl_file:
with open(directory+"myhistos_Trigger_%s.p"%2018, "rb") as pkl_file:
    out = pickle.load(pkl_file)
    for name, h in out.items():
      if isinstance(h, hist.Hist):
        trigscaled[name] = h.copy()
#with open(directory+"myhistos_HT2000_0.p", "rb") as pkl_file:
with open(directory+"myhistos_QCD_%s.p"%year, "rb") as pkl_file:
    out = pickle.load(pkl_file)
    h1 = out["dist_ht"].integrate("cut",slice(2,3))
    qcdlumi = sum(h1.values(sumw2=True)[()][0])
    print("qcd: ",qcdlumi)
    print("data: ",datalumi)
    print("datafull: ",datafulllumi)
    for name, h in out.items():
      if isinstance(h, hist.Hist):
        qcdscaled[name] = h.copy()
        qcdscaled[name].scale(lumi)
        qcddatascaled[name] = h.copy()
        qcddatascaled[name].scale(datalumi/qcdlumi)
        qcddatafullscaled[name] = h.copy()
        qcddatafullscaled[name].scale(datafulllumi/qcdlumi)
def load_samples(sigscaled,sample):
      with open(directory+"myhistos_%s.p"%(sample), "rb") as pkl_file:
          out = pickle.load(pkl_file)
          sample = sample.split("_")[0]
          xsec = xsecs[sample.split("_")[0]]
          if xsec ==0:
            scale = 1
          else:
            scale= lumi*xsec/out["sumw"][sample]
          for name, h in out.items():
            if isinstance(h,hist.Hist):
              sigscaled[name] = h.copy()
              sigscaled[name].scale(scale) 
sig125scaled = {}
sig200scaled = {}
sig300scaled = {}
sig400scaled = {}
sig700scaled = {}
sig1000scaled = {}
load_samples(sig125scaled,"sig125_2")
load_samples(sig200scaled,"sig200_2")
load_samples(sig300scaled,"sig300_2")
load_samples(sig400scaled,"sig400_2")
load_samples(sig700scaled,"sig700_2")
load_samples(sig1000scaled,"sig1000_2")
sigscaled = {"sig125":sig125scaled,"sig200":sig200scaled,"sig300":sig300scaled,"sig400":sig400scaled,"sig700":sig700scaled,"sig1000":sig1000scaled}
def xbins(a):
  return [0.5*(t - s)+s for s, t in zip(a, a[1:])]
def xbins_err(a):
  return [0.5*(t - s) for s, t in zip(a, a[1:])]

def func(x,a,b,c,d):
  return a*scipy.special.erf((x-b)/c)+d

def get_sig(s,sb,rangex):
  sig = []
  bkg = []
  for i in range(len(rangex)):
    sig.append(np.sum(s[i:]))
    bkg.append(np.sum(sb[i:]))
  return(sig,bkg)
def get_sig2d(s,sb,rangex,rangey):
  sig = []
  bkg = []
  for i in range(len(rangex)):
    sig1 = []
    bkg1 = []
    for j in range(len(rangey)):
      sig1.append(np.sum(s[i:,j:]))
      bkg1.append(np.sum(sb[i:,j:]))
    sig.append(sig1)
    bkg.append(bkg1)
  return(sig,bkg)
