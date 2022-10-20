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

def make_datatrigs(samples,var="ht",systematics =False):
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


  b = qcdscaled["trigdist_%s"%var].integrate("cut",slice(5,6))#.to_hist().to_numpy()
  b0 = qcdscaled["trigdist_%s"%var].integrate("cut",slice(4,5))#.to_hist().to_numpy()
  if("ht" in var):
    b = b.rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
    b0 = b0.rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
  b1 = b.values(sumw2=True)[()][0]#.to_hist().to_numpy()[0]
  b2 = b0.values(sumw2=True)[()][0]#.to_hist().to_numpy()[0]
  b1_err = np.sqrt(b.values(sumw2=True)[()][1])#.to_hist().to_numpy()[0]
  b2_err = np.sqrt(b0.values(sumw2=True)[()][1])#.to_hist().to_numpy()[0]

  points2 = np.nan_to_num(b1/b2)
  popt2, pcov2 = curve_fit(func,xbins(b.to_hist().to_numpy()[1]),points2,p0=[0.5,500,100,0.5])
  p98bkg = 1.65*popt2[2]+popt2[1]
  p90bkg = 1.163*popt2[2]+popt2[1]

  d = trigscaled["trigdist_%s"%var].integrate("cut",slice(5,6))#.to_hist().to_numpy()
  d0 = trigscaled["trigdist_%s"%var].integrate("cut",slice(4,5))#.to_hist().to_numpy()
  if("ht" in var):
    d = d.rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
    d0 = d0.rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
  d1 = d.values(sumw2=True)[()][0]#.to_hist().to_numpy()[0]
  d2 = d0.values(sumw2=True)[()][0]#.to_hist().to_numpy()[0]
  d1_err = np.sqrt(d.values(sumw2=True)[()][1])#.to_hist().to_numpy()[0]
  d2_err = np.sqrt(d0.values(sumw2=True)[()][1])#.to_hist().to_numpy()[0]
  hx1 = hist.plotratio(
      b,b0,
      ax=ax,
      error_opts={'color': 'r', 'marker': '.'},
      unc='clopper-pearson'
  )
  hx2 = hist.plotratio(
      d,d0,
      ax=ax,
      clear=False,
      error_opts={'color': 'k', 'marker': '.'},
      unc='clopper-pearson'
  )
  points3 = np.nan_to_num(d1/d2)
  popt3, pcov3 = curve_fit(func,xbins(d.to_hist().to_numpy()[1]),points3,p0=[0.5,500,100,0.5])
  p98dat = 1.65*popt3[2]+popt3[1]
  p90dat = 1.163*popt3[2]+popt3[1]
  ax.plot(xs,func(xs,popt3[0],popt3[1],popt3[2],popt3[3]), color="black",label=labels["Trigger"])#: 90:%d 98:%d"%(p90dat,p98dat))
  ax.plot(xs,func(xs,popt2[0],popt2[1],popt2[2],popt2[3]), color="red",label="QCD")#: 90:%d 98:%d"%(p90bkg,p98bkg))
  ax.axvline(x=560,color="grey",ls="--")

  xbin = xbins(b.to_hist().to_numpy()[1])
  ratio = (b1/b2)/(d1/d2)
  ratio_err = ratio*np.sqrt( (b1_err/b1)**2 +(b2_err/b2)**2+(d1_err/d1)**2+(d2_err/d2)**2)
  hxrat = ax1.errorbar(xbin,ratio,yerr=ratio_err)
  if systematics:
    np.savetxt("systematics/triggers/trigger_systematics_18.txt",(b.to_hist().to_numpy()[1][1:],np.nan_to_num(ratio),ratio_err), delimiter=",")

  ax1.axhline(y=1,color="grey",ls="--")
  ax.set_ylim(0,1.1)
  ax1.set_ylabel("Data/QCD")
  ax1.set_ylim(0.5,1.5)
  ax.set_xlabel("")
  ax.set_ylabel("Efficiency")
  ax.legend(loc="lower right")
  fig.suptitle("HT Trigger Efficiency DoubleMu3 Reference: Data")
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
  fig.savefig("Plots/trig%s_data_%s.%s"%(var,year,ext))
  plt.close()
def make_sigtrigs(samples,var="ht",systematics =False):
  fig, (ax) = plt.subplots(
  #fig, (ax,ax1) = plt.subplots(
  #nrows=1,
  #ncols=1,
  figsize=(7,7),
  #gridspec_kw={"height_ratios": (3, 1)},
  #sharex=True
  )
  if(var=="event_sphericity"):
    xs = np.linspace(0,1,100)
    ax.set_xlabel("Event Sphericity (unbooosted)")
  elif(var=="FatJet_nconst"):
    #ax1.set_xlim([0,300])
    ax.set_xlim([0,300])
    xs = np.linspace(0,300,100)
    ax.set_xlabel("SUEP Jet Track Multiplicity")
  else:
    xs = np.linspace(0,1500,100)
    ax.set_xlabel("Ht [GeV]")
  b = qcdscaled["trigdist_%s"%var].integrate("cut",slice(1,2))#.to_hist().to_numpy()
  b0 = qcdscaled["trigdist_%s"%var].integrate("cut",slice(0,1))#.to_hist().to_numpy()
  if("ht" in var):
    b = b.rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
    b0 = b0.rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
  b1 = b.to_hist().to_numpy()[0]
  b2 = b0.to_hist().to_numpy()[0]
  hx1 = hist.plotratio(
      b,b0,
      ax=ax,
      error_opts={'color': 'r', 'marker': '.'},
      unc='clopper-pearson'
  )
  points2 = np.nan_to_num(b1/b2)
  popt2, pcov2 = curve_fit(func,xbins(b.to_hist().to_numpy()[1]),points2,p0=[0.5,500,100,0.5])
  p98bkg = 1.65*popt2[2]+popt2[1]
  p90bkg = 1.163*popt2[2]+popt2[1]
  ax.plot(xs,func(xs,popt2[0],popt2[1],popt2[2],popt2[3]), color="red",label="QCD")#: 90:%d 98:%d"%(p90bkg,p98bkg))
  for sample in samples:
        out = sigscaled[sample]
        #Trigger plots
        sx = out["trigdist_%s"%var].integrate("cut",slice(1,2))#.to_hist().to_numpy()
        s0x = out["trigdist_%s"%var].integrate("cut",slice(0,1))#.to_hist().to_numpy()
        if("ht" in var):
          s = sx.copy().rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
          s0 = s0x.copy().rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
        else:
          s = sx
          s0 = s0x
        s1 = s.to_hist().to_numpy()[0]
        s2 = s0.to_hist().to_numpy()[0]

        points = np.nan_to_num(s.to_hist().to_numpy()[0]/s0.to_hist().to_numpy()[0])
        popt, pcov = curve_fit(func,xbins(s.to_hist().to_numpy()[1]),points,p0=[0.5,500,100,0.5])
        ax.plot(xs,func(xs,popt[0],popt[1],popt[2],popt[3]), color=sigcolors[sample],label=labels[sample])#: 90:%d 98:%d "%(sample,p90sig,p98sig))
        hx = hist.plotratio(              s,s0,
            ax=ax,
            clear=False,
            error_opts={'color': sigcolors[sample], 'marker': '.'},
            unc='clopper-pearson'
        )
        ax.set_xlabel("")
        #hxrat = ax1.scatter(xbins(b.to_hist().to_numpy()[1]),(b1/b2)/(s1/s2),marker=".",color=sigcolors[sample])

  #ax1.axhline(y=1,color="grey",ls="--")
  ax.axvline(x=560,color="grey",ls="--")
  ax.set_ylim(0,1.1)
  #ax1.set_ylim(0.5,1.5)
  ax.set_label("")
  ax.set_ylabel("Efficiency")
  ax.legend(loc="lower right")
  fig.suptitle("HT Trigger Efficiency No Reference: Sig")
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
  fig.savefig("Plots/trig%s_sig_%s.%s"%(var,year,ext))
  plt.close()

def make_multitrigs(sig,varsx,qcdpf=None):
  fig, ax = plt.subplots(
  nrows=1,
  ncols=1,
  figsize=(7,7),
  )
  xs = np.linspace(0,1500,100)
  nevts = {"ht20":[],"ht30":[],"ht40":[],"ht50":[]}
  for i,var in enumerate(varsx):
    if sig == "QCD":
        s = qcdscaled["trigdist_%s"%var].integrate("cut",slice(1,2))#.to_hist().to_numpy()
        s0 = qcdscaled["trigdist_%s"%var].integrate("cut",slice(0,1))#.to_hist().to_numpy()
        if("ht" in var):
          s = s.rebin("v1",hist.Bin("v1","ht",[*range(0,700,40)]+[700,800,1000,1200,1500]))
          s0 = s0.rebin("v1",hist.Bin("v1","ht",[*range(0,700,40)]+[700,800,1000,1200,1500]))
        s1 = s.to_hist().to_numpy()[0]
        s2 = s0.to_hist().to_numpy()[0]
        points = np.nan_to_num(s1/s2)
        popt, pcov = curve_fit(func,xbins(s.to_hist().to_numpy()[1]),points,p0=[0.5,500,100,0.5])
        hx = hist.plotratio(
            s,s0,
            ax=ax,
            clear=False,
            error_opts={'color': colors[i], 'marker': '.'},
            unc='clopper-pearson'
        )
        p98sig = 1.65*popt[2]+popt[1]
        p90sig = 1.163*popt[2]+popt[1]
        ax.plot(xs,func(xs,popt[0],popt[1],popt[2],popt[3]), color=colors[i],label="%s"%var)#: 90:%d 98:%d "%(sample,p90sig,p98sig))
        for thres in [520,525,560,600]:
          thres_index = list(map(lambda i: i >= thres, s.to_hist().to_numpy()[1])).index(True)
          nevts[var].append(np.sum(s1[thres_index:]))
    else:
          out = sigscaled[sig]
          s = out["trigdist_%s"%var].integrate("cut",slice(1,2))#.to_hist().to_numpy()
          s0 = out["trigdist_%s"%var].integrate("cut",slice(0,1))#.to_hist().to_numpy()

          if("ht" in var):
            s = s.rebin("v1",hist.Bin("v1","ht",[*range(0,700,40)]+[700,800,1000,1200,1500]))
            s0 = s0.rebin("v1",hist.Bin("v1","ht",[*range(0,700,40)]+[700,800,1000,1200,1500]))
          s1 = s.to_hist().to_numpy()[0]
          s2 = s0.to_hist().to_numpy()[0]
          points = np.nan_to_num(s1/s2)
          popt, pcov = curve_fit(func,xbins(s.to_hist().to_numpy()[1]),points,p0=[0.5,500,100,0.5])
          hx = hist.plotratio(
              s,s0,
              ax=ax,
              clear=False,
              error_opts={'color': colors[i], 'marker': '.'},
              unc='clopper-pearson'
          )
          p98sig = 1.65*popt[2]+popt[1]
          p90sig = 1.163*popt[2]+popt[1]
          ax.plot(xs,func(xs,popt[0],popt[1],popt[2],popt[3]), color=colors[i],label="%s"%var)#: 90:%d 98:%d "%(sample,p90sig,p98sig))
          for thres in [520,525,560,600]:
            thres_index = list(map(lambda i: i >= thres, s.to_hist().to_numpy()[1])).index(True)
            nevts[var].append(np.sum(s1[thres_index:]))
  print(sig)
  df = pd.DataFrame(nevts,index=[520,525,560,600])
  print(df)
  ax.set_ylim(0,1.1)
  ax.legend(loc="lower right")
  ax.set_xlabel("Ht [GeV]")
  ax.set_ylabel("Efficiency")
  ax.axvline(x=520,color="grey")
  ax.axvline(x=525,color="grey")
  ax.axvline(x=560,color="grey")
  ax.axvline(x=600,color="grey")
  ax.axhline(y=0.95,color="grey")
  fig.suptitle("HT Trigger Efficiency No reference: %s"%sig)
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
  fig.savefig("Plots/trigmulti_%s_%s.%s"%(sig,year,ext))
  plt.close()
  if qcdpf is not None:
    divpf = df/((df+qcdpf).apply(np.sqrt))
    print(divpf)
  #print("%s %s %s %s"%(df["ht20"][3],df["ht30"][2],df["ht40"][1],df["ht50"][0]))
  return df


def make2dTrig(sample,cut,var2,ylab="Sphericity (Unboosted)",xlab="Ht [GeV]",yfactor=2):
          scaled = sigscaled[sample]
          s = scaled[var2].to_hist().to_numpy()
          ref = s[0][0]
          trig = s[0][1]
          x = xbins(s[2])
          y = xbins(s[3])
          xx,yy = np.meshgrid(x,y)
          z = np.nan_to_num(trig/ref)
          xxx = xx.ravel()
          yyy = yy.ravel()
          zzz = z.ravel()
          df = pd.DataFrame({"ht":xxx,"sphericity" : yyy, "trig eff":zzz})
          piv = df.pivot(index = "ht",columns = "sphericity",values = "trig eff")

          fig, ax1 = plt.subplots()
          g = sns.heatmap(np.transpose(z),cmap="Reds")
          g.invert_yaxis()
          labsx = [10*int(item.get_text()) for item in ax1.get_xticklabels()]
          labsy = [yfactor*int(item.get_text()) for item in ax1.get_yticklabels()]
          ax1.set_xticklabels(labsx)
          ax1.set_yticklabels(labsy)
          ax1.set_xlabel(xlab)
          ax1.set_ylabel(ylab)
          fig.suptitle("Trigger Efficiency")
          ax1.autoscale(axis='y', tight=True)
          ax1.autoscale(axis='x', tight=True)
          hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2)
          plt.subplots_adjust(bottom=0.20)
          fig.savefig("Plots/trigeff2d_%s_%s_%s.%s"%(sample,var2,year,ext))
          plt.close()
