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
import json

year = 2016
#year = "Run2"
ext="png"
#ext="pdf"
pd.set_option("precision",2)

region_cuts_tracks = [50,50,65,80]
region_cuts_sphere = [50,50,50,50]
inner_tracks = 18
inner_sphere = 34

parameters = {'axes.labelsize': 20,
          'axes.titlesize': 20,
          'legend.fontsize':10
          }
plt.rcParams.update(parameters)
if year == 2018:
  lumi = 60.69*1000##59.69*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
if year == 2017:
  lumi = 34.62*1000#36.74*1000 #lumi for 2017 scouting #
if year == 2016:
  lumi = 30.50*1000#35.48*1000 #lumi for 2016 scouting #
if year == "Run2":
  #lumi = 96.43*1000 #lumi for 2018+2017 scouting #
  lumi = 125.81*1000#131.91*1000 #lumi for 2018+2017 scouting #
#lumi=1 #for data2016 compare

standard = True
colors = ["black","red","green","orange","blue","magenta","cyan","yellow","brown","grey","indigo"]
sigcolors = {"sig1000":"green","sig700":"cyan","sig400":"blue","sig300":"orange","sig200":"magenta","sig125":"saddlebrown","RunA":"black","QCD":"wheat"}
cuts=["0:None","1:HTTrig","2:HT>=560","3:FJ>=2","4:nPFCand>=140"]
xsecs = {}
with open ("utils/xsections_2018.json") as json_file:
  xsecs = json.load(json_file)
#xsecs["RunA"] = 0
#xsecs["RunA_0"] = 0
#xsecs["QCD"] = lumi
#print(xsecs)

#xsecs = {"RunA_0":0,"RunA":0,"QCD":lumi,"sig1000":0.185,"sig700":0.621,"sig400":3.16,"sig300":6.59,"sig200":16.9,"sig125":45.2,"HT2000":25.24} #1000-200
#genfilter_T2_phi2 = {"sig1000":0.4929149897230587,"sig700":0.2816894976779231,"sig400":0.12259774967384872,"sig300":0.08115244345939307,"sig200":0.045499775471722015,"sig125":0.022561693317296093} 
set_lumi = None
if standard:
  #labels = {"sig1000":r"$m_{S}$ = 1000 GeV","sig700":r"$m_{S}$ = 700 GeV","sig400":r"$m_{S}$ = 400 GeV","sig300":r"$m_{S}$ = 300 GeV","sig200":r"$m_{S}$ = 200 GeV","sig125":r"$m_{S}$ = 125 GeV","RunA":"Data(1%)","QCD":"TTBar","Data":"Data(100%)","Trigger":"Trigger Data (100%)"}
  labels = {"sig1000":r"$m_{S}$ = 1000 GeV","sig700":r"$m_{S}$ = 700 GeV","sig400":r"$m_{S}$ = 400 GeV","sig300":r"$m_{S}$ = 300 GeV","sig200":r"$m_{S}$ = 200 GeV","sig125":r"$m_{S}$ = 125 GeV","RunA":"Data(1%)","QCD":"QCD","Data":"Data(100%)","Trigger":"Trigger Data (100%)"}
  file_data     = "myhistos_Data_"#_%s"%(year)  
  file_data1    = "myhistos_Data1_"#_%s"%(year) 
  file_mctrig   = "myhistos_QCD_"#_%s"%(year) 
  file_datatrig = "myhistos_Trigger_"#_%s"%(year) 
  #file_qcd      = "myhistos_TTBar_"#_%s"%(year) 
  file_qcd      = "myhistos_QCD_"#_%s"%(year) 
else:
  #year=""
  #labels = {"sig1000":r"$m_{S}$ = 1000 GeV","sig700":r"$m_{S}$ = 700 GeV","sig400":r"$m_{S}$ = 400 GeV","sig300":r"$m_{S}$ = 300 GeV","sig200":r"$m_{S}$ = 200 GeV","sig125":r"$m_{S}$ = 125 GeV","RunA":"Data(1%)","QCD":"QCD","Data":"Data(100% RunA)","Trigger":"Trigger Data (100%)"}
  #labels = {"sig1000":r"$m_{S}$ = 1000 GeV","sig700":r"$m_{S}$ = 700 GeV","sig400":r"$m_{\S}$ = 400 GeV","sig300":r"$m_{S}$ = 300 GeV","sig200":r"$m_{S}$ = 200 GeV","sig125":r"$m_{S}$ = 125 GeV","RunA":"QCDOffline","QCD":"QCD","Data":"QCDOffline","Trigger":"Trigger Data (100%)"}
  #labels = {"sig1000":r"$m_{S}$ = 1000 GeV","sig700":r"$m_{S}$ = 700 GeV","sig400":r"$m_{S}$ = 400 GeV","sig300":r"$m_{S}$ = 300 GeV","sig200":r"$m_{S}$ = 200 GeV","sig125":r"$m_{S}$ = 125 GeV","RunA":"Data(1%)","QCD":"Data_2016(1%)","Data":"Data(100% RunA)","Trigger":"Trigger Data (100%)"}
  labels = {"sig1000":r"$m_{S}$ = 1000 GeV","sig700":r"$m_{S}$ = 700 GeV","sig400":r"$m_{S}$ = 400 GeV","sig300":r"$m_{S}$ = 300 GeV","sig200":r"$m_{S}$ = 200 GeV","sig125":r"$m_{S}$ = 125 GeV","RunA":"private: sig125","QCD":"central: sig125","Data":"private: sig125","Trigger":"Trigger Data (100%)"}
  #labels = {"sig1000":r"$m_{S}$ = 1000 GeV","sig700":r"$m_{S}$ = 700 GeV","sig400":r"$m_{S}$ = 400 GeV","sig300":r"$m_{S}$ = 300 GeV","sig200":r"$m_{S}$ = 200 GeV","sig125":r"$m_{S}$ = 125 GeV","RunA":"private: sig800","QCD":"central: sig800","Data":"private: sig800","Trigger":"Trigger Data (100%)"}
  #labels = {"sig1000":r"$m_{S}$ = 1000 GeV","sig700":r"$m_{S}$ = 700 GeV","sig400":r"$m_{S}$ = 400 GeV","sig300":r"$m_{S}$ = 300 GeV","sig200":r"$m_{S}$ = 200 GeV","sig125":r"$m_{S}$ = 125 GeV","RunA":"private: sig400","QCD":"central: sig400","Data":"private: sig400","Trigger":"Trigger Data (100%)"}
  #labels = {"sig1000":r"$m_{S}$ = 1000 GeV","sig700":r"$m_{S}$ = 700 GeV","sig400":r"$m_{S}$ = 400 GeV","sig300":r"$m_{S}$ = 300 GeV","sig200":r"$m_{S}$ = 200 GeV","sig125":r"$m_{S}$ = 125 GeV","RunA":"QCD 2016","QCD":"QCD 2018","Data":"QCD 2016","Trigger":"Trigger Data (100%)"}
  #labels = {"sig1000":r"$m_{S}$ = 1000 GeV","sig700":r"$m_{S}$ = 700 GeV","sig400":r"$m_{S}$ = 400 GeV","sig300":r"$m_{S}$ = 300 GeV","sig200":r"$m_{S}$ = 200 GeV","sig125":r"$m_{S}$ = 125 GeV","RunA":"QCD offline","QCD":"QCD scouting","Data":"QCD offline","Trigger":"Trigger Data (100%)"}
  #file_data     = "myhistos_Data_%s"%(year)  
  #file_data     = "myhistos_QCD_2016"#%(year)  
  #file_data1    = "myhistos_QCD_2016"#%(year) 
  file_data     = "private/myhistos_sig125_2_T1p00_phi2.000_2018" #_offline"#%(year)  
  file_data1    = "private/myhistos_sig125_2_T1p00_phi2.000_2018"#_offline"#%(year) 
  #file_data1    = "myhistos_Data1_%s"%(year) 
  file_mctrig   = "myhistos_QCD_2018"#_%s"%(year) 
  file_datatrig = "myhistos_Trigger_2018"#_%s"%(year) 
  file_qcd      = "central/myhistos_sig125_2_T1p00_phi2.000_2018" 
  #file_qcd      = "myhistos_QCD_2018" 
  #file_qcd      = "myhistos_QCD_2018_offline_scouting3" 
  #file_qcd      = "myhistos_Data_2016" 
  set_lumi = 1

#xsecs = {"RunA_0":0,"RunA":0,"QCD":lumi,"sig1000":0.17,"sig700":0.5,"sig400":5.9,"sig300":8.9,"sig200":13.6,"HT2000":25.24} #1000-200
selection = ["Selection:\n None","Selection:\nTrigger","Selection:\nTrigger\n %s>560 GeV"%(r"$H_{t}$"),"Selection:\nTrigger\n %s>560 GeV\n 2+ AK15 Jets"%(r"$H_{t}$"),"Selection:\n Trigger\n %s>560 GeV\n 2+ AK15 Jets\n nPFcands>70"%(r"$H_{t}$")]


directory = "../outhists/"
def load_all(year):
  if not standard:
    year=""
  qcdscaled = {}
  qcddatascaled = {}
  qcddatafullscaled = {}
  datascaled = {}
  datafullscaled = {}
  trigscaled = {}
  qcdtrigscaled = {}
  datafulllumi = 0
  if year == 2018:
    lumi = 60.69*1000##59.69*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
  if year == 2017:
    lumi = 34.62*1000#36.74*1000 #lumi for 2017 scouting #
  if year == 2016:
    lumi = 30.50*1000#35.48*1000 #lumi for 2016 scouting #
  #lumi=1 #for data2016 compare
  if set_lumi:
    lumi = set_lumi
  with open(directory+"%s%s.p"%(file_data,year), "rb") as pkl_file:
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if isinstance(h, hist.Hist):
          datafullscaled[name] = h.copy()
      h1 = datafullscaled["dist_ht"].integrate("cut",slice(2,3))
      datafulllumi = sum(h1.values(sumw2=True)[()][0])
  with open(directory+"%s%s.p"%(file_data1,year), "rb") as pkl_file:
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if isinstance(h, hist.Hist):
          datascaled[name] = h.copy()
      h1 = datascaled["dist_ht"].integrate("cut",slice(2,3))
      datalumi = sum(h1.values(sumw2=True)[()][0])
  with open(directory+"%s%s.p"%(file_mctrig,year), "rb") as pkl_file:
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if isinstance(h, hist.Hist):
          qcdtrigscaled[name] = h.copy()
          qcdtrigscaled[name].scale(lumi)
  with open(directory+"%s%s.p"%(file_datatrig,year), "rb") as pkl_file:
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if isinstance(h, hist.Hist):
          trigscaled[name] = h.copy()
          trigscaled[name].scale(lumi)
  with open(directory+"%s%s.p"%(file_qcd,year), "rb") as pkl_file:
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
def load_samples(sample,year,systematic="",temp="2p00",phi="2.000",mode="generic",fullscan=True):
      fullscan=True
      if fullscan:
        todir="TotalSIG/"
      else:
        todir=""
      sigscaled = {}
#      year=2018
      temp2 = temp.replace("p",".")
      temp3 = temp.split("p")[1]
      add_0 = 3- len(temp3)
      temp2 = temp2+"0"*add_0
      #if temp == "2p00" and phi=="2.000":
      #if year==2016:
      #  scan = ""
      #else:
      #  scan = "_T%s_phi%s"%(temp,phi) 
      scan = "_T%s_phi%s"%(temp,phi) 
      if year == 2018:
        lumi = 60.69*1000##59.69*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
      if year == 2017:
        lumi = 34.62*1000#36.74*1000 #lumi for 2017 scouting #
      if year == 2016:
        lumi = 30.50*1000#35.48*1000 #lumi for 2016 scouting #
      with open(directory+"%smyhistos_%s%s%s_%s.p"%(todir,sample,systematic,scan,year), "rb") as pkl_file:
          print("open: %s\n"%("%smyhistos_%s%s%s_%s.p"%(todir,sample,systematic,scan,year)))
          out = pickle.load(pkl_file)
          samplex = sample.split("_")[0]
          
          formatting = "GluGluToSUEP_HT400_T%s_mS%s.000_mPhi%s_T%s_mode%s_TuneCP5_13TeV-pythia8"%(temp,samplex[3:],phi,temp2,mode) 
          xsec1 = xsecs[formatting]["xsec"] 
          #if year == 2016:
          #  genfilter = 1
          #else:
          #  genfilter = xsecs[formatting]["kr"] 
          genfilter = xsecs[formatting]["kr"] 
          xsec = xsec1 * genfilter
          if xsec ==0:
            scale = 1
          else:
            #if year == 2016:
            #  scale= lumi*xsec/out["sumw"]["sig"+sample[3:]]
            #else:
            #  scale= lumi*xsec/out["sumw"][sample[3:]]
            scale= lumi*xsec/out["sumw"][samplex[3:]]
          for name, h in out.items():
            if isinstance(h,hist.Hist):
              sigscaled[name] = h.copy()
              sigscaled[name].scale(scale) 
      if year == 2016 and "sig" in sample:
        with open(directory+"%smyhistos_%s%s%s_%sapv.p"%(todir,sample,systematic,scan,year), "rb") as pkl_file:
            print("open: %s\n"%("%smyhistos_%s%s%s_%sapv.p"%(todir,sample,systematic,scan,year)))
            out = pickle.load(pkl_file)
            samplex = sample.split("_")[0]
            
            formatting = "GluGluToSUEP_HT400_T%s_mS%s.000_mPhi%s_T%s_mode%s_TuneCP5_13TeV-pythia8"%(temp,samplex[3:],phi,temp2,mode) 
            xsec1 = xsecs[formatting]["xsec"] 
            #if year == 2016:
            #  genfilter = 1
            #else:
            #  genfilter = xsecs[formatting]["kr"] 
            genfilter = xsecs[formatting]["kr"] 
            xsec = xsec1 * genfilter
            if xsec ==0:
              scale = 1
            else:
              #if year == 2016:
              #  scale= lumi*xsec/out["sumw"]["sig"+sample[3:]]
              #else:
              #  scale= lumi*xsec/out["sumw"][sample[3:]]
              scale= lumi*xsec/out["sumw"][samplex[3:]]
            for name, h in out.items():
              if isinstance(h,hist.Hist):
                temp = h.copy()#.scale(scale)
                temp.scale(scale)
                #sigscaled[name] = h.copy()
                #print(name)
                #print(temp)
                #print(sigscaled[name])
                sigscaled[name].add(temp) 
      return sigscaled







def merge_years(dic1,dic2,dic3,skip=False):
  dicx = {}
  for key in dic1:
    if skip and ("dist_offlinetrk_" in key or "dist_PFcand_" in key):
      continue
    dicx[key] = dic1[key]
    dicx[key].add(dic2[key])
    dicx[key].add(dic3[key])
  return dicx


sig125scaled_sys = {} 
sig200scaled_sys = {}
sig300scaled_sys = {}
sig400scaled_sys = {}
sig700scaled_sys = {}
sig1000scaled_sys = {}
if year == "Run2":
  qcdscaled_18, qcddatascaled_18,qcddatafullscaled_18,datascaled_18,datafullscaled_18,trigscaled_18,qcdtrigscaled_18 = load_all(2018)
  qcdscaled_17, qcddatascaled_17,qcddatafullscaled_17,datascaled_17,datafullscaled_17,trigscaled_17,qcdtrigscaled_17 = load_all(2017)
  qcdscaled_16, qcddatascaled_16,qcddatafullscaled_16,datascaled_16,datafullscaled_16,trigscaled_16,qcdtrigscaled_16 = load_all(2016)

  qcdscaled = merge_years(qcdscaled_18,qcdscaled_17,qcdscaled_16) 
  qcddatascaled = merge_years(qcddatascaled_18,qcddatascaled_17,qcddatascaled_16) 
  qcddatafullscaled = merge_years(qcddatafullscaled_18,qcddatafullscaled_17,qcddatafullscaled_16) 
  datascaled = merge_years(datascaled_18,datascaled_17,datascaled_16) 
  datafullscaled = merge_years(datafullscaled_18,datafullscaled_17,datafullscaled_16) 
  trigscaled = merge_years(trigscaled_18,trigscaled_17,trigscaled_16,skip=True) 
  qcdtrigscaled = merge_years(qcdtrigscaled_18,qcdtrigscaled_17,qcdtrigscaled_16) 

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
  sig125scaled_16 =   load_samples("sig125_2",2016)
  sig200scaled_16 =   load_samples("sig200_2",2016)
  sig300scaled_16 =   load_samples("sig300_2",2016)
  sig400scaled_16 =   load_samples("sig400_2",2016)
  sig700scaled_16 =   load_samples("sig700_2",2016)
  sig1000scaled_16 =  load_samples("sig1000_2",2016)

  sig125scaled = merge_years(sig125scaled_18,sig125scaled_17,sig125scaled_16)  
  sig200scaled = merge_years(sig200scaled_18,sig200scaled_17,sig200scaled_16)  
  sig300scaled = merge_years(sig300scaled_18,sig300scaled_17,sig300scaled_16)  
  sig400scaled = merge_years(sig400scaled_18,sig400scaled_17,sig400scaled_16)  
  sig700scaled = merge_years(sig700scaled_18,sig700scaled_17,sig700scaled_16)  
  sig1000scaled = merge_years(sig1000scaled_18,sig1000scaled_17,sig1000scaled_16)  
  #for sys in ["","killtrk","AK4up","AK4down","trigup","trigdown","PUup","PUdown","PSup","PSdown","Prefireup","Prefiredown"]:
  for sys in ["","_track_up","_JES_up","_JES_down","_JER_up","_JER_down","_trigSF_up","_trigSF_down","_puweights_up","_puweights_down","_PSWeight_ISR_up","_PSWeight_FSR_up","_PSWeight_ISR_down","_PSWeight_FSR_down","_prefire_up","_prefire_down"]:
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
    sig125scaled_sys_16=   load_samples("sig125_2",2016,sys)
    sig200scaled_sys_16=   load_samples("sig200_2",2016,sys)
    sig300scaled_sys_16=   load_samples("sig300_2",2016,sys)
    sig400scaled_sys_16=   load_samples("sig400_2",2016,sys)
    sig700scaled_sys_16=   load_samples("sig700_2",2016,sys)
    sig1000scaled_sys_16 =  load_samples("sig1000_2",2016,sys)

    sig125scaled_sys[sys] =  merge_years(sig125scaled_sys_18,sig125scaled_sys_17,sig125scaled_sys_16) 
    sig200scaled_sys[sys] =  merge_years(sig200scaled_sys_18,sig200scaled_sys_17,sig200scaled_sys_16) 
    sig300scaled_sys[sys] =  merge_years(sig300scaled_sys_18,sig300scaled_sys_17,sig300scaled_sys_16) 
    sig400scaled_sys[sys] =  merge_years(sig400scaled_sys_18,sig400scaled_sys_17,sig400scaled_sys_16) 
    sig700scaled_sys[sys] =  merge_years(sig700scaled_sys_18,sig700scaled_sys_17,sig700scaled_sys_16) 
    sig1000scaled_sys[sys] = merge_years(sig1000scaled_sys_18,sig1000scaled_sys_17,sig1000scaled_sys_16) 
  sig125scaled_sys_18=   load_samples("sig125_2",2018,"_higgs_weights_up")
  sig125scaled_sys_17=   load_samples("sig125_2",2017,"_higgs_weights_up")
  sig125scaled_sys_16=   load_samples("sig125_2",2016,"_higgs_weights_up")
  sig125scaled_sys["_higgs_weights_up"] =  merge_years(sig125scaled_sys_18,sig125scaled_sys_17,sig125scaled_sys_16) 
  sig125scaled_sys_181=   load_samples("sig125_2",2018,"_higgs_weights_down")
  sig125scaled_sys_171=   load_samples("sig125_2",2017,"_higgs_weights_down")
  sig125scaled_sys_161=   load_samples("sig125_2",2016,"_higgs_weights_down")
  sig125scaled_sys["_higgs_weights_down"] =  merge_years(sig125scaled_sys_181,sig125scaled_sys_171,sig125scaled_sys_161) 
else:
  qcdscaled, qcddatascaled,qcddatafullscaled,datascaled,datafullscaled,trigscaled,qcdtrigscaled = load_all(year)
  sig125scaled =   load_samples("sig125_2",year)
  sig200scaled =   load_samples("sig200_2",year)
  sig300scaled =   load_samples("sig300_2",year)
  sig400scaled =   load_samples("sig400_2",year)
  sig700scaled =   load_samples("sig700_2",year)
  sig1000scaled =  load_samples("sig1000_2",year)

  for sys in ["","_track_up","_JES_up","_JES_down","_JER_up","_JER_down","_trigSF_up","_trigSF_down","_puweights_up","_puweights_down","_PSWeight_ISR_up","_PSWeight_FSR_up","_PSWeight_ISR_down","_PSWeight_FSR_down","_prefire_up","_prefire_down"]:
  #for sys in ["","killtrk","AK4up","AK4down","trigup","trigdown","PUup","PUdown","PSup","PSdown","Prefireup","Prefiredown"]:
    print(sys)
    sig125scaled_sys[sys] =   load_samples("sig125_2",year,sys)
    sig200scaled_sys[sys] =   load_samples("sig200_2",year,sys)
    sig300scaled_sys[sys] =   load_samples("sig300_2",year,sys)
    sig400scaled_sys[sys] =   load_samples("sig400_2",year,sys)
    sig700scaled_sys[sys] =   load_samples("sig700_2",year,sys)
    sig1000scaled_sys[sys] =  load_samples("sig1000_2",year,sys)
  #sig125scaled_sys["higgsup"] =  load_samples("sig125_2",year,"higgsup")
  #sig125scaled_sys["higgsdown"] =  load_samples("sig125_2",year,"higgsdown")
  sig125scaled_sys["_higgs_weights_up"] =  load_samples("sig125_2",year,"_higgs_weights_up")
  sig125scaled_sys["_higgs_weights_down"] =  load_samples("sig125_2",year,"_higgs_weights_down")

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
