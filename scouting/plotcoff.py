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

ext="png"
#ext="pdf"
pd.set_option("precision",2)

#parameters = {'axes.labelsize': 13,
#          'axes.titlesize': 13}
parameters = {'axes.labelsize': 20,
          'axes.titlesize': 20,
          'legend.fontsize':10
          }
plt.rcParams.update(parameters)

#with open("myhistos_sig400_0.p", "rb") as pkl_file:
lumi = 59.69*1000 #lumi for 2018 scouting # A:13.978, B: 7.064, C: 6.899, D: 31.748
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

directory = "outhists/"
#directory = "outhists/nPV/"
qcdscaled = {}
qcddatascaled = {}
qcddatafullscaled = {}
datascaled = {}
datafullscaled = {}
trigscaled = {}
datafulllumi = 0
with open(directory+"myhistos_Data.p", "rb") as pkl_file:
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
with open(directory+"myhistos_Trigger.p", "rb") as pkl_file:
    out = pickle.load(pkl_file)
    for name, h in out.items():
      if isinstance(h, hist.Hist):
        trigscaled[name] = h.copy()
#with open(directory+"myhistos_HT2000_0.p", "rb") as pkl_file:
with open(directory+"myhistos_QCD.p", "rb") as pkl_file:
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
def xbins(a):
  return [0.5*(t - s)+s for s, t in zip(a, a[1:])] 
def xbins_err(a):
  return [0.5*(t - s) for s, t in zip(a, a[1:])] 
def make_overlapdists(samples,var,cut,xlab=None,make_ratio=True,vline=None,shift_leg=False):
  if make_ratio:
    fig, (ax,ax1) = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(7,7),
        gridspec_kw={"height_ratios": (3, 1)},
        sharex=True
    )
  else:
    fig, ax = plt.subplots()
  fig.subplots_adjust(hspace=.07)
  name1 = "dist_%s"%var
  if (xlab==None):
    xlab=name1[5:]
  if "RunA" in samples:
    h1 = datascaled[name1].integrate("cut",slice(cut,cut+1))
    if("ht" in name1):
      h1 = h1.rebin("v1",hist.Bin("v1","ht",50,50,3500))
    h1_scale = h1.values(sumw2=True)[()]
    sdat = h1.to_hist().to_numpy()
    daterr = np.sqrt(h1_scale[1])
    xerr = xbins_err(sdat[1])
    #ax.scatter(sdat[1][:-1],sdat[0],color=sigcolors["RunA"],label="Data",marker=".")
    xbin = np.array(xbins(sdat[1]))
    xerr_low = [(t - s) for s, t in zip(sdat[1], xbin)]
    xerr_high = [abs(t - s) for s, t in zip(sdat[1][1:], xbin)]
    #for bin in sdat[1]:
    #  ax.axvline(x=bin,color="grey",ls="--")
    ax.errorbar(xbin,sdat[0],yerr=daterr,xerr=[xerr_low,xerr_high],color=sigcolors["RunA"],label=labels["RunA"],zorder=6,ls="None",marker=".")
    #ax.errorbar(xbin,sdat[0],yerr=daterr,xerr=xerr,color=sigcolors["RunA"],label=labels["RunA"],zorder=6,ls="None",marker=".")
  if "QCD" in samples:
    h2x = qcddatascaled[name1]
    h2= h2x.integrate("cut",slice(cut,cut+1))
    if("ht" in name1):
      h2 = h2.rebin("v1",hist.Bin("v1","ht",50,50,3500))
    h2_scale = h2.values(sumw2=True)[()]
    #print(h2_scale)
    s = h2.to_hist().to_numpy()
    s_err = np.sqrt(h2_scale[1])
    xbin = xbins(s[1])
    #print(s_err)
    #for bin in s[1]:
    #  ax.axvline(x=bin,color="red",ls="--")
    ## append an extra point at the end because the post doesn't work without it for the last bin. it needs to know where to go next
    ax.fill_between(s[1],np.append(s[0],s[0][-1]),color=sigcolors["QCD"],alpha=0.8,label="QCD",zorder=0,linestyle="-",step="post")#,)
    ax.errorbar(s[1],np.append(s[0],s[0][-1]),yerr=np.append(s_err,0),color=sigcolors["QCD"],zorder=1,ls='none')
    if(make_ratio):
      hist.plotratio(
      h1,h2,
      ax=ax1,
      clear=False,
      error_opts={'color': sigcolors["RunA"], 'marker': '+'},
      unc='num'
      )

  for sample in samples:
    if "sig" in sample:
      fil = directory+"myhistos_%s_2.p"%sample
      with open(fil, "rb") as pkl_file:
          out = pickle.load(pkl_file)
          xsec = xsecs[sample]
          scale= lumi*xsec/out["sumw"][sample]
          scaled = {}
          for name, h in out.items():
            if "dist_%s"%var != name:#if var not in name or "mu" in name or "trig" in name:
              continue
            if isinstance(h, hist.Hist):
              scaled[name] = h.copy()
              scaled[name].scale(scale)
              s = scaled[name].integrate("cut",slice(cut,cut+1))#.to_hist().to_numpy()
              if("ht" in name):
                s = s.rebin("v1",hist.Bin("v1","ht",50,50,3500))
              s_scale = s.values(sumw2=True)[()]
              s1= s.to_hist().to_numpy()
              xbin = xbins(s1[1])
              ## append an extra point at the end because the post doesn't work without it for the last bin. it needs to know where to go next
              ax.step(s1[1],np.append(s1[0],s1[0][-1]),color=sigcolors[sample],label=labels[sample],linestyle="--",where="post",zorder=2)
            ax.set_xlabel("")
  if(vline):
    ax.axvline(x=vline,color="grey",ls="--")
    if(make_ratio):
      ax1.axvline(x=vline,color="grey",ls="--")
        
  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
  if("res" in var):
    ax.set_yscale("linear")
    y1,y2 = ax.get_ylim()
    ax.set_ylim(y1,y2*1.50)
  else:
    ax.set_yscale("log")
    y1,y2 = ax.get_ylim()
    ax.set_ylim(y1,y2*100)
  if("ht" in var):
    ax.set_xlim([0,3500])
  if("PFcand_pt" in var):
    ax.set_xscale("log")
    ax.set_xlim([0.6,50])
  if("FatJet_pt" in var):
    ax.set_xlim([50,300])
  ax.set_ylabel("Events")
  if make_ratio:
    ax1.set_xlabel(xlab)
    ax1.set_ylim(0.5,1.5)     
    ax1.set_ylabel("Data/QCD")
    ax1.axhline(y=1,color="grey",ls="--")
  else:
    ax.set_xlabel(xlab)
  #ax.autoscale(axis='y', tight=True)
  if "res" in var:
    selcut = 3
  else:
    selcut = cut
  if shift_leg:
    ax.add_artist(AnchoredText(selection[selcut],loc="lower left",prop=dict(size=15)))
    ax.legend(loc="center left")
  else:
    ax.add_artist(AnchoredText(selection[selcut],loc="upper right",prop=dict(size=15)))
    ax.legend(loc="right")
  fig.savefig("Plots/overlap_dist_%s_cut%s.%s"%(var,cut,ext))
  plt.close()
  


def make_dists(sample,runPV=0):
  skip = ["trigdist_ht20","trigdist_ht30","trigdist_ht40","trigdist_ht50"]
  with open(directory+"myhistos_%s.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      xsec = xsecs[sample.split("_")[0]]
      #print(out)
      if "QCD" in sample:
        scale=lumi
      elif xsec ==0:
        scale = 1
      else:
        scale= lumi*xsec/out["sumw"][sample.split("_")[0]]
      scaled = {}
      for name, h in out.items():
        #if "SR1" in name or "2d" in name:
        if "SR1" in name or "trkID" in name or "2d" in name:
          continue
        if name in skip:
          continue
        print(name)
        if isinstance(h, hist.Hist):
          scaled[name] = h.copy()
          scaled[name].scale(scale)
      
      
          fig, ax1 = plt.subplots()
          if(runPV):
            scaled[name] = scaled[name].remove(["cut 3:fj>=2"],"cut")
            scaled[name] = scaled[name].remove(["cut 4:nPFCand75>=140"],"cut")
          else:
            scaled[name] = scaled[name].remove(["cut 3:Pre + nPVs < 30"],"cut")
            scaled[name] = scaled[name].remove(["cut 4:Pre + nPVs >=30"],"cut")
         # if "trkID" in name:
         #   scaled[name] = scaled[name].integrate("v2").copy()
          hx = hist.plot1d(
              scaled[name],
              ax=ax1,
              overlay="cut",
              stack=False,
              fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
          )
          hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
          if "trkID" not in name:
            ax1.set_yscale("log")
            ax1.autoscale(axis='y', tight=True)
          if "_pt" in name and "res" not in name and "Dispersion" not in name:
            ax1.set_xscale("log")
            ax1.set_xlim([20,200])
            if "PFcand" in name or "gen" in name:
              ax1.set_xlim([0.3,100])
          if "dR" in name:
            ax1.set_yscale("log")
            ax1.axvline(x=0.02,color="grey",ls="--")
          fig.savefig("Plots/proccess_%s_%s_PV%s.%s"%(sample,name,runPV,ext))
          plt.close()
  
def func(x,a,b,c,d):
  return a*scipy.special.erf((x-b)/c)+d 
def make_trkeff(sample,name,xlab,runPV=0):
  with open(directory+"myhistos_%s.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      sample = sample.split("_")[0]
      xsec = xsecs[sample.split("_")[0]]
      if xsec ==0:
        scale = 1
      else:
        scale= lumi*xsec/out["sumw"][sample]
      #out[name].scale(scale)
      
     
      if("IDFK" in name): 
        ###############FAKE
        #num = out[name].integrate("v2",slice(0,0.02)).copy()
        numFK = out[name].integrate("v2",slice(0.02,0.3)).copy()
        denom = out[name].integrate("v2").copy()
        fig, ax1 = plt.subplots()
        ### note that the cut order goes 0,10,1,2,3,... so cut 10 is actually number 1 and all others are shifted +1 except 10. dumb dumb dumb
        for i,cut in enumerate([3,4,5,8,1]):
        #for i,cut in enumerate([0,2,3,4,5,6,7,8,9,10,1]):
        #  print("SUM: ",sum(denom.integrate("cut",slice(cut,1+cut)).sum().values()[()]))
        #for i,cut in enumerate([0,1,2,3,4,5,6,7,8,9,10]):
        #for i,cut in enumerate([2,3,4,7,10]):
          hx1 = hist.plotratio(
              numFK.integrate("cut",slice(cut,1+cut)),denom.integrate("cut",slice(cut,1+cut)),
              ax=ax1,
              clear=False,
              error_opts={'color': colors[i], 'marker': '+'},
              unc='clopper-pearson'
          )

        #ax1.set_ylim(0,0.5)
        if "_pt" in name:
          ax1.set_xscale("log")
          ax1.set_xlim([20,200])
          if "PFcand" in name or "gen" in name:
            ax1.set_xlim([0.5,100])
        ax1.legend(["q != 0","PV =0","pt > 0.5","pt >0.75","pt >1.0",],loc="lower right")
        ax1.set_xlabel(xlab)
        ax1.set_ylabel("Fake Rate")
        #ax1.legend(["no cut", "|eta| < 2.4","q != 0","PV =0","pt > 0.5","pt >0.6","pt >0.7","pt >0.75","pt >0.8","pt >0.9","pt >1.0",],loc="lower right")
        fig.suptitle("Track Fake Rate: %s"%sample)
        hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
        fig.savefig("Plots/track_fake_%s_%s.%s"%(sample,name,ext))
        plt.close()
      else:
        ######EFF
        num = out[name].integrate("v3",slice(0,4)).integrate("v2",slice(0,0.02)).copy()
        denom = out[name].integrate("v3",slice(0,4)).integrate("v2").copy()
        numPV = out[name].integrate("v3",slice(0,1)).integrate("v2",slice(0,0.02)).copy()
        denomPV = out[name].integrate("v3",slice(0,1)).integrate("v2").copy()
        fig, ax1 = plt.subplots()
        cuts = [1,4,6]
        leg = ["pt >0.6","pt >0.8","pt >1.0"]
        #leg = ["pt >0.6","PV==0 + pt >0.6","pt >0.8","PV==0 + pt >0.8","pt >1.0","PV==0 + pt >1.0"]
        if "_pt" in name:
          cuts=[0]
          leg = ["pt> 0.5","PV==0 + pt >0.5"]
          ax1.set_xscale("log")
          ax1.set_xlim([20,200])
          if "PFcand" in name or "gen" in name:
            ax1.set_xlim([0.5,100])
        #ax1.legend(["pt > 0.5","pt >0.6","pt >0.7","pt >0.75","pt >0.8","pt >0.9","pt >1.0",],loc="lower right")
        for i,cut in enumerate(cuts):
          if(runPV==0):
            hx = hist.plotratio(
                num.integrate("cut",slice(1+cut,2+cut)),denom.integrate("cut",slice(1+cut,2+cut)),
                ax=ax1,
                clear=False,
                error_opts={'color': colors[i], 'marker': '+'},
                unc='clopper-pearson'
            )
          if(runPV==1):
            hxPV = hist.plotratio(
                numPV.integrate("cut",slice(1+cut,2+cut)),denomPV.integrate("cut",slice(1+cut,2+cut)),
                ax=ax1,
                clear=False,
                error_opts={'color': colors[i], 'marker': 'x'},
                unc='clopper-pearson'
            )
          if(runPV==2):
            hx = hist.plotratio(
                num.integrate("cut",slice(1+cut,2+cut)),denom.integrate("cut",slice(1+cut,2+cut)),
                ax=ax1,
                clear=False,
                error_opts={'color': colors[i], 'marker': '+'},
                unc='clopper-pearson'
            )
            hxPV = hist.plotratio(
                numPV.integrate("cut",slice(1+cut,2+cut)),denomPV.integrate("cut",slice(1+cut,2+cut)),
                ax=ax1,
                clear=False,
                error_opts={'color': colors[i], 'marker': 'x'},
                unc='clopper-pearson'
            )

        ax1.legend(leg,loc="lower right")
        ax1.set_ylim(0.7,1.01)
        ax1.set_xlabel(xlab)
        ax1.set_ylabel("Efficiency")
        fig.suptitle("Track Efficiency: %s"%sample)
        hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
        fig.savefig("Plots/track_eff_%s_%s_%d.%s"%(sample,name,runPV,ext))
        plt.close()

def make_multitrigs(sig,varsx,qcdpd=None):
  fig, ax = plt.subplots(
  nrows=1,
  ncols=1,
  figsize=(7,7),
  )
  xs = np.linspace(0,1500,100)
  nevts = {"ht20":[],"ht30":[],"ht40":[],"ht50":[]}
  for i,var in enumerate(varsx):
    if sig == "QCD":
        s = qcdscaled["trigdist_%s"%var].integrate("cut",slice(3,4))#.to_hist().to_numpy()
        s0 = qcdscaled["trigdist_%s"%var].integrate("cut",slice(1,2))#.to_hist().to_numpy()
        if("ht" in var):
          s = s.rebin("v1",hist.Bin("v1","ht",[*range(0,700,40)]+[700,800,1000,1200,1500]))
          s0 = s0.rebin("v1",hist.Bin("v1","ht",[*range(0,700,40)]+[700,800,1000,1200,1500]))
        s1 = s.to_hist().to_numpy()[0]
        s2 = s0.to_hist().to_numpy()[0]
        points = np.nan_to_num(s1/s2)
        popt, pcov = curve_fit(func,xbins(s.to_hist().to_numpy()[1]),points,p0=[0.5,500,100,0.5])
        hx = hist.plotratio(
            #out["trigdist_%s"%var].integrate("cut",slice(3,4)),out["trigdist_%s"%var].integrate("cut",slice(1,2)),
            s,s0,
            ax=ax,
            clear=False,
            error_opts={'color': colors[i], 'marker': '.'},
            unc='clopper-pearson'
        )
        p98sig = 1.65*popt[2]+popt[1]
        p90sig = 1.163*popt[2]+popt[1]
        ax.plot(xs,func(xs,popt[0],popt[1],popt[2],popt[3]), color=colors[i],label="%s"%var)#: 90:%d 98:%d "%(sample,p90sig,p98sig))
        for thres in [500,525,560,700]:
          thres_index = list(map(lambda i: i >= thres, s.to_hist().to_numpy()[1])).index(True)
          nevts[var].append(np.sum(s1[thres_index:]))
    else:
      with open(directory+"myhistos_%s.p"%sig, "rb") as pkl_file:
          out = pickle.load(pkl_file)
          sample = sig.split("_")[0]
          xsec = xsecs[sample.split("_")[0]]
          if xsec ==0:
            scale = 1
          else:
            scale= lumi*xsec/out["sumw"][sample]
          out["trigdist_%s"%var].scale(scale)
          s = out["trigdist_%s"%var].integrate("cut",slice(3,4))#.to_hist().to_numpy()
          s0 = out["trigdist_%s"%var].integrate("cut",slice(1,2))#.to_hist().to_numpy()

          if("ht" in var):
            s = s.rebin("v1",hist.Bin("v1","ht",[*range(0,700,40)]+[700,800,1000,1200,1500]))
            s0 = s0.rebin("v1",hist.Bin("v1","ht",[*range(0,700,40)]+[700,800,1000,1200,1500]))
          s1 = s.to_hist().to_numpy()[0]
          s2 = s0.to_hist().to_numpy()[0]
          points = np.nan_to_num(s1/s2)
          popt, pcov = curve_fit(func,xbins(s.to_hist().to_numpy()[1]),points,p0=[0.5,500,100,0.5])
          hx = hist.plotratio(
              #out["trigdist_%s"%var].integrate("cut",slice(3,4)),out["trigdist_%s"%var].integrate("cut",slice(1,2)),
              s,s0,
              ax=ax,
              clear=False,
              error_opts={'color': colors[i], 'marker': '.'},
              unc='clopper-pearson'
          )
          p98sig = 1.65*popt[2]+popt[1]
          p90sig = 1.163*popt[2]+popt[1]
          ax.plot(xs,func(xs,popt[0],popt[1],popt[2],popt[3]), color=colors[i],label="%s"%var)#: 90:%d 98:%d "%(sample,p90sig,p98sig))
          for thres in [500,525,560,700]:
            thres_index = list(map(lambda i: i >= thres, s.to_hist().to_numpy()[1])).index(True)
            nevts[var].append(np.sum(s1[thres_index:]))
  print(sig)
  df = pd.DataFrame(nevts,index=[500,525,560,700])
  print(df)
  ax.set_ylim(0,1.1)
  ax.legend(loc="lower right")
  ax.set_xlabel("Ht [GeV]")
  ax.set_ylabel("Efficiency")
  ax.axvline(x=500,color="grey")
  ax.axvline(x=525,color="grey")
  ax.axvline(x=560,color="grey")
  ax.axvline(x=700,color="grey")
  ax.axhline(y=0.90,color="grey")
  fig.suptitle("HT Trigger Efficiency CaloJet40 reference: %s"%sig)
  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
  fig.savefig("Plots/trigmulti_%s.%s"%(sig,ext))
  plt.close()
  if qcdpd is not None:
    divpd = df/((df+qcdpf).apply(np.sqrt))
    print(divpd)
  #print("%s %s %s %s"%(df["ht20"][3],df["ht30"][2],df["ht40"][1],df["ht50"][0]))
  return df
def make_trigs(samples,var="ht",systematics =False):
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
  if("Data" in samples):
      fig.subplots_adjust(hspace=.07)

      
      #b = qcdscaled["trigdist_%s"%var].integrate("cut",slice(3,4))#.to_hist().to_numpy()
      #b0 = qcdscaled["trigdist_%s"%var].integrate("cut",slice(1,2))#.to_hist().to_numpy()
      b = qcdscaled["trigdist_%s"%var].integrate("cut",slice(5,6))#.to_hist().to_numpy()
      b0 = qcdscaled["trigdist_%s"%var].integrate("cut",slice(4,5))#.to_hist().to_numpy()
      if("ht" in var):
        b = b.rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
        b0 = b0.rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
      #b1 = b.to_hist().to_numpy()[0]
      #b2 = b0.to_hist().to_numpy()[0]
      b1 = b.values(sumw2=True)[()][0]#.to_hist().to_numpy()[0]
      b2 = b0.values(sumw2=True)[()][0]#.to_hist().to_numpy()[0]
      b1_err = np.sqrt(b.values(sumw2=True)[()][1])#.to_hist().to_numpy()[0]
      b2_err = np.sqrt(b0.values(sumw2=True)[()][1])#.to_hist().to_numpy()[0]
      #print(b1)
      #print(b1_err)
      #print(b2)
      #print(b2_err)
      #if systematics ==1:
      #  b1 = b1+b1_err
      #  b2 = b2+b2_err
      #if systematics ==2:
      #  b1 = b1-b1_err
      #  b2 = b2-b2_err
      
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
      #print(d1)
      #print(d1_err)
      #print(d2)
      #print(d2_err)
      #if systematics ==3:
      #  d1 = d1+d1_err
      #  d2 = d2+d2_err
      #if systematics ==4:
      #  d1 = d1-d1_err
      #  d2 = d2-d2_err
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
      #ax.axvline(x=p98sig,color="blue",ls="--")
      #ax.axvline(x=p90sig,color="blue",ls=":")
      #ax.axvline(x=p98bkg,color="red",ls="--")
      #ax.axvline(x=p90bkg,color="red",ls=":")
      #ax.axvline(x=p98dat,color="black",ls="--")
      #ax.axvline(x=p90dat,color="black",ls=":")

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
      hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
      fig.savefig("Plots/trig%s_data.%s"%(var,ext))
      plt.close()
  else:
    b = qcdscaled["trigdist_%s"%var].integrate("cut",slice(5,6))#.to_hist().to_numpy()
    b0 = qcdscaled["trigdist_%s"%var].integrate("cut",slice(4,5))#.to_hist().to_numpy()
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
      with open(directory+"myhistos_%s.p"%sample, "rb") as pkl_file:
          out = pickle.load(pkl_file)
          sample = sample.split("_")[0]
          xsec = xsecs[sample.split("_")[0]]
          if xsec ==0:
            scale = 1
          else:
            scale= lumi*xsec/out["sumw"][sample]
          out["trigdist_%s"%var].scale(scale)
          
          

          #Trigger plots
          sx = out["trigdist_%s"%var].integrate("cut",slice(5,6))#.to_hist().to_numpy()
          s0x = out["trigdist_%s"%var].integrate("cut",slice(4,5))#.to_hist().to_numpy()
          if("ht" in var):
            s = sx.copy().rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
            s0 = s0x.copy().rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
          else:
            s = sx
            s0 = s0x
          s1 = s.to_hist().to_numpy()[0]
          s2 = s0.to_hist().to_numpy()[0]
          #if("sig1000" in sample or "sig700" in sample):
          #  s = sx.rebin("v1",hist.Bin("v1","ht",[*range(0,700,70)]+[700,800,1000,1200,1500]))
          #  s0 = s0x.rebin("v1",hist.Bin("v1","ht",[*range(0,700,70)]+[700,800,1000,1200,1500]))

          points = np.nan_to_num(s.to_hist().to_numpy()[0]/s0.to_hist().to_numpy()[0])
          popt, pcov = curve_fit(func,xbins(s.to_hist().to_numpy()[1]),points,p0=[0.5,500,100,0.5])
          #p98sig = 1.65*popt[2]+popt[1]
          #p90sig = 1.163*popt[2]+popt[1]
          ax.plot(xs,func(xs,popt[0],popt[1],popt[2],popt[3]), color=sigcolors[sample],label=labels[sample])#: 90:%d 98:%d "%(sample,p90sig,p98sig))
          hx = hist.plotratio(
              s,s0,
              #out["trigdist_%s"%var].integrate("cut",slice(3,4)),out["trigdist_%s"%var].integrate("cut",slice(1,2)),
              ax=ax,
              clear=False,
              error_opts={'color': sigcolors[sample], 'marker': '.'},
              unc='clopper-pearson'
          )
          ax.set_xlabel("")

          

          #ax.axvline(x=700,color="grey",ls="--")
          #ax.axvline(x=p98sig,color="blue",ls="--")
          #ax.axvline(x=p90sig,color="blue",ls=":")
          #ax.axvline(x=p98bkg,color="red",ls="--")
          #ax.axvline(x=p90bkg,color="red",ls=":")

          hxrat = ax1.scatter(xbins(b.to_hist().to_numpy()[1]),(b1/b2)/(s1/s2),marker=".",color=sigcolors[sample])

    ax1.axhline(y=1,color="grey",ls="--")
    ax.axvline(x=560,color="grey",ls="--")
    ax.set_ylim(0,1.1)
    ax1.set_ylim(0.5,1.5)
    if(var=="FatJet_nconst"):
      ax1.set_xlim([0,300])
      ax.set_xlim([0,300])
    ax.set_label("")
    ax.set_ylabel("Efficiency")
    ax.legend(loc="lower right")
    fig.suptitle("HT Trigger Efficiency DoubleMu3 Reference: Sig")
    hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
    fig.savefig("Plots/trig%s_sig.%s"%(var,ext))
    plt.close()



def get_sig(s,sb,rangex):
  sig = []
  bkg = []
  #print(s)
  for i in range(len(rangex)):
    sig.append(np.sum(s[i:]))
    bkg.append(np.sum(sb[i:])) # + 1e-9)
  return(sig,bkg)

#def make_signif(sample,xsec):
#  #qcdscaled = {}
#  #with open(directory+"myhistos_QCD.p", "rb") as pkl_file:
#  #    out = pickle.load(pkl_file)
#  #    for name, h in out.items():
#  #      if isinstance(h, hist.Hist):
#  #        qcdscaled[name] = h.copy()
#  with open(directory+"myhistos_%s_0.p"%sample, "rb") as pkl_file:
#      out = pickle.load(pkl_file)
#      scale= lumi*xsec/out["sumw"][sample]
#      scaled = {}
#      for name, h in out.items():
#        if "trig" in name:
#          continue
#        if isinstance(h, hist.Hist):
#          scaled[name] = h.copy()
#          scaled[name].scale(scale)
#      
#      
#          fig, ax1 = plt.subplots()
#          for cut in [0,1,2,3,4]:
#            s = scaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy()
#            sb = (qcdscaled[name].integrate("cut",slice(cut,cut+1)) + scaled[name].integrate("cut",slice(cut,cut+1))).to_hist().to_numpy()
#            xbin = xbins(s[1])
#            #sig, sigbkg = get_sig(s[0],sb[0],s[1][:-1])
#            #ax1.errorbar(s[1][:-1],sig/np.sqrt(sigbkg),(sig/(np.sqrt(sigbkg)))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(np.multiply(4,sigbkg)))),ecolor=colors[cut],color=colors[cut],label=cuts[cut],marker="+")
#            sig, sigbkg = get_sig(s[0],sb[0],xbin)
#            ax1.errorbar(xbin,sig/np.sqrt(sigbkg),(sig/(np.sqrt(sigbkg)))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(np.multiply(4,sigbkg)))),ecolor=colors[cut],color=colors[cut],label=cuts[cut],marker="+")
#          ax1.legend()
#          ax1.set_xlabel(name[5:])
#          ax1.set_ylabel("s/sqrt(s+b+0.5$b^{2}$)")
#          hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
#          fig.savefig("Plots/signif_%s.%s"%(name,ext))
#          plt.close()



def make_threshold(samples,allmaxpoints,xs,xlab):
  fig, (ax1) = plt.subplots(
      nrows=1,
      ncols=1,
      figsize=(7,7),
  )
  fig.subplots_adjust(hspace=.07)
  for sample in samples: 
       
      ax1.errorbar(xs,allmaxpoints["sig_%s"%sample],allmaxpoints["err_%s"%sample],ecolor=sigcolors[sample],color=sigcolors[sample],label=labels[sample],marker="+")
      #ax.errorbar(xs,allmaxpoints["evt_%s"%sample],1,ecolor=sigcolors[sample],color=sigcolors[sample],label=sample,marker="+")

  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax1)
  ax1.set_xlabel(xlab)
  ax1.set_ylabel("s/sqrt(s+b+$b^{2}$)")
  ax1.legend()
  fig.savefig("Plots/threshold_%s.%s"%(xlab,ext))
  plt.close()
def make_n1(samples,var,cut,maxpoints,xlab=None,shift_leg=False):
  name1 = "dist_%s"%var
  if(xlab==None):
    xlab= name1[5:]
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)

  qcd = qcdscaled[name1].integrate("cut",slice(cut,cut+1))
  qcd.label = "QCD"
  hx = hist.plot1d(
      qcd,
      ax=ax,
      stack=False,
      fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3),"color":"wheat"}
  )
  large_max = False 
  large_max2 = False 
  for sample in samples:
    with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
        out = pickle.load(pkl_file)
        #print(out)
        scale= lumi*xsecs[sample]/out["sumw"][sample]
        scaled = {}
        for name, h in out.items():
          if name1 != name or "mu" in name:
            continue
          if isinstance(h, hist.Hist):
            scaled[name] = h.copy()
            scaled[name].scale(scale)
        
        
            s = scaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy()
            b = qcdscaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy()
            #sb = np.add(np.add(s,b),0.5*np.square(b))

            xbin = xbins(s[1])
            sig, bkg = get_sig(s[0],b[0],xbin)
            sigbkg = np.add(np.add(sig,bkg),np.square(bkg))
            signifline = sig/np.sqrt(np.add(np.add(sig,bkg),np.square(bkg)))
            #sig, sigbkg = get_sig(s[0],(sb)[0],xbin)
            #signifline = sig/np.sqrt(sigbkg)
            err = (signifline)*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(np.multiply(4,sigbkg))))
            ax1.errorbar(xbin,signifline,err,ecolor=sigcolors[sample],color=sigcolors[sample],label=labels[sample],marker="+")

            ax.step(s[1],np.append(s[0],s[0][-1]),color=sigcolors[sample],label=labels[sample],linestyle="--",where="post")
            #ax.step(xbin,s[0],color=sigcolors[sample],label=labels[sample],linestyle="--",where="mid")
            if("fjn1" in name):
              maxpoints["sig_%s"%sample].append(signifline[3])
              maxpoints["err_%s"%sample].append(err[3])
              maxpoints["evt_%s"%sample].append(sum(s[0][2:]))
            else:
              maxpoints["sig_%s"%sample].append(np.nanmax(signifline))
              maxpoints["evt_%s"%sample].append(sum(s[0][np.nanargmax(signifline):]))
              maxpoints["err_%s"%sample].append(err[np.nanargmax(signifline)])
            if(np.nanmax(signifline) > 1):
              large_max = True
            if(np.nanmax(signifline) > 60):
              large_max2 = True
  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
  ax.set_yscale("log")
  y1,y2 = ax.get_ylim()
  ax.set_ylim(y1,y2*10)
  ax.set_xlabel("")
  ax1.set_xlabel(xlab)
  ax1.set_ylabel("s/sqrt(s+b+$b^{2}$)")
  ax.set_ylabel("Events")
  leg1, leg = ax.get_legend_handles_labels()
  leg = [l.replace("None","QCD") for l in leg]
  if shift_leg:
    locx = "center left"
    locy = "lower left"
  else:
    locx = "upper right"
    locy = "right"
    
  if("fjn1" in var):
    ax.add_artist(AnchoredText("Selection:\n Trigger\n %s>560 GeV\n"%(r"$H_{t}$"),loc=locx))
  elif("PFcand_ncount" in var):
    ax.add_artist(AnchoredText("Selection:\n Trigger\n %s>560 GeV\n 2+ AK15 Jets\n sphericity > 0.7"%(r"$H_{t}$"),loc=locx))
  else:
    ax.add_artist(AnchoredText(selection[cut],loc=locx))
  ax.legend(leg,loc=locy)
  #ax1.legend()
  if large_max2:
    ax1.set_ylim([0,100])
  elif large_max:
    ax1.set_ylim([0,60])
  else:
    ax1.set_ylim([0,1])
  #ax.autoscale(axis='y', tight=True)
  fig.savefig("Plots/signif_%s_%s.%s"%(var,cut,ext))
  plt.close()

  return maxpoints

def get_sig2d(s,sb,rangex,rangey):
  sig = []
  bkg = []
  #print(s)
  for i in range(len(rangex)):
    sig1 = []
    bkg1 = []
    for j in range(len(rangey)):
      sig1.append(np.sum(s[i:,j:]))
      bkg1.append(np.sum(sb[i:,j:])) # + 1e-9)
    sig.append(sig1)
    bkg.append(bkg1)
  return(sig,bkg)

def makeCombineHistograms(samples,var,cut):
  f = ROOT.TFile.Open("combineInput.root","RECREATE")
  #makeQCD = True
  for sample in samples:
    for systematic in ["","killtrk","AK4up","AK4down"]:
      with open(directory+"myhistos_%s_2%s.p"%(sample,systematic), "rb") as pkl_file:
          out = pickle.load(pkl_file)
          scale= lumi*xsecs[sample]/out["sumw"][sample]
          scaled = {}
          var2 = var+"_%s"%cut
          xvar = "SUEP Jet Track Multiplicity"
          for name, h in out.items():
            if var2 not in name:
              continue
            if isinstance(h, hist.Hist):
              scaled[name] = h.copy()
              scaled[name].scale(scale)
              s = scaled[name].to_hist().to_numpy()
              if systematic == "":
                b = qcdscaled[name].to_hist().to_numpy()
              else:
                systematic = "_"+systematic #for aesthetic purposes

              x1 = 0
              x2 = inner_tracks
              x3 = region_cuts_tracks[0]
              x4 = 300
              y1 = 30
              y2 = inner_sphere
              y3 = region_cuts_sphere[0]
              y4 = 100
              if sample == "sig200" or sample == "sig125":
                point=1
                #x0 = 70 
                #y0 =  90
              if sample == "sig300" or sample == "sig400": 
                point=2
                #x0 = 80
                #y0 = 80
              if sample == "sig700" or sample == "sig1000": 
                point=3
                #x0 = 100
                #y0 = 70
              x0 = region_cuts_tracks[point]
              y0 = region_cuts_sphere[point]
              for region in ["A","B","C","D","E","F","G","H","SR","ALL"]:
                if region == "A":
                  xx = x1
                  xxx = x2
                  yy = y1
                  yyy = y2
                elif region == "B":
                  xx = x2
                  xxx = x3
                  yy = y1
                  yyy = y2
                elif region == "C":
                  xx = x0
                  xxx = x4
                  yy = y1
                  yyy = y2
                elif region == "D":
                  xx = x1
                  xxx = x2
                  yy = y2
                  yyy = y3
                elif region == "E":
                  xx = x2
                  xxx = x3
                  yy = y2
                  yyy = y3
                elif region == "F":
                  xx = x0
                  xxx = x4
                  yy = y2
                  yyy = y3
                elif region == "G":
                  xx = x1
                  xxx = x2
                  yy = y0
                  yyy = y4
                elif region == "H":
                  xx = x2
                  xxx = x3
                  yy = y0
                  yyy = y4
                elif region == "SR":
                  xx = x0
                  xxx = x4
                  yy = y0
                  yyy = y4
                elif region == "ALL":
                  xx = 0
                  xxx = x4
                  yy = 0
                  yyy = y4
                else:
                  print("what happened")
                  pass
                h = ROOT.TH2F("%s_%s%s"%(sample,region,systematic),"%s_%s%s"%(sample,region,systematic),300,0,300,100,0,1)
                if systematic == "":
                  hb = ROOT.TH2F("QCD_%s_%s"%(sample,region),"QCD_%s_%s"%(sample,region),300,0,300,100,0,1)
                for x in range(xx,xxx):
                  for y in range(yy,yyy):
                    print(s[2][x],s[3][y],s[0][0][x][y])
                    h.Fill(s[2][x],s[3][y],s[0][0][x][y])
                    if systematic == "":
                      print(b[2][x],b[3][y],b[0][0][x][y])
                      hb.Fill(b[2][x],b[3][y],b[0][0][x][y])
                h.Write()
                if systematic == "":
                  hb.Write()
  f.Close()
def makeSRSignif(sample,var,cut,xline=None,yline=None):
  with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      scale= lumi*xsecs[sample]/out["sumw"][sample]
      scaled = {}
      var2 = var+"_%s"%cut
      print(var2)
      xvar = "SUEP Jet Track Multiplicity"
      for name, h in out.items():
        if var2 not in name:
          continue
        if isinstance(h, hist.Hist):
          scaled[name] = h.copy()
          scaled[name].scale(scale)
          s = scaled[name].to_hist().to_numpy()
          b = qcdscaled[name].to_hist().to_numpy()
          #print(s)
          sb = b[0][0]
          #sb = np.add(s[0][0],b[0][0])
          #sb = np.add(np.add(s[0][0],b[0][0]),0.5*np.square(b[0][0]))
          #sb = s[0][0]+b[0][0]#+0.5*np.square(b[0][0])
          #sb = b[0][0]*b[0][0]
          #print(b[0][0][70][70])
          sig, sigbkg = get_sig2d(s[0][0],sb,xbins(s[2]),xbins(s[3]))
          signif = sig/ np.sqrt(np.add(np.add(sig,sigbkg),np.square(sigbkg)))
          #signif = sig/ np.sqrt(sig+sigbkg)
          #signif = sig/ np.sqrt(sigbkg)
          signif = np.nan_to_num(signif)
          maxi = np.max(signif)
          maxindex = unravel_index(np.argmax(signif),signif.shape)
          maxes = heapq.nlargest(5,range(len(signif.flatten())),signif.flatten().take)
          for m in maxes:
            u = unravel_index(m,signif.shape)
          
          fig, ax = plt.subplots()
          shw = ax.imshow(np.transpose(signif), interpolation='none',origin="lower",cmap="gist_ncar")
          #shw = ax.imshow(np.transpose(signif), interpolation='none',origin="lower",cmap="autumn")
          ax.set_xticks([0,50,100,150,200,250,300])
          ax.set_xticklabels([0,50,100,150,200,250,300])
          ax.set_yticks([0,20,40,60,80,100])
          ax.set_yticklabels([0,.20,.40,.60,.80,1])
          bar = plt.colorbar(shw)
          bar.set_label("Significance")
          ax.set_xlabel(xvar)
          if( xline is not None):
            ax.axvline(x=xline,color="grey")
          if( yline is not None):
            ax.axhline(y=yline,color="grey")
          ax.set_ylabel("Boosted Sphericity")
          ax.text(maxindex[0],maxindex[1],"X=%.2f(%d,%.2f)"%(maxi,maxindex[0],maxindex[1]/100))
           
          
          ax.set_aspect("auto")
          fig.suptitle("Significance: %s"%sample)
          hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
          fig.savefig("Plots/signif2d_%s_%s_%s.%s"%(sample,var,cut,ext))
          plt.close()
def makeSRSignig9(sample="qcd",SR="SR1_suep",cut=3):
  if cut == 2 or cut == 3:
    #highx1 = 50
    #highx2 = 70
    #highy1 = 40
    #highy2 = 50
    highx2 = 70
    highy2 = 50
  else:
    #highx1 = 75
    highx2 = 100
    #highy1 = 40
    highy2 = 70
  var = "nPFCand"
  SR = SR+"_%s"%cut
  if sample == "qcd":
     h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  else:
    with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
        out = pickle.load(pkl_file)
        scale= lumi*xsecs[sample]/out["sumw"][sample]
        scaled = {}
        for name, h in out.items():
          if SR not in name or "mu" in name or "trig" in name:
            continue
          if isinstance(h, hist.Hist):
            scaled[name] = h.copy()
            scaled[name].scale(scale)
            h1 = (scaled[SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
  
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
  signif=[]
  for highx1 in range(0,highx2,2):
    signif1=[]
    for highy1 in range(30,highy2,4):
      abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
      cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
      fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
      SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]

      abinx = abin[0]
      bbinx = bbin[0]
      cbinx = cbin[0]
      dbinx = dbin[0]
      ebinx = ebin[0]
      fbinx = fbin[0]
      gbinx = gbin[0]
      hbinx = hbin[0]
      SRbinx = SRbin[0]
      A_err  = np.sqrt(abin[1])/abinx
      B_err  = np.sqrt(bbin[1])/bbinx
      C_err  = np.sqrt(cbin[1])/cbinx
      D_err  = np.sqrt(dbin[1])/dbinx
      E_err  = np.sqrt(ebin[1])/ebinx
      F_err  = np.sqrt(fbin[1])/fbinx
      G_err  = np.sqrt(gbin[1])/gbinx
      H_err  = np.sqrt(hbin[1])/hbinx
      SRbin_err = np.sqrt(SRbin[1])
      #ratx = (fbinx*(hbinx**2)*(dbinx**4))/(abinx*(ebinx**4)*cbinx*gbinx)
      ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2)) 

      error = 100*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2)
      #error = fbinx*ratx*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2)
      print(highx1,highy1,fbinx*ratx,error)
      print(highx1,highy1,SRbinx,SRbin_err)
      signif1.append(error)
    signif.append(signif1)
  signif = np.array(signif)
  mini = np.nanmin(signif)
  minindex = unravel_index(np.nanargmin(signif),signif.shape)
  #mins = heapq.nlargest(5,range(len(signif.flatten())),signif.flatten().take)
  #for m in mins:
  #  u = unravel_index(m,signif.shape)
  fig, ax = plt.subplots()
  shw = ax.imshow(np.transpose(signif), interpolation='none',origin="lower",cmap="gist_ncar")
  #shw = ax.imshow(np.transpose(signif), interpolation='none',origin="lower",cmap="autumn",norm=LogNorm(vmin=30,vmax=500))
  ax.set_xticks(range(0,35,5))
  ax.set_xticklabels([x*2 for x in range(0,35,5)])
  ax.set_yticks(range(0,10,2))
  ax.set_yticklabels([x*4+30 for x in range(0,10,2)])
  bar = plt.colorbar(shw)
  bar.set_label("Statistical Uncertainty (%)")
  ax.set_xlabel("SUEP Jet Track Multiplicity")
  ax.set_ylabel("Boosted Sphericity")
  ax.text(minindex[0],minindex[1],"X=%.2f(%d,%.2f)"%(mini,minindex[0]*2,(minindex[1]*4+30)/100))

  highx1 = minindex[0]*2
  highy1 = (minindex[1]*4+30)
  abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]

  abinx = abin[0]
  bbinx = bbin[0]
  cbinx = cbin[0]
  dbinx = dbin[0]
  ebinx = ebin[0]
  fbinx = fbin[0]
  gbinx = gbin[0]
  hbinx = hbin[0]
  SRbinx = SRbin[0]
  A_err  = np.sqrt(abin[1])/abinx
  B_err  = np.sqrt(bbin[1])/bbinx
  C_err  = np.sqrt(cbin[1])/cbinx
  D_err  = np.sqrt(dbin[1])/dbinx
  E_err  = np.sqrt(ebin[1])/ebinx
  F_err  = np.sqrt(fbin[1])/fbinx
  G_err  = np.sqrt(gbin[1])/gbinx
  H_err  = np.sqrt(hbin[1])/hbinx
  #print("A: ",(1*h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()][0])**2)
  #print("B: ",(2*h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()][0])**2)
  #print("C: ",(1*h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()][0])**2)
  #print("D: ",(2*h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()][0])**2)
  #print("E: ",(4*h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()][0])**2)
  #print("F: ",(2*h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()][0])**2)
  #print("G: ",(1*h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()][0])**2)
  #print("H: ",(2*h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()][0])**2)
  print("A: ",(1*A_err)**2)
  print("B: ",(2*B_err)**2)
  print("C: ",(1*C_err)**2)
  print("D: ",(2*D_err)**2)
  print("E: ",(4*E_err)**2)
  print("F: ",(2*F_err)**2)
  print("G: ",(1*G_err)**2)
  print("H: ",(2*H_err)**2)
  print("total: ",100*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2))
   
  ax.set_aspect("auto")
  fig.suptitle("Significance: %s"%sample)
  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
  fig.savefig("Plots/closureerr9_%s_%s_%s.%s"%(sample,var,cut,ext))
  plt.close()




def makeSR(sample,var,cut,lines=0,SR=0):
  with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      scale= lumi*xsecs[sample]/out["sumw"][sample]
      scaled = {}
      # get colormap
      ncolors = 2048
      color_array = plt.get_cmap('Blues')(range(ncolors))
      color_array2 = plt.get_cmap('Reds')(range(ncolors))
      
      # change alpha values
      color_array[:,-1] = np.linspace(0.0,1.0,ncolors)
      color_array2[:,-1] = np.linspace(0.0,1.0,ncolors)
      
      # create a colormap object
      map_object = LinearSegmentedColormap.from_list(name='blues_alpha',colors=color_array)
      map_object2 = LinearSegmentedColormap.from_list(name='reds_alpha',colors=color_array2)
      
      # register this new colormap with matplotlib
      plt.register_cmap(cmap=map_object)
      plt.register_cmap(cmap=map_object2)

      var2 = var+"_%s"%cut
      print(var2)
      xvar = "nPFCand"
      for name, h in out.items():
        if var2 not in name:
          continue
        if isinstance(h, hist.Hist):
          scaled[name] = h.copy()
          scaled[name].scale(scale)
          s = scaled[name].to_hist().to_numpy()#[0][0] #.integrate("cut",slice(cut,cut+1)).to_hist().to_numpy())
          b = qcdscaled[name].to_hist().to_numpy()#[0][0] #.integrate("cut",slice(cut,cut+1)).to_hist().to_numpy())
          print(s)
          #sb = b[0][0]#np.add(np.add(s[0][0],b[0][0]),0.5*np.square(b[0][0]))
          #sig, sigbkg = get_sig2d(s[0][0],(sb),xbins(s[2]),xbins(s[3]))
          #signif = sig/ np.sqrt(np.add(np.add(sig,sigbkg),0.5*np.square(sigbkg)))
          ##signif = sig/ np.sqrt(sigbkg)
          #signif = np.nan_to_num(signif)
          #maxi = np.max(signif)
          #maxindex = unravel_index(np.argmax(signif),signif.shape)
          #maxes = heapq.nlargest(5,range(len(signif.flatten())),signif.flatten().take)
          #for m in maxes:
          #  u = unravel_index(m,signif.shape)
          
          fig, ax1 = plt.subplots()
      
          hx = hist.plot2d(
              scaled[name].integrate("axis",slice(0,1)),
              xvar,
              ax=ax1,
          )
          hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
          fig.suptitle("SR: %s"%sample)
          fig.savefig("Plots/%s_sig_%s_%s.%s"%(var,sample,cut,ext))
          plt.close()
        
          fig, ax1 = plt.subplots()
      
          hx = hist.plot2d(
              qcdscaled[name].integrate("axis",slice(0,1)),
              xvar, 
              ax=ax1,
          )
          fig.suptitle("SR: QCD")
          hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
          fig.savefig("Plots/%s_bkg_%s.%s"%(var,cut,ext))
          plt.close()
        
          fig, ax1 = plt.subplots()
      
          h0 = hist.plot2d(
              scaled[name].integrate("axis",slice(0,1)),
              xvar, 
              ax=ax1,
              patch_opts={'cmap': 'blues_alpha',"vmin":0,"vmax":150}
          )
          h1 = hist.plot2d(
              qcdscaled[name].integrate("axis",slice(0,1)),
              xvar,
              ax=ax1,
              patch_opts={'cmap': 'reds_alpha',"vmin":0,"vmax":80000}
          )
          h2 = hist.plot2d(
              scaled[name].integrate("axis",slice(0,1)),
              xvar,
              ax=ax1,
              clear=False,
              patch_opts={'cmap': "blues_alpha","vmin":0,"vmax":150}
          )
          #if SR==0:
          #  #xline = 85
          #  #yline = 0.8
          #  xline = region_cuts_tracks[1]
          #  yline = region_cuts_sphere[1]/100. #0.5
          #if SR==1:
          #  #xline = 90
          #  #yline = 0.65
          #  xline = region_cuts_tracks[2]
          #  yline = region_cuts_sphere[2]/100. #0.5
          #if SR==2:
          #  xline = region_cuts_tracks[3]
          #  yline = region_cuts_sphere[3]/100. #0.5
          #if SR==2:
          xline = region_cuts_tracks[SR]
          yline = region_cuts_sphere[SR]/100. #0.5
          if lines==4:
            ax1.axhline(y=0.3,color="grey",ls="--")
            ax1.axhspan(0,0.3, hatch="/", color="grey",alpha=0.3)
            ax1.axvline(x=xline,color="red",ls="--")
            ax1.axhline(y=yline,color="red",ls="--")
            ax1.text(20,0.4,"A",fontsize = 22)
            ax1.text(20,0.8,"B",fontsize = 22)
            ax1.text(100,0.4,"C",fontsize = 22)
            ax1.text(100,0.8,"SR",fontsize = 22)
            ax1.text(20,0.15,"EXCLUDED",fontsize = 22)
          if lines==6:
            ax1.axhline(y=0.3,color="grey",ls="--")
            ax1.axhspan(0,0.3, hatch="/", color="grey",alpha=0.3)
            ax1.axvline(x=xline,color="red",ls="--")
            ax1.axhline(y=yline,color="red",ls="--")
            ax1.axvline(x=inner_tracks,color="blue",ls="--")
            ax1.text(0,0.4,"A",fontsize = 18)
            ax1.text(0,0.8,"D",fontsize = 18)
            ax1.text(40,0.4,"B",fontsize = 18)
            ax1.text(40,0.8,"E",fontsize = 18)
            ax1.text(100,0.4,"C",fontsize = 18)
            ax1.text(100,0.8,"SR",fontsize = 18)
            ax1.text(20,0.15,"EXCLUDED",fontsize = 22)
          if lines==9:
            ax1.axhline(y=0.3,color="grey",ls="--")
            ax1.axhspan(0,0.3, hatch="/", color="grey",alpha=0.3)
            ax1.axvline(x=inner_tracks,color="blue",ls="--")
            ax1.axhline(y=inner_sphere/100.,color="blue",ls="--")
            ax1.axvline(x=xline,color="red",ls="--")
            ax1.axhline(y=yline,color="red",ls="--")
            ax1.text(0,0.32,"A",fontsize = 18)
            ax1.text(0,0.4,"D",fontsize = 18)
            ax1.text(0,0.8,"G",fontsize = 18)
            ax1.text(40,0.32,"B",fontsize = 18)
            ax1.text(40,0.4,"E",fontsize = 18)
            ax1.text(40,0.8,"H",fontsize = 18)
            ax1.text(100,0.32,"C",fontsize = 18)
            ax1.text(100,0.4,"F",fontsize = 18)
            ax1.text(100,0.8,"SR",fontsize = 18)
            ax1.text(20,0.15,"EXCLUDED",fontsize = 22)
          fig.suptitle("SR: QCD + %s"%sample)
          ax1.set_xlabel("SUEP Jet Track Multiplicity")
          ax1.set_ylabel("Boosted Sphericity")

          hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
          fig.savefig("Plots/SR_%s_%s_bkg_%s_%s.%s"%(sample,var,cut,lines,ext))
          plt.close()
          
def make2dTrig(sample,cut,var2,ylab="Sphericity (Unboosted)",xlab="Ht [GeV]",yfactor=2):
  with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      scale= lumi*xsecs[sample]/out["sumw"][sample]
      scaled = {}
      #var2 = "trig2d_ht_event_sphericity"
      #print(var2)
      #xvar = "nPFCand"
      for name, h in out.items():
        if var2 not in name:
          continue
        if isinstance(h, hist.Hist):
          scaled[name] = h.copy()
          scaled[name].scale(scale)
          s = scaled[name].to_hist().to_numpy()
          print(s)
          ref = s[0][1]
          trig = s[0][3]
          x = xbins[s[2]]
          y = xbins[s[3]]
          xx,yy = np.meshgrid(x,y)
          z = np.nan_to_num(trig/ref)
          print(len(z),len(z[0]))
          print(len(xx[0]))
          print(len(yy[0]))
          xxx = xx.ravel()
          yyy = yy.ravel()
          zzz = z.ravel()
          print(len(xxx),len(yyy),len(zzz))
          print(yyy)
          print(zzz)
          df = pd.DataFrame({"ht":xxx,"sphericity" : yyy, "trig eff":zzz})
          print(df)
          piv = df.pivot(index = "ht",columns = "sphericity",values = "trig eff")
          
          fig, ax1 = plt.subplots()
          #sns.JointGrid(piv,x="ht",y="sphericity")
          g = sns.heatmap(np.transpose(z),cmap="Reds")
          #g = sns.heatmap(piv,cmap="Reds")
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
          hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
          plt.subplots_adjust(bottom=0.20)
          fig.savefig("Plots/trigeff2d_%s_%s.%s"%(sample,var2,ext))
          plt.close()

def make_systematics(samples,var,systematics1="",systematics2=""):
  name1 = "dist_%s"%var
  final_cut = 35 # 50 bins -> 35= 0.7 cut
  if systematics2 =="":
    cutflow = {"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[],"sig125%s"%(systematics1):[],"sig200%s"%(systematics1):[],"sig300%s"%(systematics1):[],"sig400%s"%(systematics1):[],"sig700%s"%(systematics1):[],"sig1000%s"%(systematics1):[]}
    syslist = ["",systematics1]
  else:
    cutflow = {"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[],"sig125%s"%(systematics1):[],"sig200%s"%(systematics1):[],"sig300%s"%(systematics1):[],"sig400%s"%(systematics1):[],"sig700%s"%(systematics1):[],"sig1000%s"%(systematics1):[],"sig125%s"%(systematics2):[],"sig200%s"%(systematics2):[],"sig300%s"%(systematics2):[],"sig400%s"%(systematics2):[],"sig700%s"%(systematics2):[],"sig1000%s"%(systematics2):[]}
    syslist = ["",systematics1,systematics2]
  for sample in samples:
    for systematic in syslist:#with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
      scaled = {}
      with open(directory+"myhistos_%s_2%s.p"%(sample,systematic), "rb") as pkl_file:
          out = pickle.load(pkl_file)
          #print(out)
          scale= lumi*xsecs[sample]/out["sumw"][sample]
          for name, h in out.items():
            #if name1 not in name or "mu" in name or "trig" in name:
            #  continue
            if isinstance(h, hist.Hist):
              scaled[name] = h.copy()
              scaled[name].scale(scale)
          
      for cut in [0,1,2]:#,3,4]: 
        s1 = scaled[name].integrate("cut",slice(cut,cut+1)).values()
        for (k,s) in s1.items():
          print("%s %d %s %.2f"%(sample,cut,name,s.sum()))
          cutflow[sample+systematic].append(s.sum())
      s2 = scaled["SR1_suep_3"].integrate("nPFCand",slice(0,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
      for (k,s) in s2.items():
        cutflow[sample+systematic].append(s.sum())
####  ######SR 1
      #x1 =70
      #y1 = 0.9
      x1 = region_cuts_tracks[1]
      y1 = region_cuts_sphere[1]/100.
      s3 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
      for (k,s) in s3.items():
        cutflow[sample+systematic].append(s.sum())

      s4 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
      for (k,s) in s4.items():
        cutflow[sample+systematic].append(s.sum())
####  ######SR 2
      x1 = region_cuts_tracks[2]
      y1 = region_cuts_sphere[2]/100.
      #x1 =80
      #y1 = 0.8
      s3 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
      for (k,s) in s3.items():
        cutflow[sample+systematic].append(s.sum())
      s4 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
      for (k,s) in s4.items():
        cutflow[sample+systematic].append(s.sum())
####  ######SR 3
      x1 = region_cuts_tracks[3]
      y1 = region_cuts_sphere[3]/100.
      #x1 =100
      #y1 = 0.7
      s3 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
      for (k,s) in s3.items():
        cutflow[sample+systematic].append(s.sum())
      s4 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
      for (k,s) in s4.items():
        cutflow[sample+systematic].append(s.sum())
  print(cutflow)          
  print(pd.DataFrame(cutflow))
  #print(pd.DataFrame(cutflow_sig))
  pd.set_option('display.float_format', lambda x: '%.2f' % x)
  #print(pd.DataFrame(cutflow_releff))
  #releff = pd.DataFrame(cutflow_releff)
  yields = pd.DataFrame(cutflow)
  #sigs = pd.DataFrame(cutflow_sig)
  print("##################  Yields  ################")
  cuts = ["Cut 0: No Cut:","Cut 1: Trigger", "Cut 2: $\HT > 560 \GeV$","Cut 3: AK15 Jets $>2$","Cut 4a: \\nSUEPConstituents $>%d$"%region_cuts_tracks[1],"Cut 5a: \\boostedSphericity $>0.%s$"%region_cuts_sphere[1],"Cut 4b: \\nSUEPConstituents $>%d$"%region_cuts_tracks[2],"Cut 5b: \\boostedSphericity $>0.%s$"%region_cuts_sphere[2],"Cut 4c: \\nSUEPConstituents $>%d$"%region_cuts_tracks[3],"Cut 5c:\\boostedSphericity $>0.%s$"%region_cuts_sphere[3]] 
  for i in yields.index:
    print("%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],yields["sig125"][i],yields["sig200"][i],yields["sig300"][i],yields["sig400"][i],yields["sig700"][i],yields["sig1000"][i]))
    if i == 3 or i==5 or i==7 or i==9:
      print("\\hline")
  print("##################  New Yields 1 ################")
  for i in yields.index:
    print("%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],yields["sig125%s"%(systematics1)][i],yields["sig200%s"%(systematics1)][i],yields["sig300%s"%(systematics1)][i],yields["sig400%s"%(systematics1)][i],yields["sig700%s"%(systematics1)][i],yields["sig1000%s"%(systematics1)][i]))
    if i == 3 or i==5 or i==7 or i==9:
      print("\\hline")
  if systematics2 == "":
    print("##################  Uncertainty  ################")
    for i in yields.index:
      print("%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],(yields["sig125"][i]-yields["sig125%s"%(systematics1)][i])/yields["sig125"][i],(yields["sig200"][i]-yields["sig200%s"%(systematics1)][i])/yields["sig200"][i],(yields["sig300"][i]-yields["sig300%s"%(systematics1)][i])/yields["sig300"][i],(yields["sig400"][i]-yields["sig400%s"%(systematics1)][i])/yields["sig400"][i],(yields["sig700"][i]-yields["sig700%s"%(systematics1)][i])/yields["sig700"][i],(yields["sig1000"][i]-yields["sig1000%s"%(systematics1)][i])/yields["sig1000"][i]))
      if i == 3 or i==5 or i==7 or i==9:
        print("\\hline")
  else:
    print("##################  New Yields 2 ################")
    for i in yields.index:
      print("%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],yields["sig125%s"%(systematics2)][i],yields["sig200%s"%(systematics2)][i],yields["sig300%s"%(systematics2)][i],yields["sig400%s"%(systematics2)][i],yields["sig700%s"%(systematics2)][i],yields["sig1000%s"%(systematics2)][i]))
      if i == 3 or i==5 or i==7 or i==9:
        print("\\hline")
    print("##################  Uncertainty  ################")
    for i in yields.index:
      print("%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],(yields["sig125%s"%(systematics1)][i]-yields["sig125%s"%(systematics2)][i])/yields["sig125"][i],(yields["sig200%s"%(systematics1)][i]-yields["sig200%s"%(systematics2)][i])/yields["sig200"][i],(yields["sig300%s"%(systematics1)][i]-yields["sig300%s"%(systematics2)][i])/yields["sig300"][i],(yields["sig400%s"%(systematics1)][i]-yields["sig400%s"%(systematics2)][i])/yields["sig400"][i],(yields["sig700%s"%(systematics1)][i]-yields["sig700%s"%(systematics2)][i])/yields["sig700"][i],(yields["sig1000%s"%(systematics1)][i]-yields["sig1000%s"%(systematics2)][i])/yields["sig1000"][i]))
      if i == 3 or i==5 or i==7 or i==9:
        print("\\hline")


def make_cutflow(samples,var,trkkill=""):
  name1 = "dist_%s"%var
  final_cut = 35 # 50 bins -> 35= 0.7 cut
  cutflow = {"QCD":[],"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  cutflow_sig = {"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  cutflow_releff = {"QCD":[],"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  for cut in [0,1,2]:#,3,4]: 
    b1 = qcdscaled[name1].integrate("cut",slice(cut,cut+1)).values()
    for (k,b) in b1.items():
      print("QCD %d %s %.2f"%(cut,name1,b.sum()))
      cutflow["QCD"].append(b.sum())
      if(cut >0):
        cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][cut-1])
  #b1 = qcdscaled[name1].integrate("cut",slice(4,5)).values()
  #for (k,b) in b1.items():
  #  print("QCD %d %s %.2f"%(cut,name1,b[final_cut:].sum()))
  #  cutflow["QCD"].append(b[final_cut:].sum())
  #  cutflow_releff["QCD"].append(100*b[final_cut:].sum()/cutflow["QCD"][4])
  b2 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(0,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
  for (k,b) in b2.items():
    print("QCD TESTTTTT %d %s %.2f"%(6,"test",b.sum()))
    cutflow["QCD"].append(b.sum())
    cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][2])
###########SR1 (70,.9)
  #x1 =70
  #y1 = 0.9
  x1 = region_cuts_tracks[1]
  y1 = region_cuts_sphere[1]/100.
  b3 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
  for (k,b) in b3.items():
    print("QCD TESTTTTT %d %s %.2f"%(7,"test",b.sum()))
    cutflow["QCD"].append(b.sum())
    cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][3])
  b4 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
  for (k,b) in b4.items():
    print("QCD TESTTTTT %d %s %.2f"%(8,"test",b.sum()))
    cutflow["QCD"].append(b.sum())
    cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][4])
###########SR2 (80,0.8)
  #x1 =80
  #y1 = 0.8
  x1 = region_cuts_tracks[2]
  y1 = region_cuts_sphere[2]/100.
  b3 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
  for (k,b) in b3.items():
    print("QCD TESTTTTT %d %s %.2f"%(7,"test",b.sum()))
    cutflow["QCD"].append(b.sum())
    cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][3])
  b4 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
  for (k,b) in b4.items():
    print("QCD TESTTTTT %d %s %.2f"%(8,"test",b.sum()))
    cutflow["QCD"].append(b.sum())
    cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][6])
###########SR3 (100,.70)
  #x1 =100
  #y1 = 0.7
  x1 = region_cuts_tracks[3]
  y1 = region_cuts_sphere[3]/100.
  b3 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
  for (k,b) in b3.items():
    print("QCD TESTTTTT %d %s %.2f"%(7,"test",b.sum()))
    cutflow["QCD"].append(b.sum())
    cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][3])
  b4 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
  for (k,b) in b4.items():
    print("QCD TESTTTTT %d %s %.2f"%(8,"test",b.sum()))
    cutflow["QCD"].append(b.sum())
    cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][8])
  for sample in samples:
    #with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
    with open(directory+"myhistos_%s_2%s.p"%(sample,trkkill), "rb") as pkl_file:
        out = pickle.load(pkl_file)
        #print(out)
        scale= lumi*xsecs[sample]/out["sumw"][sample]
        scaled = {}
        for name, h in out.items():
          #if name1 not in name or "mu" in name or "trig" in name:
          #  continue
          if isinstance(h, hist.Hist):
            scaled[name] = h.copy()
            scaled[name].scale(scale)
        
        for cut in [0,1,2]:#,3,4]: 
          s1 = scaled[name].integrate("cut",slice(cut,cut+1)).values()
          for (k,s) in s1.items():
            print("%s %d %s %.2f"%(sample,cut,name,s.sum()))
            cutflow[sample].append(s.sum())
            sigb = cutflow["QCD"][cut]
            signif = s.sum()/np.sqrt(s.sum()+sigb+(sigb**2))
            cutflow_sig[sample].append(signif)
            #cutflow_sig[sample+"_signif"].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][cut]))
            if(cut >0):
              cutflow_releff[sample].append(100*s.sum()/cutflow[sample][cut-1])
        #s1 = scaled[name].integrate("cut",slice(4,5)).values()
        #for (k,s) in s1.items():
        #  sval = s[final_cut:].sum()
        #  print("%s %d %s %.2f"%(sample,cut,name,sval))
        #  cutflow[sample].append(sval)
        #  cutflow_sig[sample+"_signif"].append(sval/np.sqrt(sval+cutflow["QCD"][5]+0.5*(cutflow["QCD"][5]**2)))
        #  cutflow_releff[sample].append(100*sval/cutflow[sample][4])
        s2 = scaled["SR1_suep_3"].integrate("nPFCand",slice(0,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
        for (k,s) in s2.items():
          #print("QCD TESTTTTT %d %s %.2f"%(6,"test",b.sum()))
          cutflow[sample].append(s.sum())
          cutflow_releff[sample].append(100*s.sum()/cutflow[sample][2])
          cutflow_sig[sample].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][3]+(cutflow["QCD"][3]**2)))
##############SR 1
        #x1 =70
        #y1 = 0.9
        x1 = region_cuts_tracks[1]
        y1 = region_cuts_sphere[1]/100.
        s3 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
        for (k,s) in s3.items():
          #print("QCD TESTTTTT %d %s %.2f"%(7,"test",b.sum()))
          cutflow[sample].append(s.sum())
          cutflow_releff[sample].append(100*s.sum()/cutflow[sample][3])
          cutflow_sig[sample].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][4]+(cutflow["QCD"][4]**2)))

        s4 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
        for (k,s) in s4.items():
          #print("QCD TESTTTTT %d %s %.2f"%(8,"test",b.sum()))
          cutflow[sample].append(s.sum())
          cutflow_releff[sample].append(100*s.sum()/cutflow[sample][4])
          cutflow_sig[sample].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][5]+(cutflow["QCD"][5]**2)))
##############SR 2
        #x1 =80
        #y1 = 0.8
        x1 = region_cuts_tracks[2]
        y1 = region_cuts_sphere[2]/100.
        s3 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
        for (k,s) in s3.items():
          #print("QCD TESTTTTT %d %s %.2f"%(7,"test",b.sum()))
          cutflow[sample].append(s.sum())
          cutflow_releff[sample].append(100*s.sum()/cutflow[sample][3])
          cutflow_sig[sample].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][6]+(cutflow["QCD"][6]**2)))
        s4 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
        for (k,s) in s4.items():
          #print("QCD TESTTTTT %d %s %.2f"%(8,"test",b.sum()))
          cutflow[sample].append(s.sum())
          cutflow_releff[sample].append(100*s.sum()/cutflow[sample][6])
          cutflow_sig[sample].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][7]+(cutflow["QCD"][7]**2)))
##############SR 3
        #x1 =100
        #y1 = 0.7
        x1 = region_cuts_tracks[3]
        y1 = region_cuts_sphere[3]/100.
        s3 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
        for (k,s) in s3.items():
          #print("QCD TESTTTTT %d %s %.2f"%(7,"test",b.sum()))
          cutflow[sample].append(s.sum())
          cutflow_releff[sample].append(100*s.sum()/cutflow[sample][3])
          cutflow_sig[sample].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][8]+(cutflow["QCD"][8]**2)))
        s4 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
        for (k,s) in s4.items():
          #print("QCD TESTTTTT %d %s %.2f"%(8,"test",b.sum()))
          cutflow[sample].append(s.sum())
          cutflow_releff[sample].append(100*s.sum()/cutflow[sample][8])
          cutflow_sig[sample].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][9]+(cutflow["QCD"][9]**2)))
            
  print(pd.DataFrame(cutflow))
  print(pd.DataFrame(cutflow_sig))
  pd.set_option('display.float_format', lambda x: '%.2f' % x)
  #print(pd.DataFrame(cutflow_releff))
  releff = pd.DataFrame(cutflow_releff)
  yields = pd.DataFrame(cutflow)
  sigs = pd.DataFrame(cutflow_sig)
  cuts = ["Cut 0: No Cut:","Cut 1: Trigger", "Cut 2: $\HT > 560 \GeV$","Cut 3: AK15 Jets $>2$","Cut 4a: \\nSUEPConstituents $>%d$"%region_cuts_tracks[1],"Cut 5a: \\boostedSphericity $>0.%s$"%region_cuts_sphere[1],"Cut 4b: \\nSUEPConstituents $>%d$"%region_cuts_tracks[2],"Cut 5b: \\boostedSphericity $>0.%s$"%region_cuts_sphere[2],"Cut 4c: \\nSUEPConstituents $>%d$"%region_cuts_tracks[3],"Cut 5c:\\boostedSphericity $>0.%s$"%region_cuts_sphere[3]] 
  print("##################  Yields  ################")
  for i in yields.index:
    print("%s & %.2e & %.2e & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],yields["QCD"][i],yields["sig125"][i],yields["sig200"][i],yields["sig300"][i],yields["sig400"][i],yields["sig700"][i],yields["sig1000"][i]))
    if i == 3 or i==5 or i==7 or i==9:
      print("\\hline")
  print("##################  RelEff  ################")
  for i in releff.index:
    print("%s & %.2e & %.2f & %.2f $ %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],releff["QCD"][i],releff["sig125"][i],releff["sig200"][i],releff["sig300"][i],releff["sig400"][i],releff["sig700"][i],releff["sig1000"][i]))
    if i == 3 or i==5 or i==7 or i==9:
      print("\\hline")
  print("##################  SIGS  ################")
  for i in sigs.index:
    print("%s & %.2e & %.2e & %.2e & %.2e & %.2e & %.2e \\\\"%(cuts[i],sigs["sig125"][i],sigs["sig200"][i],sigs["sig300"][i],sigs["sig400"][i],sigs["sig700"][i],sigs["sig1000"][i]))
    if i == 3 or i==5 or i==7 or i==9:
      print("\\hline")
  #pd.reset_option('display.float_format')


def make_correlation(SR,cut):
  if cut==0 or cut==1:
    high1 = 100
  else:
    high1 = 80
  var = "nPFCand"
  SR=SR+"_%s"%cut
  h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  fig, ax1 = plt.subplots()
 
  sphere = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
  #labs = []
  for i in range(len(sphere)-1): 
    h2 = h1.integrate("eventBoostedSphericity",slice(sphere[i],sphere[i+1])).to_hist().to_numpy()
    norm = np.linalg.norm(h2[0])
    xbin = xbins(h2[1])
    ax1.step(xbin[:-high1],h2[0][:-high1]/norm,color=colors[i],label="%s-%s"%(sphere[i],sphere[i+1]),linestyle="-",where="mid")
  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
  ax1.legend(title="Boosted\n Sphericity\n Bins")
  ax1.set_xlabel(var)
  ax1.set_ylabel("AU")
  ax1.set_yscale("log")
  ax1.set_xscale("log")
  ax1.autoscale(axis='y', tight=True)
  ax1.autoscale(axis='x', tight=True)
  fig.savefig("Plots/correlation_sphere_%s.%s"%(SR,ext))
  plt.close()
 

  sphere = [0,20,40,60,80,100]
  for cut in [0,15,20,25,30,35,40,45]:
    fig, ax1 = plt.subplots()
    for i in range(len(sphere)-1): 

      h2 = h1.integrate(var,slice(sphere[i],sphere[i+1])).to_hist().to_numpy()
      norm = np.linalg.norm(h2[0][cut:])
      xbin = xbins(h2[1])
      ax1.step(xbin[cut:],h2[0][cut:]/norm,color=colors[i],label="%s-%s"%(sphere[i],sphere[i+1]),linestyle="-",where="mid")
    
    hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
    ax1.legend(title="%s Bins"%var)
    ax1.set_xlabel("Boosted Sphericity")
    ax1.set_ylabel("AU")
    ax1.set_yscale("log")
    ax1.autoscale(axis='y', tight=True)
    fig.savefig("Plots/correlation_PFcand_%s_cut%s.%s"%(SR,cut,ext))
    plt.close()


def make_closure(sample="qcd",SR="SR1_suep",cut=0,point=0,yrange=1):
  high1 = region_cuts_tracks[point]
  high2 = region_cuts_sphere[point]
  #if (point ==0):
  #  high1 = 70
  #  high2 = 50
  ##if (point ==1):
  ##  high1 = 70
  ##  high2 = 90
  ##if (point ==2):
  ##  high1 = 80
  ##  high2 = 80
  ##if (point ==3):
  ##  high1 = 100
  ##  high2 = 70
  #if (point ==1):
  #  #high1 = 85
  #  #high2 = 80
  #  high1 = region_cuts_tracks[1]
  #  high2 = region_cuts_sphere[1] #0.5
  #if (point ==2):
  #  #high1 = 90
  #  #high2 = 65
  #  high1 = region_cuts_tracks[2]
  #  high2 = region_cuts_sphere[2] #0.5
  #if (point ==3):
  #  #high1 = 105
  #  #high2 = 50
  #  high1 = region_cuts_tracks[3]
  #  high2 = region_cuts_sphere[3] #0.5
  #if cut == 2 or cut ==3:
  #  #var = "FatJet_nconst"
  #  high1 = 70
  #  high2 = 70
  #  #high2 = 50
  #else:
  #  high1 = 100
  #  high2 = 60
  var = "nPFCand"
  SR = SR+"_%s"%cut
  if sample == "qcd":
     h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  elif sample == "RunA":
     h1 = datascaled[SR].integrate("axis",slice(0,1))
  elif sample == "Data":
     h1 = datafullscaled[SR].integrate("axis",slice(0,1))
  else:
    with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
        out = pickle.load(pkl_file)
        scale= lumi*xsecs[sample]/out["sumw"][sample]
        scaled = {}
        for name, h in out.items():
          if SR not in name or "mu" in name or "trig" in name:
            continue
          if isinstance(h, hist.Hist):
            scaled[name] = h.copy()
            scaled[name].scale(scale)
            h1 = (scaled[SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
  low1 =0
  low2 = 30
  high1x = 300
  high2x = 100
  
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
  abin = h1.integrate("eventBoostedSphericity",slice(low2/100,high2/100)).integrate(  var,slice(low1,high1)).sum().values(sumw2=True)[()]
  bbin = h1.integrate("eventBoostedSphericity",slice(high2/100,high2x/100)).integrate(var,slice(low1,high1)).sum().values(sumw2=True)[()]
  cbin = h1.integrate("eventBoostedSphericity",slice(low2/100,high2/100)).integrate(  var,slice(high1,high1x)).sum().values(sumw2=True)[()]
  dbin = h1.integrate("eventBoostedSphericity",slice(high2/100,high2x/100)).integrate(var,slice(high1,high1x)).sum().values(sumw2=True)[()]
  abinx = abin[0]
  bbinx = bbin[0]
  cbinx = cbin[0]
  dbinx = dbin[0]
  abin_err = abin[1]
  bbin_err = bbin[1]
  cbin_err = cbin[1]
  dbin_err = dbin[1]
  ratx = bbinx/abinx
  expected = ratx*cbinx
  err = expected*np.sqrt(abin_err/(abinx*abinx)+bbin_err/(bbinx*bbinx)+cbin_err/(cbinx*cbinx))
  print(abinx,np.sqrt(abin_err),bbinx,cbinx,dbinx,ratx,expected,dbinx/expected,err)
  hx = hist.plot1d(
      h1.integrate("eventBoostedSphericity",slice(high2/100,high2x/100)),
      ax=ax,
      stack=False,
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"blue"}
  )
  h2 = h1.copy()
  h2.scale(ratx)
  hx2 = hist.plot1d(
      h2.integrate("eventBoostedSphericity",slice(low2/100,high2/100)),
      ax=ax,
      clear=False,
      stack=False,
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"red"}
  )
  leg = ["Observed %.2f +/- %.2f"%(dbinx,np.sqrt(dbin_err)),"Predicted: %.2f +/- %.2f"%(ratx*cbinx,err),"point"]
  ax.legend(leg)
  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
  ax.set_yscale("log")
  ax.autoscale(axis='y', tight=True)
  hx1 = hist.plotratio(
      h1.integrate("eventBoostedSphericity",slice(high2/100,high2x/100)),h2.integrate("eventBoostedSphericity",slice(low2/100,high2/100)),
      ax=ax1,
      error_opts={'color': 'r', 'marker': '+'},
      unc='num'
  )
  ax1.set_xlim(high1,175)
  if yrange:
    ax1.set_ylim(0.5,1.5)
  else:
    ax1.set_ylim(0.5,5)
  if("isrsuep" in SR):
    ax1.set_xlabel("ISR Jet Track Multiplicity")
  else:
    if cut== 2 or cut ==3:
      ax1.set_xlabel("Suep Jet Track Multiplcity")
    else:
      ax1.set_xlabel("Event Tracks")
  ax.add_artist(AnchoredText("Boundary: (%s,%s)"%(high1,high2),loc="center right",prop=dict(size=12)))
  ax1.axhline(y=1,color="gray",ls="--")
  ax.set_xlabel("")
  ax1.set_ylabel("Observed/Predicted")
  fig.suptitle("4 Bin Closure: %s"%(sample))
  fig.savefig("Plots/closure_%s_%s.%s"%(sample,SR,ext))
  plt.close()
def make_closure_correction6(sample="qcd",SR="SR1_suep",cut=0,point=0,yrange=1):
  highx1 = region_cuts_tracks[0]
  highx2 = region_cuts_tracks[point]
  highy1 = region_cuts_sphere[point]
  #if cut == 2 or cut == 3:
    #var = "FatJet_nconst"
    #highx1 = 50
  #if (point==0):
  #  highx2 = 70
  #  highy1 = 50
  ##if (point==1):
  ##  highx2 = 70
  ##  highy1 = 90
  ##if (point==2):
  ##  highx2 = 80
  ##  highy1 = 80
  ##if (point==3):
  ##  highx2 = 100
  ##  highy1 = 70
  #if (point ==1):
  #  highx2 = 85
  #  highy1 = 80
  #if (point ==2):
  #  highx2 = 90
  #  highy1 = 65
  #if (point ==3):
  #  highx2 = 105
  #  highy1 = 50
  #  #highy1 = 50
  #else:
  #  highx1 = 75
  #  highx2 = 100
  #  highy1 = 50
  var = "nPFCand"
  SR = SR+"_%s"%cut
  if sample == "qcd":
     h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  elif sample == "RunA":
     h1 = datascaled[SR].integrate("axis",slice(0,1))
  elif sample == "Data":
     h1 = datafullscaled[SR].integrate("axis",slice(0,1))
  else:
    with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
        out = pickle.load(pkl_file)
        scale= lumi*xsecs[sample]/out["sumw"][sample]
        scaled = {}
        for name, h in out.items():
          if SR not in name or "mu" in name or "trig" in name:
            continue
          if isinstance(h, hist.Hist):
            scaled[name] = h.copy()
            scaled[name].scale(scale)
            h1 = (scaled[SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
  lowx =0
  lowy = 30
  highx3 = 300
  highy2 = 100
  
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
  abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  SRbin = h1.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]

  abinx = abin[0]
  bbinx = bbin[0]
  cbinx = cbin[0]
  dbinx = dbin[0]
  ebinx = ebin[0]
  SRbinx = SRbin[0]
  abin_err = abin[1]
  bbin_err = bbin[1]
  cbin_err = cbin[1]
  dbin_err = dbin[1]
  ebin_err = ebin[1]
  SRbin_err = SRbin[1]
  A_err  = np.sqrt(abin[1])/abinx
  B_err  = np.sqrt(bbin[1])/bbinx
  C_err  = np.sqrt(cbin[1])/cbinx
  D_err  = np.sqrt(dbin[1])/dbinx
  E_err  = np.sqrt(ebin[1])/ebinx
  ratx = ((ebinx**2)*abinx)/((bbinx**2)*dbinx)
  err = ratx*cbinx*np.sqrt((D_err)**2 +(2*B_err)**2 +(C_err)**2 +(A_err)**2 + (2*E_err)**2)
  hx = hist.plot1d(
      h1.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)),
      ax=ax,
      stack=False,
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"blue"}
  )
  h2 = h1.copy()
  h2.scale(ratx)
  hx2 = hist.plot1d(
      h2.integrate("eventBoostedSphericity",slice(lowy/100,highy1/100)),
      ax=ax,
      clear=False,
      stack=False,
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"red"}
  )
  #leg = ["Observed %.2f"%(SRbinx),"Predicted: %.2f"%(ratx*cbinx)]
  ax.add_artist(AnchoredText("Boundary: (%s,%s)"%(highx2,highy1),loc="center right",prop=dict(size=12)))
  leg = ["Observed %.2f +/- %.2f"%(SRbinx,np.sqrt(SRbin_err)),"Predicted: %.2f +/- %.2f"%(ratx*cbinx,err)]
  ax.legend(leg)
  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
  ax.set_yscale("log")
  ax.autoscale(axis='y', tight=True)
  hx1 = hist.plotratio(
      h1.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)),h2.integrate("eventBoostedSphericity",slice(lowy/100,highy1/100)),
      ax=ax1,
      error_opts={'color': 'r', 'marker': '+'},
      unc='num'
  )
  ax1.set_xlim(highx2,175)
  if yrange:
    ax1.set_ylim(0.5,1.5)
  if("isrsuep" in SR):
    ax1.set_xlabel("ISR Jet Track Multiplicity")
  else:
    if cut== 2 or cut ==3:
      ax1.set_xlabel("Suep Jet Track Multiplicity")
    else:
      ax1.set_xlabel("Event Tracks")
  ax.set_xlabel("")
  ax1.axhline(y=1,color="gray",ls="--")
  ax1.set_ylabel("Observed/Predicted")
  fig.suptitle("6 Bin Closure: %s"%(sample))
  fig.savefig("Plots/closure6_%s_%s.%s"%(sample,SR,ext))
  plt.close()
def make_closure_correction9(sample="qcd",SR="SR1_suep",cut=0,point=0,yrange=1):
  #if cut == 2 or cut == 3:
  highx1 = region_cuts_tracks[0]#20
  highy1 = region_cuts_sphere[0]#38
  highx2 = region_cuts_tracks[point]
  highy2 = region_cuts_sphere[point]
  #if (point ==0):
  #  highx2 = 70
  #  highy2 = 50
  ##if (point ==1):
  ##  highx2 = 70
  ##  highy2 = 90
  ##if (point ==2):
  ##  highx2 = 80
  ##  highy2 = 80
  ##if (point ==3):
  ##  highx2 = 100
  ##  highy2 = 70
  #if (point ==1):
  #  highx2 = 85
  #  highy2 = 80
  #if (point ==2):
  #  highx2 = 90
  #  highy2 = 65
  #if (point ==3):
  #  highx2 = 105
  #  highy2 = 50
  #  #highy2 = 50
  ##else:
  ##  highx1 = 75
  ##  highx2 = 100
  ##  highy1 = 40
  ##  highy2 = 50
  var = "nPFCand"
  SR = SR+"_%s"%cut
  if sample == "qcd":
     h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  elif sample == "RunA":
     h1 = datascaled[SR].integrate("axis",slice(0,1))
  elif sample == "Data":
     h1 = datafullscaled[SR].integrate("axis",slice(0,1))
  else:
    with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
        out = pickle.load(pkl_file)
        scale= lumi*xsecs[sample]/out["sumw"][sample]
        scaled = {}
        for name, h in out.items():
          if SR not in name or "mu" in name or "trig" in name:
            continue
          if isinstance(h, hist.Hist):
            scaled[name] = h.copy()
            scaled[name].scale(scale)
            h1 = (scaled[SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
  
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
  abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]

  abinx = abin[0]
  bbinx = bbin[0]
  cbinx = cbin[0]
  dbinx = dbin[0]
  ebinx = ebin[0]
  fbinx = fbin[0]
  gbinx = gbin[0]
  hbinx = hbin[0]
  SRbinx = SRbin[0]
  abin_err = abin[1]
  bbin_err = bbin[1]
  cbin_err = cbin[1]
  dbin_err = dbin[1]
  ebin_err = ebin[1]
  fbin_err = fbin[1]
  gbin_err = gbin[1]
  hbin_err = hbin[1]
  SRbin_err = SRbin[1]
  A_err  = np.sqrt(abin[1])/abinx
  B_err  = np.sqrt(bbin[1])/bbinx
  C_err  = np.sqrt(cbin[1])/cbinx
  D_err  = np.sqrt(dbin[1])/dbinx
  E_err  = np.sqrt(ebin[1])/ebinx
  F_err  = np.sqrt(fbin[1])/fbinx
  G_err  = np.sqrt(gbin[1])/gbinx
  H_err  = np.sqrt(hbin[1])/hbinx
  ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2)) 
  err = ratx*fbinx*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2)
  hx = hist.plot1d(
      h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)),
      ax=ax,
      stack=False,
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"blue"}
  )
  h2 = h1.copy()
  h2.scale(ratx)
  hx2 = hist.plot1d(
      h2.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)),
      ax=ax,
      clear=False,
      stack=False,
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"red"}
  )
  ax.add_artist(AnchoredText("Boundary: (%s,%s)"%(highx2,highy2),loc="center right",prop=dict(size=12)))
  #leg = ["Observed %.2f"%(SRbinx),"Predicted: %.2f"%(ratx*fbinx)]
  leg = ["Observed %.2f +/- %.2f"%(SRbinx,np.sqrt(SRbin_err)),"Predicted: %.2f +/- %.2f"%(ratx*fbinx,err)]
  ax.legend(leg)
  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
  ax.set_yscale("log")
  ax.autoscale(axis='y', tight=True)
  hx1 = hist.plotratio(
      h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)),h2.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)),
      ax=ax1,
      error_opts={'color': 'r', 'marker': '+'},
      unc='num'
  )
  ax1.set_xlim(highx2,175)
  if yrange:
    ax1.set_ylim(0.5,1.5)
  if("isrsuep" in SR):
    ax1.set_xlabel("ISR Jet Track Multiplicity")
  else:
    if cut== 2 or cut ==3:
      ax1.set_xlabel("Suep Jet Track Multiplicity")
    else:
      ax1.set_xlabel("Event Tracks")
  ax.set_xlabel("")
  ax1.axhline(y=1,color="gray",ls="--")
  ax1.set_ylabel("Observed/Predicted")
  fig.suptitle("9 Bin Closure: %s"%(sample))
  fig.savefig("Plots/closure9_%s_%s.%s"%(sample,SR,ext))
  plt.close()
def cutflow_correction_binned(SR="SR1_suep",cut=3,point=0,gap=0):
  #if cut == 2 or cut == 3:
  highx1 = inner_tracks
  highy1 = inner_sphere
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
    #highy2 = 50
  #else:
  #  highx1 = 75
  #  highx2 = 100
  #  highy1 = 40
  #  highy2 = 50
  var = "nPFCand"
  SR = SR+"_%s"%cut
  predicted = {"qcd":[],"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  observed = {"qcd":[],"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  sigobserved = {"qcd":[],"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  signif = {"qcd":[],"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  gapx = region_cuts_tracks[0]
  gapy = region_cuts_sphere[0]
  injected = False
  for sample in ["qcd","sig125","sig200","sig300","sig400","sig700","sig1000"]:
    if sample == "qcd":
       h1 = qcdscaled[SR].integrate("axis",slice(0,1))
    elif sample == "RunA":
       h1 = datascaled[SR].integrate("axis",slice(0,1))
    elif sample == "Data":
       h1 = datafullscaled[SR].integrate("axis",slice(0,1))
    else:
      with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
          out = pickle.load(pkl_file)
          scale= lumi*xsecs[sample]/out["sumw"][sample]
          scaled = {}
          for name, h in out.items():
            if SR not in name or "mu" in name or "trig" in name:
              continue
            if isinstance(h, hist.Hist):
              scaled[name] = h.copy()
              scaled[name].scale(scale)
              h1 = (scaled[SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
              h2 = (scaled[SR]).integrate("axis",slice(0,1))
    
    #expected = []
    #expected_err = []
    #observed = []
    #observed_err = []
    #ratio = []
    #ratio_err = []
    #points = []
    for highx2, highy2 in zip(region_cuts_tracks[1:],region_cuts_sphere[1:]):
    #for highx2, highy2 in zip([70,80,100],[90,80,70]):
      if gap == 0:
        gapx = highx2
        gapy = highy2
      if gap ==2:
        highy3 = highy2+10
        if highx2!=100:
          highx3 = highx2+10
      print(highx2,highy2)
      h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
      abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      if("sig" in sample):
        SRbinsig = h2.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
        sigobserved[sample].append(SRbinsig[0])
      else:
        sigobserved[sample].append(0)

      abinx = abin[0]
      bbinx = bbin[0]
      cbinx = cbin[0]
      dbinx = dbin[0]
      ebinx = ebin[0]
      fbinx = fbin[0]
      gbinx = gbin[0]
      hbinx = hbin[0]
      SRbinx = SRbin[0]
      abin_err = abin[1]
      bbin_err = bbin[1]
      cbin_err = cbin[1]
      dbin_err = dbin[1]
      ebin_err = ebin[1]
      fbin_err = fbin[1]
      gbin_err = gbin[1]
      hbin_err = hbin[1]
      SRbin_err = SRbin[1]
      A_err  = np.sqrt(abin[1])/abinx
      B_err  = np.sqrt(bbin[1])/bbinx
      C_err  = np.sqrt(cbin[1])/cbinx
      D_err  = np.sqrt(dbin[1])/dbinx
      E_err  = np.sqrt(ebin[1])/ebinx
      F_err  = np.sqrt(fbin[1])/fbinx
      G_err  = np.sqrt(gbin[1])/gbinx
      H_err  = np.sqrt(hbin[1])/hbinx
      SR_err  = np.sqrt(SRbin[1])/SRbinx
      ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2)) 
      err = ratx*fbinx*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2)
      err1 = (2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2
      predicted[sample].append(ratx*fbinx)
      observed[sample].append(SRbinx)
      signif[sample].append(SRbinx/(ratx*fbinx))
  pred = pd.DataFrame(predicted)
  obs = pd.DataFrame(observed)
  sobs = pd.DataFrame(sigobserved)
  signifi = pd.DataFrame(signif)
  print(pred)
  print(obs)
  print(sobs)
  print(signifi)
  for sample in ["qcd","sig125","sig200","sig300","sig400","sig700","sig1000"]:
    print("(%s,%s) %s & %.2f & %.2f & %.2f & %.2f  \\\\"%(region_cuts_tracks[1],region_cuts_sphere[1]/100.,sample,pred[sample][0],sobs[sample][0],obs[sample][0],signifi[sample][0]))
  print("\\hline")
  for sample in ["qcd","sig125","sig200","sig300","sig400","sig700","sig1000"]:
    print("(%s,%s) %s & %.2f & %.2f & %.2f & %.2f  \\\\"%(region_cuts_tracks[2],region_cuts_sphere[2]/100.,sample,pred[sample][1],sobs[sample][1],obs[sample][1],signifi[sample][1]))
  print("\\hline")
  for sample in ["qcd","sig125","sig200","sig300","sig400","sig700","sig1000"]:
    print("(%s,%s) %s & %.2f & %.2f & %.2f & %.2f  \\\\"%(region_cuts_tracks[3],region_cuts_sphere[3]/100.,sample,pred[sample][2],sobs[sample][2],obs[sample][2],signifi[sample][2]))

def compareRegionData(SR="SR1_suep",cut=0,point=0,zoom=0):
  highx1 = inner_tracks#22
  highy1 = inner_sphere#42
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100

  var = "nPFCand"
  SR = SR+"_%s"%cut
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  for sample in ["QCD","Data"]:
    if sample == "QCD":
       h1 = qcdscaled[SR].integrate("axis",slice(0,1))
    elif sample == "RunA":
       h1 = datascaled[SR].integrate("axis",slice(0,1))
    elif sample == "Data":
       h1 = datafullscaled[SR].integrate("axis",slice(0,1))
    else:
      with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
          out = pickle.load(pkl_file)
          scale= lumi*xsecs[sample]/out["sumw"][sample]
          scaled = {}
          for name, h in out.items():
            if SR not in name or "mu" in name or "trig" in name:
              continue
            if isinstance(h, hist.Hist):
              scaled[name] = h.copy()
              scaled[name].scale(scale)
              h1 = (scaled[SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
    
    
    #expected = []
    #expected_err = []
    #observed = []
    #observed_err = []
    #ratio = []
    #ratio_err = []
    #points = []
    gapx = region_cuts_tracks[0]#70
    gapy = region_cuts_sphere[0]#50
    highx2 = region_cuts_tracks[0]
    highy2 = region_cuts_sphere[0]
    #for highx2 in [70,80,90,100]:
    #  for highy2 in [70,80,90]:
    #if gap > 0:
    #  gapx = highx2
    #  gapy = highy2
    #  if gap ==2:
    #    highy3 = highy2+10
    #    if highx2!=100:
    #      highx3 = highx2+10
    h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
    abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
    bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
    cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
    dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
    ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
    fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
    gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
    hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
    #SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]

    abinx = abin[0]
    bbinx = bbin[0]
    cbinx = cbin[0]
    dbinx = dbin[0]
    ebinx = ebin[0]
    fbinx = fbin[0]
    gbinx = gbin[0]
    hbinx = hbin[0]
    #SRbinx = SRbin[0]
    abin_err = np.sqrt(abin[1])
    bbin_err = np.sqrt(bbin[1])
    cbin_err = np.sqrt(cbin[1])
    dbin_err = np.sqrt(dbin[1])
    ebin_err = np.sqrt(ebin[1])
    fbin_err = np.sqrt(fbin[1])
    gbin_err = np.sqrt(gbin[1])
    hbin_err = np.sqrt(hbin[1])
    #SRbin_err = SRbin[1]
    A_err  = abin_err/abinx
    B_err  = bbin_err/bbinx
    C_err  = cbin_err/cbinx
    D_err  = dbin_err/dbinx
    E_err  = ebin_err/ebinx
    F_err  = fbin_err/fbinx
    G_err  = gbin_err/gbinx
    H_err  = hbin_err/hbinx
    #SR_err  = np.sqrt(SRbin[1])/SRbinx
    ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2)) 
    err = ratx*fbinx*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2)
    err1 = (2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2
    #print("(%d,%f)"%(highx2,highy2/100),ratx*fbinx,SRbinx)
    if sample == "Data":
      dobserved = np.array([abinx,bbinx,cbinx,dbinx,ebinx,fbinx,gbinx,hbinx, ratx*fbinx],dtype=float)
      dobserved_err = np.array([ abin_err,bbin_err,cbin_err,dbin_err,ebin_err,fbin_err,gbin_err,hbin_err, err],dtype=float)
    else:
      observed = np.array([abinx,bbinx,cbinx,dbinx,ebinx,fbinx,gbinx,hbinx, ratx*fbinx],dtype=float)
      observed_err = np.array([ abin_err,bbin_err,cbin_err,dbin_err,ebin_err,fbin_err,gbin_err,hbin_err, err],dtype=float)
    #expected.append(ratx*fbinx)
    #expected_err.append(err)
    #observed.append(SRbinx)
    #observed_err.append(np.sqrt(SRbin_err))
    #ratio.append(SRbinx/(ratx*fbinx))
    #ratio_err.append((SRbinx/(ratx*fbinx))*np.sqrt(SR_err**2 + err1))
    #points.append("(%d,%.2f)"%(highx2,highy2/100))
    #ax.errorbar(range(12),expected,yerr=expected_err,xerr=0.5,color=sigcolors[sample],label="%s: expected"%(sample),ls='none')
  points = ["A","B","C","D","E","F","G","H","Predicted SR"]
  #  if "QCD" in sample:
  #  #  ax.fill_between([x-0.5 for x in range(10)],np.append(expected,expected[-1]),color=sigcolors[sample],alpha=0.8,zorder=0,linestyle="-",step="post")
  #    col = "black"
  #  else:
  #    col = "red" #sigcolors[sample]
  #  #ax.step(range(9),expected,color=col,label="%s: expected"%(sample),linestyle="--",where="mid")
  ratio = np.divide(dobserved,observed)
  ratio_err = ratio * np.sqrt(np.square(observed_err/observed)+np.square(dobserved_err/dobserved))
  print(ratio)
  print(ratio_err)
  ax.errorbar(range(9),observed,yerr=observed_err,xerr=0.5,color="black",label="QCD",ls='none',marker=".")
  ax.errorbar(range(9),dobserved,yerr=dobserved_err,xerr=0.5,color="red",label="Data",ls='none',marker=".")
  ax1.errorbar(range(9),ratio,yerr=ratio_err,color="black",ls='none',marker="+")
  plt.xticks(range(9),points)#, rotation="-45")
  ax.legend()
  ax.set_yscale("log")
  y1, y2 = ax.get_ylim()
  ax.set_ylim(y1,y2*10)
  #if zoom:
  #  ax1.set_ylim(0,10)
  #  ax.set_ylim(10,2000)
  #else:
  #ax1.set_ylim(0,1)
  #ax1.autoscale(axis='y', tight=True)
  ax.set_ylabel("Events")
  ax1.axhline(y=1,color="gray",ls="--")
  #ax1.set_ylabel("Observed/Predicted")
  #fig.suptitle("9 Bin Predicted vs Observed by Bin")
  fig.savefig("Plots/compareDataRegion_%s_%s.%s"%(SR,zoom,ext))
  plt.close()
def make_closure_correction_binnedFull(SR="SR1_suep",cut=0,point=0,gap=0,zoom=0):
  #if cut == 2 or cut == 3:
  highx1 = inner_tracks#20
  highy1 = inner_sphere#38
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
    #highy2 = 50
  #else:
  #  highx1 = 75
  #  highx2 = 100
  #  highy1 = 40
  #  highy2 = 50
  var = "nPFCand"
  SR = SR+"_%s"%cut
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  for sample in ["QCD","sig125","sig200","sig300","sig400","sig700","sig1000"]:
    if sample == "QCD":
       h1 = qcdscaled[SR].integrate("axis",slice(0,1))
    elif sample == "RunA":
       h1 = datascaled[SR].integrate("axis",slice(0,1))
    elif sample == "Data":
       h1 = datafullscaled[SR].integrate("axis",slice(0,1))
    else:
      with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
          out = pickle.load(pkl_file)
          scale= lumi*xsecs[sample]/out["sumw"][sample]
          scaled = {}
          for name, h in out.items():
            if SR not in name or "mu" in name or "trig" in name:
              continue
            if isinstance(h, hist.Hist):
              scaled[name] = h.copy()
              scaled[name].scale(scale)
              h1 = (scaled[SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
    
    
    expected = []
    expected_err = []
    observed = []
    observed_err = []
    ratio = []
    ratio_err = []
    points = []
    gapx = region_cuts_tracks[0]
    gapy = region_cuts_sphere[0]
    #for highx2 in [70,80,90,100]:
    #  for highy2 in [70,80,90]:
    for highx2 in region_cuts_tracks: #[70,85,90,105]:
      for highy2 in region_cuts_sphere: #[50,65,80]:
    #for highx2 in [70,85,90,105]:
    #  for highy2 in [50,65,80]:
        if gap > 0:
          gapx = highx2
          gapy = highy2
          if gap ==2:
            highy3 = highy2+10
            if highx2!=100:
              highx3 = highx2+10
        h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
        abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
        bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
        cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
        dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
        ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
        fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
        gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
        hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
        SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]

        abinx = abin[0]
        bbinx = bbin[0]
        cbinx = cbin[0]
        dbinx = dbin[0]
        ebinx = ebin[0]
        fbinx = fbin[0]
        gbinx = gbin[0]
        hbinx = hbin[0]
        SRbinx = SRbin[0]
        abin_err = abin[1]
        bbin_err = bbin[1]
        cbin_err = cbin[1]
        dbin_err = dbin[1]
        ebin_err = ebin[1]
        fbin_err = fbin[1]
        gbin_err = gbin[1]
        hbin_err = hbin[1]
        SRbin_err = SRbin[1]
        A_err  = np.sqrt(abin[1])/abinx
        B_err  = np.sqrt(bbin[1])/bbinx
        C_err  = np.sqrt(cbin[1])/cbinx
        D_err  = np.sqrt(dbin[1])/dbinx
        E_err  = np.sqrt(ebin[1])/ebinx
        F_err  = np.sqrt(fbin[1])/fbinx
        G_err  = np.sqrt(gbin[1])/gbinx
        H_err  = np.sqrt(hbin[1])/hbinx
        SR_err  = np.sqrt(SRbin[1])/SRbinx
        ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2)) 
        err = ratx*fbinx*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2)
        err1 = (2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2
        print("(%d,%f)"%(highx2,highy2/100),ratx*fbinx,SRbinx)
        expected.append(ratx*fbinx)
        expected_err.append(err)
        observed.append(SRbinx)
        observed_err.append(np.sqrt(SRbin_err))
        ratio.append(SRbinx/(ratx*fbinx))
        ratio_err.append((SRbinx/(ratx*fbinx))*np.sqrt(SR_err**2 + err1))
        points.append("(%d,%.2f)"%(highx2,highy2/100))
    #ax.errorbar(range(12),expected,yerr=expected_err,xerr=0.5,color=sigcolors[sample],label="%s: expected"%(sample),ls='none')
    if "QCD" in sample:
      ax.fill_between([x-0.5 for x in range(17)],np.append(expected,expected[-1]),color=sigcolors[sample],alpha=0.8,zorder=0,linestyle="-",step="post")
      col = "black"
    else:
      col = sigcolors[sample]
    ax.step(range(16),expected,color=col,label="%s: expected"%(sample),linestyle="--",where="mid")
    ax.errorbar(range(16),observed,yerr=observed_err,xerr=0.5,color=col,label="%s: observed"%(sample),ls='none',marker=".")
    ax1.errorbar(range(16),ratio,yerr=ratio_err,color=col,ls='none',marker="+")
    plt.xticks(range(16),points, rotation="-45")
  ax.legend()
  ax.set_yscale("log")
  y1, y2 = ax.get_ylim()
  ax.set_ylim(y1,y2*10)
  if zoom:
    ax1.set_ylim(0,10)
    ax.set_ylim(10,2000)
  else:
    ax1.set_ylim(0,50)
  #ax1.autoscale(axis='y', tight=True)
  ax.set_ylabel("Events")
  ax1.axhline(y=1,color="gray",ls="--")
  ax1.set_ylabel("Observed/Predicted")
  fig.suptitle("9 Bin Predicted vs Observed by Bin")
  fig.savefig("Plots/closureBinnedFull_%s_%s_%s.%s"%(SR,gap,zoom,ext))
  plt.close()
def make_closure_correction_binned(sample="qcd",SR="SR1_suep",cut=0,point=0,gap=0):
  #if cut == 2 or cut == 3:
  highx1 = inner_tracks#20
  highy1 = inner_sphere#38
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
    #highy2 = 50
  #else:
  #  highx1 = 75
  #  highx2 = 100
  #  highy1 = 40
  #  highy2 = 50
  var = "nPFCand"
  SR = SR+"_%s"%cut
  if sample == "qcd":
     h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  elif sample == "RunA":
     h1 = datascaled[SR].integrate("axis",slice(0,1))
  elif sample == "Data":
     h1 = datafullscaled[SR].integrate("axis",slice(0,1))
  else:
    with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
        out = pickle.load(pkl_file)
        scale= lumi*xsecs[sample]/out["sumw"][sample]
        scaled = {}
        for name, h in out.items():
          if SR not in name or "mu" in name or "trig" in name:
            continue
          if isinstance(h, hist.Hist):
            scaled[name] = h.copy()
            scaled[name].scale(scale)
            h1 = (scaled[SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
  
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  
 # if (point ==0):
 #   highx2 = 70
 #   highy2 = 70
 # if (point ==1):
 #   highx2 = 70
 #   highy2 = 90
 # if (point ==2):
 #   highx2 = 80
 #   highy2 = 80
 # if (point ==3):
 #   highx2 = 100
 #   highy2 = 70
  expected = []
  expected_err = []
  observed = []
  observed_err = []
  ratio = []
  ratio_err = []
  points = []
  gapx = region_cuts_tracks[0]
  gapy = region_cuts_sphere[0]
  #for highx2 in [70,80,90,100]:
  #  for highy2 in [70,80,90]:
  for highx2 in region_cuts_tracks:#[70,85,90,105]:
    for highy2 in region_cuts_sphere: #[50,65,80]:
      if gap > 0:
        gapx = highx2
        gapy = highy2
        if gap ==2:
          highy3 = highy2+10
          if highx2!=100:
            highx3 = highx2+10
      h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
      abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]

      abinx = abin[0]
      bbinx = bbin[0]
      cbinx = cbin[0]
      dbinx = dbin[0]
      ebinx = ebin[0]
      fbinx = fbin[0]
      gbinx = gbin[0]
      hbinx = hbin[0]
      SRbinx = SRbin[0]
      abin_err = abin[1]
      bbin_err = bbin[1]
      cbin_err = cbin[1]
      dbin_err = dbin[1]
      ebin_err = ebin[1]
      fbin_err = fbin[1]
      gbin_err = gbin[1]
      hbin_err = hbin[1]
      SRbin_err = SRbin[1]
      A_err  = np.sqrt(abin[1])/abinx
      B_err  = np.sqrt(bbin[1])/bbinx
      C_err  = np.sqrt(cbin[1])/cbinx
      D_err  = np.sqrt(dbin[1])/dbinx
      E_err  = np.sqrt(ebin[1])/ebinx
      F_err  = np.sqrt(fbin[1])/fbinx
      G_err  = np.sqrt(gbin[1])/gbinx
      H_err  = np.sqrt(hbin[1])/hbinx
      SR_err  = np.sqrt(SRbin[1])/SRbinx
      ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2)) 
      err = ratx*fbinx*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2)
      err1 = (2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2
      print("(%d,%f)"%(highx2,highy2/100),ratx*fbinx,SRbinx)
      expected.append(ratx*fbinx)
      expected_err.append(err)
      observed.append(SRbinx)
      observed_err.append(np.sqrt(SRbin_err))
      ratio.append(SRbinx/(ratx*fbinx))
      ratio_err.append((SRbinx/(ratx*fbinx))*np.sqrt(SR_err**2 + err1))
      points.append("(%d,%.2f)"%(highx2,highy2/100))
  ax.errorbar(range(16),expected,yerr=expected_err,xerr=0.5,color="red",label="expected",ls='none')
  ax.errorbar(range(16),observed,yerr=observed_err,xerr=0.5,color="blue",label="observed",ls='none')
  #ax.fill_between(range(12),expected,color="red",alpha=0.8,zorder=0,linestyle="-",step="mid")
  #ax.fill_between(range(12),observed,color="blue",alpha=0.8,zorder=0,linestyle="-",step="mid")
  ax1.errorbar(range(16),ratio,yerr=ratio_err,color="black",ls='none',marker="+")
  ax.legend()
  plt.xticks(range(16),points, rotation="-45")
  #hx = hist.plot1d(
  #    h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)),
  #    ax=ax,
  #    stack=False,
  #    fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"blue"}
  #)
  #h2 = h1.copy()
  #h2.scale(ratx)
  #hx2 = hist.plot1d(
  #    h2.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)),
  #    ax=ax,
  #    clear=False,
  #    stack=False,
  #    fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"red"}
  #)
  #ax.add_artist(AnchoredText("Boundary: (%s,%s)"%(highx2,highy2),loc="center right",prop=dict(size=12)))
  ##leg = ["Observed %.2f"%(SRbinx),"Predicted: %.2f"%(ratx*fbinx)]
  #leg = ["Observed %.2f +/- %.2f"%(SRbinx,np.sqrt(SRbin_err)),"Predicted: %.2f +/- %.2f"%(ratx*fbinx,err)]
  #ax.legend(leg)
  #hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
  ax.set_yscale("log")
  ax.autoscale(axis='y', tight=True)
  ax1.set_yscale("log")
  ax1.autoscale(axis='y', tight=True)
  #hx1 = hist.plotratio(
  #    h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)),h2.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)),
  #    ax=ax1,
  #    error_opts={'color': 'r', 'marker': '+'},
  #    unc='num'
  #)
  #ax1.set_xlim(highx2,175)
  if(sample=="qcd"):
    ax1.set_ylim(0.0,2)
  #if("isrsuep" in SR):
  #  ax1.set_xlabel("ISR Tracks")
  #else:
  #  if cut== 2 or cut ==3:
  #    ax1.set_xlabel("Suep Tracks")
  #  else:
  #    ax1.set_xlabel("Event Tracks")
  ax.set_ylabel("Events")
  ax1.axhline(y=1,color="gray",ls="--")
  ax1.set_ylabel("Observed/Predicted")
  fig.suptitle("9 Bin Closure: %s"%(sample))
  fig.savefig("Plots/closureBinned_%s_%s_%s.%s"%(sample,SR,gap,ext))
  plt.close()

def make_datacompare(sample,SR,cut,xlab=None,make_ratio=True,vline=None):
  if cut == 2 or cut == 3:
    highx1 = inner_tracks#22
    highx2 = region_cuts_tracks[0]
    highy1 = inner_sphere#42
    highy2 = region_cuts_sphere[0]#70
    #highy2 = 50
  else:
    highx1 = 75
    highx2 = 100
    highy1 = 40
    highy2 = 50
  var = "nPFCand"
  SR = SR+"_%s"%cut
  h1 = qcddatafullscaled[SR].integrate("axis",slice(0,1))
  h2 = datafullscaled[SR].integrate("axis",slice(0,1))
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
  
  #h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
  abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100))
  dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100))
  gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100))
  abin2 = h2.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100))
  dbin2 = h2.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100))
  gbin2 = h2.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100))

  print(abin.to_hist().to_numpy())
  print(dbin.to_hist().to_numpy())
  print(gbin.to_hist().to_numpy())
  b1= abin.to_hist().to_numpy()
  b2= dbin.to_hist().to_numpy()
  b3= gbin.to_hist().to_numpy()
  d1= abin2.to_hist().to_numpy()
  d2= dbin2.to_hist().to_numpy()
  d3= gbin2.to_hist().to_numpy()
  for i,(b,d) in enumerate(zip([b1,b2,b3],[d1,d2,d3])):
    fig, (ax, ax1) = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(7,7),
        gridspec_kw={"height_ratios": (3, 1)},
        sharex=True
    )
    fig.subplots_adjust(hspace=.07)
    if i==2:
      ax.step(xbins(b[1])[:highx2],b[0][:highx2],color="blue",linestyle="--",where="mid",zorder=2,label=labels["QCD"])
      ax.step(xbins(d[1])[:highx2],d[0][:highx2],color="red",linestyle="--",where="mid",zorder=2,label=labels["Data"])
      ax1.scatter(xbins(b[1])[:highx2],d[0][:highx2]/b[0][:highx2],marker=".")
    else:
      ax.step(xbins(b[1]),b[0],color="blue",linestyle="--",where="mid",zorder=2,label=labels["QCD"])
      ax.step(xbins(d[1]),d[0],color="red",linestyle="--",where="mid",zorder=2,label=labels["Data"])
      ax1.scatter(xbins(b[1]),d[0]/b[0],marker=".")
    #ax.step(s2[1][:-1],s2[0],color="red",linestyle="--",where="mid",zorder=2)
    #ax.step(s3[1][:-1],s3[0],color="green",linestyle="--",where="mid",zorder=2)
    ax.axvline(x=highx1,color="green",ls="--")
    ax.axvline(x=highx2,color="magenta",ls="--")
    ax1.axvline(x=highx1,color="green",ls="--")
    ax1.axvline(x=highx2,color="magenta",ls="--")
    ax.autoscale(axis='y', tight=True)
    ax.set_yscale("log")
    #ax.add_artist(AnchoredText(selection[cut],loc="upper right",prop=dict(size=15)))
    ax.legend(loc="right")
    ax.set_xlim([0,125])
    ax1.set_ylim([0.5,1.5])
    ax1.axhline(y=1,color="grey",ls="--")
    ax1.set_ylabel("Data/MC")
    ax.set_ylabel("Events")
    ax1.set_xlabel(xlab)
    fig.savefig("Plots/controlbins_dist_%s_cut%s_%s.%s"%(var,cut,i,ext))
    plt.close()


##############################ORGANIZE BY SECTION #######################################
########
#######
###################################### HT Trigger
############ HT Distributions
make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","sig125"],"ht",0,"Ht [GeV]",make_ratio=False)
make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","sig125","RunA","QCD"],"ht",1,"Ht [GeV]",vline=560)
######## Trigger Efficiency
#print("running trigger studies")
make_trigs(["Data"])
make_trigs(["Data"],systematics=True)
#make_trigs(["sig1000_2","sig700_2","sig400_2","sig300_2","sig200_2","sig125_2"])
#make_trigs(["Data"],"event_sphericity")
#make_trigs(["sig1000_2","sig700_2","sig400_2","sig300_2","sig200_2","sig125_2"],"event_sphericity")
#qcdpf = make_multitrigs("QCD",["ht20","ht30","ht40","ht50"])
#make_multitrigs("sig125_2",["ht20","ht30","ht40","ht50"],qcdpf)
#make_multitrigs("sig200_2",["ht20","ht30","ht40","ht50"],qcdpf)
#make_multitrigs("sig300_2",["ht20","ht30","ht40","ht50"],qcdpf)
#make_multitrigs("sig400_2",["ht20","ht30","ht40","ht50"],qcdpf)
#make_multitrigs("sig700_2",["ht20","ht30","ht40","ht50"],qcdpf)
#make_multitrigs("sig1000_2",["ht20","ht30","ht40","ht50"],qcdpf)


############################## Track Selection
#print("running track studies")
######### TRK Eff and Fakes 
#make_trkeff("sig400_2","dist_trkID_gen_pt","Gen pT [GeV]",runPV=2)
#make_trkeff("sig400_2","dist_trkID_gen_phi","Gen Phi")
#make_trkeff("sig400_2","dist_trkID_gen_eta","Gen Eta")
#make_trkeff("sig400_2","dist_trkID_gen_phi","Gen Phi",runPV=1)
#make_trkeff("sig400_2","dist_trkID_gen_eta","Gen Eta",runPV=1)
#make_trkeff("sig400_2","dist_trkIDFK_PFcand_pt","PFCand pT [GeV]") ## TODO fix fake labels
#make_trkeff("sig400_2","dist_trkIDFK_PFcand_phi","PFCand Phi")
#make_trkeff("sig400_2","dist_trkIDFK_PFcand_eta","PFCand Eta")
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
#make_overlapdists(["sig1000","sig400","sig200","sig125"],"gen_dR",2,"1-1 Minimum dR(gen,PFcand)",make_ratio=False,vline=0.02)
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"PFcand_ncount75",2,"PFCand(75) Multiplicity")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"PFcand_pt",2,"PFCand pT [GeV]")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"PFcand_eta",2,"PFCand eta")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200","sig125"],"PFcand_phi",2,"PFCand phi")
#
#
############################  FatJet Selection
#
#print("running Jet studies")
##make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","QCD"],"sphere1_suep",3,xlab="SUEP Sphericity",make_ratio=False,shift_leg=True)
##make_overlapdists(["sig1000","sig700","sig400","sig300","sig200","QCD"],"sphere1_isrsuep",3,xlab="ISR Sphericity",make_ratio=False,shift_leg=True)
##make_overlapdists(["sig1000","sig700","sig400","sig300","sig200"],"res_beta",0,make_ratio=False,xlab="Suep Jet beta - Scalar truth beta",shift_leg=True)
##make_overlapdists(["sig1000","sig700","sig400","sig300","sig200"],"res_pt",0,make_ratio=False,xlab="Suep Jet pT - Scalar truth pT",shift_leg=True)
##make_overlapdists(["sig1000","sig700","sig400","sig300","sig200"],"res_mass",0,make_ratio=False,xlab="Suep Jet mass - Scalar truth mass",shift_leg=True)
##make_overlapdists(["sig1000","sig700","sig400","sig300","sig200"],"res_dR",0,make_ratio=False,xlab="dR(Suep Jet,Scalar truth)")
##make_overlapdists(["sig1000","sig700","sig400","sig300","sig200"],"res_dEta",0,make_ratio=False,xlab="Suep Jet eta - Scalar truth eta")
##make_overlapdists(["sig1000","sig700","sig400","sig300","sig200"],"res_dPhi",0,make_ratio=False,xlab="Suep Jet phi - Scalar truth phi")
##
#make_overlapdists(["sig400"],"res_beta",0,make_ratio=False,xlab="Suep Jet beta - Scalar truth beta",shift_leg=True)
#make_overlapdists(["sig400"],"res_pt",0,make_ratio=False,xlab="Suep Jet pT - Scalar truth pT",shift_leg=True)
#make_overlapdists(["sig400"],"res_mass",0,make_ratio=False,xlab="Suep Jet mass - Scalar truth mass",shift_leg=True)
#make_overlapdists(["sig400"],"res_dR",0,make_ratio=False,xlab="dR(Suep Jet,Scalar truth)")
#make_overlapdists(["sig400"],"res_dEta",0,make_ratio=False,xlab="Suep Jet eta - Scalar truth eta")
#make_overlapdists(["sig400"],"res_dPhi",0,make_ratio=False,xlab="Suep Jet phi - Scalar truth phi")
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
##### TODO cutflow table and significance by cut
#make_cutflow(["sig1000","sig700","sig400","sig300","sig200","sig125"],"sphere1_suep")
#
#make_overlapdists(["QCD","RunA","sig1000","sig700","sig400","sig300","sig200","sig125"],"SUEP_pt",3,"SUEP pT [GeV]",make_ratio=True)
#make_overlapdists(["QCD","RunA","sig1000","sig700","sig400","sig300","sig200","sig125"],"SUEP_eta",3,"SUEP eta",make_ratio=True)
#make_overlapdists(["QCD","RunA","sig1000","sig700","sig400","sig300","sig200","sig125"],"SUEP_phi",3,"SUEP phi",make_ratio=True)
#make_overlapdists(["QCD","RunA","sig1000","sig700","sig400","sig300","sig200","sig125"],"ISR_pt",3, "ISR pT [GeV]",make_ratio=True)
#make_overlapdists(["QCD","RunA","sig1000","sig700","sig400","sig300","sig200","sig125"],"ISR_eta",3,"ISR eta",make_ratio=True)
#make_overlapdists(["QCD","RunA","sig1000","sig700","sig400","sig300","sig200","sig125"],"ISR_phi",3,"ISR phi",make_ratio=True)
#
############################# ABCD
#make_correlation("SR1_suep",3)
#make_correlation("SR1_suep",1)
#print("running ABCD studies")
#makeSR("sig200","SR1_suep",3)
##makeCombineHistograms(["sig125","sig200","sig300","sig400","sig700","sig1000"],"SR1_suep",3)
##makeSR("sig300","SR1_suep",3)
##makeSR("sig700","SR1_suep",3)
##makeSR("sig1000","SR1_suep",3)
#makeSR("sig400","SR1_suep",3)
#makeSR("sig400","SR1_suep",3,lines=4,SR=0)
#makeSR("sig400","SR1_suep",3,lines=6,SR=0)
#makeSR("sig400","SR1_suep",3,lines=9,SR=0)
#######significances
##makeSRSignif("sig200","SR1_suep",3,xline=70,yline=90)
##makeSRSignif("sig300","SR1_suep",3,xline=80,yline=80)
##makeSRSignif("sig400","SR1_suep",3,xline=80,yline=80)
##makeSRSignif("sig700","SR1_suep",3,xline=100,yline=70)
##makeSRSignif("sig1000","SR1_suep",3,xline=100,yline=70)
#makeSRSignif("sig125","SR1_suep",3,xline=region_cuts_tracks[1],yline=region_cuts_sphere[1])
#makeSRSignif("sig200","SR1_suep",3,xline=region_cuts_tracks[1],yline=region_cuts_sphere[1])
#makeSRSignif("sig300","SR1_suep",3,xline=region_cuts_tracks[2],yline=region_cuts_sphere[2])
#makeSRSignif("sig400","SR1_suep",3,xline=region_cuts_tracks[2],yline=region_cuts_sphere[2])
#makeSRSignif("sig700","SR1_suep",3,xline=region_cuts_tracks[3],yline=region_cuts_sphere[3])
#makeSRSignif("sig1000","SR1_suep",3,xline=region_cuts_tracks[3],yline=region_cuts_sphere[3])
######closure
#make_closure("qcd","SR1_suep",3,yrange=0)
#make_closure_correction9("qcd","SR1_suep",3)
#make_closure_correction6("qcd","SR1_suep",3)
#makeSRSignig9("qcd","SR1_suep",3) # error plot
######signal contamination
#make_closure_correction9("sig125","SR1_suep",3, point=1)
#make_closure_correction9("sig200","SR1_suep",3, point=1)
#make_closure_correction9("sig300","SR1_suep",3, point=2)
#make_closure_correction9("sig400","SR1_suep",3, point=2)
#make_closure_correction9("sig700","SR1_suep",3, point=3)
#make_closure_correction9("sig1000","SR1_suep",3,point=3)
#
###data validation
#make_closure("RunA","SR1_suep",3)
#make_closure_correction6("RunA","SR1_suep",3)
#make_closure_correction9("RunA","SR1_suep",3)
#make_closure("Data","SR1_isrsuep",3)
#make_closure_correction9("Data","SR1_isrsuep",3)
#make_closure_correction6("Data","SR1_isrsuep",3)
#compareRegionData(SR="SR1_suep",cut=0,point=0,zoom=0)
#
#
#for g in [0,1,2]:
#  make_closure_correction_binned("qcd","SR1_suep",3,gap=g)
#  make_closure_correction_binned("sig125","SR1_suep",3,gap=g)
#  make_closure_correction_binned("sig200","SR1_suep",3,gap=g)
#  make_closure_correction_binned("sig300","SR1_suep",3,gap=g)
#  make_closure_correction_binned("sig400","SR1_suep",3,gap=g)
#  make_closure_correction_binned("sig700","SR1_suep",3,gap=g)
#  make_closure_correction_binned("sig1000","SR1_suep",3,gap=g)
#make_closure_correction_binnedFull("SR1_suep",3,gap=2,zoom=0)
#make_closure_correction_binnedFull("SR1_suep",3,gap=2,zoom=1)
######signal contamination
#cutflow_correction_binned()
#cutflow_correction_binned(gap=1)
##cutflow_correction_binned(gap=2)




#
############### EXTRA
#####################APPENDIX TRIGGER
#make_trigs(["sig1000_2","sig400_2"],"FatJet_nconst")
#make2dTrig("sig400",2,"trig2d_ht_event_sphericity")
#make2dTrig("sig400",2,"trig2d_ht_FatJet_nconst",ylab="Suep Jet Track Multiplicity",yfactor=6)
#make2dTrig("sig1000",2,"trig2d_ht_event_sphericity")
#make2dTrig("sig1000",2,"trig2d_ht_FatJet_nconst",ylab="Suep Jet Track Multiplicity",yfactor=6)
####################APPENDIX Basic Distributions 
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"n_pfMu",1,"n PF Muons")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"Jet_pt",1,"AK4 Jet pT [GeV]")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"Jet_eta",1,"AK4 Jet eta")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"Jet_phi",1,"AK4 Jet phi")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"n_jetId",1,"n AK4 Jets")
####################APPENDIX Sphericity 
#spheremax = {"err_sig1000":[],"err_sig700":[],"err_sig400":[],"err_sig300":[],"err_sig200":[],"sig_sig1000":[],"sig_sig700":[],"sig_sig400":[],"sig_sig300":[],"sig_sig200":[],"evt_sig1000":[],"evt_sig700":[],"evt_sig400":[],"evt_sig300":[],"evt_sig200":[]}
#make_n1(["sig1000","sig700","sig400","sig300","sig200"],"sphere1_suep",4,spheremax,xlab="Boosted Sphericity 1 (SUEP Jet)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200"],"sphere_suep",4,spheremax,xlab="Boosted Sphericity 2 (SUEP Jet)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200"],"sphere1_isr",4,spheremax,xlab="Boosted Sphericity 1 (Not ISR Jet)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200"],"sphere_isr",4,spheremax,xlab="Boosted Sphericity 2 (Not ISR Jet)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200"],"sphere1_16",4,spheremax,xlab="Boosted Sphericity 1 (DeltaPhi > 1.6)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200"],"sphere_16",4,spheremax,xlab="Boosted Sphericity 2 (DeltaPhi > 1.6)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200"],"sphere1_10",4,spheremax,xlab="Boosted Sphericity 1 (DeltaPhi > 1.0)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200"],"sphere_10",4,spheremax,xlab="Boosted Sphericity 2 (DeltaPhi > 1.0)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200"],"sphere1_8",4,spheremax,xlab="Boosted Sphericity 1 (DeltaPhi > 0.8)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200"],"sphere_8",4,spheremax,xlab="Boosted Sphericity 2 (DeltaPhi > 0.8)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200"],"sphere1_4",4,spheremax,xlab="Boosted Sphericity 1 (DeltaPhi > 0.4)",shift_leg=True)
#make_n1(["sig1000","sig700","sig400","sig300","sig200"],"sphere_4",4,spheremax,xlab="Boosted Sphericity 2 (DeltaPhi > 0.4)",shift_leg=True)
#make_threshold(["sig1000","sig700","sig400","sig300","sig200"],spheremax,["s1_s","s_s","s1_i","s_i","s1_16", "s_16","s1_10","s_10","s1_8", "s_8", "s1_4","s_4"],"Sphericity Calculations")
#########APPENDIX Event Shape Variable comparisons
#make_overlapdists(["sig400"],"sphere_suep",3,xlab="SUEP Sphericity (r=2)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"cparam_suep",3,xlab="SUEP C Parameter (r=2)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"dparam_suep",3,xlab="SUEP D Parameter (r=2)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"aplanarity_suep",3,xlab="SUEP Aplanarity (r=2)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"sphere1_suep",3,xlab="SUEP Sphericity (r=1)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"cparam1_suep",3,xlab="SUEP C Parameter (r=1)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"dparam1_suep",3,xlab="SUEP D Parameter (r=1)",make_ratio=False,shift_leg=True)
#make_overlapdists(["sig400"],"aplanarity1_suep",3,xlab="SUEP Aplanarity (r=1)",make_ratio=False,shift_leg=True)
#
#make_datacompare("qcd","SR1_suep",cut=3,xlab="SUEP Jet Track Multiplicity",make_ratio=False)



#make_dists("QCD")
#make_dists("sig400_2")
#make_cutflow(["sig1000","sig700","sig400","sig300","sig200"],"sphere1_suep")
#make_systematics(["sig1000","sig700","sig400","sig300","sig200"],"sphere1_suep",systematics1="killtrk")
#make_systematics(["sig1000","sig700","sig400","sig300","sig200"],"sphere1_suep",systematics1="trigup",systematics2="trigdown")
#make_systematics(["sig1000","sig700","sig400","sig300","sig200"],"sphere1_suep",systematics1="PUup",systematics2="PUdown")
#make_systematics(["sig1000","sig700","sig400","sig300","sig200"],"sphere1_suep",systematics1="AK4up",systematics2="AK4down")
