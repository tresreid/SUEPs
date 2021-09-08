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
#from pathlib import Path
#partType = {0:"all",11:"electron",13:"muon",22:"photon",211:"pion",100:"hadron",1:"pv >= 2",2:"pv >=2; matched==1",3:"pv >= 2; matched==1; nHits >= 10",4:"pv >= 2; matched==1; nHits>=10; pt > 1",5:"pv >= 2; matched==1; pt>100",6:"pt>100",-1:"pv >= 2; matched==1;|eta|<1.0",-2:"pv >= 2; matched==1;|eta|>=1.0",-3:"pv >= 2; matched==1;|eta|<1.0, pt>100",-4:"pv >= 2; matched==1;|eta|>=1.0,pt>100",7:"pv >= 2; matched==1, pt resolution < 0.02(0.04) for |eta|<(>)1.0",
#8:"pv >= 2; matched==1;|dz| < 10",9:"pv >=2; matched==1(|eta| >1.0)",10:"pv >= 2; matched==1(|eta|>1.0);|dz| < 10",11:"pv >= 2; matched==1(|eta|>1.0);|dz| < 10; dzErr < 0.05",12:"pv >= 2;|dz| < 10",13:"pv >= 2;|dz| < 10; dzErr < 0.05"}

lumi = 59.74*1000
print("opening")
def openReco(name,xsec):
  dr = []
  with open('data/%s.txt'%name) as f:
      #xsec = 0.17
      for line in f.readlines():
        if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
          continue
        cols = line.rstrip().split(' ')
        dr.append({
          "wgt":xsec*lumi/10000,
          "pt":float(cols[1]),"eta":float(cols[2]),"phi":float(cols[3]),
          "jetTracks":int(cols[4]),"allTracks":int(cols[5]),
          "t1":float(cols[6]),"t2":float(cols[7]),"t3":float(cols[8]),
          #"t21":float(cols[7])/float(cols[6]),"t32":float(cols[8])/float(cols[7])
          "t21":float(cols[9]),"t32":float(cols[10]),
          "rho0":float(cols[11]),"rho1":float(cols[12]),"rho2":float(cols[13])
          })
  df = pd.DataFrame(dr)
  del dr
  df["phi"] = df["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
  return df

#df_mD1_T1 = openReco("track_mDark1_temp1_v0",5.9)
#df_mD1_T2 = openReco("track_mDark1_temp2_v0",5.9)
#df_mD1_T5 = openReco("track_mDark1_temp5_v0",5.9)
#df_mD2_T1 = openReco("track_mDark2_temp1_v0",5.9)
#df_mD2_T5 = openReco("track_mDark2_temp5_v0",5.9)
#df_mD5_T1 = openReco("track_mDark5_temp1_v0",5.9)
#df_mD5_T2 = openReco("track_mDark5_temp2_v0",5.9)
#df_mD5_T5 = openReco("track_mDark5_temp5_v0",5.9)
df1000 =openReco("variables_sig_1000_v0",0.17)
df750 = openReco("variables_sig_750_v0",0.5)
df400 = openReco("variables_sig_400_v0",5.9)
df300 = openReco("variables_sig_300_v0",8.9)
df200 = openReco("variables_sig_200_v0",13.6)

gc.collect()
          
#xsecs = [311900,29070,5962,1207,119.9,25.24] # signal xsec are (125,34.8),(300,8.9), (400,5.9), (750,0.5), (1000,0.17)
#files = [300,500,700,1000,1500,2000]
xsecs = [5962,1207,119.9,25.24] # signal xsec are (125,34.8),(300,8.9), (400,5.9), (750,0.5), (1000,0.17)
files = [700,1000,1500,2000]
qcddr =[]
qcdi=0 # don;t overlap entries from different files
line_count=0
for xsec,f1 in zip(xsecs,files):
#with open('data/track_qcd_1000_v0.txt') as f:
  num_lines = sum(1 for line in open("data/variables_qcd_%s_v0.txt"%f1)) 
  f=open("data/variables_qcd_%s_v0.txt"%f1)
  print(f1)
  #print(num_lines)
  for line in f.readlines():
    if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
      continue
    line_count = line_count+1
    cols = line.rstrip().split(' ')
#    if (line_count > num_lines/100):
#      break
    #print(qcddr)
    qcddr.append({
          "wgt":xsec*lumi/100000,
          "pt":float(cols[1]),"eta":float(cols[2]),"phi":float(cols[3]),
          "jetTracks":int(cols[4]),"allTracks":int(cols[5]),
          "t1":float(cols[6]),"t2":float(cols[7]),"t3":float(cols[8]),
          "t21":float(cols[9]),"t32":float(cols[10]),
          "rho0":float(cols[11]),"rho1":float(cols[12]),"rho2":float(cols[13])
      })
  qcdi = qcdi+1
qcd_df = pd.DataFrame(qcddr)
#print(qcd_df)
del qcddr
#print(qcd_df)
qcd_df["phi"] = qcd_df["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
#gc.collect()



print("plotting")
def trk_var(df,qcd_df,name,idtype):
  fig, ax = plt.subplots(2,2)
  fig.suptitle("%s: "%(name)+partType[idtype],y=1.0)
  
  ax[0,0].set_xlabel("trk PV")    
  ax[1,0].set_xlabel("trk Quality")    
  ax[0,1].set_xlabel("matched")    
  ax[1,1].set_xlabel("chi2")    
  ax[0,0].set_yscale('log')
  ax[0,1].set_yscale('log')
  ax[1,0].set_yscale('log')
  ax[1,1].set_yscale('log')
  
  ax[0,0].hist(df[df["min_dR"] < 0.05]["trk_pv"]      ,bins=4,range=[0,4],   density=False, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,0].hist(df[df["min_dR"] >= 0.05]["trk_pv"]     ,bins=4,range=[0,4],   density=False, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,0].hist(qcd_df["trk_pv"]                       ,bins=4,range=[0,4],   density=False, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,0].hist(df[df["min_dR"] < 0.05]["trk_quality"] ,bins=8,range=[-2,6],  density=False, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,0].hist(df[df["min_dR"] >= 0.05]["trk_quality"],bins=8,range=[-2,6],  density=False, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,0].hist(qcd_df["trk_quality"]                  ,bins=8,range=[-2,6],  density=False, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[0,1].hist(df[df["min_dR"] < 0.05]["trk_matched"] ,bins=2,range=[0,2],   density=False, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,1].hist(df[df["min_dR"] >= 0.05]["trk_matched"],bins=2,range=[0,2],   density=False, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,1].hist(qcd_df["trk_matched"]                  ,bins=2,range=[0,2],   density=False, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,1].hist(np.clip(df[df["min_dR"] < 0.05]["trk_chi2"],0,145)    ,bins=10,range=[0,150],density=False, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,1].hist(np.clip(df[df["min_dR"] >= 0.05]["trk_chi2"],0,145)   ,bins=10,range=[0,150],density=False, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,1].hist(np.clip(qcd_df["trk_chi2"],0,145)                     ,bins=10,range=[0,150],density=False, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  
  ax[0,0].legend()
  ax[1,0].legend()
  ax[0,1].legend()
  ax[1,1].legend()
  fig.tight_layout()
  fig.savefig("Plots/var/matched_distribtuion_trks1_%s_%s.png"%(name,idtype))
  plt.close()
  fig, ax = plt.subplots(2,2)
  fig.suptitle("%s: "%(name)+partType[idtype],y=1.0)
  
  ax[0,0].set_xlabel("trk PV")    
  ax[1,0].set_xlabel("trk Quality")    
  ax[0,1].set_xlabel("matched")    
  ax[1,1].set_xlabel("chi2")    
  
  ax[0,0].hist(df[df["min_dR"] < 0.05]["trk_pv"]      ,bins=4,range=[0,4],   density=True, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,0].hist(df[df["min_dR"] >= 0.05]["trk_pv"]     ,bins=4,range=[0,4],   density=True, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,0].hist(qcd_df["trk_pv"]                       ,bins=4,range=[0,4],   density=True, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,0].hist(df[df["min_dR"] < 0.05]["trk_quality"] ,bins=8,range=[-2,6],  density=True, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,0].hist(df[df["min_dR"] >= 0.05]["trk_quality"],bins=8,range=[-2,6],  density=True, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,0].hist(qcd_df["trk_quality"]                  ,bins=8,range=[-2,6],  density=True, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[0,1].hist(df[df["min_dR"] < 0.05]["trk_matched"] ,bins=2,range=[0,2],   density=True, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,1].hist(df[df["min_dR"] >= 0.05]["trk_matched"],bins=2,range=[0,2],   density=True, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,1].hist(qcd_df["trk_matched"]                  ,bins=2,range=[0,2],   density=True, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,1].hist(np.clip(df[df["min_dR"] < 0.05]["trk_chi2"],0,19.5)    ,bins=20,range=[0,20],density=True, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,1].hist(np.clip(df[df["min_dR"] >= 0.05]["trk_chi2"],0,19.5)   ,bins=20,range=[0,20],density=True, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,1].hist(np.clip(qcd_df["trk_chi2"] ,0,19.5)                    ,bins=20,range=[0,20],density=True, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  
  ax[0,0].legend()
  ax[1,0].legend()
  ax[0,1].legend()
  ax[1,1].legend()
  fig.tight_layout()
  fig.savefig("Plots/var/matched_distribtuion_trks1_%s_%s_norm.png"%(name,idtype))
  plt.close()
  
  
  fig, ax = plt.subplots(2,2)
  fig.suptitle("%s: "%(name)+partType[idtype],y=1.0)
  
  ax[0,0].set_xlabel("pT Resolution")    
  ax[1,0].set_xlabel("pT Error")    
  ax[0,1].set_xlabel("nHits")    
  ax[1,1].set_xlabel("q/p")    
  ax[0,0].set_yscale('log')
  ax[0,1].set_yscale('log')
  ax[1,0].set_yscale('log')
  ax[1,1].set_yscale('log')
  if idtype in [7]:
    pt_res_high1 = 0.1 
  else:
    pt_res_high1 = 1 
  
  ax[0,0].hist(np.clip(df[df["min_dR"] < 0.05]["pt_res"],0,pt_res_high1), bins=100,range=[0,pt_res_high1],density=False,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,0].hist(np.clip(df[df["min_dR"] >= 0.05]["pt_res"],0,pt_res_high1),bins=100,range=[0,pt_res_high1],density=False,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,0].hist(np.clip(qcd_df["pt_res"],0,pt_res_high1),           bins=100,range=[0,pt_res_high1],density=False,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,0].hist(np.clip(df[df["min_dR"] < 0.05]["pt_Err"],0,2),  bins=50,range=[0,2], density=False,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,0].hist(np.clip(df[df["min_dR"] >= 0.05]["pt_Err"],0,2), bins=50,range=[0,2], density=False,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,0].hist(np.clip(qcd_df["pt_Err"],0,2),                   bins=50,range=[0,2], density=False,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[0,1].hist(np.clip(df[df["min_dR"] < 0.05]["trk_nHits"],0,50),     bins=50,range=[0,50],density=False,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,1].hist(np.clip(df[df["min_dR"] >= 0.05]["trk_nHits"],0,50),    bins=50,range=[0,50],density=False,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,1].hist(np.clip(qcd_df["trk_nHits"],0,50),                      bins=50,range=[0,50],density=False,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,1].hist(np.clip(df[df["min_dR"] < 0.05]["qOverp"],0,0.1),    bins=100,range=[0,.1],density=False,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,1].hist(np.clip(df[df["min_dR"] >= 0.05]["qOverp"],0,0.1),   bins=100,range=[0,.1],density=False,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,1].hist(np.clip(qcd_df["qOverp"],0,0.1),                     bins=100,range=[0,.1],density=False,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  
  ax[0,0].legend()
  ax[1,0].legend()
  ax[0,1].legend()
  ax[1,1].legend()
  fig.tight_layout()
  fig.savefig("Plots/var/matched_distribtuion_trks2_%s_%s.png"%(name,idtype))
  plt.close()
  fig, ax = plt.subplots(2,2)
  fig.suptitle("%s: "%(name)+partType[idtype],y=1.0)
  
  ax[0,0].set_xlabel("pT Resolution")    
  ax[1,0].set_xlabel("pT Error")    
  ax[0,1].set_xlabel("nHits")    
  ax[1,1].set_xlabel("q/p")    
  if idtype in [-3,-4,5,6]:
    pt_res_high = 0.2 
  else:
    pt_res_high = 0.1 
  ax[0,0].hist(np.clip(df[df["min_dR"] < 0.05]["pt_res"],0,pt_res_high), bins=100,range=[0,pt_res_high],density=True,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,0].hist(np.clip(df[df["min_dR"] >= 0.05]["pt_res"],0,pt_res_high),bins=100,range=[0,pt_res_high],density=True,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,0].hist(np.clip(qcd_df["pt_res"],0,pt_res_high),                  bins=100,range=[0,pt_res_high],density=True,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,0].hist(np.clip(df[df["min_dR"] < 0.05]["pt_Err"],0,0.5),  bins=50,range=[0,.5], density=True,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,0].hist(np.clip(df[df["min_dR"] >= 0.05]["pt_Err"],0,0.5), bins=50,range=[0,.5], density=True,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,0].hist(np.clip(qcd_df["pt_Err"],0,0.5),                   bins=50,range=[0,.5], density=True,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[0,1].hist(np.clip(df[df["min_dR"] < 0.05]["trk_nHits"],0,30),     bins=30,range=[0,30],density=True,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,1].hist(np.clip(df[df["min_dR"] >= 0.05]["trk_nHits"],0,30),    bins=30,range=[0,30],density=True,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,1].hist(np.clip(qcd_df["trk_nHits"],0,30),                      bins=30,range=[0,30],density=True,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,1].hist(np.clip(df[df["min_dR"] < 0.05]["qOverp"],0,0.04),    bins=100,range=[0,.04],density=True,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,1].hist(np.clip(df[df["min_dR"] >= 0.05]["qOverp"],0,0.04),   bins=100,range=[0,.04],density=True,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,1].hist(np.clip(qcd_df["qOverp"],0,0.04),                     bins=100,range=[0,.04],density=True,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  
  ax[0,0].legend()
  ax[1,0].legend()
  ax[0,1].legend()
  ax[1,1].legend()
  fig.tight_layout()
  fig.savefig("Plots/var/matched_distribtuion_trks2_%s_%s_norm.png"%(name,idtype))
  plt.close()

  fig, ax = plt.subplots(2,2)
  fig.suptitle("%s: "%(name)+partType[idtype],y=1.0)
  
  ax[0,0].set_xlabel("trk dz Significance")    
  ax[1,0].set_xlabel("trk PV Quality")    
  ax[0,1].set_xlabel("|dz PV0|")    
  ax[1,1].set_xlabel("dz Error PV0")    
  ax[0,0].set_yscale('log')
  ax[0,1].set_yscale('log')
  ax[1,0].set_yscale('log')
  ax[1,1].set_yscale('log')
  
  ax[0,0].hist(np.clip(df[df["min_dR"] < 0.05]["trk_dzSig"],0,2500)      ,bins=100,range=[0,2500],   density=False, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,0].hist(np.clip(df[df["min_dR"] >= 0.05]["trk_dzSig"],0,2500)     ,bins=100,range=[0,2500],   density=False, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,0].hist(np.clip(qcd_df["trk_dzSig"],0,2500)                       ,bins=100,range=[0,2500],   density=False, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,0].hist(df[df["min_dR"] < 0.05]["trk_PVQuality"]  ,bins=8,range=[0,8],  density=False, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,0].hist(df[df["min_dR"] >= 0.05]["trk_PVQuality"] ,bins=8,range=[0,8],  density=False, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,0].hist(qcd_df["trk_PVQuality"]                  ,bins=8,range=[0,8],  density=False, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[0,1].hist(np.clip(df[df["min_dR"] < 0.05]["trk_dzPV0"],0,10)  ,bins=100,range=[0,10],   density=False, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,1].hist(np.clip(df[df["min_dR"] >= 0.05]["trk_dzPV0"],0,10) ,bins=100,range=[0,10],   density=False, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,1].hist(np.clip(qcd_df["trk_dzPV0"],0,10)                   ,bins=100,range=[0,10],   density=False, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,1].hist(np.clip(df[df["min_dR"] < 0.05]["trk_dzErrorPV0"],0,20)    ,bins=100,range=[0,20],density=False, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,1].hist(np.clip(df[df["min_dR"] >= 0.05]["trk_dzErrorPV0"],0,20)   ,bins=100,range=[0,20],density=False, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,1].hist(np.clip(qcd_df["trk_dzErrorPV0"],0,20)                     ,bins=100,range=[0,20],density=False, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  
  ax[0,0].legend()
  ax[1,0].legend()
  ax[0,1].legend()
  ax[1,1].legend()
  fig.tight_layout()
  fig.savefig("Plots/var/matched_distribtuion_trks3_%s_%s.png"%(name,idtype))
  plt.close()
  fig, ax = plt.subplots(2,2)
  fig.suptitle("%s: "%(name)+partType[idtype],y=1.0)
  
  ax[0,0].set_xlabel("trk dz Significance")    
  ax[1,0].set_xlabel("trk PV Quality")    
  ax[0,1].set_xlabel("|dz PV0|")    
  ax[1,1].set_xlabel("dz Error PV0")    
  
  ax[0,0].hist(np.clip(df[df["min_dR"] < 0.05]["trk_dzSig"],0,1000)      ,bins=100,range=[0,1000],  density=True, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,0].hist(np.clip(df[df["min_dR"] >= 0.05]["trk_dzSig"],0,1000)     ,bins=100,range=[0,1000],  density=True, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,0].hist(np.clip(qcd_df["trk_dzSig"],0,1000)                       ,bins=100,range=[0,1000],  density=True, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,0].hist(df[df["min_dR"] < 0.05]["trk_PVQuality"] ,bins=8,range=[0,8],  density=True, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,0].hist(df[df["min_dR"] >= 0.05]["trk_PVQuality"],bins=8,range=[0,8],  density=True, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,0].hist(qcd_df["trk_PVQuality"]                  ,bins=8,range=[0,8],  density=True, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[0,1].hist(np.clip(df[df["min_dR"] < 0.05]["trk_dzPV0"],0,10) ,bins=100,range=[0,10],       density=True, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,1].hist(np.clip(df[df["min_dR"] >= 0.05]["trk_dzPV0"],0,10),bins=100,range=[0,10],       density=True, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,1].hist(np.clip(qcd_df["trk_dzPV0"],0,10)                  ,bins=100,range=[0,10],       density=True, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,1].hist(np.clip(df[df["min_dR"] < 0.05]["trk_dzErrorPV0"],0,0.2)    ,bins=100,range=[0,0.2],density=True, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,1].hist(np.clip(df[df["min_dR"] >= 0.05]["trk_dzErrorPV0"],0,0.2)   ,bins=100,range=[0,0.2],density=True, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,1].hist(np.clip(qcd_df["trk_dzErrorPV0"],0,0.2)                     ,bins=100,range=[0,0.2],density=True, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  
  ax[0,0].legend()
  ax[1,0].legend()
  ax[0,1].legend()
  ax[1,1].legend()
  fig.tight_layout()
  fig.savefig("Plots/var/matched_distribtuion_trks3_%s_%s_norm.png"%(name,idtype))
  plt.close()


def get_hist(ax):
  n, bins= [],[]
  for rect in ax.patches:
    ((x0,y0), (x1,y1)) = rect.get_bbox().get_points()
    n.append(y1-y0)
    bins.append(x0)
  bins.append(x1)
  return n,bins

def gaussian(x, mean, amplitude, standard_deviation):
    return amplitude * np.exp( - ((x - mean) / standard_deviation) ** 2)

#def closure(df_bkg,var1,binx,var2,biny,sig1000,sig750,sig400,sig300,sig200,SR,gauss,sel1,sel2):
def closure(var1,binx,var2,biny,SR,gauss,sel1,sel2):
  # SR=0: signal region is D. 1: signal region is C
  df_bkg = qcd_df[(qcd_df[var1] > sel1) & (qcd_df[var2] > sel2)]
  sig1000 = df1000[(df1000[var1] > sel1) & (df1000[var2] > sel2)]
  sig750 = df750[(df750[var1] > sel1) & (df750[var2] > sel2)]
  sig400 = df400[(df400[var1] > sel1) & (df400[var2] > sel2)]
  sig300 = df300[(df300[var1] > sel1) & (df300[var2] > sel2)]
  sig200 = df200[(df200[var1] > sel1) & (df200[var2] > sel2)]

  tot_sig10 = sig1000["wgt"].sum()
  tot_sig7 = sig750["wgt"].sum()
  tot_sig4 = sig400["wgt"].sum()
  tot_sig3 = sig300["wgt"].sum()
  tot_sig2 = sig200["wgt"].sum()
  #tot_bkg = df_bkg["wgt"].sum()
  all_closure = []
  dr_close=[]
  print("i j bkgA bkgB bkgC bkgD predicted predicted_err_sys predicted_err_stat sig_1000 eff_1000 signif_1000 sig_750 eff_750 signif_750 sig_400 eff_400 signif_400 sig_300 eff_300 signif_300 sig_200 eff_200 signif_200") 
  for i in binx:
    for j in biny:
      bkgA = df_bkg[(df_bkg[var1] < i) & (df_bkg[var2] < j)]["wgt"].sum()
      bkgB = df_bkg[(df_bkg[var1] < i) & (df_bkg[var2] > j)]["wgt"].sum()
      bkgC = df_bkg[(df_bkg[var1] > i) & (df_bkg[var2] < j)]["wgt"].sum()
      bkgD = df_bkg[(df_bkg[var1] > i) & (df_bkg[var2] > j)]["wgt"].sum()
      if SR:
        sig_1000= sig1000[(sig1000[var1] > i) & (sig1000[var2] > j)]["wgt"].sum()
        sig_750 = sig750[(sig750[var1] > i) & (sig750[var2] > j)]["wgt"].sum()
        sig_400 = sig400[(sig400[var1] > i) & (sig400[var2] > j)]["wgt"].sum()
        sig_300 = sig300[(sig300[var1] > i) & (sig300[var2] > j)]["wgt"].sum()
        sig_200 = sig200[(sig200[var1] > i) & (sig200[var2] > j)]["wgt"].sum()
        bkg = bkgD
        predicted = bkgB*bkgC/bkgA
      else:
        sig_1000= sig1000[(sig1000[var1] > i) & (sig1000[var2] < j)]["wgt"].sum()
        sig_750 = sig750[(sig750[var1] > i) & (sig750[var2] < j)]["wgt"].sum()
        sig_400 = sig400[(sig400[var1] > i) & (sig400[var2] < j)]["wgt"].sum()
        sig_300 = sig300[(sig300[var1] > i) & (sig300[var2] < j)]["wgt"].sum()
        sig_200 = sig200[(sig200[var1] > i) & (sig200[var2] < j)]["wgt"].sum()
        bkg = bkgC
        predicted = bkgA*bkgD/bkgB
      
      predicted_err_sys = predicted * (1/bkgA + 1/bkgB + 1/bkg)**(0.5)
      predicted_err_stat = (predicted)**(0.5)
      signif_10 = sig_1000/(sig_1000+bkg)**(0.5) 
      signif_7 = sig_750/(sig_750+bkg)**(0.5) 
      signif_4 = sig_400/(sig_400+bkg)**(0.5) 
      signif_3 = sig_300/(sig_300+bkg)**(0.5) 
      signif_2 = sig_200/(sig_200+bkg)**(0.5) 

      closure = (predicted-bkg)/predicted
      closed = abs(closure) < 0.5
      all_closure.append(closure)
      #closed = (predicted - predicted_err_sys -predicted_err_stat) + (bkgC + bkgC**(0.5)) < 0
#      if closed:
  #      print("%d %.2f %d %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %d"%(i,j,SR,bkgA,bkgB,bkgC,bkgD,predicted,predicted_err_sys,predicted_err_stat,sig_1000,sig_1000/tot_sig10,signif_10,sig_750,sig_750/tot_sig7,signif_7,sig_400,sig_400/tot_sig4,signif_4,sig_300,sig_300/tot_sig3,signif_3,sig_200,sig_200/tot_sig2,signif_2,closure, closed)) 

      dr_close.append({"i":i, "j":j, "bkgA":bkgA, "bkgB":bkgB, "bkgC":bkgC, "bkgD":bkgD, "predicted":predicted, "predicted_err_sys":predicted_err_sys, "predicted_err_stat":predicted_err_stat, "sig_1000":sig_1000, "eff_1000":sig_1000/tot_sig10, "signif_1000":signif_10, "sig_750":sig_750, "eff_750":sig_750/tot_sig7, "signif_750":signif_7, "sig_400":sig_400, "eff_400":sig_400/tot_sig4, "signif_400":signif_4, "sig_300":sig_300, "eff_300":sig_300/tot_sig3, "signif_300":signif_3, "sig_200":sig_200, "eff_200":sig_200/tot_sig2, "signif_200":signif_2,"closure":closure 
        })
  df_close = pd.DataFrame(dr_close)      

  fig, ax1 = plt.subplots(1,1)
  SR_tit = ["C","D"]
  fig.suptitle("SR %s: %s %s "%(SR_tit[SR],var1,var2),y=1.0)
  ax1.hist(df_close["closure"],bins=100)
  ax1.set_xlabel("closure")
  if gauss:
    bin_heights, bin_borders = get_hist(ax1)
    bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
    popt, _ = curve_fit(gaussian, bin_centers, bin_heights, p0=[0., 10., 1.])
    x_interval_for_fit = np.linspace(bin_borders[0], bin_borders[-1], 10000)
    ax1.plot(x_interval_for_fit, gaussian(x_interval_for_fit, *popt), label='fit')
    ax1.axvline(x=popt[0],linestyle='-',color='red')
    ax1.axvline(x=popt[0]+popt[2],linestyle=':',color='black')
    ax1.axvline(x=popt[0]-popt[2],linestyle=':',color='black')
    ax1.text(0,4,r'$\mu=%.4f$'%popt[0])
    ax1.text(0,3,r'$\sigma=%.4f$'%popt[2])
  fig.tight_layout()
  Path("Plots/closure").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/closure/closure_%s_%s_%s"%(SR,var1,var2))
  plt.close()

  fig, ax2 = plt.subplots(1,1)
  SR_tit = ["C","D"]
  fig.suptitle("SR %s: %s %s "%(SR_tit[SR],var1,var2),y=1.0)
  piv = df_close.pivot("j","i","closure")
  ax2 = sns.heatmap(piv,cmap="seismic",center=0.0)
  ax2.invert_yaxis()
  ax2.set_yticklabels(['{:.2f}'.format(float(t.get_text())) for t in ax2.get_yticklabels()])
  ax2.set_xlabel("%s Cut"%var1)
  ax2.set_ylabel("%s Cut"%var2)

  fig.tight_layout()
  Path("Plots/closure").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/closure/closuremap_%s_%s_%s"%(SR,var1,var2))
  plt.close()

  df_close = df_close[abs(df_close["closure"]) <=0.5]
  df_close_1000 = df_close[df_close["eff_1000"] > 0.85].sort_values(["i","j"],ascending=(True,True)).sort_values(["signif_1000"],ascending=False)
  df_close_1000.to_csv("Plots/closure/optimal_sig1000_%s_%s_%s.txt"%(SR,var1,var2))
  df_close_750 = df_close[df_close["eff_750"] > 0.85].sort_values(["i","j"],ascending=(True,True)).sort_values(["signif_750"],ascending=False)
  df_close_750.to_csv("Plots/closure/optimal_sig750_%s_%s_%s.txt"%(SR,var1,var2))
  df_close_400 = df_close[df_close["eff_400"] > 0.85].sort_values(["i","j"],ascending=(True,True)).sort_values(["signif_400"],ascending=False)
  df_close_400.to_csv("Plots/closure/optimal_sig400_%s_%s_%s.txt"%(SR,var1,var2))
  df_close_300 = df_close[df_close["eff_300"] > 0.85].sort_values(["i","j"],ascending=(True,True)).sort_values(["signif_300"],ascending=False)
  df_close_300.to_csv("Plots/closure/optimal_sig300_%s_%s_%s.txt"%(SR,var1,var2))
  df_close_200 = df_close[df_close["eff_200"] > 0.85].sort_values(["i","j"],ascending=(True,True)).sort_values(["signif_200"],ascending=False)
  df_close_200.to_csv("Plots/closure/optimal_sig200_%s_%s_%s.txt"%(SR,var1,var2))

  for sig in [1000,750,400,300,200]:
    signif = "signif_%s"%sig
    fig, ax3 = plt.subplots(1,1)
    SR_tit = ["C","D"]
    fig.suptitle("SR %s sig%s: %s %s "%(SR_tit[SR],sig,var1,var2),y=1.0)
    piv = df_close[abs(df_close["closure"]) <= 0.5].pivot("j","i",signif)
    ax3 = sns.heatmap(piv,cmap="winter")
    ax3.invert_yaxis()
    ax3.set_yticklabels(['{:.2f}'.format(float(t.get_text())) for t in ax3.get_yticklabels()])
    ax3.set_xlabel("%s Cut"%var1)
    ax3.set_ylabel("%s Cut"%var2)
    fig.tight_layout()
    Path("Plots/signifmap").mkdir(parents=True,exist_ok=True)
    fig.savefig("Plots/signifmap/signifmap_%s_%s_%s_%s"%(SR,sig,var1,var2))
    plt.close()

    sigs = "sig_%s"%sig
    fig, ax4 = plt.subplots(1,1)
    SR_tit = ["C","D"]
    fig.suptitle("SR %s sig%s: %s %s "%(SR_tit[SR],sig,var1,var2),y=1.0)
    piv = df_close[abs(df_close["closure"]) <= 0.5].pivot("j","i",sigs)
    ax4 = sns.heatmap(piv,cmap="winter")
    ax4.invert_yaxis()
    ax4.set_yticklabels(['{:.2f}'.format(float(t.get_text())) for t in ax4.get_yticklabels()])
    ax4.set_xlabel("%s Cut"%var1)
    ax4.set_ylabel("%s Cut"%var2)
    fig.tight_layout()
    Path("Plots/yieldmap").mkdir(parents=True,exist_ok=True)
    fig.savefig("Plots/yieldmap/yieldmap_%s_%s_%s_%s"%(SR,sig,var1,var2))
    plt.close()

  
def get_sig(df_sig,df_bkg,var,binx,reverse=False):
  sig = []
  bkg = []
  tot_sig = df_sig["wgt"].sum()
  tot_bkg = df_bkg["wgt"].sum()
  for i in binx:
    if(reverse):
      sig.append(df_sig[df_sig[var] < i]["wgt"].sum())
      bkg.append(df_bkg[df_bkg[var] < i]["wgt"].sum() + 1e-9)
    else:
      sig.append(df_sig[df_sig[var] > i]["wgt"].sum())
      bkg.append(df_bkg[df_bkg[var] > i]["wgt"].sum() + 1e-9)
  return(sig,tot_sig,bkg,tot_bkg)

#plot_id=0
def make_2d_correlation(df, var1,steps1, var2,steps2):

  fig, (ax1) = plt.subplots(1,1,figsize=(21,7))
  ax1.set_title("")    
  sub_df = df
  h= ax1.hist2d(sub_df[var1],sub_df[var2],bins=[len(steps1)-1,len(steps2)-1],range=[[steps1[0],steps1[-1]],[steps2[0],steps2[-1]]],norm=matplotlib.colors.LogNorm())
  fig.colorbar(h[3], ax=ax1)
  ax1.set_xlabel(var1)
  ax1.set_ylabel(var2)

  fig.tight_layout()
  Path("Plots/2d").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/2d/2d_%s_%s.png"%(var1,var2))
  plt.close()

def make_2d_SR(df, var1,steps1, var2,steps2,qcd,sig,xline,yline):

  fig, (ax1) = plt.subplots(1,1,figsize=(21,7))
  ax1.set_title("sig%s"%sig)    
  sub_df = df
  h1= ax1.hist2d(qcd_df[var1],qcd_df[var2],bins=[len(steps1)-1,len(steps2)-1],range=[[steps1[0],steps1[-1]],[steps2[0],steps2[-1]]],norm=matplotlib.colors.LogNorm(),cmap=matplotlib.cm.spring)
  fig.colorbar(h1[3], ax=ax1)
  h= ax1.hist2d(sub_df[var1],sub_df[var2],bins=[len(steps1)-1,len(steps2)-1],range=[[steps1[0],steps1[-1]],[steps2[0],steps2[-1]]],norm=matplotlib.colors.LogNorm(),cmap=matplotlib.cm.winter)
  fig.colorbar(h[3], ax=ax1)
  ax1.set_xlabel(var1)
  ax1.set_ylabel(var2)
  ax1.axvline(x=xline,linestyle=':',color='black')
  ax1.axhline(y=yline,linestyle=':',color='black')

  fig.tight_layout()
  Path("Plots/2d").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/2d/2dSR_%s_%s_%s.png"%(sig,var1,var2))
  plt.close()

def make_eff_combo(reco_group,qcd_group,signal, var, binx, eta_cuts=0):
  fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(21,7))
  

  fig.suptitle("sig%s"%(signal)) 
 
  colors = ["red","green","orange","blue","black","magenta"]
  sig,tot_sig,bkg1,tot_bkg = get_sig(reco_group,qcd_group,var,binx) 
  bkg2 = np.array(bkg1)
  bkg3 = np.square(0.5*bkg2)
  bkg = np.add(bkg2,bkg3)
  sigr,tot_sigr,bkg1r,tot_bkgr = get_sig(reco_group,qcd_group,var,binx,True) 
  bkg2r = np.array(bkg1r)
  bkg3r = np.square(0.5*bkg2r)
  bkgr = np.add(bkg2r,bkg3r)

  ax1.hist(reco_group[var],  bins=binx,histtype=u'step',density=True,weights=reco_group["wgt"],color="r",linestyle="solid",label="sig")
  ax1.hist(qcd_group[var],   bins=binx,histtype=u'step',density=True,weights=qcd_group["wgt"],color="black",linestyle="dashed",label="qcd")

  ax2.errorbar(binx,sig/(np.sqrt(np.add(sig,bkg))),(sig/(np.sqrt(np.add(sig,bkg))))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(4*np.add(sig,bkg)))),ecolor="r",label="signif",color="r",linestyle="dashdot",errorevery=1)
  ax2.errorbar(binx,sigr/(np.sqrt(np.add(sigr,bkgr))),(sigr/(np.sqrt(np.add(sigr,bkgr))))*np.sqrt(np.add(np.reciprocal(sigr),np.reciprocal(4*np.add(sigr,bkgr)))),ecolor="b",label="signif_reverse",color="b",linestyle="dashdot",errorevery=1)

  ax3.errorbar(binx,np.multiply(bkg1,1./tot_bkg),np.multiply(bkg1,1./tot_bkg)*np.sqrt(np.add(np.reciprocal(bkg1),np.reciprocal(tot_bkg))),ecolor="black",label="bkg_eff",color="black",linestyle="dashed",errorevery=1)
  ax3.errorbar(binx,np.multiply(bkg1r,1./tot_bkgr),np.multiply(bkg1r,1./tot_bkgr)*np.sqrt(np.add(np.reciprocal(bkg1r),np.reciprocal(tot_bkgr))),ecolor="m",label="bkg_eff_reverse",color="m",linestyle="dashed",errorevery=1)
  ax3.errorbar(binx,np.multiply(sig,1./tot_sig),np.multiply(sig,1./tot_sig)*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(tot_sig))),ecolor="r",label="sig_eff",color="r",linestyle="solid",errorevery=1)
  ax3.errorbar(binx,np.multiply(sigr,1./tot_sigr),np.multiply(sigr,1./tot_sigr)*np.sqrt(np.add(np.reciprocal(sigr),np.reciprocal(tot_sigr))),ecolor="b",label="sig_eff_reverse",color="b",linestyle="solid",errorevery=1)

  ax1.set_ylabel("Events")
  ax2.set_ylabel("Significance")
  ax3.set_ylabel("Efficiency")
  ax1.set_xlabel(var)
  ax2.set_xlabel(var)
  ax3.set_xlabel(var)
  #if(signal==1000):
  #  ax2.set_ylim(0,25)
  #if(signal==750):
  #  ax2.set_ylim(0,35)
  #if(signal==400):
  #  ax2.set_ylim(0,50)
  #if(signal==300):
  #  ax2.set_ylim(0,30)
  #if(signal==200):
  #  ax2.set_ylim(0,8)
  ax2.grid()
  ax1.legend()
  ax2.legend()
  ax3.legend()
  ax1.set_yscale('log')
  #ax1.set_xscale('log')
  fig.tight_layout()
  Path("Plots/combo").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/combo/combo_%s_%s.png"%(signal,var))
  plt.close()

#def make_peak_sig(reco_id_list,qcd_id_list,signal, parts,binx,eta_cuts=0):
#  peaks = []
#  peak_errs = []
#  labels = []
#  for reco_id,qcd_id,part in zip(reco_id_list,qcd_id_list,parts):
#    for i in [0,1,2,3,4,5]:
#      if(eta_cuts):
#        #cut = [0.1,.5, 1.5,1.75,2.0,2.5]
#        cut = [2.5,2.4,2.0,1.75,1.5,1.0]
#        reco_id = reco_id[abs(reco_id["eta"]) < cut[i]]
#        qcd_id = qcd_id[abs(qcd_id["eta"]) < cut[i]]
#        lab1 = "|eta|<"
#      else:
#        cut = [0.1,0.5,0.6,.75,1.0,2.0]
#        reco_id = reco_id[reco_id["pt"] > cut[i]]
#        qcd_id = qcd_id[qcd_id["pt"] > cut[i]]
#        lab1 = "pt>"
#      reco_group = reco_id.groupby(['entry']).first()
#      reco_group['nTracks'] = reco_id.groupby(['entry']).size()
#      qcd_group = qcd_id.groupby(['entry']).first()
#      qcd_group['nTracks'] = qcd_id.groupby(['entry']).size()
#      sig,tot_sig,bkg1,tot_bkg = get_sig(reco_group,qcd_group,"nTracks",binx) 
#      bkg2 = np.array(bkg1)
#      bkg3 = np.square(0.5*bkg2)
#      bkg = np.add(bkg2,bkg3)
#      signif = sig/(np.sqrt(np.add(sig,bkg)))
#      signig_err = (sig/(np.sqrt(np.add(sig,bkg))))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(4*np.add(sig,bkg))))
#      peak = max(signif)
#      peak_err = signig_err[np.argmax(signif)]
#      peaks.append(peak)
#      peak_errs.append(peak_err)
#      labels.append("%s: %s%s"%(partType[part],lab1,cut[i]))
#
#  print(peaks)   
#  fig, axs = plt.subplots(1,1)
#  axs.errorbar(peaks,labels,xerr=peak_errs,fmt="o")
#  axs.set_xlabel("Peak Significance")
#  fig.tight_layout()
#  fig.savefig("Plots/peak/peaks_%s_%s.png"%(signal,eta_cuts))
#  plt.close()


# Get IDs
print("making IDs")

def ID_p(df):
  return df[(df["trk_pv"] >=2)]
def ID_pm(df):
  return df[(df["trk_pv"] >=2) & (df["trk_matched"]==1)]
def ID_pm2(df):
  return df[(df["trk_pv"] >=2) & (((df["trk_matched"]==1) & abs(df["eta"] >=1.0)) | abs(df["eta"] < 1.0))]
def ID_pmh(df):
  return df[(df["trk_pv"] >=2) & (df["trk_matched"]==1) & (df["trk_nHits"]>=10)]
def ID_pmht(df):
  return df[(df["trk_pv"] >=2) & (df["trk_matched"]==1) & (df["trk_nHits"]>=10) & (df["pt"] > 1.0)]
def ID_pmt(df):
  return df[(df["trk_pv"] >=2) & (df["trk_matched"]==1) & (df["pt"] > 100.0)]
def ID_t(df):
  return df[(df["pt"] > 100.0)]
def ID_electron(df):
  return df[(abs(df["gen_id"]) == 11)]
def ID_muon(df):
  return df[(abs(df["gen_id"]) == 13)]
def ID_pion(df):
  return df[(abs(df["gen_id"]) == 211)]
def ID_hadron(df):
  return df[(abs(df["gen_id"]) != 211) &(abs(df["gen_id"])>100)]
def ID_barrel(df):
  return df[abs(df["eta"])<1.0]
def ID_endcap(df):
  return df[abs(df["eta"])>=1.0]
def ID_ptRes(df):
  return df[((abs(df["eta"])>=1.0) & (df["pt_res"]< 0.04)) | ((abs(df["eta"])<1.0) & (df["pt_res"]< 0.02))]
def ID_HiptRes(df):
  return df[(df["pt"]<=100) | ((abs(df["eta"])>=1.0) & (df["pt_res"]< 0.04) & (df["pt"]>100)) | ((abs(df["eta"])<1.0) & (df["pt_res"]< 0.02) & (df["pt"]>100))]
def ID_dz(df):
  return df[abs(df["trk_dzPV0"]) < 10]
def ID_dzerr(df):
  return df[abs(df["trk_dzErrorPV0"]) < 0.05]

#qcd_p = ID_p(qcd_df)  
#qcd_pm = ID_pm(qcd_df) 
#qcd_pmh = ID_pmh(qcd_df)  
#qcd_pmht = ID_pmht(qcd_df)  
#qcd_pmt = ID_pmt(qcd_df)  
#qcd_t = ID_t(qcd_df)  
#qcd_pmr = ID_ptRes(qcd_pm)  
#qcd_pmz = ID_dz(qcd_pm)  
#qcd_pz = ID_dz(qcd_p)  
#
#df1000_p     =   ID_p(df1000) 
#df1000_pm   =   ID_pm(df1000) 
#df1000_pmh  =  ID_pmh(df1000) 
#df1000_pmht = ID_pmht(df1000) 
#df1000_pmt  =  ID_pmt(df1000) 
#df1000_pmr  =  ID_ptRes(df1000_pm) 
#df1000_pmz  =  ID_dz(df1000_pm) 
#df1000_pz  =  ID_dz(df1000_p) 
#df1000_t  =  ID_t(df1000) 
#
#df750_p     =   ID_p(df750) 
#df750_pm   =   ID_pm(df750) 
#df750_pmh  =  ID_pmh(df750) 
#df750_pmht = ID_pmht(df750) 
#df750_pmt  =  ID_pmt(df750) 
#df750_t  =  ID_t(df750) 
#df750_pmr  =  ID_ptRes(df750_pm) 
#df750_pmz  =  ID_dz(df750_pm) 
#df750_pz  =  ID_dz(df750_p) 
#
#df400_p     =   ID_p(df400) 
#df400_pm   =   ID_pm(df400) 
#df400_pmh  =  ID_pmh(df400) 
#df400_pmht = ID_pmht(df400) 
#df400_pmt  =  ID_pmt(df400) 
#df400_t  =  ID_t(df400) 
#df400_pmr  =  ID_ptRes(df400_pm) 
#df400_pmz  =  ID_dz(df400_pm) 
#df400_pz  =  ID_dz(df400_p) 
#
#df300_p     =   ID_p(df300) 
#df300_pm   =   ID_pm(df300) 
#df300_pmh  =  ID_pmh(df300) 
#df300_pmht = ID_pmht(df300) 
#df300_pmt  =  ID_pmt(df300) 
#df300_t  =  ID_t(df300) 
#df300_pmr  =  ID_ptRes(df300_pm) 
#df300_pmz  =  ID_dz(df300_pm) 
#df300_pz  =  ID_dz(df300_p) 
#
#df200_p     =   ID_p(df200) 
#df200_pm   =   ID_pm(df200) 
#df200_pmh  =  ID_pmh(df200) 
#df200_pmht = ID_pmht(df200) 
#df200_pmt  =  ID_pmt(df200) 
#df200_t  =  ID_t(df200) 
#df200_pmr  =  ID_ptRes(df200_pm) 
#df200_pmz  =  ID_dz(df200_pm) 
#df200_pz  =  ID_dz(df200_p) 
#
#df1000_barrel = ID_barrel(df1000_pm)
#df750_barrel = ID_barrel(df750_pm)
#df400_barrel = ID_barrel(df400_pm)
#df300_barrel = ID_barrel(df300_pm)
#df200_barrel = ID_barrel(df200_pm)
#qcd_barrel = ID_barrel(qcd_pm)
#df1000_endcap = ID_endcap(df1000_pm)
#df750_endcap = ID_endcap(df750_pm)
#df400_endcap = ID_endcap(df400_pm)
#df300_endcap = ID_endcap(df300_pm)
#df200_endcap = ID_endcap(df200_pm)
#qcd_endcap = ID_endcap(qcd_pm)
#
#df1000_barrelHiPt = ID_barrel(df1000_pmt)
#df750_barrelHiPt = ID_barrel(df750_pmt)
#df400_barrelHiPt = ID_barrel(df400_pmt)
#df300_barrelHiPt = ID_barrel(df300_pmt)
#df200_barrelHiPt = ID_barrel(df200_pmt)
#qcd_barrelHiPt = ID_barrel(qcd_pmt)
#df1000_endcapHiPt = ID_endcap(df1000_pmt)
#df750_endcapHiPt = ID_endcap(df750_pmt)
#df400_endcapHiPt = ID_endcap(df400_pmt)
#df300_endcapHiPt = ID_endcap(df300_pmt)
#df200_endcapHiPt = ID_endcap(df200_pmt)
#qcd_endcapHiPt = ID_endcap(qcd_pmt)
#
##df_mD1_T1_p   =   ID_p(df_mD1_T1)
#df_mD1_T1_pm  =  ID_pm(df_mD1_T1)
#df_mD1_T1_pmr   =   ID_ptRes(df_mD1_T1_pm)
#df_mD1_T1_pmz   =   ID_dz(df_mD1_T1_pm)
##df_mD1_T1_pmq = ID_pmq(df_mD1_T1)
##df_mD1_T2_p   =   ID_p(df_mD1_T2)
#df_mD1_T2_pm  =  ID_pm(df_mD1_T2)
#df_mD1_T2_pmr   =   ID_ptRes(df_mD1_T2_pm)
#df_mD1_T2_pmz   =   ID_dz(df_mD1_T2_pm)
##df_mD1_T2_pmq = ID_pmq(df_mD1_T2)
##df_mD1_T5_p   =   ID_p(df_mD1_T5)
#df_mD1_T5_pm  =  ID_pm(df_mD1_T5)
#df_mD1_T5_pmr   =   ID_ptRes(df_mD1_T5_pm)
#df_mD1_T5_pmz   =   ID_dz(df_mD1_T5_pm)
##df_mD1_T5_pmq = ID_pmq(df_mD1_T5)
##df_mD2_T1_p   =   ID_p(df_mD2_T1)
#df_mD2_T1_pm  =  ID_pm(df_mD2_T1)
#df_mD2_T1_pmr   =   ID_ptRes(df_mD2_T1_pm)
#df_mD2_T1_pmz   =   ID_dz(df_mD2_T1_pm)
##df_mD2_T1_pmq = ID_pmq(df_mD2_T1)
##df_mD2_T5_p   =   ID_p(df_mD2_T5)
#df_mD2_T5_pm  =  ID_pm(df_mD2_T5)
#df_mD2_T5_pmr   =   ID_ptRes(df_mD2_T5_pm)
#df_mD2_T5_pmz   =   ID_dz(df_mD2_T5_pm)
##df_mD2_T5_pmq = ID_pmq(df_mD2_T5)
##df_mD5_T1_p   =   ID_p(df_mD5_T1)
#df_mD5_T1_pm  =  ID_pm(df_mD5_T1)
#df_mD5_T1_pmr   =   ID_ptRes(df_mD5_T1_pm)
#df_mD5_T1_pmz   =   ID_dz(df_mD5_T1_pm)
##df_mD5_T1_pmq = ID_pmq(df_mD5_T1)
##df_mD5_T2_p   =   ID_p(df_mD5_T2)
#df_mD5_T2_pm  =  ID_pm(df_mD5_T2)
#df_mD5_T2_pmr   =   ID_ptRes(df_mD5_T2_pm)
#df_mD5_T2_pmz   =   ID_dz(df_mD5_T2_pm)
##df_mD5_T2_pmq = ID_pmq(df_mD5_T2)
##df_mD5_T5_p   =   ID_p(df_mD5_T5)
#df_mD5_T5_pm  =  ID_pm(df_mD5_T5)
#df_mD5_T5_pmr   =   ID_ptRes(df_mD5_T5_pm)
#df_mD5_T5_pmz   =   ID_dz(df_mD5_T5_pm)
##df_mD5_T5_pmq = ID_pmq(df_mD5_T5)
#
#
#df_mD1_T1_pmrt   =   ID_t(df_mD1_T1_pmr)
#df_mD1_T2_pmrt   =   ID_t(df_mD1_T2_pmr)
#df_mD1_T5_pmrt   =   ID_t(df_mD1_T5_pmr)
#df_mD2_T1_pmrt   =   ID_t(df_mD2_T1_pmr)
#df_mD2_T5_pmrt   =   ID_t(df_mD2_T5_pmr)
#df_mD5_T1_pmrt   =   ID_t(df_mD5_T1_pmr)
#df_mD5_T2_pmrt   =   ID_t(df_mD5_T2_pmr)
#df_mD5_T5_pmrt   =   ID_t(df_mD5_T5_pmr)
#df1000_pmrt = ID_t(df1000_pmr)
#df750_pmrt = ID_t(df750_pmr)
#df400_pmrt = ID_t(df400_pmr)
#df300_pmrt = ID_t(df300_pmr)
#df200_pmrt = ID_t(df200_pmr)
#qcd_pmrt = ID_t(qcd_pmr)
#
#df_mD1_T1_pmrtx   =   ID_HiptRes(df_mD1_T1_pm)
#df_mD1_T2_pmrtx   =   ID_HiptRes(df_mD1_T2_pm)
#df_mD1_T5_pmrtx   =   ID_HiptRes(df_mD1_T5_pm)
#df_mD2_T1_pmrtx   =   ID_HiptRes(df_mD2_T1_pm)
#df_mD2_T5_pmrtx   =   ID_HiptRes(df_mD2_T5_pm)
#df_mD5_T1_pmrtx   =   ID_HiptRes(df_mD5_T1_pm)
#df_mD5_T2_pmrtx   =   ID_HiptRes(df_mD5_T2_pm)
#df_mD5_T5_pmrtx   =   ID_HiptRes(df_mD5_T5_pm)
#df1000_pmrtx = ID_HiptRes(df1000_pm)
#df750_pmrtx = ID_HiptRes(df750_pm)
#df400_pmrtx = ID_HiptRes(df400_pm)
#df300_pmrtx = ID_HiptRes(df300_pm)
#df200_pmrtx = ID_HiptRes(df200_pm)
#qcd_pmrtx = ID_HiptRes(qcd_pm)
#
#qcd_pm2 = ID_pm2(qcd_df) 
#df1000_pm2 = ID_pm2(df1000)
#df750_pm2 = ID_pm2(df750)
#df400_pm2 = ID_pm2(df400)
#df300_pm2 = ID_pm2(df300)
#df200_pm2 = ID_pm2(df200)
#qcd_pm2z  =  ID_dz(qcd_pm2) 
#df1000_pm2z  =  ID_dz(df1000_pm2) 
#df750_pm2z  =  ID_dz(df750_pm2) 
#df400_pm2z  =  ID_dz(df400_pm2) 
#df300_pm2z  =  ID_dz(df300_pm2) 
#df200_pm2z  =  ID_dz(df200_pm2) 
#
#qcd_pm2ze  =  ID_dzerr(qcd_pm2z) 
#df1000_pm2ze  =  ID_dzerr(df1000_pm2z) 
#df750_pm2ze  =  ID_dzerr(df750_pm2z) 
#df400_pm2ze  =  ID_dzerr(df400_pm2z) 
#df300_pm2ze  =  ID_dzerr(df300_pm2z) 
#df200_pm2ze  =  ID_dzerr(df200_pm2z) 
#
#qcd_pze  =  ID_dzerr(qcd_pm2z) 
#df1000_pze  =  ID_dzerr(df1000_pz) 
#df750_pze  =  ID_dzerr(df750_pz) 
#df400_pze  =  ID_dzerr(df400_pz) 
#df300_pze  =  ID_dzerr(df300_pz) 
#df200_pze  =  ID_dzerr(df200_pz) 

pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50,200])
eta_bins = np.array(range(-250,250,25))/100.
phi_bins = np.array(range(-31,31,5))/10.

#processes = []
#processes2 = []
#
#processes.append( mp.Process(target=trk_var, args=(df1000,qcd_df,"sig1000",0)))
#processes.append( mp.Process(target=trk_var, args=(df750,qcd_df,"sig750",0)))
#processes.append( mp.Process(target=trk_var, args=(df400,qcd_df,"sig400",0)))
#processes.append( mp.Process(target=trk_var, args=(df300,qcd_df,"sig300",0)))
#processes.append( mp.Process(target=trk_var, args=(df200,qcd_df,"sig200",0)))
#
#processes.append( mp.Process(target=trk_var, args=(df1000_p,qcd_p,"sig1000",1)))
#processes.append( mp.Process(target=trk_var, args=(df750_p,qcd_p,"sig750",1)))
#processes.append( mp.Process(target=trk_var, args=(df400_p,qcd_p,"sig400",1)))
#processes.append( mp.Process(target=trk_var, args=(df300_p,qcd_p,"sig300",1)))
#processes.append( mp.Process(target=trk_var, args=(df200_p,qcd_p,"sig200",1)))
#
#processes.append( mp.Process(target=trk_var, args=(df1000_pm,qcd_pm,"sig1000",2)))
#processes.append( mp.Process(target=trk_var, args=(df750_pm,qcd_pm,"sig750",2)))
#processes.append( mp.Process(target=trk_var, args=(df400_pm,qcd_pm,"sig400",2)))
#processes.append( mp.Process(target=trk_var, args=(df300_pm,qcd_pm,"sig300",2)))
#processes.append( mp.Process(target=trk_var, args=(df200_pm,qcd_pm,"sig200",2)))
#
#processes2.append( mp.Process(target=trk_var, args=(df1000_pm2,qcd_pm2,"sig1000",9)))
#processes2.append( mp.Process(target=trk_var, args=(df750_pm2,qcd_pm2,"sig750",9)))
#processes2.append( mp.Process(target=trk_var, args=(df400_pm2,qcd_pm2,"sig400",9)))
#processes2.append( mp.Process(target=trk_var, args=(df300_pm2,qcd_pm2,"sig300",9)))
#processes2.append( mp.Process(target=trk_var, args=(df200_pm2,qcd_pm2,"sig200",9)))
#
#processes2.append( mp.Process(target=trk_var, args=(df1000_pm2z,qcd_pm2z,"sig1000",10)))
#processes2.append( mp.Process(target=trk_var, args=(df750_pm2z,qcd_pm2z,"sig750",10)))
#processes2.append( mp.Process(target=trk_var, args=(df400_pm2z,qcd_pm2z,"sig400",10)))
#processes2.append( mp.Process(target=trk_var, args=(df300_pm2z,qcd_pm2z,"sig300",10)))
#processes2.append( mp.Process(target=trk_var, args=(df200_pm2z,qcd_pm2z,"sig200",10)))
#
#processes2.append( mp.Process(target=trk_var, args=(df1000_pm2ze,qcd_pm2ze,"sig1000",11)))
#processes2.append( mp.Process(target=trk_var, args=(df750_pm2ze,qcd_pm2ze,"sig750",11)))
#processes2.append( mp.Process(target=trk_var, args=(df400_pm2ze,qcd_pm2ze,"sig400",11)))
#processes2.append( mp.Process(target=trk_var, args=(df300_pm2ze,qcd_pm2ze,"sig300",11)))
#processes2.append( mp.Process(target=trk_var, args=(df200_pm2ze,qcd_pm2ze,"sig200",11)))


combos = []
#
tau_bins = [0.01*x for x in range(0,100,1)]
rho_bins = [.01*x for x in range(0,250,5)]
#combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000, "t21",tau_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750, "t21",tau_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400, "t21",tau_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300, "t21",tau_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200, "t21",tau_bins)))
#
#combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000, "t32",tau_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750, "t32",tau_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400, "t32",tau_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300, "t32",tau_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200, "t32",tau_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho1",rho_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho1",rho_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho1",rho_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho1",rho_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho1",rho_bins)))
#
#combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho2",rho_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho2",rho_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho2",rho_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho2",rho_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho2",rho_bins)))
#
#combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho0",rho_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho0",rho_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho0",rho_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho0",rho_bins)))
#combos.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho0",rho_bins)))

combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"jetTracks",range(0,300,5))))
combos.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "jetTracks",range(0,300,5))))
combos.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "jetTracks",range(0,300,5))))
combos.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "jetTracks",range(0,300,5))))
combos.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "jetTracks",range(0,300,5))))
#print("nTracks") 
#for p in combos:
#  p.start()
#for p in combos:
#  p.join()
#print("2d plots tau")
#make_2d_correlation(qcd_df, "jetTracks",range(0,500), "t21",tau_bins)
#make_2d_correlation(qcd_df, "jetTracks",range(0,500), "t32",tau_bins)
#print("2d plots rho")
#make_2d_correlation(qcd_df, "jetTracks",range(0,500), "rho1",rho_bins)
#make_2d_correlation(qcd_df, "jetTracks",range(0,500), "rho2",rho_bins)
#make_2d_correlation(qcd_df, "jetTracks",range(0,500), "rho0",rho_bins)

tracksel = 70
tausel= 0.5
rho0sel=0.2
rho1sel=0.2
rho2sel=0.1

SR_taus=[]
SR_taus.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "t21",tau_bins,qcd_df,1000,tracksel,tausel)))
SR_taus.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "t32",tau_bins,qcd_df,1000,tracksel,tausel)))
SR_taus.append(mp.Process(target=make_2d_SR, args=(df750, "jetTracks",range(0,500), "t21",tau_bins,qcd_df,750,tracksel,tausel)))
SR_taus.append(mp.Process(target=make_2d_SR, args=(df750, "jetTracks",range(0,500), "t32",tau_bins,qcd_df,750,tracksel,tausel)))
SR_taus.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "t21",tau_bins,qcd_df,400,tracksel,tausel)))
SR_taus.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "t32",tau_bins,qcd_df,400,tracksel,tausel)))
SR_taus.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "t21",tau_bins,qcd_df,300,tracksel,tausel)))
SR_taus.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "t32",tau_bins,qcd_df,300,tracksel,tausel)))
SR_taus.append(mp.Process(target=make_2d_SR, args=(df200, "jetTracks",range(0,500), "t21",tau_bins,qcd_df,200,tracksel,tausel)))
SR_taus.append(mp.Process(target=make_2d_SR, args=(df200, "jetTracks",range(0,500), "t32",tau_bins,qcd_df,200,tracksel,tausel)))

SR_rhos = []
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho0",rho_bins,qcd_df,1000,tracksel,rho0sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho1",rho_bins,qcd_df,1000,tracksel,rho1sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho2",rho_bins,qcd_df,1000,tracksel,rho2sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df750, "jetTracks",range(0,500), "rho0",rho_bins,qcd_df,750,tracksel,rho0sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df750, "jetTracks",range(0,500), "rho1",rho_bins,qcd_df,750,tracksel,rho1sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df750, "jetTracks",range(0,500), "rho2",rho_bins,qcd_df,750,tracksel,rho2sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "rho0",rho_bins,qcd_df,400,tracksel,rho0sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "rho1",rho_bins,qcd_df,400,tracksel,rho1sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "rho2",rho_bins,qcd_df,400,tracksel,rho2sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "rho0",rho_bins,qcd_df,300,tracksel,rho0sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "rho1",rho_bins,qcd_df,300,tracksel,rho1sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "rho2",rho_bins,qcd_df,300,tracksel,rho2sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df200, "jetTracks",range(0,500), "rho0",rho_bins,qcd_df,200,tracksel,rho0sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df200, "jetTracks",range(0,500), "rho1",rho_bins,qcd_df,200,tracksel,rho1sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df200, "jetTracks",range(0,500), "rho2",rho_bins,qcd_df,200,tracksel,rho2sel)))

taus=[]
taus.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"t21",[0.01*x for x in range(60,100,2)],0,1,tracksel,tausel)))
taus.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"t21",[0.01*x for x in range(60,100,2)],1,1,tracksel,tausel)))
taus.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"t32",[0.01*x for x in range(60,100,2)],0,1,tracksel,tausel)))
taus.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"t32",[0.01*x for x in range(60,100,2)],1,1,tracksel,tausel)))

rhos = []
rhos.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho0",[0.01*x for x in range(50,150,2)],0,0,tracksel,rho0sel)))
rhos.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho0",[0.01*x for x in range(50,150,2)],1,0,tracksel,rho0sel)))
rhos.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho1",[0.01*x for x in range(50,150,2)],0,0,tracksel,rho1sel)))
rhos.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho1",[0.01*x for x in range(50,150,2)],1,0,tracksel,rho1sel)))
rhos.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho2",[0.01*x for x in range(0,100,5)],0,0,tracksel,rho2sel)))
rhos.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho2",[0.01*x for x in range(0,100,5)],1,0,tracksel,rho2sel)))
#print("2d SR tau")
#for p in SR_taus:
#  p.start()
#for p in SR_taus:
#  p.join()
#print("2d SR rho")
#for p in SR_rhos:
#  p.start()
#for p in SR_rhos:
#  p.join()
print("closure tau")
for p in taus:
  p.start()
for p in taus:
  p.join()
print("closure rho")
for p in rhos:
  p.start()
for p in rhos:
  p.join()
