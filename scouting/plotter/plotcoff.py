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
#from ROOT import TFile
#from rootpy.plotting import Hist2D

from utils.utils import *
from utils.trigplots import *
from utils.dists import *
from utils.signalregion import *
from utils.cutflow import *
from utils.trk import *
from utils.closure import *





#############################ORGANIZE BY SECTION #######################################
#######
######
##################################### HT Trigger
########## HT Distributions
##make_dists("sig400")
#make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","sig125","QCD"],"ht",0,"Ht [GeV]",make_ratio=False,vline=[560,1200])
#make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","sig125","RunA","QCD"],"ht",1,"Ht [GeV]",vline=[560,1200])
####### Trigger Efficiency
#print("running trigger studies")
#make_datatrigs(["Data"])
#make_datatrigs(["Data"],systematics=True)
#make_sigtrigs(["sig1000","sig700","sig400","sig300","sig200","sig125"])
#
#
############################## Track Selection
#print("running track studies")
######## TRK Eff and Fakes 
##make_trkeff("sig200","dist_trkID_gen_pt","Gen pT [GeV]",runPV=2)
##make_trkeff("sig200","dist_trkID_gen_phi","Gen Phi")
##make_trkeff("sig200","dist_trkID_gen_eta","Gen Eta")
##make_trkeff("sig200","dist_trkID_gen_phi","Gen Phi",runPV=1)
##make_trkeff("sig200","dist_trkID_gen_eta","Gen Eta",runPV=1)
##make_trkeff("sig200","dist_trkIDFK_PFcand_pt","PFCand pT [GeV]") ## TODO fix fake labels
##make_trkeff("sig200","dist_trkIDFK_PFcand_phi","PFCand Phi")
##make_trkeff("sig200","dist_trkIDFK_PFcand_eta","PFCand Eta")
##make_trkeff("sig1000","dist_trkID_gen_pt","Gen pT [GeV]",runPV=2)
##make_trkeff("sig1000","dist_trkID_gen_phi","Gen Phi")
##make_trkeff("sig1000","dist_trkID_gen_eta","Gen Eta")
##make_trkeff("sig1000","dist_trkID_gen_phi","Gen Phi",runPV=1)
##make_trkeff("sig1000","dist_trkID_gen_eta","Gen Eta",runPV=1)
##make_trkeff("sig1000","dist_trkIDFK_PFcand_pt","PFCand pT [GeV]") ## TODO fix fake labels
##make_trkeff("sig1000","dist_trkIDFK_PFcand_phi","PFCand Phi")
##make_trkeff("sig1000","dist_trkIDFK_PFcand_eta","PFCand Eta")
##make_trkeff("sig400","dist_trkID_gen_pt","Gen pT [GeV]",runPV=2)
##make_trkeff("sig400","dist_trkID_gen_phi","Gen Phi")
##make_trkeff("sig400","dist_trkID_gen_eta","Gen Eta")
##make_trkeff("sig400","dist_trkID_gen_phi","Gen Phi",runPV=1)
##make_trkeff("sig400","dist_trkID_gen_eta","Gen Eta",runPV=1)
##make_trkeff("sig400","dist_trkIDFK_PFcand_pt","PFCand pT [GeV]") ## TODO fix fake labels
##make_trkeff("sig400","dist_trkIDFK_PFcand_phi","PFCand Phi")
##make_trkeff("sig400","dist_trkIDFK_PFcand_eta","PFCand Eta")
#maxpoints = {"err_sig1000":[],"err_sig700":[],"err_sig400":[],"err_sig300":[],"err_sig200":[],"err_sig125":[],"sig_sig1000":[],"sig_sig700":[],"sig_sig400":[],"sig_sig300":[],"sig_sig200":[],"sig_sig125":[],"evt_sig1000":[],"evt_sig700":[],"evt_sig400":[],"evt_sig300":[],"evt_sig200":[],"evt_sig125":[]}
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"PFcand_ncount50",4,maxpoints,"PFCand(50) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"PFcand_ncount60",4,maxpoints,"PFCand(60) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"PFcand_ncount70",4,maxpoints,"PFCand(70) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"PFcand_ncount75",4,maxpoints,"PFCand(75) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"PFcand_ncount80",4,maxpoints,"PFCand(80) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"PFcand_ncount90",4,maxpoints,"PFCand(90) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"PFcand_ncount100",4,maxpoints,"PFCand(100) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"PFcand_ncount150",4,maxpoints,"PFCand(150) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"PFcand_ncount200",4,maxpoints,"PFCand(200) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"PFcand_ncount300",4,maxpoints,"PFCand(300) Multiplicity")
#make_threshold(["sig1000","sig700","sig400","sig300","sig200","sig125"],maxpoints,[.5,.6,.7,.75,.8,.9,1.0,1.5,2,3],"Track pt threshold")
#
##make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"n_pvs",2,"nPV")
#make_overlapdists(["sig1000","sig400","sig200","sig125"],"gen_dR",2,"1-1 Minimum dR(gen,PFcand)",make_ratio=False,vline=[0.02])
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"PFcand_ncount75",2,"PFCand(75) Multiplicity")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"PFcand_pt",2,"PFCand pT [GeV]")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"PFcand_eta",2,"PFCand eta")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"PFcand_phi",2,"PFCand phi")
#
#
############################  FatJet Selection
#
#print("running Jet studies")
#make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","sig125","QCD"],"sphere1_suep",3,xlab="SUEP Sphericity",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","sig125","QCD"],"sphere1_isrsuep",3,xlab="ISR Sphericity",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","sig125"],"res_beta",0,make_ratio=False,xlab="Suep Jet beta - Scalar truth beta",shift_leg=True)
#make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","sig125"],"res_pt",0,make_ratio=False,xlab="Suep Jet pT - Scalar truth pT",shift_leg=True)
#make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","sig125"],"res_mass",0,make_ratio=False,xlab="Suep Jet mass - Scalar truth mass",shift_leg=True)
#make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","sig125"],"res_dR",0,make_ratio=False,xlab="dR(Suep Jet,Scalar truth)")
#make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","sig125"],"res_dEta",0,make_ratio=False,xlab="Suep Jet eta - Scalar truth eta")
#make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","sig125"],"res_dPhi",0,make_ratio=False,xlab="Suep Jet phi - Scalar truth phi")
#
#maxpointsfj = {"err_sig1000":[],"err_sig700":[],"err_sig400":[],"err_sig300":[],"err_sig200":[],"err_sig125":[],"sig_sig1000":[],"sig_sig700":[],"sig_sig400":[],"sig_sig300":[],"sig_sig200":[],"sig_sig125":[],"evt_sig1000":[],"evt_sig700":[],"evt_sig400":[],"evt_sig300":[],"evt_sig200":[],"evt_sig125":[]}
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"fjn1_FatJet_ncount50",2,maxpointsfj,xlab="AK15(50) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"fjn1_FatJet_ncount100",2,maxpointsfj,xlab="AK15(100) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"fjn1_FatJet_ncount150",2,maxpointsfj,xlab="AK15(150) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"fjn1_FatJet_ncount200",2,maxpointsfj,xlab="AK15(200) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"fjn1_FatJet_ncount250",2,maxpointsfj,xlab="AK15(250) Multiplicity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"fjn1_FatJet_ncount300",2,maxpointsfj,xlab="AK15(300) Multiplicity") 
#make_threshold(["sig1000","sig700","sig400","sig300","sig200","sig125"],maxpointsfj,[50,100,150,200,250,300],"AK15 pt threshold")
#
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"FatJet_pt",3,"AK15 Jet pT [GeV]")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"FatJet_eta",3,"AK15 Jet Eta")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"FatJet_phi",3,"AK15 Jet Phi")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"FatJet_ncount50",3,"AK15 Jet(50) Multiplicity")
########################### BOOSTING and sphericity
### TODO ISR removal methods
#print("running sphericity studies")
#empty = {"err_sig1000":[],"err_sig700":[],"err_sig400":[],"err_sig300":[],"err_sig200":[],"err_sig125":[],"sig_sig1000":[],"sig_sig700":[],"sig_sig400":[],"sig_sig300":[],"sig_sig200":[],"sig_sig125":[],"evt_sig1000":[],"evt_sig700":[],"evt_sig400":[],"evt_sig300":[],"evt_sig200":[],"evt_sig125":[]}
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"FatJet_nconst",3,empty,xlab="SUEP Jet Track Multiplicity") 
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"FatJet_nconst",4,empty,xlab="SUEP Jet Track Multiplicity") 
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep",3,empty,xlab="Boosted Sphericity",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep",4,empty,xlab="Boosted Sphericity",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"event_sphericity",3,empty,xlab="Unboosted Sphericity")
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"event_sphericity",4,empty,xlab="Unboosted Sphericity")
#
#
#make_overlapdists(["QCD","RunA","sig1000","sig700","sig400","sig300","sig200","sig125"],"SUEP_pt",3,"SUEP pT [GeV]",make_ratio=True)
#make_overlapdists(["QCD","RunA","sig1000","sig700","sig400","sig300","sig200","sig125"],"SUEP_eta",3,"SUEP eta",make_ratio=True)
#make_overlapdists(["QCD","RunA","sig1000","sig700","sig400","sig300","sig200","sig125"],"SUEP_phi",3,"SUEP phi",make_ratio=True)
#make_overlapdists(["QCD","RunA","sig1000","sig700","sig400","sig300","sig200","sig125"],"ISR_pt",3, "ISR pT [GeV]",make_ratio=True)
#make_overlapdists(["QCD","RunA","sig1000","sig700","sig400","sig300","sig200","sig125"],"ISR_eta",3,"ISR eta",make_ratio=True)
#make_overlapdists(["QCD","RunA","sig1000","sig700","sig400","sig300","sig200","sig125"],"ISR_phi",3,"ISR phi",make_ratio=True)
#
################################# ABCD
#make_correlation("SR1_suep",3)
#make_correlation("SR1_suep",1)
#print("running ABCD studies")
#makeSR("sig200","SR1_suep",3)
#makeSR("sig400","SR1_suep",3)
#makeSR("sig700","SR1_suep",3)
#makeSR("sig1000","SR1_suep",3)
#makeSR("sig400","SR1_suep",3,lines=4,SR=0)
#makeSR("sig400","SR1_suep",3,lines=6,SR=0)
#makeSR("sig400","SR1_suep",3,lines=9,SR=0)
#makeSR("sig200","SR1_suep",3,lines=4,SR=0)
#makeSR("sig400","SR1_suep",3,lines=4,SR=0)
#makeSR("sig1000","SR1_suep",3,lines=4,SR=0)
#######significances
#makeSRSignif("sig125","SR1_suep",3,xline=region_cuts_tracks[1],yline=region_cuts_sphere[1])
#makeSRSignif("sig200","SR1_suep",3,xline=region_cuts_tracks[1],yline=region_cuts_sphere[1])
#makeSRSignif("sig300","SR1_suep",3,xline=region_cuts_tracks[2],yline=region_cuts_sphere[2])
#makeSRSignif("sig400","SR1_suep",3,xline=region_cuts_tracks[2],yline=region_cuts_sphere[2])
#makeSRSignif("sig700","SR1_suep",3,xline=region_cuts_tracks[3],yline=region_cuts_sphere[3])
#makeSRSignif("sig1000","SR1_suep",3,xline=region_cuts_tracks[3],yline=region_cuts_sphere[3])
######closure
#make_closure("QCD","SR1_suep",3,yrange=0,chi=True)
#make_closure_correction6("QCD","SR1_suep",3,chi=True)
#make_closure_correction6("QCD","SR1_suep",3,chi=True,rebin=True,yrange=1)
#make_closure_correction9("QCD","SR1_suep",3,chi=True)
#make_closure_correction9("QCD","SR1_suep",3,chi=True,rebin=True,yrange=1)
#makeSRSignig9("QCD","SR1_suep",3) # error plot
#########signal Injection closure
#make_closure_correction9("sig125","SR1_suep",3, point=0,yrange=0)
#make_closure_correction9("sig200","SR1_suep",3, point=0,yrange=0)
#make_closure_correction9("sig300","SR1_suep",3, point=0,yrange=0)
#make_closure_correction9("sig400","SR1_suep",3, point=0,yrange=0)
#make_closure_correction9("sig700","SR1_suep",3, point=0,yrange=0)
#make_closure_correction9("sig1000","SR1_suep",3, point=0,yrange=0)
#make_closure_correction9("sig125","SR1_suep",3, point=0,yrange=0,rebin=True)
#make_closure_correction9("sig200","SR1_suep",3, point=0,yrange=0,rebin=True)
#make_closure_correction9("sig300","SR1_suep",3, point=0,yrange=0,rebin=True)
#make_closure_correction9("sig400","SR1_suep",3, point=0,yrange=0,rebin=True)
#make_closure_correction9("sig700","SR1_suep",3, point=0,yrange=0,rebin=True)
#make_closure_correction9("sig1000","SR1_suep",3, point=0,yrange=0,rebin=True)
##
###data validation
#make_closure("RunA","SR1_suep",3,chi=True)
#make_closure_correction6("RunA","SR1_suep",3,chi=True)
#make_closure_correction9("RunA","SR1_suep",3,chi=True)
#make_closure("Data","SR1_isrsuep",3,chi=True)
##make_closure_correction6("Data","SR1_isrsuep",3,chi=True,rebin=True)
##make_closure_correction6("Data","SR1_isrsuep",3,chi=True)
##make_closure_correction9("Data","SR1_isrsuep",3,chi=True)
##make_closure_correction9("Data","SR1_isrsuep",3,chi=True,rebin=True)
##make_closure_correction9("Data","SR1_suep",3,chi=True)
##make_closure_correction9("Data","SR1_suep",3,chi=True,rebin=True)
#make_datacompare("qcd","SR1_suep",cut=3,xlab="SUEP Jet Track Multiplicity",make_ratio=False)
#make_datacompare2("qcd","SR1_suep",cut=3,xlab="Boosted Sphericity",make_ratio=False)




##make_closure_correction_binnedFull(["QCD","sig125"],"SR1_suep",3,gap=2,zoom=0)
##make_closure_correction_binnedFull(["QCD","sig125"],"SR1_suep",3,gap=2,zoom=1)
##make_closure_correction_binnedFull(["QCD","sig200"],"SR1_suep",3,gap=2,zoom=0)
##make_closure_correction_binnedFull(["QCD","sig200"],"SR1_suep",3,gap=2,zoom=1)
##make_closure_correction_binnedFull(["QCD","sig300"],"SR1_suep",3,gap=2,zoom=0)
##make_closure_correction_binnedFull(["QCD","sig300"],"SR1_suep",3,gap=2,zoom=1)
##make_closure_correction_binnedFull(["QCD","sig400"],"SR1_suep",3,gap=2,zoom=0)
##make_closure_correction_binnedFull(["QCD","sig400"],"SR1_suep",3,gap=2,zoom=1)
##make_closure_correction_binnedFull(["QCD","sig700"],"SR1_suep",3,gap=2,zoom=0)
##make_closure_correction_binnedFull(["QCD","sig700"],"SR1_suep",3,gap=2,zoom=1)
##make_closure_correction_binnedFull(["QCD","sig1000"],"SR1_suep",3,gap=2,zoom=0)
##make_closure_correction_binnedFull(["QCD","sig1000"],"SR1_suep",3,gap=2,zoom=1)

#
#for g in [0,1,2]:
#  make_closure_correction_binned("qcd","SR1_suep",3,gap=g)
#  make_closure_correction_binned("sig125","SR1_suep",3,gap=g)
#  make_closure_correction_binned("sig200","SR1_suep",3,gap=g)
#  make_closure_correction_binned("sig300","SR1_suep",3,gap=g)
#  make_closure_correction_binned("sig400","SR1_suep",3,gap=g)
#  make_closure_correction_binned("sig700","SR1_suep",3,gap=g)
#  make_closure_correction_binned("sig1000","SR1_suep",3,gap=g)
#compareRegionData(SR="SR1_suep",cut=0,point=0,zoom=0)




#
############### EXTRA
#####################APPENDIX TRIGGER
#qcdpf = make_multitrigs("QCD",["ht20","ht30","ht40","ht50"])
#make_multitrigs("sig125",["ht20","ht30","ht40","ht50"],qcdpf)
#make_multitrigs("sig200",["ht20","ht30","ht40","ht50"],qcdpf)
#make_multitrigs("sig300",["ht20","ht30","ht40","ht50"],qcdpf)
#make_multitrigs("sig400",["ht20","ht30","ht40","ht50"],qcdpf)
#make_multitrigs("sig700",["ht20","ht30","ht40","ht50"],qcdpf)
#make_multitrigs("sig1000",["ht20","ht30","ht40","ht50"],qcdpf)
#make_datatrigs(["Data"],"event_sphericity")
#make_sigtrigs(["sig1000","sig700","sig400","sig300","sig200","sig125"],"event_sphericity")
##make_sigtrigs(["sig1000","sig400"],"FatJet_nconst")
#make2dTrig("sig400",2,"trig2d_ht_event_sphericity")
#make2dTrig("sig400",2,"trig2d_ht_FatJet_nconst",ylab="Suep Jet Track Multiplicity",yfactor=6)
#make2dTrig("sig1000",2,"trig2d_ht_event_sphericity")
#make2dTrig("sig1000",2,"trig2d_ht_FatJet_nconst",ylab="Suep Jet Track Multiplicity",yfactor=6)
####################APPENDIX Basic Distributions 
#make_overlapdists(["QCD","RunA","sig1000","sig200","sig125"],"n_pfMu",1,"n PF Muons")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"Jet_pt",2,"AK4 Jet pT [GeV]")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"Jet_eta",2,"AK4 Jet eta")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"Jet_phi",2,"AK4 Jet phi")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"n_jetId",2,"n AK4 Jets")
####################APPENDIX Sphericity 
#spheremax = {"err_sig1000":[],"err_sig700":[],"err_sig400":[],"err_sig300":[],"err_sig200":[],"err_sig125":[],"sig_sig1000":[],"sig_sig700":[],"sig_sig400":[],"sig_sig300":[],"sig_sig200":[],"sig_sig125":[],"evt_sig1000":[],"evt_sig700":[],"evt_sig400":[],"evt_sig300":[],"evt_sig200":[],"evt_sig125":[]}
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep",4,spheremax,xlab="Boosted Sphericity 1 (SUEP Jet)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere_suep",4,spheremax,xlab="Boosted Sphericity 2 (SUEP Jet)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_isr",4,spheremax,xlab="Boosted Sphericity 1 (Not ISR Jet)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere_isr",4,spheremax,xlab="Boosted Sphericity 2 (Not ISR Jet)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_16",4,spheremax,xlab="Boosted Sphericity 1 (DeltaPhi > 1.6)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere_16",4,spheremax,xlab="Boosted Sphericity 2 (DeltaPhi > 1.6)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_10",4,spheremax,xlab="Boosted Sphericity 1 (DeltaPhi > 1.0)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere_10",4,spheremax,xlab="Boosted Sphericity 2 (DeltaPhi > 1.0)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_8",4,spheremax,xlab="Boosted Sphericity 1 (DeltaPhi > 0.8)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere_8",4,spheremax,xlab="Boosted Sphericity 2 (DeltaPhi > 0.8)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_4",4,spheremax,xlab="Boosted Sphericity 1 (DeltaPhi > 0.4)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere_4",4,spheremax,xlab="Boosted Sphericity 2 (DeltaPhi > 0.4)",shift_leg=True)
#make_threshold(["sig1000","sig700","sig400","sig300","sig200","sig125"],spheremax,["s1_s","s_s","s1_i","s_i","s1_16", "s_16","s1_10","s_10","s1_8", "s_8", "s1_4","s_4"],"Sphericity Calculations")
#########APPENDIX Event Shape Variable comparisons
#shapemax = {"err_sig1000":[],"err_sig700":[],"err_sig400":[],"err_sig300":[],"err_sig200":[],"err_sig125":[],"sig_sig1000":[],"sig_sig700":[],"sig_sig400":[],"sig_sig300":[],"sig_sig200":[],"sig_sig125":[],"evt_sig1000":[],"evt_sig700":[],"evt_sig400":[],"evt_sig300":[],"evt_sig200":[],"evt_sig125":[]}
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere_suep",4,shapemax,xlab="SUEP Sphericity (r=2)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"cparam_suep",4,shapemax,xlab="SUEP C Parameter (r=2)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"dparam_suep",4,shapemax,xlab="SUEP D Parameter (r=2)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"aplanarity_suep",4,shapemax,xlab="SUEP Aplanarity (r=2)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep",4,shapemax,xlab="SUEP Sphericity (r=1)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"cparam1_suep",4,shapemax,xlab="SUEP C Parameter (r=1)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"dparam1_suep",4,shapemax,xlab="SUEP D Parameter (r=1)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200","sig125"],"aplanarity1_suep",4,shapemax,xlab="SUEP Aplanarity (r=1)",shift_leg=True)
#make_threshold(["sig1000","sig700","sig400","sig300","sig200","sig125"],shapemax,["S2","C2","D2","A2","S1","C1","D1","A1"],"Event Shape Calculations")
#
#make_overlapdists(["sig400"],"sphere_suep",3,xlab="SUEP Sphericity (r=2)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"cparam_suep",3,xlab="SUEP C Parameter (r=2)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"dparam_suep",3,xlab="SUEP D Parameter (r=2)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"aplanarity_suep",3,xlab="SUEP Aplanarity (r=2)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"sphere1_suep",3,xlab="SUEP Sphericity (r=1)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"cparam1_suep",3,xlab="SUEP C Parameter (r=1)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"dparam1_suep",3,xlab="SUEP D Parameter (r=1)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"aplanarity1_suep",3,xlab="SUEP Aplanarity (r=1)",make_ratio=False,shift_leg=True)



###############Distributions
#make_dists("QCD")
######################### CUTFLOW TABLES
#make_cutflow(["sig1000","sig700","sig400","sig300","sig200","sig125"],"ht")
#allsys=[]
#make_systematics(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep",allsys,"Trigger Efficiency",systematics1="_trigSF_up",systematics2="_trigSF_down")
#make_systematics(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep",allsys,"AK4 Jet Energy Scale Corrections",systematics1="_JES_up",systematics2="_JES_down")
#make_systematics(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep",allsys,"AK4 Jet Energy Resolution Corrections",systematics1="_JER_up",systematics2="_JER_down")
#make_systematics(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep",allsys,"Pile-up reweighing",systematics1="_puweights_up",systematics2="_puweights_down")
#make_systematics(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep",allsys,"Track Reconstruction Efficiency",systematics1="_track_up")
#make_systematics(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep",allsys,"Parton shower ISR",systematics1="_PSWeight_ISR_up",systematics2="_PSWeight_ISR_down")
#make_systematics(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep",allsys,"Parton shower FSR",systematics1="_PSWeight_FSR_up",systematics2="_PSWeight_FSR_down")
#make_systematics(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep",allsys,"Pre-fire  weight",systematics1="_prefire_up",systematics2="_prefire_down")
#make_systematics(["sig125"],"sphere1_suep",allsys,"Higgs \pt reweighing",systematics1="_higgs_weights_up",systematics2="_higgs_weights_down")
#for lin in allsys:
#  print(lin)
#####Signal Contamination
##cutflow_correction_binned()
#cutflow_correction_binned(gap=1)
##cutflow_correction_binned(gap=2)

####################Limits
#makeCombineHistograms(["sig125","sig200","sig300","sig400","sig700","sig1000"],"SR1_suep",3)
makeCombineHistogramsOffline("SR1_suep",3,"QCD")
makeCombineHistogramsOffline("SR1_suep",3,"Data")
#
#temp = "2p00"
#phi = "2.000"
#makeCombineHistogramsOffline("SR1_suep",3,"sig500",temp=temp,phi=phi,load_ondemand=True)
#makeCombineHistogramsOffline("SR1_suep",3,"sig600",temp=temp,phi=phi,load_ondemand=True)
#makeCombineHistogramsOffline("SR1_suep",3,"sig800",temp=temp,phi=phi,load_ondemand=True)
#makeCombineHistogramsOffline("SR1_suep",3,"sig900",temp=temp,phi=phi,load_ondemand=True)
#makeCombineHistogramsOffline("SR1_suep",3,"sig700",temp=temp,phi=phi,load_ondemand=True)
#makeCombineHistogramsOffline("SR1_suep",3,"sig400",temp=temp,phi=phi,load_ondemand=True)
#makeCombineHistogramsOffline("SR1_suep",3,"sig300",temp=temp,phi=phi,load_ondemand=True)
#makeCombineHistogramsOffline("SR1_suep",3,"sig200",temp=temp,phi=phi,load_ondemand=True)
#makeCombineHistogramsOffline("SR1_suep",3,"sig125",temp=temp,phi=phi,load_ondemand=True)
#makeCombineHistogramsOffline("SR1_suep",3,"sig1000",temp=temp, phi=phi,load_ondemand=True)
#make_limits()
#make_limits(scan=0)
#make_limits(scan=2)
#make_limits(scan=3)
#make_limits(scan=5)

for phi in ["2.000"]:
  for temp in ["0p50", "1p00", "2p00", "4p00", "8p00"]:
    makeCombineHistogramsOffline("SR1_suep",3,"sig500",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig600",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig800",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig900",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig700",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig400",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig300",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig200",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig125",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig1000",temp=temp, phi=phi,load_ondemand=True,fullscan=True)
for phi in ["3.000"]:
  for temp in ["0p75", "12p0", "1p50", "3p00", "6p00"]:
  #for temp in ["0p75", "12p0", "1p50", "3p00", "6p00"]:
    makeCombineHistogramsOffline("SR1_suep",3,"sig500",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig600",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig800",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig900",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig700",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig400",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig300",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig200",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig125",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig1000",temp=temp, phi=phi,load_ondemand=True,fullscan=True)
for phi in ["4.000"]:
  #for temp in ["4p00"]:
  for temp in ["16p0", "1p00", "2p00", "4p00", "8p00"]:
    makeCombineHistogramsOffline("SR1_suep",3,"sig500",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig600",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig800",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig900",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig700",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig400",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig300",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig200",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig125",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig1000",temp=temp, phi=phi,load_ondemand=True,fullscan=True)
for phi in ["8.000"]:
  #for temp in ["2p00", "4p00", "8p00"]:
  for temp in ["32p0", "16p0", "2p00", "4p00", "8p00"]:
    makeCombineHistogramsOffline("SR1_suep",3,"sig500",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig600",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig800",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig900",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig700",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig400",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig300",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig200",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig125",temp=temp,phi=phi,load_ondemand=True,fullscan=True)
    makeCombineHistogramsOffline("SR1_suep",3,"sig1000",temp=temp, phi=phi,load_ondemand=True,fullscan=True)

