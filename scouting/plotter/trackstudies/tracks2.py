import uproot
import ROOT
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import awkward as ak
from multiprocessing import Pool

from utils import *
import sys

pt_bins = np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50])
eta_bins = np.array(range(-250,275,25))/100.
phi_bins = np.array(range(-31,31,5))/10.

xsecs = {"HT200":1551000.0,"HT300":323400.0,"HT500":30140.0,"HT700":6344.0,"HT1000":1092.0,"HT1500":99.76,"HT2000":20.35}


i_min = 0
i_max = 10
if (len(sys.argv)) > 1:
  i_min = int(sys.argv[1])
  i_max = int(sys.argv[2])
  print(i_min,i_max)
def getvals(arr,ind,drss,iss,jss,issx):
  if len(arr)==0:
    return drss,iss,jss,issx
  if len(arr[0])==0:
    return drss,iss,jss,issx
  mindr = arr.min()
  if mindr > 0.3:
    return drss,iss,jss,issx
  drss.append(mindr)
  xs,ys = divmod(arr.argmin(), arr.shape[1])
  iss.append(xs)
  jss.append(ys)
  arr1 = np.delete(np.delete(arr,ys,1),xs,0)
  issx.append(ind[xs])
  ind1 = np.delete(ind,xs,0)
  return getvals(arr1,ind1,drss,iss,jss,issx)

def openfile_off():
  datasets ={} 
  with open("reco_lums.txt") as f:
    for i,line in enumerate(f):
      if i < i_min or i > i_max:
        continue
      datasets["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-PromptReco-v1+MINIAOD_test/%s"%line.strip()] = "mmtree/tree"

#    "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-PromptReco-v1+MINIAOD/lumsec229-233.root" : "mmtree/tree",
## "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-PromptReco-v1+MINIAOD/lumsec1-242.root" : "mmtree/tree",
## "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-PromptReco-v1+MINIAOD/lumsec1-259.root" : "mmtree/tree",
# "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-PromptReco-v1+MINIAOD/lumsec73-252.root" : "mmtree/tree",
## "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-PromptReco-v1+MINIAOD/lumsec4-238.root" : "mmtree/tree",
# "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-PromptReco-v1+MINIAOD/lumsec25-258.root" : "mmtree/tree",
  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_200_numEvent500.root": "mmtree/tree",
  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_300_numEvent500.root": "mmtree/tree",
  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_500_numEvent500.root": "mmtree/tree",
  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_700_numEvent500.root": "mmtree/tree",
  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_1000_numEvent500.root": "mmtree/tree",
  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_1500_numEvent500.root": "mmtree/tree",
  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_2000_numEvent500.root": "mmtree/tree"
  #}
  tree = uproot.lazy(datasets)
  offlineTrack_pt        = ak.flatten(tree["offlineTrack_pt"])#.array())
  offlineTrack_eta       = ak.flatten(tree["offlineTrack_eta"])#.array())
  offlineTrack_phi       = ak.flatten(tree["offlineTrack_phi"])#.array())
  offlineTrack_quality   = ak.flatten(tree["offlineTrack_quality"])#.array())
  offlineTrack_dzError   = ak.flatten(tree["offlineTrack_dzError"])#.array())
  counts = ak.count(tree["offlineTrack_pt"],axis=-1)
  events = []
  wgts = []
  for i,event in enumerate(tree["event"]):
    events.append(np.repeat(event,counts[i]))
    #if i <500:
    #  xsec = xsecs["HT200"]
    #elif i <1000:
    #  xsec = xsecs["HT300"]
    #elif i <1500:
    #  xsec = xsecs["HT500"]
    #elif i <2000:
    #  xsec = xsecs["HT700"]
    #elif i <2500:
    #  xsec = xsecs["HT1000"]
    #elif i <3000:
    #  xsec = xsecs["HT1500"]
    #else:
    #  xsec = xsecs["HT2000"]
    xsec = 1
    wgts.append(np.repeat(xsec/500,counts[i]))
  event = ak.flatten(events)
  wgt = ak.flatten(wgts)
  
  dfoff = pd.DataFrame({
  'wgt': wgt,
  'event':event, 
  'offlineTrack_pt':offlineTrack_pt, 
  'offlineTrack_eta':offlineTrack_eta, 
  'offlineTrack_phi':offlineTrack_phi, 
  'offlineTrack_quality': offlineTrack_quality, 
  'offlineTrack_dzError': offlineTrack_dzError, 
  })
  return dfoff#,dfon
def openfile_on():
  datasets ={} 
  with open("scouting_lums.txt") as f:
    for i,line in enumerate(f):
      if i< i_min or i > i_max:
        continue
      datasets["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-v1+RAW_test/%s"%line.strip()] = "mmtree/tree"

#  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_200_numEvent500.root": "mmtree/tree",
#  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_300_numEvent500.root": "mmtree/tree",
#  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_500_numEvent500.root": "mmtree/tree",
#  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_700_numEvent500.root": "mmtree/tree",
#  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_1000_numEvent500.root": "mmtree/tree",
#  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_1500_numEvent500.root": "mmtree/tree",
#  #"../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_2000_numEvent500.root": "mmtree/tree"
#"root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-v1+RAW/lumsec226-231_B662479F-F449-E811-9EAA-FA163E293BC0.root.root" : "mmtree/tree", 
#"root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-v1+RAW/lumsec227-229_28A20AA8-D149-E811-828D-FA163EAC6D11.root.root" : "mmtree/tree",
#"root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-v1+RAW/lumsec229-233_248E57E2-E449-E811-8C0C-FA163E6AE23B.root.root" : "mmtree/tree",
#"root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-v1+RAW/lumsec230-232_BE152A8E-D149-E811-94BF-FA163E5DED89.root.root" : "mmtree/tree",
#"root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-v1+RAW/lumsec232-237_98F3B9E6-F449-E811-8599-FA163ED29C3D.root.root" : "mmtree/tree",
#"root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-v1+RAW/lumsec233-235_307E0A88-D149-E811-88AA-FA163ECE7C6A.root.root" : "mmtree/tree"
#  }
  tree = uproot.lazy(datasets)
  event    = ak.flatten(ak.broadcast_arrays(tree["event"][:,np.newaxis],tree["PFcand_pt"]))#.array())
  #offlineTrack_ht        = tree["htoff"]#.array()
  onlineTrack_pt         = ak.flatten(tree["PFcand_pt"])#.array())
  onlineTrack_eta        = ak.flatten(tree["PFcand_eta"])#.array())
  onlineTrack_phi        = ak.flatten(tree["PFcand_phi"])#.array())
  onlineTrack_q          = ak.flatten(tree["PFcand_q"])#.array())
  counts = ak.count(tree["PFcand_pt"],axis=-1)
  events = []
  wgts = []
  for i,event in enumerate(tree["event"]):
    events.append(np.repeat(event,counts[i]))
    #if i <500:
    #  xsec = xsecs["HT200"]
    #elif i <1000:
    #  xsec = xsecs["HT300"]
    #elif i <1500:
    #  xsec = xsecs["HT500"]
    #elif i <2000:
    #  xsec = xsecs["HT700"]
    #elif i <2500:
    #  xsec = xsecs["HT1000"]
    #elif i <3000:
    #  xsec = xsecs["HT1500"]
    #else:
    #  xsec = xsecs["HT2000"]
    xsec =1
    wgts.append(np.repeat(xsec,counts[i]))
  event = ak.flatten(events)
  wgt = ak.flatten(wgts)

  dfon = pd.DataFrame({
  'wgt': wgt,
  'event':event, 
  #'onlineTrack_dR':onlineTrack_dR, 
  'onlineTrack_pt':onlineTrack_pt, 
  'onlineTrack_eta':onlineTrack_eta, 
  'onlineTrack_phi':onlineTrack_phi, 
  'onlineTrack_q':onlineTrack_q, 
  })
  return dfon#,dfon

dfoff1 = openfile_off()
print("offline loaded")
dfoff2 = openfile_on()
print("online loaded")
dfoff2 = dfoff2[(dfoff2["onlineTrack_pt"] >= 0.75)& (abs(dfoff2["onlineTrack_eta"]) <= 2.4) & (abs(dfoff2["onlineTrack_q"]) == 1)]

dfoff1["offlineTrack_paired"] =0
list1 = dfoff1["event"].unique()
list2 = dfoff2["event"].unique()
#print(list1)
#print(list2)
intersection = list(set(list1) & (set(list2)))
print("intersection")
print(len(list1),len(list2),len(intersection))
#for x, group in grouped1:
#  print("1:"x)
#for x, group in grouped2:
#  print(x)
  #grouped1["offlineTrack_paired"] =0
  #grouped1.iloc[iss] = 1
#issx = ak.flatten(matching(grouped1,grouped2))
#ys, xs = zip(*grouped1)

dfoff1x = dfoff1[dfoff1["event"].isin(intersection)]
dfoff2x = dfoff2[dfoff2["event"].isin(intersection)]
grouped1 = dfoff1x.groupby("event")
grouped2 = dfoff2x.groupby("event")
def matching(grouped1, grouped2):
  issx0 = []
  for i,(x, group) in enumerate(grouped1):
    if (i%100 ==0):
      print(i)
    #if (i>50):
    #  break
    dR= []
    #print(1,group)
    #print(2,grouped2.get_group(x))
    group = grouped1.get_group(x)
    group2 = grouped2.get_group(x)
    ind =[]
    for eta1, phi1,indi in zip(group["offlineTrack_eta"],group["offlineTrack_phi"],group.index):
      ind.append(indi)
      dr_row = []
      for eta2, phi2 in zip(group2["onlineTrack_eta"],group2["onlineTrack_phi"]):
        dEta = eta1-eta2
        dPhi = phi1 -phi2
        if dPhi > np.pi:
          dPhi = 2*np.pi-dPhi
        if dPhi > np.pi:
          dPhi = 2*np.pi+dPhi
        dr_row.append(((dEta)**2+(dPhi)**2))
      dR.append(dr_row)
    #print(dR)
    dR= np.array(dR)
    mindrs, iss, jss,issx = getvals(dR,ind,[],[],[],[])
    issx0.append(issx)
    #dfoff1x[dfoff1x["event"]==x]["offlineTrack_paired"].ilox[
  return issx0
#p = Pool(10)
#issx0 = p.map(matching,grouped1,grouped2)
#issx0 = p.map(matching,grouped1)
issx0 = matching(grouped1,grouped2)
print(len(issx0))
issx = ak.flatten(issx0)
print(len(issx))
print(len(dfoff1x))
dfoff1["offlineTrack_paired"].iloc[issx] = 1
  #print(grouped1)
  #print(issx)
  #print(iss)
  
  #print(mindrs)
  #print(iss)
  #print(jss)
  
  #print(2,dfoff2[dfoff2["offlineTrack_event"] == x])

  
#dfoff = dfoff[(dfoff["offlineTrack_pt"] >= 0.75) & (dfoff["offlineTrack_quality"] == 1) & (abs(dfoff["offlineTrack_eta"]) <=2.4)]
#dfoff = dfoff1x
dfoff = dfoff1[dfoff1["event"].isin(intersection)]
df2off = dfoff[(dfoff["offlineTrack_paired"] == 1)]# & (dfoff["offlineTrack_PFcandpt"] >= 0.75)& (abs(dfoff["offlineTrack_PFcandeta"]) <= 2.4) & (dfoff["offlineTrack_PFcandpv"] == 0) & (abs(dfoff["offlineTrack_PFcandq"]) == 1)]
#df2on = dfon[dfon["onlineTrack_paired"] == 1]
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
  ax1.set_ylim([0,1])
  ax1.legend()
  ax.legend()
  np.savetxt("hists/num_%s_%d_%d.txt"%(var,i_min,i_max),h2[0])
  np.savetxt("hists/denom_%s_%d_%d.txt"%(var,i_min,i_max),h1[0])
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

#make_scatter("pt")
#make_scatter("eta")
#make_scatter("phi")
#make_scatter("ht",2)
#make_scatter("dz")
#make_hist("pvnum")
make_hist("pt")
make_hist("eta")
make_hist("phi")
make_hist("quality")
##make_hist("dz")
##make_hist("dxy")
##make_hist("chi2")
make_hist("dzError")
##make_hist("ptError")
##
#
##make_scatter("pt",1)
##make_scatter("eta",1)
##make_scatter("phi",1)
###make_scatter("dz",1)
##make_hist("pt",1)
##make_hist("eta",1)
##make_hist("phi",1)
###make_hist("dz",1)
#
#make_hist2d("pt","eta")
def make_hist_total(var,version=0):
  fig, (ax,ax1) = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(7,7),
        gridspec_kw={"height_ratios": (3, 1)},
        sharex=True
    )
  fig.subplots_adjust(hspace=.07)
  v3 = "Offline"
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
 
  n1_tot = np.zeros(len(xbin)-1)
  n2_tot = np.zeros(len(xbin)-1)
  skip = [400,425,450,475,500,525,575,600,625]
  for i1,i2 in zip(range(0,1600,25),range(25,1625,25)):
    if i1 in skip:
      continue
    n2 = np.loadtxt("hists/num_%s_%d_%d.txt"%(var,i1,i2))
    n1 = np.loadtxt("hists/denom_%s_%d_%d.txt"%(var,i1,i2))
    print("n2: ",n2)
    print("n1: ",n1)
    n2_tot = np.add(n2_tot,n2)
    n1_tot = np.add(n1_tot,n1)
  print("n2 tot: ",n2_tot)
  print("n1 tot: ",n1_tot)
  h1 = ax.hist(xbin[:-1],bins=xbin,weights=n1_tot,color="red",label="Offline Tracks")
  h2 = ax.hist(xbin[:-1],bins=xbin,weights=n2_tot,color="blue",label="Paired Offline Tracks")

  
  print(h1)
  print(h2)
  error = np.sqrt(1/h2[0] + 1/h2[0])*(h2[0]/h1[0]) 
  ax1.errorbar(xbins(h1[1]),h2[0]/h1[0],yerr=error,xerr=xbins_err(h1[1]),marker="+",ls="none")
  ax1.set_ylim([0,1])
  ax1.legend()
  ax.legend()
  np.savetxt("hists/num_%s_tot.txt"%(var),h2[0])
  np.savetxt("hists/denom_%s_tot.txt"%(var),h1[0])
  fig.savefig("Plots/trackhist_tot_%s_%s.png"%(var,version))
  plt.close()
make_hist_total("pt")
make_hist_total("eta")
make_hist_total("phi")
make_hist_total("quality")
make_hist_total("dzError")
