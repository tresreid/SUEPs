import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib
import pandas as pd
import gc
import multiprocessing as mp
from pathlib import Path
from scipy.optimize import curve_fit
import seaborn as sns
from scipy.stats import binned_statistic_2d, binned_statistic
from matplotlib.colors import LogNorm, Normalize
import uproot
from plotter import *
from plotter2 import *



cutvals = [0,1,600,2,200]
pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50,200])
eta_bins = np.array(range(-250,250,25))/100.
phi_bins = np.array(range(-31,31,5))/10.
xsecs = [5962,1207,119.9,25.24] #700-200 in order # signal xsec are (125,34.8),(300,8.9), (400,5.9), (750,0.5), (1000,0.17)
#files = [700,1000,1500,2000]
xsec = [0.17,0.5,5.9,8.9,13.6] #1000-200

cutflowHt = ["triggerHT","triggerHT","ht","n_fatjet","n_pfcand"]
cutvalsHt = [0,1,600,2,200]
cutflowMu = ["triggerMu","triggerMu","n_pfMu","n_fatjet","n_pfcand"]
cutvalsMu = [0,1,4,2,200]

def runPlotSet(df,sig,cutflow,cutvals):
  plot_distribution(df,sig,"ht",range(0,1500,10)                                      ,cutflow,cutvals,0,1)
  plot_distribution(df,sig,"n_pfcand",range(0,550,10)                                 ,cutflow,cutvals,0,1)
  plot_distribution(df,sig,"event_sphericity",[x*0.01 for x in range(0,100,1)]        ,cutflow,cutvals,0,1)
  plot_distribution(df,sig,"eventBoosted_sphericity",[x*0.01 for x in range(0,100,1)] ,cutflow,cutvals,0,1)
  plot_distribution(df,sig,"n_jet",range(0,20,1)                                      ,cutflow,cutvals,0,1)
  plot_distribution(df,sig,"n_fatjet",range(0,10,1)                                   ,cutflow,cutvals,0,1)
#  plot_distribution(df,sig,"n_pfMu",range(0,10,1)                                     ,cutflow,cutvals,0,1) #not in QCD Yet
def runPlotSetJet(df,sig,cutflow,cutvals,pf): 
  plot_distributionv2(pf,df,sig,"Jet_pt",range(0,500,10)                               ,cutflow,cutvals,0,1)
  plot_distributionv2(pf,df,sig,"Jet_eta",eta_bins                                    ,cutflow,cutvals,0,0)
  plot_distributionv2(pf,df,sig,"Jet_phi",phi_bins                                    ,cutflow,cutvals,0,0)
def runPlotSetFatJet(df,sig,cutflow,cutvals,pf2):
  plot_distributionv2(pf2,df,sig,"FatJet_pt",range(0,500,10)                            ,cutflow,cutvals,0,1)
  plot_distributionv2(pf2,df,sig,"FatJet_eta",eta_bins                                 ,cutflow,cutvals,0,0)
  plot_distributionv2(pf2,df,sig,"FatJet_phi",phi_bins                                 ,cutflow,cutvals,0,0)
def runPlotSetTracks(df,sig,cutflow,cutvals,pf3):
  plot_distributionv2(pf3,df,sig,"PFcand_pt",range(0,100,1)                ,cutflow,cutvals,0,1)
  plot_distributionv2(pf3,df,sig,"PFcand_eta",eta_bins                ,cutflow,cutvals,0,0)
  plot_distributionv2(pf3,df,sig,"PFcand_phi",phi_bins                ,cutflow,cutvals,0,0)

#signam = ["sig400_darkPho","sig400_darkPhoHad","sig400_generic","sig200_darkPho","sig200_darkPhoHad","sig200_generic"]
#for sig in signam:
#  df, pfJet,pfFat,pftrack = openReco("newData_ntrack/%s_ntrack.root"%sig,5.9,0)
##  trigger(df,sig) 
#  runPlotSet(df,sig,cutflowHt,cutvalsHt)
#  runPlotSetJet(df,sig,cutflowHt,cutvalsHt,pfJet)
#  runPlotSetFatJet(df,sig,cutflowHt,cutvalsHt,pfFat)
#  runPlotSetTracks(df,sig,cutflowHt,cutvalsHt,pftrack)
#  plot_distribution(df,sig,"n_pfMu",range(0,10,1)                                     ,cutflowHt,cutvalsHt,0,1)
#
#  runPlotSet(df,sig+"MU",cutflowMu,cutvalsMu)
#  runPlotSetJet(df,sig+"MU",cutflowMu,cutvalsMu,pfJet)
#  runPlotSetFatJet(df,sig+"MU",cutflowMu,cutvalsMu,pfFat)
#  runPlotSetTracks(df,sig+"MU",cutflowMu,cutvalsMu,pftrack)
#  plot_distribution(df,sig+"MU","n_pfMu",range(0,10,1)                                     ,cutflowMu,cutvalsMu,0,1)
#  del df
#  del pfJet
#  del pfFat
#  del pftrack
#  gc.collect()


#QCD
#dfqcd, pfJetqcd,pfFatqcd = openReco("HT700",5962,2)
dfqcd = openReco("HT700",5962,2)
# trigger(df,sig)

runPlotSet(dfqcd,"QCD700",cutflowHt,cutvalsHt)
#runPlotSetJet(dfqcd,"QCD700",cutflowHt,cutvalsHt,pfJetqcd)
#runPlotSetFatJet(dfqcd,"QCD700",cutflowHt,cutvalsHt,pfFatqcd)

#  plot_distribution(df,sig+"Mu","ht",range(0,1500,10)                      ,cutflow,cutvals,0,1)
#  plot_distribution(df,sig+"Mu","n_pfcand",range(0,550,10)                ,cutflow,cutvals,0,1)
#  plot_distribution(df,sig+"Mu","event_sphericity",[x*0.01 for x in range(0,100,1)]        ,cutflow,cutvals,0,1)
#  plot_distribution(df,sig+"Mu","eventBoosted_sphericity",[x*0.01 for x in range(0,100,1)] ,cutflow,cutvals,0,1)
#  plot_distribution(df,sig+"Mu","n_jet",range(0,20,1)                   ,cutflow,cutvals,0,1)
#  plot_distribution(df,sig+"Mu","n_fatjet",range(0,10,1)                ,cutflow,cutvals,0,1)
#  plot_distribution(df,sig+"Mu","n_pfMu",range(0,10,1)                ,cutflow,cutvals,0,1)
#  #plot_distributionv2(pfsig400_darkPho,dfsig400_darkPho,"sig400DarkPho","PFcand_pt",range(0,100,1)                ,cutflow,cutvals,0,1)
#  #plot_distributionv2(pfsig400_darkPho,dfsig400_darkPho,"sig400DarkPho","PFcand_eta",eta_bins                ,cutflow,cutvals,0,0)
#  #plot_distributionv2(pfsig400_darkPho,dfsig400_darkPho,"sig400DarkPho","PFcand_phi",phi_bins                ,cutflow,cutvals,0,0)



#make_2d_correlation(hltsignal,"sig300", "ht",range(0,1500,10), "eventBoosted_sphericity",[x*0.01 for x in range(0,100,1)])
#make_2d_correlation(hltsignal,"sig300", "ht",range(0,1500,10), "event_sphericity",[x*0.01 for x in range(0,100,1)])
#make_2d_correlation(hltMC,"MC", "ht",range(0,1500,10), "eventBoosted_sphericity",[x*0.01 for x in range(0,100,1)])
#make_2d_correlation(hltMC,"MC", "ht",range(0,1500,10), "event_sphericity",[x*0.01 for x in range(0,100,1)])
#make_2d_correlation(hltdata,"DataPFComm", "ht",range(0,1500,10), "eventBoosted_sphericity",[x*0.01 for x in range(0,100,1)])
#make_2d_correlation(hltdata,"DataPFComm", "ht",range(0,1500,10), "event_sphericity",[x*0.01 for x in range(0,100,1)])






