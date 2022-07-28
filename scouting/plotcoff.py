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

#ext="png"
ext="pdf"
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
xsecs = {"RunA_0":0,"RunA":0,"QCD":lumi,"sig1000":0.17,"sig750":0.5,"sig400":5.9,"sig300":8.9,"sig200":13.6,"HT2000":25.24} #1000-200
colors = ["black","red","green","orange","blue","magenta","cyan","yellow","brown","grey"]
cuts=["0:None","1:HTTrig","2:HT>=600","3:FJ>=2","4:nPFCand>=140"]
sigcolors = {"sig1000":"green","sig750":"cyan","sig400":"blue","sig300":"orange","sig200":"magenta","RunA":"black","QCD":"wheat"}
labels = {"sig1000":r"$m_{\phi}$ = 1000 GeV","sig750":r"$m_{\phi}$ = 750 GeV","sig400":r"$m_{\phi}$ = 400 GeV","sig300":r"$m_{\phi}$ = 300 GeV","sig200":r"$m_{\phi}$ = 200 GeV","RunA":"Data(1%)","QCD":"QCD","Data":"Data(100% RunA)","Trigger":"Trigger Data (100%)"}

selection = ["Selection:\n None","Selection:\nTrigger","Selection:\nTrigger\n %s>600 GeV"%(r"$H_{t}$"),"Selection:\nTrigger\n %s>600 GeV\n 2+ AK15 Jets"%(r"$H_{t}$"),"Selection:\n Trigger\n %s>600 GeV\n 2+ AK15 Jets\n nPFcands>70"%(r"$H_{t}$")]

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
  return [0.5*(t - s) for s, t in zip(a, a[1:])] 
def make_overlapdists(samples,var,cut,xlab=None,make_ratio=True,vline=None):
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
    xerr = xbins(sdat[1])
    #ax.scatter(sdat[1][:-1],sdat[0],color=sigcolors["RunA"],label="Data",marker=".")
    ax.errorbar(sdat[1][:-1],sdat[0],yerr=daterr,xerr=xerr,color=sigcolors["RunA"],label=labels["RunA"],zorder=6,ls="None",marker=".")
  if "QCD" in samples:
    h2x = qcddatascaled[name1]
    h2= h2x.integrate("cut",slice(cut,cut+1))
    if("ht" in name1):
      h2 = h2.rebin("v1",hist.Bin("v1","ht",50,50,3500))
    h2_scale = h2.values(sumw2=True)[()]
    print(h2_scale)
    s = h2.to_hist().to_numpy()
    s_err = np.sqrt(h2_scale[1])
    print(s_err)
    ax.fill_between(s[1][:-1],s[0],color=sigcolors["QCD"],alpha=0.8,label="QCD",zorder=0,linestyle="-",step="mid")#,)
    #ax.step(s[1][:-1],s[0],color=sigcolors["QCD"],label="QCD",linestyle="-",where="mid",zorder=5)
    ax.errorbar(s[1][:-1],s[0],yerr=s_err,color=sigcolors["QCD"],zorder=1,ls='none')
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
              #s.scale(1./sum(s_scale[0]))
              s1= s.to_hist().to_numpy()
              ax.step(s1[1][:-1],s1[0],color=sigcolors[sample],label=labels[sample],linestyle="--",where="mid",zorder=2)
            ax.set_xlabel("")
  if(vline):
    ax.axvline(x=vline,color="grey",ls="--")
    if(make_ratio):
      ax1.axvline(x=vline,color="grey",ls="--")
        
  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
  if("res" in var):
    ax.set_yscale("linear")
  else:
    ax.set_yscale("log")
  if("ht" in var):
    ax.set_xlim([0,3500])
  if("PFcand_pt" in var):
    ax.set_xscale("log")
    ax.set_xlim([0.6,50])
  ax.set_ylabel("Events")
  if make_ratio:
    ax1.set_xlabel(xlab)
    ax1.set_ylim(0.5,1.5)     
    ax1.set_ylabel("Data/QCD")
    ax1.axhline(y=1,color="grey",ls="--")
  else:
    ax.set_xlabel(xlab)
  ax.autoscale(axis='y', tight=True)
  ax.add_artist(AnchoredText(selection[cut],loc="upper right",prop=dict(size=15)))
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
          if "_pt" in name and "res" not in name:
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
def make_trkeff(sample,name,xlab):
  with open(directory+"myhistos_%s.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      sample = sample.split("_")[0]
      xsec = xsecs[sample.split("_")[0]]
      if xsec ==0:
        scale = 1
      else:
        scale= lumi*xsec/out["sumw"][sample]
      out[name].scale(scale)
      
      num = out[name].integrate("v2",slice(0,0.02)).copy()
      numFK = out[name].integrate("v2",slice(0.02,0.3)).copy()
      denom = out[name].integrate("v2").copy()
     
      if("IDFK" in name): 
        ###############FAKE
        fig, ax1 = plt.subplots()
        for i,cut in enumerate([1,2,3,6,9]):
          hx1 = hist.plotratio(
              numFK.integrate("cut",slice(1+cut,2+cut)),denom.integrate("cut",slice(1+cut,2+cut)),
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
        #ax1.legend(["|eta| < 2.4","q != 0","PV =0","pt > 0.5","pt >0.6","pt >0.7","pt >0.75","pt >0.8","pt >0.9","pt >1.0",],loc="lower right")
        fig.suptitle("Track Fake Rate: %s"%sample)
        hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
        fig.savefig("Plots/track_fake_%s_%s.%s"%(sample,name,ext))
        plt.close()
      else:
        fig, ax1 = plt.subplots()
        cuts = [1,4,6]
        leg = ["pt >0.6","pt >0.8","pt >1.0"]
        if "_pt" in name:
          cuts=[0]
          leg = ["pt> 0.5"]
          ax1.set_xscale("log")
          ax1.set_xlim([20,200])
          if "PFcand" in name or "gen" in name:
            ax1.set_xlim([0.5,100])
        #ax1.legend(["pt > 0.5","pt >0.6","pt >0.7","pt >0.75","pt >0.8","pt >0.9","pt >1.0",],loc="lower right")
        for i,cut in enumerate(cuts):
          hx = hist.plotratio(
              num.integrate("cut",slice(1+cut,2+cut)),denom.integrate("cut",slice(1+cut,2+cut)),
              ax=ax1,
              clear=False,
              error_opts={'color': colors[i], 'marker': '+'},
              unc='clopper-pearson'
          )

        ax1.legend(leg,loc="lower right")
        ax1.set_ylim(0.7,1.01)
        ax1.set_xlabel(xlab)
        fig.suptitle("Track Efficiency: %s"%sample)
        hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
        fig.savefig("Plots/track_eff_%s_%s.%s"%(sample,name,ext))
        plt.close()

def make_multitrigs(sig,varsx):
  fig, ax = plt.subplots(
  nrows=1,
  ncols=1,
  figsize=(7,7),
  )
  xs = np.linspace(0,1500,100)
  nevts = {"ht20":[],"ht30":[],"ht40":[],"ht50":[]}
  for i,var in enumerate(varsx):
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
        popt, pcov = curve_fit(func,s.to_hist().to_numpy()[1][:-1],points,p0=[0.5,500,100,0.5])
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
        #for thres in [500,550,600,650,700]:
        #  thres_index = list(map(lambda i: i >= thres, s.to_hist().to_numpy()[1])).index(True)
        #  nevts[var].append(np.sum(s1[thres_index:]))
  print(sig)
  #print(pd.DataFrame(nevts,index=[500,550,600,650,700]))
  ax.set_ylim(0,1.1)
  ax.legend(loc="lower right")
  ax.set_xlabel("Ht [GeV]")
  fig.suptitle("HT Trigger Efficiency CaloJet40 reference: %s"%sig)
  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
  fig.savefig("Plots/trigmulti_%s.%s"%(sig,ext))
  plt.close()
def make_trigs(samples,var="ht"):
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

      
      b = qcdscaled["trigdist_%s"%var].integrate("cut",slice(3,4))#.to_hist().to_numpy()
      b0 = qcdscaled["trigdist_%s"%var].integrate("cut",slice(1,2))#.to_hist().to_numpy()
      if("ht" in var):
        b = b.rebin("v1",hist.Bin("v1","ht",[*range(0,700,10)]+[700,800,1000,1200,1500]))
        b0 = b0.rebin("v1",hist.Bin("v1","ht",[*range(0,700,10)]+[700,800,1000,1200,1500]))
      b1 = b.to_hist().to_numpy()[0]
      b2 = b0.to_hist().to_numpy()[0]
      points2 = np.nan_to_num(b1/b2)
      popt2, pcov2 = curve_fit(func,b.to_hist().to_numpy()[1][:-1],points2,p0=[0.5,500,100,0.5])
      p98bkg = 1.65*popt2[2]+popt2[1]
      p90bkg = 1.163*popt2[2]+popt2[1]
      
      d = trigscaled["trigdist_%s"%var].integrate("cut",slice(3,4))#.to_hist().to_numpy()
      d0 = trigscaled["trigdist_%s"%var].integrate("cut",slice(1,2))#.to_hist().to_numpy()
      if("ht" in var):
        d = d.rebin("v1",hist.Bin("v1","ht",[*range(0,700,10)]+[700,800,1000,1200,1500]))
        d0 = d0.rebin("v1",hist.Bin("v1","ht",[*range(0,700,10)]+[700,800,1000,1200,1500]))
      d1 = d.to_hist().to_numpy()[0]
      d2 = d0.to_hist().to_numpy()[0]
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
      popt3, pcov3 = curve_fit(func,d.to_hist().to_numpy()[1][:-1],points3,p0=[0.5,500,100,0.5])
      p98dat = 1.65*popt3[2]+popt3[1]
      p90dat = 1.163*popt3[2]+popt3[1]
      ax.plot(xs,func(xs,popt3[0],popt3[1],popt3[2],popt3[3]), color="black",label=labels["Trigger"])#: 90:%d 98:%d"%(p90dat,p98dat))
      ax.plot(xs,func(xs,popt2[0],popt2[1],popt2[2],popt2[3]), color="red",label="QCD")#: 90:%d 98:%d"%(p90bkg,p98bkg))

      ax.axvline(x=600,color="grey",ls="--")
      #ax.axvline(x=p98sig,color="blue",ls="--")
      #ax.axvline(x=p90sig,color="blue",ls=":")
      #ax.axvline(x=p98bkg,color="red",ls="--")
      #ax.axvline(x=p90bkg,color="red",ls=":")
      #ax.axvline(x=p98dat,color="black",ls="--")
      #ax.axvline(x=p90dat,color="black",ls=":")

      hxrat = ax1.scatter(b.to_hist().to_numpy()[1][:-1],(b1/b2)/(d1/d2),marker=".")

      ax1.axhline(y=1,color="grey",ls="--")
      ax.set_ylim(0,1.1)
      ax1.set_ylabel("Data/QCD")
      ax1.set_ylim(0.5,1.5)
      ax.set_xlabel("")
      ax.legend(loc="lower right")
      fig.suptitle("HT Trigger Efficiency CaloJet40 reference: Data")
      hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
      fig.savefig("Plots/trig%s_data.%s"%(var,ext))
      plt.close()
  else:
    b = qcdscaled["trigdist_%s"%var].integrate("cut",slice(3,4))#.to_hist().to_numpy()
    b0 = qcdscaled["trigdist_%s"%var].integrate("cut",slice(1,2))#.to_hist().to_numpy()
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
    popt2, pcov2 = curve_fit(func,b.to_hist().to_numpy()[1][:-1],points2,p0=[0.5,500,100,0.5])
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
          sx = out["trigdist_%s"%var].integrate("cut",slice(3,4))#.to_hist().to_numpy()
          s0x = out["trigdist_%s"%var].integrate("cut",slice(1,2))#.to_hist().to_numpy()
          if("ht" in var):
            s = sx.copy().rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
            s0 = s0x.copy().rebin("v1",hist.Bin("v1","ht",[*range(0,700,20)]+[700,800,1000,1200,1500]))
          else:
            s = sx
            s0 = s0x
          s1 = s.to_hist().to_numpy()[0]
          s2 = s0.to_hist().to_numpy()[0]
          #if("sig1000" in sample or "sig750" in sample):
          #  s = sx.rebin("v1",hist.Bin("v1","ht",[*range(0,700,70)]+[700,800,1000,1200,1500]))
          #  s0 = s0x.rebin("v1",hist.Bin("v1","ht",[*range(0,700,70)]+[700,800,1000,1200,1500]))

          points = np.nan_to_num(s.to_hist().to_numpy()[0]/s0.to_hist().to_numpy()[0])
          #popt, pcov = curve_fit(func,s.to_hist().to_numpy()[1][:-1],points,p0=[0.5,500,100,0.5])
          #p98sig = 1.65*popt[2]+popt[1]
          #p90sig = 1.163*popt[2]+popt[1]
          #ax.plot(xs,func(xs,popt[0],popt[1],popt[2],popt[3]), color=sigcolors[sample],label=labels[sample])#: 90:%d 98:%d "%(sample,p90sig,p98sig))
          hx = hist.plotratio(
              s,s0,
              #out["trigdist_%s"%var].integrate("cut",slice(3,4)),out["trigdist_%s"%var].integrate("cut",slice(1,2)),
              ax=ax,
              clear=False,
              error_opts={'color': sigcolors[sample], 'marker': '.'},
              unc='clopper-pearson'
          )
          ax.set_xlabel("")

          

          #ax.axvline(x=600,color="grey",ls="--")
          #ax.axvline(x=p98sig,color="blue",ls="--")
          #ax.axvline(x=p90sig,color="blue",ls=":")
          #ax.axvline(x=p98bkg,color="red",ls="--")
          #ax.axvline(x=p90bkg,color="red",ls=":")

          hxrat = ax1.scatter(b.to_hist().to_numpy()[1][:-1],(b1/b2)/(s1/s2),marker=".",color=sigcolors[sample])

    ax1.axhline(y=1,color="grey",ls="--")
    ax.set_ylim(0,1.1)
    ax1.set_ylim(0.5,1.5)
    if(var=="FatJet_nconst"):
      ax1.set_xlim([0,300])
      ax.set_xlim([0,300])
    ax.set_label("")
    ax.legend(loc="lower right")
    fig.suptitle("HT Trigger Efficiency CaloJet40 reference: Sig")
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

def make_signif(sample,xsec):
  #qcdscaled = {}
  #with open(directory+"myhistos_QCD.p", "rb") as pkl_file:
  #    out = pickle.load(pkl_file)
  #    for name, h in out.items():
  #      if isinstance(h, hist.Hist):
  #        qcdscaled[name] = h.copy()
  with open(directory+"myhistos_%s_0.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      scale= lumi*xsec/out["sumw"][sample]
      scaled = {}
      for name, h in out.items():
        if "trig" in name:
          continue
        if isinstance(h, hist.Hist):
          scaled[name] = h.copy()
          scaled[name].scale(scale)
      
      
          fig, ax1 = plt.subplots()
          for cut in [0,1,2,3,4]:
            s = scaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy()
            sb = (qcdscaled[name].integrate("cut",slice(cut,cut+1)) + scaled[name].integrate("cut",slice(cut,cut+1))).to_hist().to_numpy()
            sig, sigbkg = get_sig(s[0],sb[0],s[1][:-1])
            ax1.errorbar(s[1][:-1],sig/np.sqrt(sigbkg),(sig/(np.sqrt(sigbkg)))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(np.multiply(4,sigbkg)))),ecolor=colors[cut],color=colors[cut],label=cuts[cut],marker="+")
          ax1.legend()
          ax1.set_xlabel(name[5:])
          ax1.set_ylabel("s/sqrt(s+b+0.5$b^{2}$)")
          hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
          fig.savefig("Plots/signif_%s.%s"%(name,ext))
          plt.close()



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
  ax1.set_ylabel("s/sqrt(s+b+0.5$b^{2}$)")
  ax1.legend()
  fig.savefig("Plots/threshold_%s.%s"%(xlab,ext))
  plt.close()
def make_n1(samples,var,cut,maxpoints,xlab=None):
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
            sb = np.add(np.add(s,b),0.5*np.square(b))

            sig, sigbkg = get_sig(s[0],(sb)[0],s[1][:-1])
            signifline = sig/np.sqrt(sigbkg)
            err = (signifline)*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(np.multiply(4,sigbkg))))
            ax1.errorbar(s[1][:-1],signifline,err,ecolor=sigcolors[sample],color=sigcolors[sample],label=labels[sample],marker="+")

            ax.step(s[1][:-1],s[0],color=sigcolors[sample],label=labels[sample],linestyle="--",where="post")
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
  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
  ax.set_yscale("log")
  ax.set_xlabel("")
  ax1.set_xlabel(xlab)
  ax1.set_ylabel("s/sqrt(s+b+0.5$b^{2}$)")
  ax.set_ylabel("Events")
  leg1, leg = ax.get_legend_handles_labels()
  leg = [l.replace("None","QCD") for l in leg]
  if("fjn1" in var):
    ax.add_artist(AnchoredText("Selection:\n Trigger\n %s>600 GeV\n nPFcands>70\n sphericity > 0.7"%(r"$H_{t}$"),loc="upper right"))
  elif("PFcand_ncount" in var):
    ax.add_artist(AnchoredText("Selection:\n Trigger\n %s>600 GeV\n 2+ AK15 Jets\n sphericity > 0.7"%(r"$H_{t}$"),loc="upper right"))
  else:
    ax.add_artist(AnchoredText(selection[cut],loc="upper right"))
  ax.legend(leg,loc="right")
  #ax1.legend()
  if large_max:
    ax1.set_ylim([0,50])
  else:
    ax1.set_ylim([0,1])
  ax.autoscale(axis='y', tight=True)
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

def makeSRSignif(sample,var,cut):
  with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      scale= lumi*xsecs[sample]/out["sumw"][sample]
      scaled = {}
      var2 = var+"_%s"%cut
      print(var2)
      xvar = "nPFCand"
      for name, h in out.items():
        if var2 not in name:
          continue
        if isinstance(h, hist.Hist):
          scaled[name] = h.copy()
          scaled[name].scale(scale)
          s = scaled[name].to_hist().to_numpy()
          b = qcdscaled[name].to_hist().to_numpy()
          print(s)
          sb = np.add(np.add(s[0][0],b[0][0]),0.5*np.square(b[0][0]))
          sig, sigbkg = get_sig2d(s[0][0],(sb),s[2][:-1],s[3][:-1])
          signif = sig/ np.sqrt(sigbkg)
          signif = np.nan_to_num(signif)
          maxi = np.max(signif)
          maxindex = unravel_index(np.argmax(signif),signif.shape)
          maxes = heapq.nlargest(5,range(len(signif.flatten())),signif.flatten().take)
          for m in maxes:
            u = unravel_index(m,signif.shape)
          
          fig, ax = plt.subplots()
          shw = ax.imshow(np.transpose(signif), interpolation='none',origin="lower",cmap="autumn")
          ax.set_xticks([0,50,100,150,200,250,300])
          ax.set_xticklabels([0,50,100,150,200,250,300])
          ax.set_yticks([0,20,40,60,80,100])
          ax.set_yticklabels([0,.20,.40,.60,.80,1])
          bar = plt.colorbar(shw)
          bar.set_label("Significance")
          ax.set_xlabel(xvar)
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
    highy2 = 70
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
  ax.set_xlabel("SUEP Jet Multiplicity")
  ax.set_ylabel("Boosted Sphericity")
  ax.text(minindex[0],minindex[1],"X=%.2f(%d,%.2f)"%(mini,minindex[0]*2,(minindex[1]*4+30)/100))

  highx1 = minindex[0]*2
  highy1 = (minindex[1]*4+30)
  print("A: ",h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()][0])
  print("B: ",h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()][0])
  print("C: ",h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()][0])
  print("D: ",h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()][0])
  print("E: ",h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()][0])
  print("F: ",h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()][0])
  print("G: ",h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()][0])
   
  ax.set_aspect("auto")
  fig.suptitle("Significance: %s"%sample)
  hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
  fig.savefig("Plots/closureerr9_%s_%s_%s.%s"%(sample,var,cut,ext))
  plt.close()




def makeSR(sample,var,cut,lines=0):
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
          sb = np.add(np.add(s[0][0],b[0][0]),0.5*np.square(b[0][0]))
          sig, sigbkg = get_sig2d(s[0][0],(sb),s[2][:-1],s[3][:-1])
          signif = sig/ np.sqrt(sigbkg)
          signif = np.nan_to_num(signif)
          maxi = np.max(signif)
          maxindex = unravel_index(np.argmax(signif),signif.shape)
          maxes = heapq.nlargest(5,range(len(signif.flatten())),signif.flatten().take)
          for m in maxes:
            u = unravel_index(m,signif.shape)
          
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
          if lines==4:
            ax1.axhline(y=0.3,color="grey",ls="--")
            ax1.axhspan(0,0.3, hatch="/", color="grey",alpha=0.3)
            ax1.axvline(x=70,color="red",ls="--")
            ax1.axhline(y=0.5,color="red",ls="--")
            ax1.text(20,0.4,"A",fontsize = 22)
            ax1.text(20,0.8,"B",fontsize = 22)
            ax1.text(100,0.4,"C",fontsize = 22)
            ax1.text(100,0.8,"SR",fontsize = 22)
            ax1.text(20,0.15,"EXCLUDED",fontsize = 22)
          if lines==6:
            ax1.axhline(y=0.3,color="grey",ls="--")
            ax1.axhspan(0,0.3, hatch="/", color="grey",alpha=0.3)
            ax1.axvline(x=70,color="red",ls="--")
            ax1.axhline(y=0.5,color="red",ls="--")
            ax1.axvline(x=22,color="blue",ls="--")
            ax1.text(0,0.4,"A",fontsize = 18)
            ax1.text(0,0.7,"D",fontsize = 18)
            ax1.text(40,0.4,"B",fontsize = 18)
            ax1.text(40,0.7,"E",fontsize = 18)
            ax1.text(100,0.4,"C",fontsize = 18)
            ax1.text(100,0.7,"SR",fontsize = 18)
            ax1.text(20,0.15,"EXCLUDED",fontsize = 22)
          if lines==9:
            ax1.axhline(y=0.3,color="grey",ls="--")
            ax1.axhspan(0,0.3, hatch="/", color="grey",alpha=0.3)
            ax1.axvline(x=22,color="blue",ls="--")
            ax1.axhline(y=0.42,color="blue",ls="--")
            ax1.axvline(x=70,color="red",ls="--")
            ax1.axhline(y=0.5,color="red",ls="--")
            ax1.text(0,0.32,"A",fontsize = 18)
            ax1.text(0,0.43,"D",fontsize = 18)
            ax1.text(0,0.7,"G",fontsize = 18)
            ax1.text(40,0.32,"B",fontsize = 18)
            ax1.text(40,0.43,"E",fontsize = 18)
            ax1.text(40,0.7,"H",fontsize = 18)
            ax1.text(100,0.32,"C",fontsize = 18)
            ax1.text(100,0.43,"F",fontsize = 18)
            ax1.text(100,0.7,"SR",fontsize = 18)
            ax1.text(20,0.15,"EXCLUDED",fontsize = 22)
          fig.suptitle("SR: QCD + %s"%sample)
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
          x = s[2][:-1]
          y = s[3][:-1]
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

def make_cutflow(samples,var):
  name1 = "dist_%s"%var
  final_cut = 35 # 50 bins -> 35= 0.7 cut
  #cutflow = {"QCD":[],"sig200":[],"sig300":[],"sig400":[],"sig750":[],"sig1000":[],"sig200_signif":[],"sig300_signif":[],"sig400_signif":[],"sig750_signif":[],"sig1000_signif":[]}
  cutflow = {"QCD":[],"sig200":[],"sig300":[],"sig400":[],"sig750":[],"sig1000":[]}
  cutflow_sig = {"sig200_signif":[],"sig300_signif":[],"sig400_signif":[],"sig750_signif":[],"sig1000_signif":[]}
  cutflow_releff = {"QCD":[],"sig200":[],"sig300":[],"sig400":[],"sig750":[],"sig1000":[]}
  #cutflow = {"QCD":[],"sig200":[],"sig200_yield":[],"sig300":[],"sig300_yield":[],"sig400":[],"sig400_yield":[],"sig750":[],"sig750_yield":[],"sig1000":[],"sig1000_yield":[]}
  for cut in [0,1,2,3,4]: 
    b1 = qcdscaled[name1].integrate("cut",slice(cut,cut+1)).values()
    for (k,b) in b1.items():
      print("QCD %d %s %.2f"%(cut,name1,b.sum()))
      cutflow["QCD"].append(b.sum())
      if(cut >0):
        cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][cut-1])
  b1 = qcdscaled[name1].integrate("cut",slice(4,5)).values()
  for (k,b) in b1.items():
    print("QCD %d %s %.2f"%(cut,name1,b[final_cut:].sum()))
    cutflow["QCD"].append(b[final_cut:].sum())
    cutflow_releff["QCD"].append(100*b[final_cut:].sum()/cutflow["QCD"][4])
  for sample in samples:
    with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
        out = pickle.load(pkl_file)
        #print(out)
        scale= lumi*xsecs[sample]/out["sumw"][sample]
        scaled = {}
        for name, h in out.items():
          if name1 not in name or "mu" in name or "trig" in name:
            continue
          if isinstance(h, hist.Hist):
            scaled[name] = h.copy()
            scaled[name].scale(scale)
        
            for cut in [0,1,2,3,4]: 
              s1 = scaled[name].integrate("cut",slice(cut,cut+1)).values()
              for (k,s) in s1.items():
                print("%s %d %s %.2f"%(sample,cut,name,s.sum()))
                cutflow[sample].append(s.sum())
                cutflow_sig[sample+"_signif"].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][cut]))
                if(cut >0):
                  cutflow_releff[sample].append(100*s.sum()/cutflow[sample][cut-1])
            s1 = scaled[name].integrate("cut",slice(4,5)).values()
            #print(s1)
            for (k,s) in s1.items():
              sval = s[final_cut:].sum()
              print("%s %d %s %.2f"%(sample,cut,name,sval))
              cutflow[sample].append(sval)
              cutflow_sig[sample+"_signif"].append(sval/np.sqrt(sval+cutflow["QCD"][5]))
              cutflow_releff[sample].append(100*sval/cutflow[sample][4])
            
  print(pd.DataFrame(cutflow))
  print(pd.DataFrame(cutflow_sig))
  pd.set_option('display.float_format', lambda x: '%.2f' % x)
  print(pd.DataFrame(cutflow_releff))
  pd.reset_option('display.float_format')


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
    ax1.step(h2[1][:-(high1+1)],h2[0][:-high1]/norm,color=colors[i],label="%s-%s"%(sphere[i],sphere[i+1]),linestyle="-",where="post")
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
      ax1.step(h2[1][cut:-1],h2[0][cut:]/norm,color=colors[i],label="%s-%s"%(sphere[i],sphere[i+1]),linestyle="-",where="post")
    
    hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
    ax1.legend(title="%s Bins"%var)
    ax1.set_xlabel("Boosted Sphericity")
    ax1.set_ylabel("AU")
    ax1.set_yscale("log")
    ax1.autoscale(axis='y', tight=True)
    fig.savefig("Plots/correlation_PFcand_%s_cut%s.%s"%(SR,cut,ext))
    plt.close()


def make_closure(sample="qcd",SR="SR1_suep",cut=0):
  if cut == 2 or cut ==3:
    #var = "FatJet_nconst"
    high1 = 70
    high2 = 50
  else:
    high1 = 100
    high2 = 60
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
  leg = ["Observed %.2f +/- %.2f"%(dbinx,np.sqrt(dbin_err)),"Expected: %.2f +/- %.2f"%(ratx*cbinx,err)]
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
  ax1.set_ylim(0.5,1.5)
  if("isrsuep" in SR):
    ax1.set_xlabel("ISR Tracks")
  else:
    if cut== 2 or cut ==3:
      ax1.set_xlabel("Suep Tracks")
    else:
      ax1.set_xlabel("Event Tracks")
  ax.set_xlabel("")
  ax1.set_ylabel("Observed/Expected")
  fig.suptitle("4 Bin Closure: %s"%(sample))
  fig.savefig("Plots/closure_%s_%s.%s"%(sample,SR,ext))
  plt.close()
def make_closure_correction6(sample="qcd",SR="SR1_suep",cut=0):
  if cut == 2 or cut == 3:
    #var = "FatJet_nconst"
    highx1 = 22
    #highx1 = 50
    highx2 = 70
    highy1 = 50
  else:
    highx1 = 75
    highx2 = 100
    highy1 = 50
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
  ratx = ((ebinx**2)*abinx)/((bbinx**2)*dbinx)
  #expected = ratx*cbinx
  #err = expected*np.sqrt(abin_err/(abinx*abinx)+bbin_err/(bbinx*bbinx)+cbin_err/(cbinx*cbinx))
  #print(abinx,np.sqrt(abin_err),bbinx,cbinx,dbinx,ratx,expected,dbinx/expected,err)
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
  #leg = ["Observed %.2f +/- %.2f"%(dbinx,np.sqrt(dbin_err)),"Expected: %.2f +/- %.2f"%(ratx*cbinx,err)]
  leg = ["Observed %.2f"%(SRbinx),"Expected: %.2f"%(ratx*cbinx)]
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
  ax1.set_ylim(0.5,1.5)
  if("isrsuep" in SR):
    ax1.set_xlabel("ISR Tracks")
  else:
    if cut== 2 or cut ==3:
      ax1.set_xlabel("Suep Tracks")
    else:
      ax1.set_xlabel("Event Tracks")
  ax.set_xlabel("")
  ax1.set_ylabel("Observed/Expected")
  fig.suptitle("6 Bin Closure: %s"%(sample))
  fig.savefig("Plots/closure6_%s_%s.%s"%(sample,SR,ext))
  plt.close()
def make_closure_correction9(sample="qcd",SR="SR1_suep",cut=0):
  if cut == 2 or cut == 3:
    highx1 = 22
    highx2 = 70
    highy1 = 42
    highy2 = 50
  else:
    highx1 = 75
    highx2 = 100
    highy1 = 40
    highy2 = 50
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
  #ratx = (fbinx*(hbinx**2)*(dbinx**4))/(abinx*(ebinx**4)*cbinx*gbinx)
  ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2)) 
  #expected = ratx*cbinx
  #err = expected*np.sqrt(abin_err/(abinx*abinx)+bbin_err/(bbinx*bbinx)+cbin_err/(cbinx*cbinx))
  #print(abinx,np.sqrt(abin_err),bbinx,cbinx,dbinx,ratx,expected,dbinx/expected,err)
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
#  leg = ["Observed %.2f +/- %.2f"%(dbinx,np.sqrt(dbin_err)),"Expected: %.2f +/- %.2f"%(ratx*cbinx,err)]
  leg = ["Observed %.2f"%(SRbinx),"Expected: %.2f"%(ratx*fbinx)]
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
  ax1.set_ylim(0.5,1.5)
  if("isrsuep" in SR):
    ax1.set_xlabel("ISR Tracks")
  else:
    if cut== 2 or cut ==3:
      ax1.set_xlabel("Suep Tracks")
    else:
      ax1.set_xlabel("Event Tracks")
  ax.set_xlabel("")
  ax1.set_ylabel("Observed/Expected")
  fig.suptitle("9 Bin Closure: %s"%(sample))
  fig.savefig("Plots/closure9_%s_%s.%s"%(sample,SR,ext))
  plt.close()

def make_datacompare(sample,SR,cut,xlab=None,make_ratio=True,vline=None):
  if cut == 2 or cut == 3:
    highx1 = 22
    highx2 = 70
    highy1 = 42
    highy2 = 50
  else:
    highx1 = 75
    highx2 = 100
    highy1 = 40
    highy2 = 50
  var = "nPFCand"
  SR = SR+"_%s"%cut
  #if sample == "qcd":
  h1 = qcddatafullscaled[SR].integrate("axis",slice(0,1))
  #elif sample == "RunA":
  h2 = datafullscaled[SR].integrate("axis",slice(0,1))
  #else:
  #  with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
  #      out = pickle.load(pkl_file)
  #      scale= lumi*xsecs[sample]/out["sumw"][sample]
  #      scaled = {}
  #      for name, h in out.items():
  #        if SR not in name or "mu" in name or "trig" in name:
  #          continue
  #        if isinstance(h, hist.Hist):
  #          scaled[name] = h.copy()
  #          scaled[name].scale(scale)
  #          h1 = (scaled[SR]).integrate("axis",slice(0,1))
  #          #h1 = (scaled[SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
  
  #h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
  abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100))#.integrate(  var,slice(lowx,highx1  ))#.sum().values(sumw2=True)[()]
  #bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100))#.integrate(  var,slice(highx1,highx2))#.sum().values(sumw2=True)[()]
  #cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100))#.integrate(  var,slice(highx2,highx3))#.sum().values(sumw2=True)[()]
  dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100))#.integrate(  var,slice(lowx,highx1  ))#.sum().values(sumw2=True)[()]
  #ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100))#.integrate(  var,slice(highx1,highx2))#.sum().values(sumw2=True)[()]
  #fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100))#.integrate(  var,slice(highx2,highx3))#.sum().values(sumw2=True)[()]
  gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100))#.integrate(  var,slice(lowx,highx1  ))#.sum().values(sumw2=True)[()]
  #hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100))#.integrate(  var,slice(highx1,highx2))#.sum().values(sumw2=True)[()]
  #SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100))#.integrate(  var,slice(highx2,highx3))#.sum().values(sumw2=True)[()]
  abin2 = h2.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100))#.integrate(  var,slice(lowx,highx1  ))#.sum().values(sumw2=True)[()]
  dbin2 = h2.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100))#.integrate(  var,slice(lowx,highx1  ))#.sum().values(sumw2=True)[()]
  gbin2 = h2.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100))#.integrate(  var,slice(lowx,highx1  ))#.sum().values(sumw2=True)[()]

  #abinx = abin[0]
  #bbinx = bbin[0]
  #cbinx = cbin[0]
  #dbinx = dbin[0]
  #ebinx = ebin[0]
  #fbinx = fbin[0]
  #gbinx = gbin[0]
  #hbinx = hbin[0]
  #SRbinx = SRbin[0]
  #abin_err = abin[1]
  #bbin_err = bbin[1]
  #cbin_err = cbin[1]
  #dbin_err = dbin[1]
  #ebin_err = ebin[1]
  #fbin_err = fbin[1]
  #gbin_err = gbin[1]
  #hbin_err = hbin[1]
  #SRbin_err = SRbin[1]
  print(abin.to_hist().to_numpy())
  print(dbin.to_hist().to_numpy())
  print(gbin.to_hist().to_numpy())
  b1= abin.to_hist().to_numpy()
  b2= dbin.to_hist().to_numpy()
  b3= gbin.to_hist().to_numpy()
  d1= abin2.to_hist().to_numpy()
  d2= dbin2.to_hist().to_numpy()
  d3= gbin2.to_hist().to_numpy()
  #ax.step(s1[1][:-1],s1[0],color=sigcolors[sample],label=labels[sample],linestyle="--",where="mid",zorder=2)
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
      ax.step(b[1][:highx2],b[0][:highx2],color="blue",linestyle="--",where="mid",zorder=2,label=labels["QCD"])
      ax.step(d[1][:highx2],d[0][:highx2],color="red",linestyle="--",where="mid",zorder=2,label=labels["Data"])
      ax1.scatter(b[1][:highx2],d[0][:highx2]/b[0][:highx2],marker=".")
    else:
      ax.step(b[1][:-1],b[0],color="blue",linestyle="--",where="mid",zorder=2,label=labels["QCD"])
      ax.step(d[1][:-1],d[0],color="red",linestyle="--",where="mid",zorder=2,label=labels["Data"])
      ax1.scatter(b[1][:-1],d[0]/b[0],marker=".")
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
    ax1.set_xlabel("SUEP Jet Track Multiplicity")
    fig.savefig("Plots/controlbins_dist_%s_cut%s_%s.%s"%(var,cut,i,ext))
    plt.close()
  #if make_ratio:
  #  fig, (ax,ax1) = plt.subplots(
  #      nrows=2,
  #      ncols=1,
  #      figsize=(7,7),
  #      gridspec_kw={"height_ratios": (3, 1)},
  #      sharex=True
  #  )
  #else:
  #  fig, ax = plt.subplots()
  #fig.subplots_adjust(hspace=.07)
  #name1 = "dist_%s"%var
  #if (xlab==None):
  #  xlab=name1[5:]
  #if "RunA" in samples:
  #  #h1 = datascaled[name1].integrate("cut",slice(cut,cut+1))
  #  #if("ht" in name1):
  #  #  h1 = h1.rebin("v1",hist.Bin("v1","ht",50,50,3500))
  #  #h1_scale = h1.values(sumw2=True)[()]
  #  #sdat = h1.to_hist().to_numpy()
  #  #daterr = np.sqrt(h1_scale[1])
  #  #xerr = xbins(sdat[1])
  #  #ax.scatter(sdat[1][:-1],sdat[0],color=sigcolors["RunA"],label="Data",marker=".")
  #  ax.errorbar(sdat[1][:-1],sdat[0],yerr=daterr,xerr=xerr,color=sigcolors["RunA"],label=labels["Data"],zorder=6,ls="None",marker=".")
  #if "QCD" in samples:
  #  h2x = qcddatascaled[name1]
  #  h2= h2x.integrate("cut",slice(cut,cut+1))
  #  if("ht" in name1):
  #    h2 = h2.rebin("v1",hist.Bin("v1","ht",50,50,3500))
  #  h2_scale = h2.values(sumw2=True)[()]
  #  print(h2_scale)
  #  s = h2.to_hist().to_numpy()
  #  s_err = np.sqrt(h2_scale[1])
  #  print(s_err)
  #  ax.fill_between(s[1][:-1],s[0],color=sigcolors["QCD"],alpha=0.8,label="QCD",zorder=0,linestyle="-",step="mid")#,)
  #  #ax.step(s[1][:-1],s[0],color=sigcolors["QCD"],label="QCD",linestyle="-",where="mid",zorder=5)
  #  ax.errorbar(s[1][:-1],s[0],yerr=s_err,color=sigcolors["QCD"],zorder=1,ls='none')
  #  if(make_ratio):
  #    hist.plotratio(
  #    h1,h2,
  #    ax=ax1,
  #    clear=False,
  #    error_opts={'color': sigcolors["RunA"], 'marker': '+'},
  #    unc='num'
  #    )

  #for sample in samples:
  #  if "sig" in sample:
  #    fil = directory+"myhistos_%s_2.p"%sample
  #    with open(fil, "rb") as pkl_file:
  #        out = pickle.load(pkl_file)
  #        xsec = xsecs[sample]
  #        scale= lumi*xsec/out["sumw"][sample]
  #        scaled = {}
  #        for name, h in out.items():
  #          if "dist_%s"%var != name:#if var not in name or "mu" in name or "trig" in name:
  #            continue
  #          if isinstance(h, hist.Hist):
  #            scaled[name] = h.copy()
  #            scaled[name].scale(scale)
  #            s = scaled[name].integrate("cut",slice(cut,cut+1))#.to_hist().to_numpy()
  #            if("ht" in name):
  #              s = s.rebin("v1",hist.Bin("v1","ht",50,50,3500))
  #            s_scale = s.values(sumw2=True)[()]
  #            #s.scale(1./sum(s_scale[0]))
  #            s1= s.to_hist().to_numpy()
  #            ax.step(s1[1][:-1],s1[0],color=sigcolors[sample],label=labels[sample],linestyle="--",where="mid",zorder=2)
  #          ax.set_xlabel("")
  #if(vline):
  #  ax.axvline(x=vline,color="grey",ls="--")
  #  if(make_ratio):
  #    ax1.axvline(x=vline,color="grey",ls="--")
  #      
  #hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2,ax=ax)
  #if("res" in var):
  #  ax.set_yscale("linear")
  #else:
  #  ax.set_yscale("log")
  #if("ht" in var):
  #  ax.set_xlim([0,3500])
  #if("PFcand_pt" in var):
  #  ax.set_xscale("log")
  #  ax.set_xlim([0.6,50])
  #ax.set_ylabel("Events")
  #if make_ratio:
  #  ax1.set_xlabel(xlab)
  #  ax1.set_ylim(0.5,1.5)     
  #  ax1.set_ylabel("Data/QCD")
  #  ax1.axhline(y=1,color="grey",ls="--")
  #else:
  #  ax.set_xlabel(xlab)


##########################ORGANIZE BY SECTION #######################################
####
###
################################## HT Trigger
######## HT Distributions
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"ht",0,"Ht [GeV]",make_ratio=False)
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200","RunA","QCD"],"ht",1,"Ht [GeV]",vline=600)
######## Trigger Efficiency
#print("running trigger studies")
#make_trigs(["Data"])
#make_trigs(["sig1000_2","sig750_2","sig400_2","sig300_2","sig200_2"])
#make_trigs(["Data"],"event_sphericity")
#make_trigs(["sig1000_2","sig750_2","sig400_2","sig300_2","sig200_2"],"event_sphericity")
#make_multitrigs("sig400_2",["ht20","ht30","ht40","ht50"])
#make_multitrigs("sig750_2",["ht20","ht30","ht40","ht50"])
#make_multitrigs("sig1000_2",["ht20","ht30","ht40","ht50"])
#
#
############################## Track Selection
#print("running track studies")
######## TRK Eff and Fakes 
#make_trkeff("sig400_2","dist_trkID_gen_pt","Gen pT [GeV]") #TODO check why efficiency is so high?
#make_trkeff("sig400_2","dist_trkID_gen_phi","Gen Phi")
#make_trkeff("sig400_2","dist_trkID_gen_eta","Gen Eta")
#make_trkeff("sig400_2","dist_trkIDFK_PFcand_pt","PFCand pT [GeV]") ## TODO fix fake labels
#make_trkeff("sig400_2","dist_trkIDFK_PFcand_phi","PFCand Phi")
#make_trkeff("sig400_2","dist_trkIDFK_PFcand_eta","PFCand Eta")
#maxpoints = {"err_sig1000":[],"err_sig750":[],"err_sig400":[],"err_sig300":[],"err_sig200":[],"sig_sig1000":[],"sig_sig750":[],"sig_sig400":[],"sig_sig300":[],"sig_sig200":[],"evt_sig1000":[],"evt_sig750":[],"evt_sig400":[],"evt_sig300":[],"evt_sig200":[]}
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount50",4,maxpoints,"PFCand(50) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount60",4,maxpoints,"PFCand(60) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount70",4,maxpoints,"PFCand(70) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount75",4,maxpoints,"PFCand(75) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount80",4,maxpoints,"PFCand(80) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount90",4,maxpoints,"PFCand(90) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount100",4,maxpoints,"PFCand(100) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount150",4,maxpoints,"PFCand(150) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount200",4,maxpoints,"PFCand(200) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount300",4,maxpoints,"PFCand(300) Multiplicity")
#make_threshold(["sig1000","sig750","sig400","sig300","sig200"],maxpoints,[.5,.6,.7,.75,.8,.9,1.0,1.5,2,3],"track_pt_cut")
##
#make_overlapdists(["sig1000","sig400","sig200"],"gen_dR",3,"1-1 Minimum dR(gen,PFcand)",make_ratio=False,vline=0.02)
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"PFcand_ncount75",2,"PFCand(75) Multiplicity")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"PFcand_pt",2,"PFCand pT [GeV]")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"PFcand_eta",2,"PFCand eta")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"PFcand_phi",2,"PFCand phi")
#
#
############################  FatJet Selection
#
#print("running Jet studies")
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200","QCD"],"sphere1_suep",3,xlab="sphericity",make_ratio=False)
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200","QCD"],"sphere1_isrsuep",3,xlab="sphericity",make_ratio=False)
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"res_pt",0,make_ratio=False,xlab="Suep Jet pT - Scalar truth pT")
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"res_mass",0,make_ratio=False,xlab="Suep Jet mass - Scalar truth mass")
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"res_dR",0,make_ratio=False,xlab="dR(Suep Jet,Scalar truth)")
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"res_dEta",0,make_ratio=False,xlab="Suep Jet eta - Scalar truth eta")
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"res_dPhi",0,make_ratio=False,xlab="Suep Jet phi - Scalar truth phi")
#
#maxpointsfj = {"err_sig1000":[],"err_sig750":[],"err_sig400":[],"err_sig300":[],"err_sig200":[],"sig_sig1000":[],"sig_sig750":[],"sig_sig400":[],"sig_sig300":[],"sig_sig200":[],"evt_sig1000":[],"evt_sig750":[],"evt_sig400":[],"evt_sig300":[],"evt_sig200":[]}
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount50",4,maxpointsfj,xlab="AK15(50) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount100",4,maxpointsfj,xlab="AK15(100) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount150",4,maxpointsfj,xlab="AK15(150) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount200",4,maxpointsfj,xlab="AK15(200) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount250",4,maxpointsfj,xlab="AK15(250) Multiplicity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount300",4,maxpointsfj,xlab="AK15(300) Multiplicity") 
#make_threshold(["sig1000","sig750","sig400","sig300","sig200"],maxpointsfj,[50,100,150,200,250,300],"fatjet_pt_cut")
#
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"FatJet_pt",3,"AK15 Jet pT [GeV]")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"FatJet_eta",3,"AK15 Jet Eta")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"FatJet_phi",3,"AK15 Jet Phi")
#make_overlapdists(["QCD","RunA","sig1000","sig400","sig200"],"FatJet_ncount50",3,"AK15 Jet(50) Multiplicity")
########################### BOOSTING and sphericity
### TODO ISR removal methods
#print("running sphericity studies")
#empty = {"err_sig1000":[],"err_sig750":[],"err_sig400":[],"err_sig300":[],"err_sig200":[],"sig_sig1000":[],"sig_sig750":[],"sig_sig400":[],"sig_sig300":[],"sig_sig200":[],"evt_sig1000":[],"evt_sig750":[],"evt_sig400":[],"evt_sig300":[],"evt_sig200":[]}
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"FatJet_nconst",3,empty,xlab="SUEP Jet Track Multiplicity") 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"FatJet_nconst",4,empty,xlab="SUEP Jet Track Multiplicity") 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere1_suep",3,empty,xlab="Boosted Sphericity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere1_suep",4,empty,xlab="Boosted Sphericity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"event_sphericity",3,empty,xlab="Unboosted Sphericity")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"event_sphericity",4,empty,xlab="Unboosted Sphericity")
#### TODO cutflow table and significance by cut
#make_cutflow(["sig1000","sig750","sig400","sig300","sig200"],"sphere1_suep")
#
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"SUEP_pt",3,"SUEP pT [GeV]",make_ratio=False)
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"SUEP_eta",3,"SUEP eta",make_ratio=False)
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"SUEP_phi",3,"SUEP phi",make_ratio=False)
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"ISR_pt",3, "ISR pT [GeV]",make_ratio=False)
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"ISR_eta",3,"ISR eta",make_ratio=False)
#make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"ISR_phi",3,"ISR phi",make_ratio=False)

############################ ABCD
#make_correlation("SR1_suep",3)
#make_correlation("SR1_suep",1)
#print("running ABCD studies")
#makeSR("sig200","SR1_suep",3)
#makeSR("sig300","SR1_suep",3)
#makeSR("sig400","SR1_suep",3)
#makeSR("sig750","SR1_suep",3)
#makeSR("sig1000","SR1_suep",3)
#makeSRSignif("sig200","SR1_suep",3)
#makeSRSignif("sig300","SR1_suep",3)
#makeSR("sig400","SR1_suep",3)
#makeSR("sig400","SR1_suep",3,lines=4)
#makeSR("sig400","SR1_suep",3,lines=6)
#makeSR("sig400","SR1_suep",3,lines=9)
#makeSRSignif("sig750","SR1_suep",3)
#makeSRSignif("sig1000","SR1_suep",3)
#make_closure("qcd","SR1_suep",3)
#make_closure_correction9("qcd","SR1_suep",3)
#make_closure_correction6("qcd","SR1_suep",3)
#makeSRSignig9("qcd","SR1_suep",3)
###signal contamination
#make_closure_correction9("sig200","SR1_suep",3)
#make_closure_correction9("sig300","SR1_suep",3)
#make_closure_correction9("sig400","SR1_suep",3)
#make_closure_correction9("sig750","SR1_suep",3)
#make_closure_correction9("sig1000","SR1_suep",3)
#
###data validation
#make_closure("RunA","SR1_suep",3)
#make_closure_correction6("RunA","SR1_suep",3)
#make_closure_correction9("RunA","SR1_suep",3)
#make_closure("Data","SR1_isrsuep",3)
#make_closure_correction9("Data","SR1_isrsuep",3)
#make_closure_correction6("Data","SR1_isrsuep",3)

make_datacompare("qcd","SR1_suep",cut=3,xlab="test",make_ratio=False)





#for sig in ["sig200","sig300","sig400","sig750","sig1000"]:
#  for i in [0,1,2,3]:
#    makeSR(sig,"SR1_suep",i)
#    makeSR(sig,"SR1_isr",i)
#    makeSR(sig,"SR1_16",i)
#    makeSR(sig,"SR1_10",i)
#    makeSR(sig,"SR1_8",i)
#    makeSR(sig,"SR1_4",i)
#make_closure("qcd","SR1_suep",1)
#make_closure_correction9("qcd","SR1_suep",1)
#make_closure_correction6("qcd","SR1_suep",1)
#make_closure("qcd","SR1_16",1)
#make_closure_correction9("qcd","SR1_16",1)
#make_closure_correction6("qcd","SR1_16",1)
#make_closure("qcd","SR1_16",3)
#make_closure_correction9("qcd","SR1_16",3)
#make_closure_correction6("qcd","SR1_16",3)
#
#
############### EXTRA
#####################APPENDIX TRIGGER
#make_trigs(["sig1000_2","sig400_2"],"FatJet_nconst")
#make2dTrig("sig400",2,"trig2d_ht_event_sphericity")
#make2dTrig("sig400",2,"trig2d_ht_FatJet_nconst",ylab="Suep Jet Track Multiplicity",yfactor=6)
#make2dTrig("sig1000",2,"trig2d_ht_event_sphericity")
#make2dTrig("sig1000",2,"trig2d_ht_FatJet_nconst",ylab="Suep Jet Track Multiplicity",yfactor=6)
#
########BEST SPHERICITY
#maxpointssphere = {"err_sig1000":[],"err_sig750":[],"err_sig400":[],"err_sig300":[],"err_sig200":[],"sig_sig1000":[],"sig_sig750":[],"sig_sig400":[],"sig_sig300":[],"sig_sig200":[],"evt_sig1000":[],"evt_sig750":[],"evt_sig400":[],"evt_sig300":[],"evt_sig200":[]}
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere1_16",4,maxpointssphere) 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere_16",4,maxpointssphere) 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere1_10",4,maxpointssphere) 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere_10",4,maxpointssphere) 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere1_8",4,maxpointssphere) 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere_8",4,maxpointssphere) 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere1_4",4,maxpointssphere) 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere_4",4,maxpointssphere) 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere1_suep",4,maxpointssphere) 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere_suep",4,maxpointssphere) 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere1_isr",4,maxpointssphere) 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"sphere_isr",4,maxpointssphere) 
#make_threshold(["sig1000","sig750","sig400","sig300","sig200"],maxpointssphere,["s1_16","s_16","s1_10","s_10","s1_8","s_8","s1_4","s_4","s1_s","s_s","s1_i","s_i"],"Sphericity_wrt_ISR_RM")

#make_dists("QCD")
#make_dists("sig400_2")
