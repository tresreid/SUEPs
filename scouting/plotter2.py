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
import ROOT
import mplhep as hep
from ROOT import TMath, TLegend, TF1, TLine
plt.style.use(hep.style.ROOT)

lumi = 59.74*1000
def openReco(name,xsec,qcd,extra=False):
  dfs = []
  #hlts = []
  pfs = []
  pfs2 = []
  pfs3 = []
  prefix = "/uscms/home/mreid/nobackup/sueps/analysis/CMSSW_10_6_0/src/PhysicsTools/"
  if qcd==1:
    fs =["%s_split0.root"%name,"%s_split1.root"%name,"%s_split2.root"%name,"%s_split3.root"%name,"%s_split4.root"%name]
    treen = "tree"
  if qcd==2:
    fs = np.loadtxt("rootfiles/%s.txt"%(name),dtype=str)
    #prefix = "" 
    prefix = "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCD/%s/"%(name)
    treen = "mmtree/tree"
  else:
    #prefix += "Signal/"
    fs = [name]
    treen = "mmtree/tree"
  print(fs)
  batch_count=0
  count = 0
  for fnum in fs:
    print(fnum)
    try:
      with uproot.open(prefix+"%s"%(fnum)) as file:
        if (count % 100 == 0):
           print("%s/%s"%(count,len(fs)))
#        if count > 30:
#          break
        count= count+1
      #file = uproot.open(prefix+"%s"%(fnum))
        t= file[treen]
        hlt1 = t.pandas.df(["hltResult"])
        if qcd == 0:
          df1 = t.pandas.df(["ht","n_pfcand","suepJet_sphericity","eventBoosted_sphericity","event_sphericity","n_pfMu","n_pfEl","Muon_totPt","Electron_totPt","n_fatjet","n_jet"])
          df1["n_pfLep"] = df1["n_pfMu"]+df1["n_pfEl"]
          df1["htNoMu"] = df1["ht"]-df1["Muon_totPt"]
          df1["htNoLep"] = df1["htNoMu"]-df1["Electron_totPt"]
        else:
          df1 = t.pandas.df(["ht","n_pfcand","suepJet_sphericity","eventBoosted_sphericity","event_sphericity","n_fatjet","n_jet"])
        df1["triggerHT"] = hlt1.loc[(slice(None), 7),:].reset_index()["hltResult"] #410 trigger = 7, doubleMu3 = 2
        df1["triggerMu"] = hlt1.loc[(slice(None), 2),:].reset_index()["hltResult"] #410 trigger = 7, doubleMu3 = 2
        dfs.append(df1)
        if(extra):
          pf1 = t.pandas.df(["Jet_pt","Jet_eta","Jet_phi"])
          pf1 = pf1.reset_index()
          pfs.append(pf1)
          pf2 = t.pandas.df(["FatJet_pt","FatJet_eta","FatJet_phi"])
          pf2 = pf2.reset_index()
          pfs2.append(pf2)
          pf3 = t.pandas.df(["PFcand_pt","PFcand_eta","PFcand_phi"])
          pf3 = pf3.reset_index()
          pfs3.append(pf3)
    except OSError:
      print("file not found: %s %s"%(name,prefix+fnum))
      continue
  df = pd.concat(dfs,copy=False)
  df["wgt"] = xsec*lumi/len(df)
  #return df
  if(extra):
    pf = pd.concat(pfs,copy=False)
    pf2 = pd.concat(pfs2,copy=False)
    pf3 = pd.concat(pfs3,copy=False)
    return [df,pf,pf2,pf3]
  else:
    return df
#def openCutflow(name,xsec,qcd):
#  hlts = []
#  prefix = "/uscms/home/mreid/nobackup/sueps/analysis/CMSSW_10_6_0/src/PhysicsTools/"
#  if qcd==1:
#    fs =["%s_split0.root"%name,"%s_split1.root"%name,"%s_split2.root"%name,"%s_split3.root"%name,"%s_split4.root"%name]
#    treen = "tree"
#    #fs = np.loadtxt("rootfiles/%s.txt"%(name),dtype=str)
#    #if "test" in name:
#    #  prefix += "QCD/HT2000/"
#    #else:
#    #  prefix += "QCD/%s/"%(name)
#  if qcd==2:
#    fs = np.loadtxt("rootfiles/%s.txt"%(name),dtype=str)
#    prefix = "" 
#  else:
#    #prefix += "Signal/"
#    fs = [name]
#    treen = "mmtree/tree"
#  print(fs)
#  batch_count=0
#  for fnum in fs:
#    print(fnum)
#    try:
#      file = uproot.open(prefix+"%s"%(fnum))
#    except OSError:
#      print("file not found: %s %s"%(name,prefix+fnum))
#      continue
#    t= file[treen]
#    hlt1 = t.pandas.df(["hltResult","ht","n_pfcand","suepJet_sphericity","eventBoosted_sphericity","event_sphericity"])
#    hlt1 = hlt1[hlt1["ht"] > 600]
#    hlt1["batch"] = batch_count
#    print(hlt1)
#    hlts.append(hlt1)
#    batch_count = batch_count+1
#  hlt = pd.concat(hlts)
#  hlt = pd.DataFrame(hlt.to_records())
#  hlt["entry"]= hlt["entry"] +1000000*hlt["batch"]
#  print(hlt)
#  hltx = hlt.pivot(index="entry",columns="subentry",values="hltResult")
#  hltx["ht"] = hlt.groupby("entry")["ht"].max()#values[0]
#  hltx["suepJet_sphericity"] = hlt.groupby("entry")["suepJet_sphericity"].max()#values[0]
#  hltx["n_pfcand"] = hlt.groupby("entry")["n_pfcand"].max()#values[0]
#  hltx["eventBoosted_sphericity"] = hlt.groupby("entry")["eventBoosted_sphericity"].max()#values[0]
#  hltx["event_sphericity"] = hlt.groupby("entry")["event_sphericity"].max()#values[0]
#  return hltx

#def plot_distribution(df,qcd_df,var,rx,bx,norm,log):
#    fig, ax1 = plt.subplots()
#    ax1.hist(df[df["PFcand_fromsuep"] == 1][var]      ,bins=bx,range=rx,   density=norm, histtype=u'step',weights=df[df["PFcand_fromsuep"] == 1]["wgt"],color="blue",label="true")
#    ax1.hist(df[df["PFcand_fromsuep"] == 0][var]      ,bins=bx,range=rx,   density=norm, histtype=u'step',weights=df[df["PFcand_fromsuep"] == 0]["wgt"],color="red",label="false")
#    ax1.hist(qcd_df[var]                              ,bins=bx,range=rx,   density=norm, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
#    ax1.legend()
#    ax1.set_xlabel(var)
#    if norm:
#      ax1.set_ylabel("AU")
#    else:
#      ax1.set_ylabel("events")
#    if log:
#      ax1.set_yscale('log')
#    Path("Plots/var").mkdir(parents=True,exist_ok=True)
#    fig.savefig("Plots/var/matched_distribtuion_%s_norm%s_log%s"%(var,norm,log))
#    plt.close()
#
#
#
#
#def make_eff(df,dfID,gen_df,var,bins,idtype,sample):
#  print("running %s eff"%var)
#
#  all_group = df.groupby(pd.cut(df[var],bins))["wgt"].sum().to_numpy()
#  reco_group = df[(df["PFcand_fromsuep"] == 1)].groupby(pd.cut(df[(df["PFcand_fromsuep"] == 1)][var],bins))["wgt"].sum().to_numpy()
#  fake_group = df[(df["PFcand_fromsuep"] == 0)].groupby(pd.cut(df[(df["PFcand_fromsuep"] == 0)][var],bins))["wgt"].sum().to_numpy()
#  ID_group = dfID[(dfID["PFcand_fromsuep"] == 1)].groupby(pd.cut(dfID[(dfID["PFcand_fromsuep"] == 1)][var],bins))["wgt"].sum().to_numpy()
#  fakeID_group = dfID[(dfID["PFcand_fromsuep"] == 0)].groupby(pd.cut(dfID[(dfID["PFcand_fromsuep"] == 0)][var],bins))["wgt"].sum().to_numpy()
#  allID_group = dfID.groupby(pd.cut(dfID[var],bins))["wgt"].sum().to_numpy()
#  gen_group = gen_df.groupby(pd.cut(gen_df[var],bins))["wgt"].sum().to_numpy()
#
#
#  eff = pd.DataFrame()
#  eff["range"] = (bins[1:]-bins[:-1])/2.
#  eff["recoeff"] = (reco_group/gen_group) #reco matched/ all gen
#  eff["reco_yerr"]=(reco_group/gen_group)*np.sqrt((1/reco_group)+(1/gen_group))
#  eff["IDeff"] = (ID_group/reco_group) # reco-matched ID / reco-matched
#  eff["ID_yerr"]=(ID_group/reco_group)*np.sqrt((1/reco_group)+(1/ID_group))
#  eff["fakeRate"] = (fake_group/all_group) # not reco-matched ID / all reco
#  eff["fake_yerr"]=(fake_group/all_group)*np.sqrt((1/fake_group)+(1/all_group))
#  eff["purity"] = (reco_group/all_group) # reco-matched ID / all reco
#  eff["pure_yerr"]=(reco_group/all_group)*np.sqrt((1/reco_group)+(1/all_group))
#  eff["fakeIDeff"] = (fakeID_group/allID_group) # not reco-matched ID / all reco
#  eff["fakeID_yerr"]=(fakeID_group/allID_group)*np.sqrt((1/allID_group)+(1/fakeID_group))
#  eff["totaleff"] = (ID_group/gen_group) #reco matched ID / all gen
#  eff["total_yerr"]=(ID_group/gen_group)*np.sqrt((1/reco_group)+(1/gen_group))
#
#  if "phi" in var:
#    eff_reco = np.nanmean(eff["recoeff"].to_numpy())
#    eff_id = np.nanmean(eff["IDeff"].to_numpy())
#    eff_fake = np.nanmean(eff["fakeRate"].to_numpy())
#    eff_pure = np.nanmean(eff["purity"].to_numpy())
#    eff_fakeid = np.nanmean(eff["fakeIDeff"].to_numpy())
#    eff_total = np.nanmean(eff["totaleff"].to_numpy())
#    label1="reco eff: %.1f%%"%(100*eff_reco)
#    label2="ID eff: %.1f%%"%(100*eff_id)
#    label3="fake Rate: %.1f%%"%(100*eff_fake)
#    label4="purity: %.1f%%"%(100*eff_pure)
#    label5="fake ID Rate: %.1f%%"%(100*eff_fakeid)
#    label6="Total Eff: %.1f%%"%(100*eff_total)
#  elif "pt" in var:
#    eff_reco =   np.nanmean(eff[eff["range"]>10]["recoeff"].to_numpy())
#    eff_id =     np.nanmean(eff[eff["range"]>10]["IDeff"].to_numpy())
#    eff_fake =   np.nanmean(eff[eff["range"]>10]["fakeRate"].to_numpy())
#    eff_pure =   np.nanmean(eff[eff["range"]>10]["purity"].to_numpy())
#    eff_fakeid = np.nanmean(eff[eff["range"]>10]["fakeIDeff"].to_numpy())
#    eff_total =  np.nanmean(eff[eff["range"]>10]["totaleff"].to_numpy())
#    label1="reco eff: %.1f%%"%(100*eff_reco)
#    label2="ID eff: %.1f%%"%(100*eff_id)
#    label3="fake Rate: %.1f%%"%(100*eff_fake)
#    label4="purity: %.1f%%"%(100*eff_pure)
#    label5="fake ID Rate: %.1f%%"%(100*eff_fakeid)
#    label6="Total Eff: %.1f%%"%(100*eff_total)
#  else:
#    label1="reco eff"
#    label2="ID eff"
#    label3="fake Rate"
#    label4="purity"
#    label5="fake ID Rate"
#    label6="Total Eff"
#
#
#
#  fig, ax = plt.subplots(2,sharex=True)
#  fig.suptitle("%s: "%(sample)) #+partType[idtype])
#  ax[0].set_ylabel("events")
#  ax[1].set_ylabel("efficiency")
#  if "pt" in var:
#    ax[0].set_yscale('log')
#    ax[0].set_xscale('log')
#    ax[1].set_xscale('log')
#
#  ax[0].hist(df[(df["PFcand_fromsuep"] == 1)][var], bins=bins,histtype=u'step',weights=df[(df["PFcand_fromsuep"] == 1)]["wgt"],color="blue",label="matched")
#  ax[0].hist(df[(df["PFcand_fromsuep"] == 0)][var],bins=bins,histtype=u'step',weights=df[(df["PFcand_fromsuep"] == 0)]["wgt"],color="red",label="!matched")
#  ax[0].hist(df[var], bins=bins,histtype=u'step',weights=df["wgt"],color="black",label="all reco")
#  ax[0].hist(gen_df[var], bins=bins,histtype=u'step',weights=gen_df["wgt"],color="magenta",label="gen")
#
#  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["recoeff"].to_numpy(),eff["reco_yerr"].to_numpy(),xerr=eff["range"],ls='none',    label=label1,color="blue")
#  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["fakeRate"].to_numpy(),eff["fake_yerr"].to_numpy(),xerr=eff["range"],ls='none',   label=label3,color="red")
#  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["purity"].to_numpy(),eff["pure_yerr"].to_numpy(),xerr=eff["range"],ls='none',     label=label4,color="cyan")
#
#  ax[1].set_ylim([0,1.01])
#  ax[1].set_xlabel(var)
#  ax[0].set_xlabel(var)
#  ax[0].legend(loc="lower left")
#  ax[1].legend(loc="lower left")
#  fig.tight_layout()
#  Path("Plots/eff").mkdir(parents=True,exist_ok=True)
#  fig.savefig("Plots/eff/efficiency_%s_%s_%sv1.png"%(var,idtype,sample))
#  plt.close()
#
#  fig, ax = plt.subplots(2,sharex=True)
#  fig.suptitle("%s: "%(sample))#+partType[idtype])
#  ax[0].set_ylabel("events")
#  ax[1].set_ylabel("efficiency")
#  if "pt" in var:
#    ax[0].set_yscale('log')
#    ax[0].set_xscale('log')
#    ax[1].set_xscale('log')
#
#  ax[0].hist(dfID[(dfID["PFcand_fromsuep"] == 1)][var], bins=bins,histtype=u'step',weights=dfID[(dfID["PFcand_fromsuep"] == 1)]["wgt"],color="green",label="matched+ID")
#  ax[0].hist(dfID[(dfID["PFcand_fromsuep"] == 0)][var], bins=bins,histtype=u'step',weights=dfID[(dfID["PFcand_fromsuep"] == 0)]["wgt"],color="cyan",label="!matched+ID")
#  ax[0].hist(df[var], bins=bins,histtype=u'step',weights=df["wgt"],color="black",label="all reco")
#  ax[0].hist(gen_df[var], bins=bins,histtype=u'step',weights=gen_df["wgt"],color="magenta",label="gen")
#
#  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["IDeff"].to_numpy(),eff["ID_yerr"].to_numpy(),xerr=eff["range"],ls='none',        label=label2,color="green")
#  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["fakeIDeff"].to_numpy(),eff["fakeID_yerr"].to_numpy(),xerr=eff["range"],ls='none',label=label5,color="orange")
#  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["totaleff"].to_numpy(),eff["total_yerr"].to_numpy(),xerr=eff["range"],ls='none',  label=label6,color="black")
#
#  ax[1].set_ylim([0,1.01])
#  ax[1].set_xlabel(var)
#  ax[0].set_xlabel(var)
#  ax[0].legend(loc="lower left")
#  ax[1].legend(loc="lower left")
#  fig.tight_layout()
#  Path("Plots/eff").mkdir(parents=True,exist_ok=True)
#  fig.savefig("Plots/eff/efficiency_%s_%s_%sv2.png"%(var,idtype,sample))
#  plt.close()


def make_eff_combo(reco_id,qcd_id,signal, part, binx, eta_cuts=0):
  fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(21,7))


  fig.suptitle("sig%s: %s"%(signal,"X"))#partType[part]))

  colors = ["red","green","orange","blue","black","magenta"]
  for i in [0,1,2,3,4,5]:
    if(eta_cuts):
      cut = [2.5,2.4,2.0,1.75,1.5,1.0]
      reco_id = reco_id[abs(reco_id["PFcand_eta"]) < cut[i]]
      qcd_id = qcd_id[abs(qcd_id["PFcand_eta"]) < cut[i]]
      lab1 = "|eta|<"
    else:
      cut = [0.1,0.5,0.6,.75,1.0,2.0]
      reco_id = reco_id[reco_id["PFcand_pt"] > cut[i]]
      qcd_id = qcd_id[qcd_id["PFcand_pt"] > cut[i]]
      lab1 = "pt>"
    reco_group = reco_id.groupby(['entry']).first()
    reco_group['nTracks'] = reco_id.groupby(['entry']).size()
    qcd_group = qcd_id.groupby(['entry']).first()
    qcd_group['nTracks'] = qcd_id.groupby(['entry']).size()
    sig,tot_sig,bkg1,tot_bkg = get_sig(reco_group,qcd_group,"nTracks",binx)
    bkg2 = np.array(bkg1)
    bkg3 = np.square(0.5*bkg2)
    bkg = np.add(bkg2,bkg3)

    ax1.hist(reco_group["nTracks"],  bins=binx,histtype=u'step',range=[0,binx*10],weights=reco_group["wgt"],color=colors[i],linestyle="solid",label="sig:%s%.2f"%(lab1,cut[i]))
    ax1.hist(qcd_group["nTracks"],   bins=binx,histtype=u'step',range=[0,binx*10],weights=qcd_group["wgt"],color=colors[i],linestyle="dashed",label="qcd:%s%.2f"%(lab1,cut[i]))
    ax2.errorbar(range(0,binx*10,10),sig/(np.sqrt(np.add(sig,bkg))),(sig/(np.sqrt(np.add(sig,bkg))))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(4*np.add(sig,bkg)))),ecolor=colors[i],label="signif: %s%.2f"%(lab1,cut[i]),color=colors[i],linestyle="dashdot",errorevery=1)
    ax3.errorbar(range(0,binx*10,10),np.multiply(sig,1./tot_sig),np.multiply(sig,1./tot_sig)*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(tot_sig))),ecolor=colors[i],label="sig_eff:%s%.2f"%(lab1,cut[i]),color=colors[i],linestyle="solid",errorevery=1)
    ax3.errorbar(range(0,binx*10,10),np.multiply(bkg1,1./tot_bkg),np.multiply(bkg1,1./tot_bkg)*np.sqrt(np.add(np.reciprocal(bkg1),np.reciprocal(tot_bkg))),ecolor=colors[i],label="bkg_eff:%s%.2f"%(lab1,cut[i]),color=colors[i],linestyle="dashed",errorevery=1)

  ax1.set_ylabel("Events")
  ax2.set_ylabel("Significance")
  ax3.set_ylabel("Efficiency")
  ax1.set_xlabel("nTracks")
  ax2.set_xlabel("nTracks")
  ax3.set_xlabel("nTracks")
  if(signal==1000):
    ax2.set_ylim(0,25)
  if(signal==750):
    ax2.set_ylim(0,35)
  if(signal==400):
    ax2.set_ylim(0,50)
  if(signal==300):
    ax2.set_ylim(0,30)
  if(signal==200):
    ax2.set_ylim(0,8)
  ax2.grid()
  ax1.legend()
  ax2.legend()
  ax3.legend()
  ax1.set_yscale('log')
  fig.tight_layout()
  Path("Plots/nTracks").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/nTracks/nTracks_%s_%s_%s.png"%(signal,part,eta_cuts))
  plt.close()

def get_sig(df_sig,df_bkg,var,binx):
  sig = []
  bkg = []
  tot_sig = df_sig["wgt"].sum()
  tot_bkg = df_bkg["wgt"].sum()
  for i in range(0,binx*10,10):
    sig.append(df_sig[df_sig[var] > i]["wgt"].sum())
    bkg.append(df_bkg[df_bkg[var] > i]["wgt"].sum() + 1e-9)
  return(sig,tot_sig,bkg,tot_bkg)


def make_2d_correlation(sub_df,name, var1,steps1, var2,steps2):

  fig, (ax1) = plt.subplots(1,1)
  ax1.set_title("%s: %s vs %s"%(name,var1,var2))
  
  h= ax1.hist2d(sub_df[var1],sub_df[var2],bins=[len(steps1)-1,len(steps2)-1],range=[[steps1[0],steps1[-1]],[steps2[0],steps2[-1]]],norm=matplotlib.colors.LogNorm())
  fig.colorbar(h[3], ax=ax1)
  ax1.set_xlabel(var1)
  ax1.set_ylabel(var2)


  fig.tight_layout()
  Path("Plots/2d").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/2d/2d_%s_%s_%s.png"%(var1,var2,name))
  plt.close()


def plot_distribution(df,name,var,rx,cutflow,cutvals,norm,log):
    fig, ax1 = plt.subplots()
    cut_i =0
    colors = ["black","red","blue","magenta","orange"]
    for cut,cutval in zip(cutflow,cutvals):
      df = df[df[cut] >= cutval]
      ax1.hist(df[var]      ,bins=len(rx)-1,range=[rx[0],rx[-1]],   density=norm, histtype=u'step',weights=df["wgt"],color=colors[cut_i],label="%s >= %s"%(cut,cutval))
      cut_i=cut_i+1
    ax1.legend()
    ax1.set_xlabel(var)
    if norm:
      ax1.set_ylabel("AU")
    else:
      ax1.set_ylabel("events")
    if log:
      ax1.set_yscale('log')
    Path("Plots/var").mkdir(parents=True,exist_ok=True)
    fig.savefig("Plots/var/distribtuion_%s_%s_norm%s_log%s"%(name,var,norm,log))
    plt.close()

def plot_distributionv2(pf,df,name,var,rx,cutflow,cutvals,norm,log):
    fig, ax1 = plt.subplots()
    cut_i =0
    colors = ["black","red","blue","magenta","orange"]
    df["pass"] = True
    for cut,cutval in zip(cutflow,cutvals):
      df["pass"] = (df["pass"]==True) & (df[cut] >= cutval)
      filter_list = df[df["pass"] ==True].index
      ax1.hist(pf[pf["entry"].isin(filter_list)][var]      ,bins=len(rx)-1,range=[rx[0],rx[-1]],   density=norm, histtype=u'step',color=colors[cut_i],label="%s >= %s"%(cut,cutval))
      cut_i=cut_i+1
    ax1.legend()
    ax1.set_xlabel(var)
    if norm:
      ax1.set_ylabel("AU")
    else:
      ax1.set_ylabel("events")
    if log:
      ax1.set_yscale('log')
    Path("Plots/var").mkdir(parents=True,exist_ok=True)
    fig.savefig("Plots/var/distribtuion_%s_%s_norm%s_log%s"%(name,var,norm,log))
    plt.close()
