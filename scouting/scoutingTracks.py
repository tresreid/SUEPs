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
from plotter import *



#open files
#hlt125, df125 =openReco("SUEP_125_htcut/flat_step3_mMed-125_mDark-2_temp-2_decay-darkPhoHad_n-200_5385393_numEvent100000000.root",13.6,0)
#hltqcd, dfqcd = openReco("QCD_15to7000_htcut/flat_A634C731-5B65-A143-975A-741A8DF5DFE8_numEvent100000000.root",25.24,0)
#hltdata, dfdata = openReco("data18_numEvent100000.root",1,0)
#hltdata = openTrigg("trigger2.root",1,0)
#hltdata = openTrigg("triggerFull2.root",1,0)
#hltMC = openTrigg("qcdtest1_numEvent100000000.root",1,0)
#hltsignal = openTrigg("sampletest.root",1,0)
#hltdata = openTrigg("newtriggerPFComm_numEvent1000000.root",1,0)
#hltMC = openTrigg("newTriggerMC.root",1,0)
#hltsignal = openTrigg("signal300.root",1,0)



#hltdata = openTrigg("newData/ptThreshold_Data_numEvent1000000.root",1,0)
#hltMC = openTrigg("newData/ptThreshold_MC.root",1,0)
#hltsignal = openTrigg("newData/sig300m2t2.root",1,0)
#trigger(hltdata,"data")
#trigger(hltMC,"MC")
#trigger(hltsignal,"signal300")

hltsignal400m1t1 = openTrigg("newData/sig400m1t1.root",1,0)
trigger(hltsignal400m1t1,"signal400m1t1")
hltsignal400m1t2 = openTrigg("newData/sig400m1t2.root",1,0)
trigger(hltsignal400m1t2,"signal400m1t2")
hltsignal400m1t5 = openTrigg("newData/sig400m1t5.root",1,0)
trigger(hltsignal400m1t5,"signal400m1t5")
hltsignal400m2t1 = openTrigg("newData/sig400m2t1.root",1,0)
trigger(hltsignal400m2t1,"signal400m2t1")
hltsignal400m2t5 = openTrigg("newData/sig400m2t5.root",1,0)
trigger(hltsignal400m2t5,"signal400m2t5")
hltsignal400m5t1 = openTrigg("newData/sig400m5t1.root",1,0)
trigger(hltsignal400m5t1,"signal400m5t1")
hltsignal400m5t2 = openTrigg("newData/sig400m5t2.root",1,0)
trigger(hltsignal400m5t2,"signal400m5t2")
hltsignal400m5t5 = openTrigg("newData/sig400m5t5.root",1,0)
trigger(hltsignal400m5t5,"signal400m5t5")

## plot variable distributions
#plot_distribution(df200,dfqcd,"PFcand_pt",[0,50] ,50,0,0)
#plot_distribution(df200,dfqcd,"PFcand_pt",[0,50] ,50,1,0)
#plot_distribution(df200,dfqcd,"PFcand_pt",[0,150],50,0,1)
#plot_distribution(df200,dfqcd,"PFcand_pt",[0,150],50,1,1)
#
#plot_distribution(df200,dfqcd,"PFcand_eta",[-3.2,3.2] ,50,0,0)
#plot_distribution(df200,dfqcd,"PFcand_eta",[-3.2,3.2] ,50,1,0)
#plot_distribution(df200,dfqcd,"PFcand_eta",[-3.2,3.2] ,50,0,1)
#plot_distribution(df200,dfqcd,"PFcand_eta",[-3.2,3.2] ,50,1,1)
#
#plot_distribution(df200,dfqcd,"PFcand_phi",[-3.2,3.2] ,50,0,0)
#plot_distribution(df200,dfqcd,"PFcand_phi",[-3.2,3.2] ,50,1,0)
#plot_distribution(df200,dfqcd,"PFcand_phi",[-3.2,3.2] ,50,0,1)
#plot_distribution(df200,dfqcd,"PFcand_phi",[-3.2,3.2] ,50,1,1)
#
#plot_distribution(df200,dfqcd,"PFcand_m",[0,1] ,100,0,0)
#plot_distribution(df200,dfqcd,"PFcand_m",[0,1] ,100,1,0)
#plot_distribution(df200,dfqcd,"PFcand_m",[0,1] ,100,0,1)
#plot_distribution(df200,dfqcd,"PFcand_m",[0,1] ,100,1,1)
#
#plot_distribution(df200,dfqcd,"PFcand_vertex",[0,10] ,10,0,0)
#plot_distribution(df200,dfqcd,"PFcand_vertex",[0,10] ,10,1,0)
#plot_distribution(df200,dfqcd,"PFcand_vertex",[0,10] ,10,0,1)
#plot_distribution(df200,dfqcd,"PFcand_vertex",[0,10] ,10,1,1)
#
#plot_distribution(df200,dfqcd,"PFcand_q",[-1,1] ,3,0,0)
#plot_distribution(df200,dfqcd,"PFcand_q",[-1,1] ,3,1,0)
#plot_distribution(df200,dfqcd,"PFcand_q",[-1,1] ,3,0,1)
#plot_distribution(df200,dfqcd,"PFcand_q",[-1,1] ,3,1,1)
#
#
## make Track ID efficiency plots
#pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50,200])
#eta_bins = np.array(range(-250,250,25))/100.
#phi_bins = np.array(range(-31,31,5))/10.
#make_eff(df200,df200,df200,"PFcand_pt",pt_bins,1,"sig200")


#make significance for Track ID
#make_eff_combo(df200,dfqcd,200, 1,30)
