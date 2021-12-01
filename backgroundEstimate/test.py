import uproot
import numpy as np
import pandas as pd

file = uproot.open("../root/PrivateSamples.SUEP_2018_mMed-1000_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root")
t= file["TreeMaker2/PreSelection"]
print(t.arrays(["Shape_sphericity_boosted","Shape_sphericity"],library="pd"))
#print(t["Shape_sphericity_boosted","Shape_sphericity"].array(library="pd"))
