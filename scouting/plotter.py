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
from ROOT import TMath, TLegend, TF1
plt.style.use(hep.style.ROOT)

lumi = 57
def openReco(name,xsec,qcd):
  dfs = []
  hlts = []
  #prefix = "root://eoscms.cern.ch//eos/cms/store/group/ml/AnomalyHackathon/SUEP/scouting/"
  prefix = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Scouting_v0.0/2018/"
  #prefix = "root://cmseos.fnal.gov//store/group/lpcsuep/Samples/"
  if qcd:
    fs = np.loadtxt("rootfiles/%s.txt"%(name),dtype=str)
    if "test" in name:
      prefix += "QCD/HT2000/"
    else:
      prefix += "QCD/%s/"%(name)
  else:
    #prefix += "Signal/"
    fs = [name]
  print(fs)
  for fnum in fs:
    print(fnum)
    try:
      file = uproot.open(prefix+"%s"%(fnum))
    except OSError:
      print("file not found: %s %s"%(name,prefix+fnum))
      continue
    t= file["mmtree/tree"]
    #t= file["TreeMaker2/PreSelection"]
    hlt1 = t.pandas.df(["hltResult","ht"])
    df1 = t.pandas.df([
      "PFcand_pt","PFcand_eta","PFcand_phi","PFcand_m"
      ,"PFcand_q","PFcand_vertex","PFcand_fromsuep","ht"
    ])
    hlts.append(hlt1)
    dfs.append(df1)
  df = pd.concat(dfs)
  df = pd.DataFrame(df.to_records())
  hlt = pd.concat(hlts)
  hlt = pd.DataFrame(hlt.to_records())
  df["wgt"] = xsec*lumi/len(df)
  #print(df)
  #print(hlt)
  return [hlt,df]
def openTrigg(name,xsec,qcd):
  hlts = []
  prefix = "/uscms/home/mreid/nobackup/sueps/analysis/CMSSW_10_6_0/src/PhysicsTools/"
  if qcd:
    fs = np.loadtxt("rootfiles/%s.txt"%(name),dtype=str)
    if "test" in name:
      prefix += "QCD/HT2000/"
    else:
      prefix += "QCD/%s/"%(name)
  else:
    #prefix += "Signal/"
    fs = [name]
  print(fs)
  for fnum in fs:
    print(fnum)
    try:
      file = uproot.open(prefix+"%s"%(fnum))
    except OSError:
      print("file not found: %s %s"%(name,prefix+fnum))
      continue
    t= file["mmtree/tree"]
    hlt1 = t.pandas.df(["hltResult","ht","suepJet_sphericity","n_pfcand","n_bpfcand","n_jet","n_fatjet","eventBoosted_sphericity","event_sphericity"])
    hlt1 = hlt1[hlt1["ht"] > 250]
    #print(hlt1)
    hlts.append(hlt1)
  hlt = pd.concat(hlts)
  hlt = pd.DataFrame(hlt.to_records())
  hltx = hlt.pivot(index="entry",columns="subentry",values="hltResult")
  hltx["ht"] = hlt.groupby("entry")["ht"].max()#values[0]
  hltx["suepJet_sphericity"] = hlt.groupby("entry")["suepJet_sphericity"].max()#values[0]
  hltx["n_pfcand"] = hlt.groupby("entry")["n_pfcand"].max()#values[0]
  hltx["n_bpfcand"] = hlt.groupby("entry")["n_bpfcand"].max()#values[0]
  hltx["n_jet"] = hlt.groupby("entry")["n_jet"].max()#values[0]
  hltx["n_fatjet"] = hlt.groupby("entry")["n_fatjet"].max()#values[0]
  hltx["eventBoosted_sphericity"] = hlt.groupby("entry")["eventBoosted_sphericity"].max()#values[0]
  hltx["event_sphericity"] = hlt.groupby("entry")["event_sphericity"].max()#values[0]
  #print(hltx)
  return hltx


def make_trigDist(h_no_selection,h1_no_selection,h_before_selection,variable,name):
    Path("Plots/eff").mkdir(parents=True,exist_ok=True)
    #func = TF1("func","[0]*TMath::Erf((x-[1])/[2])+1",300,800)
    #func.SetParameters(0.1,500,5)
    c0 = ROOT.TCanvas("c0%s"%(variable), "my canvas 0 %s"%variable)
    h_no_selection.Draw()
    h_no_selection.SetLineColor(3) # 2=red
    h1_no_selection.Draw("same")
    h1_no_selection.SetLineColor(1) # 2=red
    h_before_selection.Draw("same")
    h_before_selection.SetLineColor(2) # 2=red
    h_no_selection.GetXaxis().SetTitle(variable)
    h_no_selection.GetYaxis().SetTitle("Events")

    n0 = h_no_selection.GetEntries()
    n1 = h1_no_selection.GetEntries()
    n2 = h_before_selection.GetEntries()

    leg = TLegend(.73,.32,.97,.53)
    leg.AddEntry(h_no_selection,"no cuts: %s"%n0,"l")
    leg.AddEntry(h_before_selection,"ref fired only: %s"%n2,"l")
    leg.AddEntry(h1_no_selection,"410trig fired only: %s"%n1,"l")
    leg.Draw()
    c0.SaveAs("Plots/eff/trigger410PreDist_%s_%s.png"%(variable,name))

def make_trigeffPlot(h_before_selection,h1_after_selection,variable,name):
    Path("Plots/eff").mkdir(parents=True,exist_ok=True)
    #func = TF1("func","[0]*TMath::Erf((x-[1])/[2])+1",300,800)
    #func.SetParameters(0.1,500,5)
    c1 = ROOT.TCanvas("c1%s"%(variable), "my canvas 1 %s"%variable)
    h_before_selection.Draw()
    h_before_selection.SetLineColor(1) # 2=red
    h1_after_selection.Draw("same")
    h1_after_selection.SetLineColor(2) # 2=red
    h_before_selection.GetXaxis().SetTitle(variable)
    h_before_selection.GetYaxis().SetTitle("Events")

    n0 = h_before_selection.GetEntries()
    n1 = h1_after_selection.GetEntries()
    leg = TLegend(.73,.32,.97,.53)
    leg.AddEntry(h_before_selection,"ref fired only: %s"%n0,"l")
    leg.AddEntry(h1_after_selection,"+410trig fired: %s"%n1,"l")
    leg.Draw()
    c1.SaveAs("Plots/eff/trigger410Dist_%s_%s.png"%(variable,name))


    g1_efficiency = ROOT.TGraphAsymmErrors()
    g1_efficiency.Divide(h1_after_selection,h_before_selection,"cl=0.683 b(1,1) mode")
    c1x = ROOT.TCanvas("c1x%s"%variable, "my canvas 1x %s"%variable)
    g1_efficiency.Draw()
    g1_efficiency.GetXaxis().SetTitle(variable)
    g1_efficiency.GetYaxis().SetTitle("Efficiency")
    #g1_efficiency.Fit('func','R')
    c1x.SaveAs("Plots/eff/trigger410Eff_%s_%s.png"%(variable,name))

def trigger(df,name):

    fig, ax1 = plt.subplots()
    fig, ax2 = plt.subplots()
    bins = range(0,1500,20)

    h_no_selection = ROOT.TH1F("h_no_selection","",50,0,1500) #no cuts
    h1_no_selection = ROOT.TH1F("h1_no_selection","",50,0,1500) # 410 trigger only
    h_before_selection = ROOT.TH1F("h_before_selection","",50,0,1500) # ref trigger only
    h1_after_selection  = ROOT.TH1F("h1_after_selection","",50,0,1500)
    #h2_after_selection  = ROOT.TH1F("h2_after_selection","",100,0,1500) #DST_HT450_PFScouting
    #h3_after_selection  = ROOT.TH1F("h3_after_selection","",100,0,1500) # both 410 and 450
    h_before_selection1 = ROOT.TH1F("h_before_selection1","",50,0,1)
    h1_after_selection1  = ROOT.TH1F("h1_after_selection1","",50,0,1)
    h_before_selection2 = ROOT.TH1F("h_before_selection2","",100,0,1000)
    h1_after_selection2  = ROOT.TH1F("h1_after_selection2","",100,0,1000)
    h_before_selection3 = ROOT.TH1F("h_before_selection3","",150,0,150)
    h1_after_selection3  = ROOT.TH1F("h1_after_selection3","",150,0,150)
    h_before_selection4 = ROOT.TH1F("h_before_selection4","",10,0,10)
    h1_after_selection4  = ROOT.TH1F("h1_after_selection4","",10,0,10)
    h_before_selection5 = ROOT.TH1F("h_before_selection5","",10,0,10) 
    h1_after_selection5  = ROOT.TH1F("h1_after_selection5","",10,0,10)
    h_before_selection6 = ROOT.TH1F("h_before_selection6","",50,0,1) 
    h1_after_selection6  = ROOT.TH1F("h1_after_selection6","",50,0,1) 
    h_before_selection7 = ROOT.TH1F("h_before_selection7","",50,0,1) 
    h1_after_selection7  = ROOT.TH1F("h1_after_selection7","",50,0,1) 
#HLT Trigger DST_DoubleMu1_noVtx_CaloScouting_v2 1 0 DST_DoubleMu1_noVtx_CaloScouting_v*
#HLT Trigger DST_DoubleMu3_noVtx_CaloScouting_Monitoring_v6 1 1 DST_DoubleMu3_noVtx_CaloScouting_v*
#HLT Trigger DST_DoubleMu3_noVtx_CaloScouting_v6 1 1 DST_DoubleMu3_noVtx_CaloScouting_v*
#HLT Trigger DST_DoubleMu3_noVtx_Mass10_PFScouting_v3 0 2 DST_DoubleMu3_noVtx_Mass10_PFScouting_v*
#HLT Trigger DST_L1HTT_CaloScouting_PFScouting_v15 1 3 DST_L1HTT_CaloScouting_PFScouting_v*
#HLT Trigger DST_CaloJet40_CaloScouting_PFScouting_v15 1 4 DST_CaloJet40_CaloScouting_PFScouting_v*
#HLT Trigger DST_HT250_CaloScouting_v10 1 5 DST_HT250_CaloScouting_v*
#HLT Trigger DST_HT410_PFScouting_v16 1 6 DST_HT410_PFScouting_v*
    for row in df.itertuples(index=False):
      #print(row)
      #break
      #if row[4]: #L1HTT
      #if row[5]:#calojet40
      ht = row[8]
      h_no_selection.Fill(ht)
      if row[7]:
        h1_no_selection.Fill(ht)
      if row[2]: #DoubleMu3
        #ht = row[8]
        suep_sphere= row[9]
        npfcand= row[10]
        nbpfcand= row[11]
        njet= row[12]
        nfatjet= row[13]
        event_bsphere = row[14]
        event_sphere = row[15]
        h_before_selection.Fill(ht)
        if(ht >500):
          h_before_selection1.Fill(suep_sphere)
          h_before_selection2.Fill(npfcand)
          h_before_selection3.Fill(nbpfcand)
          h_before_selection4.Fill(njet)
          h_before_selection5.Fill(nfatjet)
          h_before_selection6.Fill(event_bsphere)
          h_before_selection7.Fill(event_sphere)
          if row[7]:
        #if row[1]:
        #if row[6]:
            h1_after_selection.Fill(ht)
            h1_after_selection1.Fill(suep_sphere)
            h1_after_selection2.Fill(npfcand)
            h1_after_selection3.Fill(nbpfcand)
            h1_after_selection4.Fill(njet)
            h1_after_selection5.Fill(nfatjet)
            h1_after_selection6.Fill(event_bsphere)
            h1_after_selection7.Fill(event_sphere)
        #if row[0]:
        ##if row[7]:
        #  h2_after_selection.Fill(ht)
        #if row[1] or row[0]:
        ##if row[6] or row[7]:
        #  h3_after_selection.Fill(ht)

    #make_trigDist(h_no_selection,h1_no_selection,h_before_selection,"ht",name)
    make_trigeffPlot(h_before_selection,h1_after_selection,"ht",name)
    #make_trigeffPlot(h_no_selection,h1_no_selection,"ht","noref_%s"%name)
    #make_trigeffPlot(h_before_selection6,h1_after_selection6,"event_boost_sphericity",name)
    #make_trigeffPlot(h_before_selection7,h1_after_selection7,"event_sphericity",name)

    #make_trigeffPlot(h_before_selection1,h1_after_selection1,"suep_sphere",name)
    #make_trigeffPlot(h_before_selection2,h1_after_selection2,"npfcand",name)
    #make_trigeffPlot(h_before_selection3,h1_after_selection3,"nbpfcand",name)
    #make_trigeffPlot(h_before_selection4,h1_after_selection4,"njet",name)
    #make_trigeffPlot(h_before_selection5,h1_after_selection5,"nfatjet",name)
    #make_trigeffPlot(h_before_selection6,h1_after_selection6,"event_sphere",name)
    #Path("Plots/eff").mkdir(parents=True,exist_ok=True)
    #func = TF1("func","[0]*TMath::Erf((x-[1])/[2])+1",300,800)
    #func.SetParameters(0.1,500,5)
    #c1 = ROOT.TCanvas("c1", "my canvas 1")
    #h_before_selection.Draw()
    #h1_after_selection.Draw("same")
    #h1_after_selection.SetLineColor(2) # 2=red
    #h_before_selection.GetXaxis().SetTitle("Ht")
    #h_before_selection.GetYaxis().SetTitle("Events")
    #c1.SaveAs("Plots/eff/eff3_%s_410.png"%(name))
    #g1_efficiency = ROOT.TGraphAsymmErrors()
    #g1_efficiency.Divide(h1_after_selection,h_before_selection,"cl=0.683 b(1,1) mode")
    #c1x = ROOT.TCanvas("c1x", "my canvas 1x")
    #g1_efficiency.Draw()
    #g1_efficiency.GetXaxis().SetTitle("Ht")
    #g1_efficiency.GetYaxis().SetTitle("Efficiency")
    #g1_efficiency.Fit('func','R')
    #c1x.SaveAs("Plots/eff/eff3x_%s_410.png"%(name))


    #c2 = ROOT.TCanvas("c2", "my canvas 2")
    #h_before_selection.Draw()
    #h2_after_selection.Draw("same")
    #h2_after_selection.SetLineColor(2)
    #h_before_selection.GetXaxis().SetTitle("Ht")
    #h_before_selection.GetYaxis().SetTitle("Events")
    #c2.SaveAs("Plots/eff/eff3_%s_450.png"%(name))
    #g2_efficiency = ROOT.TGraphAsymmErrors()
    #g2_efficiency.Divide(h2_after_selection,h_before_selection,"cl=0.683 b(1,1) mode")
    #c2x = ROOT.TCanvas("c2x", "my canvas 2x")
    #g2_efficiency.Draw()
    #g1_efficiency.GetXaxis().SetTitle("Ht")
    #g1_efficiency.GetYaxis().SetTitle("Efficiency")
    #c2x.SaveAs("Plots/eff/eff3x_%s_450.png"%(name))

    #c3 = ROOT.TCanvas("c3", "my canvas 3")
    #h_before_selection.Draw()
    #h3_after_selection.Draw("same")
    #h3_after_selection.SetLineColor(2)
    #h_before_selection.GetXaxis().SetTitle("Ht")
    #h_before_selection.GetYaxis().SetTitle("Events")
    #c3.SaveAs("Plots/eff/eff3_%s_both.png"%(name))
    #g3_efficiency = ROOT.TGraphAsymmErrors()
    #g3_efficiency.Divide(h3_after_selection,h_before_selection,"cl=0.683 b(1,1) mode")
    #c3x = ROOT.TCanvas("c3x", "my canvas 3x")
    #g3_efficiency.Draw()
    #g1_efficiency.GetXaxis().SetTitle("Ht")
    #g1_efficiency.GetYaxis().SetTitle("Efficiency")
    #c3x.SaveAs("Plots/eff/eff3x_%s_both.png"%(name))

def plot_distribution(df,qcd_df,var,rx,bx,norm,log):
    fig, ax1 = plt.subplots()
    ax1.hist(df[df["PFcand_fromsuep"] == 1][var]      ,bins=bx,range=rx,   density=norm, histtype=u'step',weights=df[df["PFcand_fromsuep"] == 1]["wgt"],color="blue",label="true")
    ax1.hist(df[df["PFcand_fromsuep"] == 0][var]      ,bins=bx,range=rx,   density=norm, histtype=u'step',weights=df[df["PFcand_fromsuep"] == 0]["wgt"],color="red",label="false")
    ax1.hist(qcd_df[var]                              ,bins=bx,range=rx,   density=norm, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
    ax1.legend()
    ax1.set_xlabel(var)
    if norm:
      ax1.set_ylabel("AU")
    else:
      ax1.set_ylabel("events")
    if log:
      ax1.set_yscale('log')
    Path("Plots/var").mkdir(parents=True,exist_ok=True)
    fig.savefig("Plots/var/matched_distribtuion_%s_norm%s_log%s"%(var,norm,log))
    plt.close()




def make_eff(df,dfID,gen_df,var,bins,idtype,sample):
  print("running %s eff"%var)

  all_group = df.groupby(pd.cut(df[var],bins))["wgt"].sum().to_numpy()
  reco_group = df[(df["PFcand_fromsuep"] == 1)].groupby(pd.cut(df[(df["PFcand_fromsuep"] == 1)][var],bins))["wgt"].sum().to_numpy()
  fake_group = df[(df["PFcand_fromsuep"] == 0)].groupby(pd.cut(df[(df["PFcand_fromsuep"] == 0)][var],bins))["wgt"].sum().to_numpy()
  ID_group = dfID[(dfID["PFcand_fromsuep"] == 1)].groupby(pd.cut(dfID[(dfID["PFcand_fromsuep"] == 1)][var],bins))["wgt"].sum().to_numpy()
  fakeID_group = dfID[(dfID["PFcand_fromsuep"] == 0)].groupby(pd.cut(dfID[(dfID["PFcand_fromsuep"] == 0)][var],bins))["wgt"].sum().to_numpy()
  allID_group = dfID.groupby(pd.cut(dfID[var],bins))["wgt"].sum().to_numpy()
  gen_group = gen_df.groupby(pd.cut(gen_df[var],bins))["wgt"].sum().to_numpy()


  eff = pd.DataFrame()
  eff["range"] = (bins[1:]-bins[:-1])/2.
  eff["recoeff"] = (reco_group/gen_group) #reco matched/ all gen
  eff["reco_yerr"]=(reco_group/gen_group)*np.sqrt((1/reco_group)+(1/gen_group))
  eff["IDeff"] = (ID_group/reco_group) # reco-matched ID / reco-matched
  eff["ID_yerr"]=(ID_group/reco_group)*np.sqrt((1/reco_group)+(1/ID_group))
  eff["fakeRate"] = (fake_group/all_group) # not reco-matched ID / all reco
  eff["fake_yerr"]=(fake_group/all_group)*np.sqrt((1/fake_group)+(1/all_group))
  eff["purity"] = (reco_group/all_group) # reco-matched ID / all reco
  eff["pure_yerr"]=(reco_group/all_group)*np.sqrt((1/reco_group)+(1/all_group))
  eff["fakeIDeff"] = (fakeID_group/allID_group) # not reco-matched ID / all reco
  eff["fakeID_yerr"]=(fakeID_group/allID_group)*np.sqrt((1/allID_group)+(1/fakeID_group))
  eff["totaleff"] = (ID_group/gen_group) #reco matched ID / all gen
  eff["total_yerr"]=(ID_group/gen_group)*np.sqrt((1/reco_group)+(1/gen_group))

  if "phi" in var:
    eff_reco = np.nanmean(eff["recoeff"].to_numpy())
    eff_id = np.nanmean(eff["IDeff"].to_numpy())
    eff_fake = np.nanmean(eff["fakeRate"].to_numpy())
    eff_pure = np.nanmean(eff["purity"].to_numpy())
    eff_fakeid = np.nanmean(eff["fakeIDeff"].to_numpy())
    eff_total = np.nanmean(eff["totaleff"].to_numpy())
    label1="reco eff: %.1f%%"%(100*eff_reco)
    label2="ID eff: %.1f%%"%(100*eff_id)
    label3="fake Rate: %.1f%%"%(100*eff_fake)
    label4="purity: %.1f%%"%(100*eff_pure)
    label5="fake ID Rate: %.1f%%"%(100*eff_fakeid)
    label6="Total Eff: %.1f%%"%(100*eff_total)
  elif "pt" in var:
    eff_reco =   np.nanmean(eff[eff["range"]>10]["recoeff"].to_numpy())
    eff_id =     np.nanmean(eff[eff["range"]>10]["IDeff"].to_numpy())
    eff_fake =   np.nanmean(eff[eff["range"]>10]["fakeRate"].to_numpy())
    eff_pure =   np.nanmean(eff[eff["range"]>10]["purity"].to_numpy())
    eff_fakeid = np.nanmean(eff[eff["range"]>10]["fakeIDeff"].to_numpy())
    eff_total =  np.nanmean(eff[eff["range"]>10]["totaleff"].to_numpy())
    label1="reco eff: %.1f%%"%(100*eff_reco)
    label2="ID eff: %.1f%%"%(100*eff_id)
    label3="fake Rate: %.1f%%"%(100*eff_fake)
    label4="purity: %.1f%%"%(100*eff_pure)
    label5="fake ID Rate: %.1f%%"%(100*eff_fakeid)
    label6="Total Eff: %.1f%%"%(100*eff_total)
  else:
    label1="reco eff"
    label2="ID eff"
    label3="fake Rate"
    label4="purity"
    label5="fake ID Rate"
    label6="Total Eff"



  fig, ax = plt.subplots(2,sharex=True)
  fig.suptitle("%s: "%(sample)) #+partType[idtype])
  ax[0].set_ylabel("events")
  ax[1].set_ylabel("efficiency")
  if "pt" in var:
    ax[0].set_yscale('log')
    ax[0].set_xscale('log')
    ax[1].set_xscale('log')

  ax[0].hist(df[(df["PFcand_fromsuep"] == 1)][var], bins=bins,histtype=u'step',weights=df[(df["PFcand_fromsuep"] == 1)]["wgt"],color="blue",label="matched")
  ax[0].hist(df[(df["PFcand_fromsuep"] == 0)][var],bins=bins,histtype=u'step',weights=df[(df["PFcand_fromsuep"] == 0)]["wgt"],color="red",label="!matched")
  ax[0].hist(df[var], bins=bins,histtype=u'step',weights=df["wgt"],color="black",label="all reco")
  ax[0].hist(gen_df[var], bins=bins,histtype=u'step',weights=gen_df["wgt"],color="magenta",label="gen")

  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["recoeff"].to_numpy(),eff["reco_yerr"].to_numpy(),xerr=eff["range"],ls='none',    label=label1,color="blue")
  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["fakeRate"].to_numpy(),eff["fake_yerr"].to_numpy(),xerr=eff["range"],ls='none',   label=label3,color="red")
  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["purity"].to_numpy(),eff["pure_yerr"].to_numpy(),xerr=eff["range"],ls='none',     label=label4,color="cyan")

  ax[1].set_ylim([0,1.01])
  ax[1].set_xlabel(var)
  ax[0].set_xlabel(var)
  ax[0].legend(loc="lower left")
  ax[1].legend(loc="lower left")
  fig.tight_layout()
  Path("Plots/eff").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/eff/efficiency_%s_%s_%sv1.png"%(var,idtype,sample))
  plt.close()

  fig, ax = plt.subplots(2,sharex=True)
  fig.suptitle("%s: "%(sample))#+partType[idtype])
  ax[0].set_ylabel("events")
  ax[1].set_ylabel("efficiency")
  if "pt" in var:
    ax[0].set_yscale('log')
    ax[0].set_xscale('log')
    ax[1].set_xscale('log')

  ax[0].hist(dfID[(dfID["PFcand_fromsuep"] == 1)][var], bins=bins,histtype=u'step',weights=dfID[(dfID["PFcand_fromsuep"] == 1)]["wgt"],color="green",label="matched+ID")
  ax[0].hist(dfID[(dfID["PFcand_fromsuep"] == 0)][var], bins=bins,histtype=u'step',weights=dfID[(dfID["PFcand_fromsuep"] == 0)]["wgt"],color="cyan",label="!matched+ID")
  ax[0].hist(df[var], bins=bins,histtype=u'step',weights=df["wgt"],color="black",label="all reco")
  ax[0].hist(gen_df[var], bins=bins,histtype=u'step',weights=gen_df["wgt"],color="magenta",label="gen")

  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["IDeff"].to_numpy(),eff["ID_yerr"].to_numpy(),xerr=eff["range"],ls='none',        label=label2,color="green")
  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["fakeIDeff"].to_numpy(),eff["fakeID_yerr"].to_numpy(),xerr=eff["range"],ls='none',label=label5,color="orange")
  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["totaleff"].to_numpy(),eff["total_yerr"].to_numpy(),xerr=eff["range"],ls='none',  label=label6,color="black")

  ax[1].set_ylim([0,1.01])
  ax[1].set_xlabel(var)
  ax[0].set_xlabel(var)
  ax[0].legend(loc="lower left")
  ax[1].legend(loc="lower left")
  fig.tight_layout()
  Path("Plots/eff").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/eff/efficiency_%s_%s_%sv2.png"%(var,idtype,sample))
  plt.close()


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
