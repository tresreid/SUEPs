import uproot
import ROOT
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import awkward as ak

from utils import *

pt_bins = np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50])
eta_bins = np.array(range(-250,275,25))/100.
phi_bins = np.array(range(-31,31,5))/10.

xsecs = {"HT200":1551000.0,"HT300":323400.0,"HT500":30140.0,"HT700":6344.0,"HT1000":1092.0,"HT1500":99.76,"HT2000":20.35}

def openfile(HT="1000"):
  #directory = uproot.open("../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_%s_numEvent5.root"%HT)
  directory = uproot.open("../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_%s_numEvent500.root"%HT)
  tree = directory["mmtree/tree"]
  wgt = xsecs["HT%s"%HT]/len(tree["ht"].array()) 
  offlineTrack_dR        = ak.flatten(tree["offlineTrack_dR"].array())
  offlineTrack_pt        = ak.flatten(tree["offlineTrack_pt"].array())
  offlineTrack_eta       = ak.flatten(tree["offlineTrack_eta"].array())
  offlineTrack_phi       = ak.flatten(tree["offlineTrack_phi"].array())
  offlineTrack_dz        = ak.flatten(tree["offlineTrack_dz"].array())
  offlineTrack_quality   = ak.flatten(tree["offlineTrack_quality"].array())
#  offlineTrack_dxy       = ak.flatten(tree["offlineTrack_dxy"].array())
  offlineTrack_dzError   = ak.flatten(tree["offlineTrack_dzError"].array())
#  offlineTrack_ptError   = ak.flatten(tree["offlineTrack_ptError"].array())
#  offlineTrack_chi2      = ak.flatten(tree["offlineTrack_chi2"].array())
  offlineTrack_PFcandpt  = ak.flatten(tree["offlineTrack_PFcandpt"].array())
  offlineTrack_PFcandeta = ak.flatten(tree["offlineTrack_PFcandeta"].array())
  offlineTrack_PFcandphi = ak.flatten(tree["offlineTrack_PFcandphi"].array())
  offlineTrack_PFcanddz  = ak.flatten(tree["offlineTrack_PFcanddz"].array())
  offlineTrack_PFcandq   = ak.flatten(tree["offlineTrack_PFcandq"].array())
  offlineTrack_PFcandpv  = ak.flatten(tree["offlineTrack_PFcandpv"].array())
  offlineTrack_paired    = ak.flatten(tree["offlineTrack_paired"].array())
  offlineTrack_event    = ak.flatten(tree["offlineTrack_event"].array())
  offlineTrack_ht        = tree["htoff"].array()
  offlineTrack_PFcandht  = tree["ht"].array()
  
  onlineTrack_dR         = ak.flatten(tree["onlineTrack_dR"].array())
  onlineTrack_pt         = ak.flatten(tree["PFcand_pt"].array())
  onlineTrack_eta        = ak.flatten(tree["PFcand_eta"].array())
  onlineTrack_phi        = ak.flatten(tree["PFcand_phi"].array())
  onlineTrack_q          = ak.flatten(tree["PFcand_q"].array())
  #onlineTrack_dz         = ak.flatten(tree["PFcand_dz"].array())
  onlineTrack_offlinept  = ak.flatten(tree["onlineTrack_offlinept"].array())
  onlineTrack_offlineeta = ak.flatten(tree["onlineTrack_offlineeta"].array())
  onlineTrack_offlinephi = ak.flatten(tree["onlineTrack_offlinephi"].array())
  #onlineTrack_offlinedz  = ak.flatten(tree["onlineTrack_offlinedz"].array())
  onlineTrack_paired     = ak.flatten(tree["onlineTrack_paired"].array())
  
  dfht = pd.DataFrame({
  'offlineTrack_ht': offlineTrack_ht, 
  'offlineTrack_PFcandht':offlineTrack_PFcandht, 
  })
  dfoff = pd.DataFrame({
  'offlineTrack_dR':offlineTrack_dR, 
  'offlineTrack_pt':offlineTrack_pt, 
  'offlineTrack_eta':offlineTrack_eta, 
  'offlineTrack_phi':offlineTrack_phi, 
  'offlineTrack_quality': offlineTrack_quality, 
  'offlineTrack_dz': offlineTrack_dz, 
  'offlineTrack_event': offlineTrack_event, 
#  'offlineTrack_dxy': offlineTrack_dxy, 
  'offlineTrack_dzError': offlineTrack_dzError, 
#  'offlineTrack_ptError': offlineTrack_ptError, 
#  'offlineTrack_chi2': offlineTrack_chi2, 
  'offlineTrack_PFcandpt':offlineTrack_PFcandpt, 
  'offlineTrack_PFcandeta':offlineTrack_PFcandeta, 
  'offlineTrack_PFcandphi':offlineTrack_PFcandphi, 
  'offlineTrack_PFcanddz':offlineTrack_PFcanddz, 
  'offlineTrack_PFcanddzError':offlineTrack_PFcanddz, 
  'offlineTrack_PFcandptError':offlineTrack_PFcanddz, 
  'offlineTrack_PFcandchi2':offlineTrack_PFcanddz, 
  'offlineTrack_PFcandq':offlineTrack_PFcandq, 
  'offlineTrack_PFcandpv':offlineTrack_PFcandpv, 
  'offlineTrack_paired':offlineTrack_paired, 
  })
  dfon = pd.DataFrame({
  'onlineTrack_dR':onlineTrack_dR, 
  'onlineTrack_pt':onlineTrack_pt, 
  'onlineTrack_eta':onlineTrack_eta, 
  'onlineTrack_phi':onlineTrack_phi, 
  'onlineTrack_q':onlineTrack_q, 
  #'onlineTrack_dz':onlineTrack_dz, 
  'onlineTrack_offlinept': onlineTrack_offlinept, 
  'onlineTrack_offlineeta':onlineTrack_offlineeta, 
  'onlineTrack_offlinephi':onlineTrack_offlinephi, 
  #'onlineTrack_offlinedz':onlineTrack_offlinedz, 
  'onlineTrack_paired':onlineTrack_paired, 
  })
  #mapping = {item:i for i, item in enumerate(dfoff["offlineTrack_dz"].unique())}
  dfoff["offlineTrack_pvnum"] = np.digitize(dfoff["offlineTrack_dz"],np.array(range(-960,960,1))/32)#.apply(lambda x: mapping[x])
  #dfoff.groupby(["offlineTrack_event"])["offlineTrack_pvsum"] = dfoff.groupby(["offlineTrack_event","offlineTrack_pvnum"])["offlineTrack_pt"].sum()
  #dfoff["offlineTrack_pvnum"] = (
  #  dfoff.groupby(["offlineTrack_event","offlineTrack_dz"].transform('nunique'))
  #dfoff["offlineTrack_pvnum"] = dfoff.groupby(["offlineTrack_event","offlineTrack_dz"])['offlineTrack_pt'].sum()

  dfht["wgt"] = wgt
  dfoff["wgt"] = wgt
  dfon["wgt"] = wgt
  dfon = dfon[dfon["onlineTrack_q"] != 0]
  return dfht,dfoff,dfon

#dfht1, dfoff1,dfon1 = openfile("1000")
#print(dfoff1[["offlineTrack_event","offlineTrack_dz","offlineTrack_pvnum"]])
dfht1, dfoff1,dfon1 = openfile("200")
dfht2, dfoff2,dfon2 = openfile("300")
dfht3, dfoff3,dfon3 = openfile("500")
dfht4, dfoff4,dfon4 = openfile("700")
dfht5, dfoff5,dfon5 = openfile("1000")
dfht6, dfoff6,dfon6 = openfile("1500")
dfht7, dfoff7,dfon7 = openfile("2000")
dfht  = pd.concat([dfht1,dfht2,dfht3,dfht4,dfht5,dfht6,dfht7])
dfoff = pd.concat([dfoff1,dfoff2,dfoff3,dfoff4,dfoff5,dfoff6,dfoff7])
dfon  = pd.concat([dfon1,dfon2,dfon3,dfon4,dfon5,dfon6,dfon7])
#dfoff = dfoff[(dfoff["offlineTrack_pt"] >= 0.75) & (dfoff["offlineTrack_quality"] == 1) & (abs(dfoff["offlineTrack_eta"]) <=2.4)]
#df2off = dfoff[(dfoff["offlineTrack_paired"] == 1)]
df2off = dfoff[(dfoff["offlineTrack_paired"] == 1) & (dfoff["offlineTrack_PFcandpt"] >= 0.75)& (abs(dfoff["offlineTrack_PFcandeta"]) <= 2.4) & (abs(dfoff["offlineTrack_PFcandq"]) == 1)]
#df2off = dfoff[(dfoff["offlineTrack_paired"] == 1) & (dfoff["offlineTrack_PFcandpt"] >= 0.75)& (abs(dfoff["offlineTrack_PFcandeta"]) <= 2.4) & (dfoff["offlineTrack_PFcandpv"] == 0) & (abs(dfoff["offlineTrack_PFcandq"]) == 1)]
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
  elif version ==2:
    v1 = "offlineTrack_"
    v2 = "offlineTrack_PFcand"
    v3 = "Offline"
    v4 = "Online"
    df= dfht
    df2= dfht
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
    x = np.linspace(0,100,100)
  else:
    ax1.set_xlabel("%s track %s"%(v3,var))
    ax.set_ylabel("%s track %s"%(v4,var))
    ax1.set_ylabel("residual")
    ax1.set_ylim(-0.005,0.005)
    if var == "ht":
      x = np.linspace(0,1600,100)
      ax1.set_ylim(-100,500)
    else:
      x = np.linspace(-3,3,100)
  ax.plot(x, x, '-r', label='y=x')
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
  elif var == "phi":
    xbin = phi_bins
    ax1.set_xlabel("%s Track %s"%(v3,var))
  elif var == "dz":
    xbin = np.array(range(-100,100,1))/10.
    ax1.set_xlabel("%s Track %s"%(v3,var))
  elif var == "quality":
    xbin = np.array(range(0,3,1))
    ax1.set_xlabel("%s Track %s"%(v3,var))
  elif "pv" in var:
    xbin = np.array(range(800,1400,1))
    ax1.set_xlabel("%s Track %s"%(v3,var))
  else:
    xbin = np.array(range(0,100,1))/100 
    ax1.set_xlabel("%s Track %s"%(v3,var))
  ax1.set_ylabel("Ratio" )
  ax.set_ylabel("nTracks")
  
  h1 = ax.hist(df["%s%s"%(v1,var)] ,bins=xbin,weights=df["wgt"],color="red",label="%s Tracks"%v3)
  h2 = ax.hist(df2["%s%s"%(v1,var)],bins=xbin,weights=df2["wgt"],color="blue",label="Paired %s Tracks"%v3)

  
  ax1.errorbar(xbins(h1[1]),h2[0]/h1[0],yerr=0.1,xerr=xbins_err(h1[1]),marker="+",ls="none")
  print(h1)
  print(h2)
  ax1.legend()
  ax.legend()
  fig.savefig("Plots/trackhist_%s_%s.png"%(var,version))
  plt.close()
def make_hist2d(var1,var2,version=0):
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
  fig1, (ax1) = plt.subplots(
   #     nrows=2,
   #     ncols=1,
   #     figsize=(7,7),
   #     gridspec_kw={"height_ratios": (3, 1)},
   #     sharex=True
    )
  fig2, (ax2) = plt.subplots()
  fig3, (ax3) = plt.subplots()
  #fig.subplots_adjust(hspace=.07)
  if var1 == "pt":
    xbin = pt_bins
    ax1.set_xlabel("%s Track pT [GeV]"%v3)
    ax2.set_xlabel("%s Track pT [GeV]"%v3)
    ax3.set_xlabel("%s Track pT [GeV]"%v3)
  else:
    ax1.set_xlabel("%s Track %s"%(v3,var1))
    ax2.set_xlabel("%s Track %s"%(v3,var1))
    ax3.set_xlabel("%s Track %s"%(v3,var1))
    if var1 == "eta":
      xbin = eta_bins
    elif var1 == "phi":
      xbin = phi_bins
    elif var1 == "dz":
      xbin = np.array(range(-100,100,1))/10.
    elif var1 == "quality":
      xbin = np.array(range(0,3,1))
    elif "pv" in var1:
      xbin = np.array(range(800,1400,1))
    else:
      xbin = np.array(range(0,100,1))/100 
  if var2 == "pt":
    ybin = pt_bins
    ax1.set_ylabel("%s Track pT [GeV]"%v3)
    ax2.set_ylabel("%s Track pT [GeV]"%v3)
    ax3.set_ylabel("%s Track pT [GeV]"%v3)
  else:
    ax1.set_ylabel("%s Track %s"%(v3,var2))
    ax2.set_ylabel("%s Track %s"%(v3,var2))
    ax3.set_ylabel("%s Track %s"%(v3,var2))
    if var2 == "eta":
      ybin = eta_bins
    elif var2 == "phi":
      ybin = phi_bins
    elif var2 == "dz":
      ybin = np.array(range(-100,100,1))/10.
    elif var2 == "quality":
      ybin = np.array(range(0,3,1))
    elif "pv" in var2:
      ybin = np.array(range(800,1400,1))
    else:
      ybin = np.array(range(0,100,1))/100 
  #ax1.set_ylabel("Ratio" )
  #ax.set_ylabel("nTracks")
  
  h1 = ax1.hist2d(df["%s%s"%(v1,var1)] ,df["%s%s"%(v1,var2)] ,bins=[xbin,ybin],weights=df["wgt"])
  h2 = ax2.hist2d(df2["%s%s"%(v1,var1)] ,df2["%s%s"%(v1,var2)] ,bins=[xbin,ybin],weights=df2["wgt"])
  #h3 = ax3.hist2d(h2[0]/h1[0] ,bins=[xbin,ybin])
  #ax3.imshow((h2[0]/h1[0]).T,origin='lower')
  X,Y = np.meshgrid(h2[2],h2[1])
  data = h2[0]/h1[0]
  h3 = ax3.pcolor(X,Y,data)
  print(data)
  #for yi,y in enumerate(h2[2]):
  #  for xi,x in enumerate(h2[1]):
  #      print(x,y)
  #      print(xi,yi)
  #      print(data[xi,yi])
  #      ax3.text(x + 0.5, y + 0.5, '%.4f' % data[xi, yi],
  #               horizontalalignment='center',
  #               verticalalignment='center',
  #               )

  fig3.colorbar(h3)
  fig2.colorbar(h2[3])
  fig1.colorbar(h1[3])
  print(h1)
  print(h2)
  print(h2[0]/h1[0])
  print(h2[1])
  print(h2[2])
  #h3 = ax3.hist2d(df2["%s%s"%(v1,var1)] ,df2["%s%s"%(v1,var2)] ,bins=[xbin,ybin],weights=df2["wgt"])
  #h2 = ax2.hist2d(df2["%s%s"%(v1,var)],bins=xbin,weights=df2["wgt"],color="blue",label="Paired %s Tracks"%v3)

  
  #ax1.errorbar(xbins(h1[1]),h2[0]/h1[0],yerr=0.1,xerr=xbins_err(h1[1]),marker="+",ls="none")
  #print(h1)
  #print(h2)
  #ax1.legend()
  #ax.legend()
  print(len(data),len(data[0]),len(data[5]))
  np.savetxt("../systematics/triggers/track_drop_%s.txt"%(year),np.nan_to_num(data), delimiter=",")
  fig1.savefig("Plots/trackhist2d_%s_%s_%s.png"%(var1,var2,version))
  fig2.savefig("Plots/trackhist2dpaired_%s_%s_%s.png"%(var1,var2,version))
  fig3.savefig("Plots/trackhist2dratio_%s_%s_%s.png"%(var1,var2,version))
  plt.close()

make_scatter("pt")
make_scatter("eta")
make_scatter("phi")
make_scatter("ht",2)
make_scatter("dz")
make_hist("pvnum")
make_hist("pt")
make_hist("eta")
make_hist("phi")
make_hist("quality")
#make_hist("dz")
#make_hist("dxy")
#make_hist("chi2")
make_hist("dzError")
#make_hist("ptError")
#

make_scatter("pt",1)
make_scatter("eta",1)
make_scatter("phi",1)
#make_scatter("dz",1)
make_hist("pt",1)
make_hist("eta",1)
make_hist("phi",1)
#make_hist("dz",1)

make_hist2d("pt","eta")
