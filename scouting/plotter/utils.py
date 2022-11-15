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
year = "Run3"
#year = 2017
ext="png"
#ext="pdf"
pd.set_option("precision",2)

parameters = {'axes.labelsize': 20,
          'axes.titlesize': 20,
          'legend.fontsize':10
          }
plt.rcParams.update(parameters)
if year == 2018:
  lumi = 59.69*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
if year == 2017:
  lumi = 36.74*1000 #lumi for 2017 scouting #
if year == 2016:
  lumi = 35.48*1000 #lumi for 2016 scouting #
if year == "Run3":
  lumi = 96.43*1000 #lumi for 2018+2017 scouting #
  #lumi = 131.91*1000 #lumi for 2018+2017 scouting #
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
def load_all(year):
  qcdscaled = {}
  qcddatascaled = {}
  qcddatafullscaled = {}
  datascaled = {}
  datafullscaled = {}
  trigscaled = {}
  qcdtrigscaled = {}
  datafulllumi = 0
  if year == 2018:
    lumi = 59.69*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
  if year == 2017:
    lumi = 36.74*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
  if year == 2016:
    lumi = 35.48*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
  with open(directory+"myhistos_Data_%s.p"%year, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if isinstance(h, hist.Hist):
          datafullscaled[name] = h.copy()
      h1 = datafullscaled["dist_ht"].integrate("cut",slice(2,3))
      datafulllumi = sum(h1.values(sumw2=True)[()][0])
  with open(directory+"myhistos_Data1_%s.p"%year, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if isinstance(h, hist.Hist):
          datascaled[name] = h.copy()
      h1 = datascaled["dist_ht"].integrate("cut",slice(2,3))
      datalumi = sum(h1.values(sumw2=True)[()][0])
  #with open(directory+"myhistos_MCTrigger_%s.p"%year, "rb") as pkl_file:
  with open(directory+"myhistos_QCD_%s.p"%year, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if isinstance(h, hist.Hist):
          qcdtrigscaled[name] = h.copy()
          qcdtrigscaled[name].scale(lumi)
  with open(directory+"myhistos_Trigger_%s.p"%year, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if isinstance(h, hist.Hist):
          trigscaled[name] = h.copy()
          trigscaled[name].scale(lumi)
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
  return qcdscaled, qcddatascaled,qcddatafullscaled,datascaled,datafullscaled,trigscaled, qcdtrigscaled
def load_samples(sample,year,systematic=""):
      sigscaled = {}
      if year == 2018:
        lumi = 59.69*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
      if year == 2017:
        lumi = 36.74*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
      if year == 2016:
        lumi = 35.48*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
      with open(directory+"myhistos_%s%s_%s.p"%(sample,systematic,year), "rb") as pkl_file:
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
      return sigscaled







def merge_years(dic1,dic2):
  dic3 = {}
  for key in dic1:
    dic3[key] = dic1[key]
    dic3[key].add(dic2[key])
  return dic3


sig125scaled_sys = {} 
sig200scaled_sys = {}
sig300scaled_sys = {}
sig400scaled_sys = {}
sig700scaled_sys = {}
sig1000scaled_sys = {}
if year == "Run3":
  qcdscaled_18, qcddatascaled_18,qcddatafullscaled_18,datascaled_18,datafullscaled_18,trigscaled_18,qcdtrigscaled_18 = load_all(2018)
  qcdscaled_17, qcddatascaled_17,qcddatafullscaled_17,datascaled_17,datafullscaled_17,trigscaled_17,qcdtrigscaled_17 = load_all(2017)

  qcdscaled = merge_years(qcdscaled_18,qcdscaled_17) 
  qcddatascaled = merge_years(qcddatascaled_18,qcddatascaled_17) 
  qcddatafullscaled = merge_years(qcddatafullscaled_18,qcddatafullscaled_17) 
  datascaled = merge_years(datascaled_18,datascaled_17) 
  datafullscaled = merge_years(datafullscaled_18,datafullscaled_17) 
  trigscaled = merge_years(trigscaled_18,trigscaled_17) 
  qcdtrigscaled = merge_years(qcdtrigscaled_18,qcdtrigscaled_17) 

  sig125scaled_18 =   load_samples("sig125_2",2018)
  sig200scaled_18 =   load_samples("sig200_2",2018)
  sig300scaled_18 =   load_samples("sig300_2",2018)
  sig400scaled_18 =   load_samples("sig400_2",2018)
  sig700scaled_18 =   load_samples("sig700_2",2018)
  sig1000scaled_18 =  load_samples("sig1000_2",2018)
  sig125scaled_17 =   load_samples("sig125_2",2017)
  sig200scaled_17 =   load_samples("sig200_2",2017)
  sig300scaled_17 =   load_samples("sig300_2",2017)
  sig400scaled_17 =   load_samples("sig400_2",2017)
  sig700scaled_17 =   load_samples("sig700_2",2017)
  sig1000scaled_17 =  load_samples("sig1000_2",2017)

  sig125scaled = merge_years(sig125scaled_18,sig125scaled_17)  
  sig200scaled = merge_years(sig200scaled_18,sig200scaled_17)  
  sig300scaled = merge_years(sig300scaled_18,sig300scaled_17)  
  sig400scaled = merge_years(sig400scaled_18,sig400scaled_17)  
  sig700scaled = merge_years(sig700scaled_18,sig700scaled_17)  
  sig1000scaled = merge_years(sig1000scaled_18,sig1000scaled_17)  
  for sys in ["","killtrk","AK4up","AK4down","trigup","trigdown","PUup","PUdown","PSup","PSdown","Prefireup","Prefiredown"]:
    sig125scaled_sys_18=   load_samples("sig125_2",2018,sys)
    sig200scaled_sys_18=   load_samples("sig200_2",2018,sys)
    sig300scaled_sys_18=   load_samples("sig300_2",2018,sys)
    sig400scaled_sys_18=   load_samples("sig400_2",2018,sys)
    sig700scaled_sys_18=   load_samples("sig700_2",2018,sys)
    sig1000scaled_sys_18 =  load_samples("sig1000_2",2018,sys)
    sig125scaled_sys_17=   load_samples("sig125_2",2017,sys)
    sig200scaled_sys_17=   load_samples("sig200_2",2017,sys)
    sig300scaled_sys_17=   load_samples("sig300_2",2017,sys)
    sig400scaled_sys_17=   load_samples("sig400_2",2017,sys)
    sig700scaled_sys_17=   load_samples("sig700_2",2017,sys)
    sig1000scaled_sys_17 =  load_samples("sig1000_2",2017,sys)

    sig125scaled_sys[sys] =  merge_years(sig125scaled_sys_18,sig125scaled_sys_17) 
    sig200scaled_sys[sys] =  merge_years(sig200scaled_sys_18,sig200scaled_sys_17) 
    sig300scaled_sys[sys] =  merge_years(sig300scaled_sys_18,sig300scaled_sys_17) 
    sig400scaled_sys[sys] =  merge_years(sig400scaled_sys_18,sig400scaled_sys_17) 
    sig700scaled_sys[sys] =  merge_years(sig700scaled_sys_18,sig700scaled_sys_17) 
    sig1000scaled_sys[sys] = merge_years(sig1000scaled_sys_18,sig1000scaled_sys_17) 
  sig125scaled_sys_18=   load_samples("sig125_2",2018,"higgsup")
  sig125scaled_sys_17=   load_samples("sig125_2",2017,"higgsup")
  sig125scaled_sys["higgsup"] =  merge_years(sig125scaled_sys_18,sig125scaled_sys_17) 
  sig125scaled_sys_181=   load_samples("sig125_2",2018,"higgsdown")
  sig125scaled_sys_171=   load_samples("sig125_2",2017,"higgsdown")
  sig125scaled_sys["higgsdown"] =  merge_years(sig125scaled_sys_181,sig125scaled_sys_171) 
else:
  qcdscaled, qcddatascaled,qcddatafullscaled,datascaled,datafullscaled,trigscaled,qcdtrigscaled = load_all(year)
  sig125scaled =   load_samples("sig125_2",year)
  sig200scaled =   load_samples("sig200_2",year)
  sig300scaled =   load_samples("sig300_2",year)
  sig400scaled =   load_samples("sig400_2",year)
  sig700scaled =   load_samples("sig700_2",year)
  sig1000scaled =  load_samples("sig1000_2",year)

  for sys in ["","killtrk","AK4up","AK4down","trigup","trigdown","PUup","PUdown","PSup","PSdown","Prefireup","Prefiredown"]:
    sig125scaled_sys[sys] =   load_samples("sig125_2",year,sys)
    sig200scaled_sys[sys] =   load_samples("sig200_2",year,sys)
    sig300scaled_sys[sys] =   load_samples("sig300_2",year,sys)
    sig400scaled_sys[sys] =   load_samples("sig400_2",year,sys)
    sig700scaled_sys[sys] =   load_samples("sig700_2",year,sys)
    sig1000scaled_sys[sys] =  load_samples("sig1000_2",year,sys)
  sig125scaled_sys["higgsup"] =  load_samples("sig125_2",year,"higgsup")
  sig125scaled_sys["higgsdown"] =  load_samples("sig125_2",year,"higgsdown")

sigscaled = {"sig125":sig125scaled,"sig200":sig200scaled,"sig300":sig300scaled,"sig400":sig400scaled,"sig700":sig700scaled,"sig1000":sig1000scaled}
sigscaled_sys = {"sig125":sig125scaled_sys,"sig200":sig200scaled_sys,"sig300":sig300scaled_sys,"sig400":sig400scaled_sys,"sig700":sig700scaled_sys,"sig1000":sig1000scaled_sys}
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
