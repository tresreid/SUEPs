import uproot
import ROOT
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import awkward as ak
from multiprocessing import Pool

with open("monitor_scouting.txt") as f:
  for i,line in enumerate(f):
    key = line.split()[0]
    datasets = "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-v1+RAW/%s"%key
    #datasets = "root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-PromptReco-v1+MINIAOD/%s"%key

  #directory = uproot.open("../../../test2/CMSSW_10_6_26/src/PhysicsTools/qcdtest_%s_numEvent5.root"%HT)
    directory = uproot.open(datasets)
    tree = directory["mmtree/tree"]
    lums = tree["lumSec"].array()
    print("eos root://cmseos.fnal.gov/ mv /store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-v1+RAW/%s /store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-v1+RAW/lumsec%s-%s_%s.root"%(key,lums[0],lums[-1],key))
    #print("eos root://cmseos.fnal.gov/ mv /store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-PromptReco-v1+MINIAOD/%s /store/group/lpcsuep/Scouting/Monitor/ParkingScoutingMonitor+Run2018A-PromptReco-v1+MINIAOD/lumsec%s-%s_%s.root"%(key,lums[0],lums[-1]),i)
