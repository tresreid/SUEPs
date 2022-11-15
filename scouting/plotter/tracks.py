import uproot
import ROOT
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import awkward as ak

from utils import *

pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50])
eta_bins = np.array(range(-250,250,25))/100.
phi_bins = np.array(range(-31,31,5))/10.

#directory = uproot.open("../../../CMSSW_10_6_26/src/PhysicsTools/qcdtest_numEvent100.root")
directory = uproot.open("../../../testsite/CMSSW_10_6_26/src/PhysicsTools/qcdtest_numEvent100.root")
tree = directory["mmtree/tree"]

offlineTrack_dR        = ak.flatten(tree["offlineTrack_dR"].array())
offlineTrack_pt        = ak.flatten(tree["offlineTrack_pt"].array())
offlineTrack_eta       = ak.flatten(tree["offlineTrack_eta"].array())
offlineTrack_phi       = ak.flatten(tree["offlineTrack_phi"].array())
offlineTrack_dz        = ak.flatten(tree["offlineTrack_dz"].array())
offlineTrack_PFcandpt  = ak.flatten(tree["offlineTrack_PFcandpt"].array())
offlineTrack_PFcandeta = ak.flatten(tree["offlineTrack_PFcandeta"].array())
offlineTrack_PFcandphi = ak.flatten(tree["offlineTrack_PFcandphi"].array())
offlineTrack_PFcanddz  = ak.flatten(tree["offlineTrack_PFcanddz"].array())
offlineTrack_paired    = ak.flatten(tree["offlineTrack_paired"].array())

onlineTrack_dR         = ak.flatten(tree["onlineTrack_dR"].array())
onlineTrack_pt         = ak.flatten(tree["PFcand_pt"].array())
onlineTrack_eta        = ak.flatten(tree["PFcand_eta"].array())
onlineTrack_phi        = ak.flatten(tree["PFcand_phi"].array())
#onlineTrack_dz         = ak.flatten(tree["PFcand_dz"].array())
onlineTrack_offlinept  = ak.flatten(tree["onlineTrack_offlinept"].array())
onlineTrack_offlineeta = ak.flatten(tree["onlineTrack_offlineeta"].array())
onlineTrack_offlinephi = ak.flatten(tree["onlineTrack_offlinephi"].array())
#onlineTrack_offlinedz  = ak.flatten(tree["onlineTrack_offlinedz"].array())
onlineTrack_paired     = ak.flatten(tree["onlineTrack_paired"].array())

dfoff = pd.DataFrame({
'offlineTrack_dR':offlineTrack_dR, 
'offlineTrack_pt':offlineTrack_pt, 
'offlineTrack_eta':offlineTrack_eta, 
'offlineTrack_phi':offlineTrack_phi, 
'offlineTrack_dz': offlineTrack_dz, 
'offlineTrack_PFcandpt':offlineTrack_PFcandpt, 
'offlineTrack_PFcandeta':offlineTrack_PFcandeta, 
'offlineTrack_PFcandphi':offlineTrack_PFcandphi, 
'offlineTrack_PFcanddz':offlineTrack_PFcanddz, 
'offlineTrack_paired':offlineTrack_paired, 
})
df2off = dfoff[dfoff["offlineTrack_paired"] == 1]
dfon = pd.DataFrame({
'onlineTrack_dR':onlineTrack_dR, 
'onlineTrack_pt':onlineTrack_pt, 
'onlineTrack_eta':onlineTrack_eta, 
'onlineTrack_phi':onlineTrack_phi, 
#'onlineTrack_dz':onlineTrack_dz, 
'onlineTrack_offlinept': onlineTrack_offlinept, 
'onlineTrack_offlineeta':onlineTrack_offlineeta, 
'onlineTrack_offlinephi':onlineTrack_offlinephi, 
#'onlineTrack_offlinedz':onlineTrack_offlinedz, 
'onlineTrack_paired':onlineTrack_paired, 
})
df2on = dfon[dfon["onlineTrack_paired"] == 1]
#print(df2)


def make_scatter(var,version=0):
  if version ==0:
    v1 = "offlineTrack_"
    v2 = "offlineTrack_PFcand"
    v3 = "Offline"
    v4 = "Online"
    df= dfoff
    df2= df2off
  else:
    v1 = "onlineTrack_"
    v2 = "onlineTrack_offline"
    v3 = "Online"
    v4 = "Offline"
    df= dfon
    df2= df2on
  fig, (ax,ax1) = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(7,7),
        gridspec_kw={"height_ratios": (3, 1)},
        sharex=True
    )
  fig.subplots_adjust(hspace=.07)
  
  ax.scatter(df2["%s%s"%(v1,var)],df2["%s%s"%(v2,var)],color="blue",label="%s vs %s %s"%(v3,v4,var),marker="+")
  ax1.scatter(df2["%s%s"%(v1,var)],df2["%s%s"%(v1,var)]-df2["%s%s"%(v2,var)],color="blue",label="%s - %s %s"%(v3,v4,var),marker="+")
  
  # hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax1)
  if var == "pt":
    ax1.set_xlabel("%s track pT [GeV]"%v3)
    ax.set_ylabel("%s track pT [GeV]"%v4)
    ax1.set_ylabel("residual")
    ax1.set_ylim(-0.5,0.5)
  else:
    ax1.set_xlabel("%s track %s"%(v3,var))
    ax.set_ylabel("%s track %s"%(v4,var))
    ax1.set_ylabel("residual")
    ax1.set_ylim(-0.005,0.005)
  ax1.legend()
  ax.legend()
  fig.savefig("Plots/track_%s_%s.png"%(var,version))
  plt.close()

def make_hist(var,version=0):
  if version ==0:
    v1 = "offlineTrack_"
    v2 = "offlineTrack_PFcand"
    v3 = "Offline"
    v4 = "Online"
    df= dfoff
    df2= df2off
  else:
    v1 = "onlineTrack_"
    v2 = "onlineTrack_offline"
    v3 = "Online"
    v4 = "Offline"
    df= dfon
    df2= df2on
  fig, (ax,ax1) = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(7,7),
        gridspec_kw={"height_ratios": (3, 1)},
        sharex=True
    )
  fig.subplots_adjust(hspace=.07)
  if var == "pt":
    xbin = pt_bins
    ax1.set_xlabel("%s Track pT [GeV]"%v3)
  elif var == "eta":
    xbin = eta_bins
    ax1.set_xlabel("%s Track %s"%(v3,var))
  elif var == "dz":
    xbin = np.array(range(-100,100,1))/10.
    ax1.set_xlabel("%s Track %s"%(v3,var))
  else:
    xbin = phi_bins
    ax1.set_xlabel("%s Track %s"%(v3,var))
  ax1.set_ylabel("Ratio" )
  ax.set_ylabel("nTracks")
  
  h1 = ax.hist(df["%s%s"%(v1,var)],bins=xbin,color="red",label="%s Tracks"%v3)
  h2 = ax.hist(df2["%s%s"%(v1,var)],bins=xbin,color="blue",label="Paired %s Tracks"%v3)

  
  ax1.errorbar(xbins(h1[1]),h2[0]/h1[0],yerr=0.1,xerr=xbins_err(h1[1]),marker="+",ls="none")
  print(h1)
  print(h2)
  ax1.legend()
  ax.legend()
  fig.savefig("Plots/trackhist_%s_%s.png"%(var,version))
  plt.close()

make_scatter("pt")
make_scatter("eta")
make_scatter("phi")
#make_scatter("dz")
make_hist("pt")
make_hist("eta")
make_hist("phi")
make_hist("dz")
make_scatter("pt",1)
make_scatter("eta",1)
make_scatter("phi",1)
#make_scatter("dz",1)
make_hist("pt",1)
make_hist("eta",1)
make_hist("phi",1)
#make_hist("dz",1)
