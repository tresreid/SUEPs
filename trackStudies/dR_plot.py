import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib
import pandas as pd
import gc
import multiprocessing as mp
#from pathlib import Path
partType = {0:"all",11:"electron",13:"muon",22:"photon",211:"pion",100:"hadron",1:"pv >= 2",2:"pv >=2; matched==1",3:"pv >= 2; matched==1; nHits >= 10",4:"pv >= 2; matched==1; nHits>=10; pt > 1",5:"pv >= 2; matched==1; pt>100",6:"pt>100",-1:"pv >= 2; matched==1;|eta|<1.0",-2:"pv >= 2; matched==1;|eta|>=1.0",-3:"pv >= 2; matched==1;|eta|<1.0, pt>100",-4:"pv >= 2; matched==1;|eta|>=1.0,pt>100",7:"pv >= 2; matched==1, pt resolution < 0.02(0.04) for |eta|<(>)1.0",
8:"pv >= 2; matched==1;|dz| < 10",9:"pv >=2; matched==1(|eta| >1.0)",10:"pv >= 2; matched==1(|eta|>1.0);|dz| < 10",11:"pv >= 2; matched==1(|eta|>1.0);|dz| < 10; dzErr < 0.05",12:"pv >= 2;|dz| < 10",13:"pv >= 2;|dz| < 10; dzErr < 0.05"}

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
          "min_dR":float(cols[3]),"is_isr":int(cols[6]),"wgt":xsec*lumi/10000,
          "pt":float(cols[7]),"eta":float(cols[8]),"phi":float(cols[9]),
          "trk_pv":int(cols[13]),
          "trk_matched":int(cols[14]),
          "trk_foundHits":int(cols[15]),
          "trk_lostHits":int(cols[16]),
          "trk_chi2":float(cols[17]),
          "trk_nHits":int(cols[18]),
          "trk_nPHits":int(cols[19]),
          "trk_quality":int(cols[20]),
          "gen_id":int(cols[21]),
          "size":int(cols[22]),
          "entry":int(cols[23]),
          "pt_Err":float(cols[24]),
          "qOverp":float(cols[25]),
          "trk_PVQuality":int(cols[26]),
          "trk_dzPV0":abs(float(cols[27])),
          "trk_dzErrorPV0":float(cols[28])
          })
  df = pd.DataFrame(dr)
  del dr
  df["phi"] = df["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
  df["pt_res"] = df["pt_Err"]/df["pt"]
  df["trk_dzSig"] = df["trk_dzPV0"]/df["trk_dzErrorPV0"]
  return df

df_mD1_T1 = openReco("track_mDark1_temp1_v0",5.9)
df_mD1_T2 = openReco("track_mDark1_temp2_v0",5.9)
df_mD1_T5 = openReco("track_mDark1_temp5_v0",5.9)
df_mD2_T1 = openReco("track_mDark2_temp1_v0",5.9)
df_mD2_T5 = openReco("track_mDark2_temp5_v0",5.9)
df_mD5_T1 = openReco("track_mDark5_temp1_v0",5.9)
df_mD5_T2 = openReco("track_mDark5_temp2_v0",5.9)
df_mD5_T5 = openReco("track_mDark5_temp5_v0",5.9)
df1000 = openReco("track_sig_1000_v0",0.17)
df750 = openReco("track_sig_750_v0",0.5)
df400 = openReco("track_sig_400_v0",5.9)
df300 = openReco("track_sig_300_v0",8.9)
df200 = openReco("track_sig_200_v0",13.6)

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
  num_lines = sum(1 for line in open("data/track_qcd_%s_v0.txt"%f1)) 
  f=open("data/track_qcd_%s_v0.txt"%f1)
  print(f1)
  #print(num_lines)
  for line in f.readlines():
    if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
      continue
    line_count = line_count+1
    cols = line.rstrip().split(' ')
    #if int(cols[23]) > 1000:
#    if (line_count > num_lines/100):
#      break
    #print(qcddr)
    qcddr.append({
      "min_dR":float(cols[3]),"is_isr":int(cols[6]),"wgt":xsec*lumi/100000,
      "pt":float(cols[7]),"eta":float(cols[8]),"phi":float(cols[9]),
      "trk_pv":int(cols[13]),
      "trk_matched":int(cols[14]),
      "trk_foundHits":int(cols[15]),
      "trk_lostHits":int(cols[16]),
      "trk_chi2":float(cols[17]),
      "trk_nHits":int(cols[18]),
      "trk_nPHits":int(cols[19]),
      "trk_quality":int(cols[20]),
      "gen_id":int(cols[21]),
      "size":int(cols[22]),
      "entry":int(cols[23]) + 100000*qcdi,
      "pt_Err":float(cols[24]),
      "qOverp":float(cols[25]),
      "trk_PVQuality":int(cols[26]),
      "trk_dzPV0":abs(float(cols[27])),
      "trk_dzErrorPV0":float(cols[28])
      })
  qcdi = qcdi+1
qcd_df = pd.DataFrame(qcddr)
#print(qcd_df)
del qcddr
#print(qcd_df)
qcd_df["phi"] = qcd_df["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
qcd_df["pt_res"] = qcd_df["pt_Err"]/qcd_df["pt"]
qcd_df["trk_dzSig"] = qcd_df["trk_dzPV0"]/qcd_df["trk_dzErrorPV0"]
#gc.collect()
################GEN INFO
print("opening gen")

def openGen(name,xsec):
  with open('data/%s.txt'%name) as f:
      #xsec = 0.17
      gen = []
      for line in f.readlines():
        if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
          continue
        cols = line.rstrip().split(' ')
        gen.append({
          "wgt":xsec*lumi/10000,
          "pt":float(cols[0]),"eta":float(cols[1]),"phi":float(cols[2]),"gen_id":int(cols[3]),"is_isr":int(cols[4]),
          "suep_size":int(cols[5]), "isr_size":int(cols[6]),"entry":int(cols[7])
          })
  gen_df = pd.DataFrame(gen)
  del gen
  gen_df["phi"] = gen_df["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
  return gen_df

gen_df_mD1_T1 = openGen("gentrack_mDark1_temp1_v0",5.9)
gen_df_mD1_T2 = openGen("gentrack_mDark1_temp2_v0",5.9)
gen_df_mD1_T5 = openGen("gentrack_mDark1_temp5_v0",5.9)
gen_df_mD2_T1 = openGen("gentrack_mDark2_temp1_v0",5.9)
gen_df_mD2_T5 = openGen("gentrack_mDark2_temp5_v0",5.9)
gen_df_mD5_T1 = openGen("gentrack_mDark5_temp1_v0",5.9)
gen_df_mD5_T2 = openGen("gentrack_mDark5_temp2_v0",5.9)
gen_df_mD5_T5 = openGen("gentrack_mDark5_temp5_v0",5.9)
gen_df1000 = openGen("gentrack_sig_1000_v0",0.17)
gen_df750 = openGen("gentrack_sig_750_v0",0.5)
gen_df400 = openGen("gentrack_sig_400_v0",5.9)
gen_df300 = openGen("gentrack_sig_300_v0",8.9)
gen_df200 = openGen("gentrack_sig_200_v0",13.6)

gc.collect()
          
#xsecs = [311900,29070,5962,1207,119.9,25.24] # signal xsec are (125,34.8), (400,5.9), (750,0.5), (1000,0.17)
#files = [300,500,700,1000,1500,2000]
xsecs = [5962,1207,119.9,25.24] # signal xsec are (125,34.8), (400,5.9), (750,0.5), (1000,0.17)
files = [700,1000,1500,2000]
qcdgen =[]
qcdj=0
for xsec,f1 in zip(xsecs,files):
#with open('data/track_qcd_1000_v0.txt') as f:
  f=open("data/gentrack_qcd_%s_v0.txt"%f1)
  for line in f.readlines():
    if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
      continue
    cols = line.rstrip().split(' ')
    qcdgen.append({
        "wgt":xsec*lumi/100000,
        "pt":float(cols[0]),"eta":float(cols[1]),"phi":float(cols[2]),"gen_id":int(cols[3]),"is_isr":int(cols[4]),
        "suep_size":int(cols[5]), "isr_size":int(cols[6]),"entry":int(cols[7]) + 100000*qcdj
      })
  qcdj= qcdj+1
gen_qcddf = pd.DataFrame(qcdgen)
del qcdgen
gc.collect()
print("panda")
gen_qcddf["phi"] = gen_qcddf["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)



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

def make_eff(df,dfID,gen_df,var,bins,idtype,sample):
  print("running %s eff"%var)
  
  all_group = df.groupby(pd.cut(df[var],bins))["wgt"].sum().to_numpy()
  reco_group = df[(df["min_dR"] < 0.05)].groupby(pd.cut(df[(df["min_dR"] < 0.05)][var],bins))["wgt"].sum().to_numpy()
  fake_group = df[(df["min_dR"] >= 0.05)].groupby(pd.cut(df[(df["min_dR"] >= 0.05)][var],bins))["wgt"].sum().to_numpy()
  ID_group = dfID[(dfID["min_dR"] < 0.05)].groupby(pd.cut(dfID[(dfID["min_dR"] < 0.05)][var],bins))["wgt"].sum().to_numpy()
  fakeID_group = dfID[(dfID["min_dR"] >= 0.05)].groupby(pd.cut(dfID[(dfID["min_dR"] >= 0.05)][var],bins))["wgt"].sum().to_numpy()
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
  fig.suptitle("%s: "%(sample)+partType[idtype])
  ax[0].set_ylabel("events")    
  ax[1].set_ylabel("efficiency")    
  if "pt" in var:
    ax[0].set_yscale('log')
    ax[0].set_xscale('log')
    ax[1].set_xscale('log')
  
  ax[0].hist(df[(df["min_dR"] < 0.05)][var], bins=bins,histtype=u'step',weights=df[(df["min_dR"] < 0.05)]["wgt"],color="blue",label="matched")
  ax[0].hist(df[(df["min_dR"] >= 0.05)][var],bins=bins,histtype=u'step',weights=df[(df["min_dR"] >= 0.05)]["wgt"],color="red",label="!matched")
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
  fig.savefig("Plots/eff/efficiency_%s_%s_%sv1.png"%(var,idtype,sample))
  plt.close()

  fig, ax = plt.subplots(2,sharex=True)
  fig.suptitle("%s: "%(sample)+partType[idtype])
  ax[0].set_ylabel("events")    
  ax[1].set_ylabel("efficiency")    
  if "pt" in var:
    ax[0].set_yscale('log')
    ax[0].set_xscale('log')
    ax[1].set_xscale('log')
  
  ax[0].hist(dfID[(dfID["min_dR"] < 0.05)][var], bins=bins,histtype=u'step',weights=dfID[(dfID["min_dR"] < 0.05)]["wgt"],color="green",label="matched+ID")
  ax[0].hist(dfID[(dfID["min_dR"] >= 0.05)][var], bins=bins,histtype=u'step',weights=dfID[(dfID["min_dR"] >= 0.05)]["wgt"],color="cyan",label="!matched+ID")
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
  fig.savefig("Plots/eff/efficiency_%s_%s_%sv2.png"%(var,idtype,sample))
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

#plot_id=0
def make_2d_correlation(df, var1,steps1, var2,steps2):

  fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(21,7))
  ax1.set_title("All Reco Tracks")    
  sub_df = df
  h= ax1.hist2d(sub_df[var1],sub_df[var2],bins=[len(steps1)-1,len(steps2)-1],range=[[steps1[0],steps1[-1]],[steps2[0],steps2[-1]]],norm=matplotlib.colors.LogNorm())
  fig.colorbar(h[3], ax=ax1)
  ax1.set_xlabel(var1)
  ax1.set_ylabel(var2)

  ax2.set_title("True Tracks")    
  sub_df = df[df["min_dR"]< 0.05]
  h= ax2.hist2d(sub_df[var1],sub_df[var2],bins=[len(steps1)-1,len(steps2)-1],range=[[steps1[0],steps1[-1]],[steps2[0],steps2[-1]]],norm=matplotlib.colors.LogNorm())
  fig.colorbar(h[3], ax=ax2)
  ax2.set_xlabel(var1)
  ax2.set_ylabel(var2)

  ax3.set_title("Fake Tracks")    
  sub_df = df[df["min_dR"] >= 0.05]
  h= ax3.hist2d(sub_df[var1],sub_df[var2],bins=[len(steps1)-1,len(steps2)-1],range=[[steps1[0],steps1[-1]],[steps2[0],steps2[-1]]],norm=matplotlib.colors.LogNorm())
  fig.colorbar(h[3], ax=ax3)
  ax3.set_xlabel(var1)
  ax3.set_ylabel(var2)

  fig.tight_layout()
  fig.savefig("Plots/2d/2d_%s_%s.png"%(var1,var2))
  plt.close()

def pfMatched(df,qcd,sig,title):
  pf_true = df[(df["trk_matched"]==1) & (df["min_dR"] < 0.05)]
  nopf_true = df[(df["trk_matched"]==0) & (df["min_dR"] < 0.05)]
  pf_fake = df[(df["trk_matched"]==1) & (df["min_dR"] >= 0.05)]
  nopf_fake = df[(df["trk_matched"]==0) & (df["min_dR"] >= 0.05)]
  qcdpf = qcd[qcd["trk_matched"]==1]
  qcdnopf = qcd[qcd["trk_matched"]==0]

  for norm in [0,1]:
    fig, ax = plt.subplots(1,1)
    fig.suptitle("%s: %s"%(sig,partType[title]))
    ax.set_ylabel("Events")
    ax.set_xlabel("pT")
    ax.set_yscale('log')
    ax.hist(qcdpf["pt"],  bins=100,histtype=u'step',range=[0,100],density=norm,  weights=qcdpf["wgt"],color="black",linestyle="dashed", label="qcd pfMatched")
    ax.hist(qcdnopf["pt"],bins=100,histtype=u'step',range=[0,100],density=norm,weights=qcdnopf["wgt"],color="orange",linestyle="dashed",label="qcd !pfMatched")
    ax.legend()
    fig.tight_layout()
    fig.savefig("Plots/PFMatched/pfMatchedDist_%s_pt_qcd_%s_%s.png"%(sig,title,norm))
    plt.close()
    fig, ax = plt.subplots(1,1)
    fig.suptitle("%s: %s"%(sig,partType[title]))
    ax.set_ylabel("Events")
    ax.set_xlabel("pT")
    ax.set_yscale('log')
    ax.hist(pf_true["pt"],  bins=100,histtype=u'step',range=[0,100],density=norm,  weights=pf_true["wgt"],color="green",linestyle="solid", label="pfMatched True")
    ax.hist(nopf_true["pt"],bins=100,histtype=u'step',range=[0,100],density=norm,weights=nopf_true["wgt"],color="blue",linestyle="solid",label="!pfMatched True")
    ax.hist(pf_fake["pt"],  bins=100,histtype=u'step',range=[0,100],density=norm,  weights=pf_fake["wgt"],color="magenta",linestyle="solid", label="pfMatched Fake")
    ax.hist(nopf_fake["pt"],bins=100,histtype=u'step',range=[0,100],density=norm,weights=nopf_fake["wgt"],color="r",linestyle="solid",label="!pfMatched Fake")
    ax.legend()
    fig.tight_layout()
    fig.savefig("Plots/PFMatched/pfMatchedDist_%s_pt_sig_%s_%s.png"%(sig,title,norm))
    plt.close()

    fig, ax = plt.subplots(1,1)
    fig.suptitle("%s: %s"%(sig,partType[title]))
    ax.set_ylabel("Events")
    ax.set_xlabel("pT")
    ax.set_yscale('log')
    ax.hist(pf_true["pt"],  bins=100,histtype=u'step',range=[0,100],density=norm,  weights=pf_true["wgt"],color="green",linestyle="solid", label="pfMatched True")
    ax.hist(nopf_true["pt"],bins=100,histtype=u'step',range=[0,100],density=norm,weights=nopf_true["wgt"],color="blue",linestyle="solid",label="!pfMatched True")
    ax.hist(pf_fake["pt"],  bins=100,histtype=u'step',range=[0,100],density=norm,  weights=pf_fake["wgt"],color="magenta",linestyle="solid", label="pfMatched Fake")
    ax.hist(nopf_fake["pt"],bins=100,histtype=u'step',range=[0,100],density=norm,weights=nopf_fake["wgt"],color="r",linestyle="solid",label="!pfMatched Fake")
    ax.hist(qcdpf["pt"],  bins=100,histtype=u'step',range=[0,100],density=norm,      weights=qcdpf["wgt"],color="black",linestyle="dashed", label="qcd pfMatched")
    ax.hist(qcdnopf["pt"],bins=100,histtype=u'step',range=[0,100],density=norm,    weights=qcdnopf["wgt"],color="orange",linestyle="dashed",label="qcd !pfMatched")
    ax.legend()
    fig.tight_layout()
    fig.savefig("Plots/PFMatched/pfMatchedDist_%s_pt_%s_%s.png"%(sig,title,norm))
    plt.close()

    fig, ax = plt.subplots(1,1)
    fig.suptitle("%s: %s"%(sig,partType[title]))
    ax.set_ylabel("Events")
    ax.set_xlabel("eta")
    ax.set_yscale('log')
    ax.hist(pf_true["eta"],  bins=100,histtype=u'step',range=[-2.5,2.5],density=norm,  weights=pf_true["wgt"],color="green",linestyle="solid", label="pfMatched True")
    ax.hist(nopf_true["eta"],bins=100,histtype=u'step',range=[-2.5,2.5],density=norm,weights=nopf_true["wgt"],color="blue",linestyle="solid",label="!pfMatched True")
    ax.hist(pf_fake["eta"],  bins=100,histtype=u'step',range=[-2.5,2.5],density=norm,  weights=pf_fake["wgt"],color="magenta",linestyle="solid", label="pfMatched Fake")
    ax.hist(nopf_fake["eta"],bins=100,histtype=u'step',range=[-2.5,2.5],density=norm,weights=nopf_fake["wgt"],color="r",linestyle="solid",label="!pfMatched Fake")
    ax.hist(qcdpf["eta"],  bins=100,histtype=u'step',  range=[-2.5,2.5],density=norm,    weights=qcdpf["wgt"],color="black",linestyle="dashed", label="qcd pfMatched")
    ax.hist(qcdnopf["eta"],bins=100,histtype=u'step',  range=[-2.5,2.5],density=norm,  weights=qcdnopf["wgt"],color="orange",linestyle="dashed",label="qcd !pfMatched")
    ax.legend()
    fig.tight_layout()
    fig.savefig("Plots/PFMatched/pfMatchedDist_%s_eta_%s_%s.png"%(sig,title,norm))
    plt.close()


def make_eff_combo(reco_id,qcd_id,signal, part, binx, eta_cuts=0):
  fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(21,7))
  

  fig.suptitle("sig%s: %s"%(signal,partType[part])) 
 
  colors = ["red","green","orange","blue","black","magenta"]
  for i in [0,1,2,3,4,5]:
    if(eta_cuts):
      cut = [2.5,2.4,2.0,1.75,1.5,1.0]
      reco_id = reco_id[abs(reco_id["eta"]) < cut[i]]
      qcd_id = qcd_id[abs(qcd_id["eta"]) < cut[i]]
      lab1 = "|eta|<"
    else:
      cut = [0.1,0.5,0.6,.75,1.0,2.0]
      reco_id = reco_id[reco_id["pt"] > cut[i]]
      qcd_id = qcd_id[qcd_id["pt"] > cut[i]]
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
  fig.savefig("Plots/nTracks/nTracks_%s_%s_%s.png"%(signal,part,eta_cuts))
  plt.close()

def make_peak_sig(reco_id_list,qcd_id_list,signal, parts,binx,eta_cuts=0):
  peaks = []
  peak_errs = []
  labels = []
  for reco_id,qcd_id,part in zip(reco_id_list,qcd_id_list,parts):
    for i in [0,1,2,3,4,5]:
      if(eta_cuts):
        #cut = [0.1,.5, 1.5,1.75,2.0,2.5]
        cut = [2.5,2.4,2.0,1.75,1.5,1.0]
        reco_id = reco_id[abs(reco_id["eta"]) < cut[i]]
        qcd_id = qcd_id[abs(qcd_id["eta"]) < cut[i]]
        lab1 = "|eta|<"
      else:
        cut = [0.1,0.5,0.6,.75,1.0,2.0]
        reco_id = reco_id[reco_id["pt"] > cut[i]]
        qcd_id = qcd_id[qcd_id["pt"] > cut[i]]
        lab1 = "pt>"
      reco_group = reco_id.groupby(['entry']).first()
      reco_group['nTracks'] = reco_id.groupby(['entry']).size()
      qcd_group = qcd_id.groupby(['entry']).first()
      qcd_group['nTracks'] = qcd_id.groupby(['entry']).size()
      sig,tot_sig,bkg1,tot_bkg = get_sig(reco_group,qcd_group,"nTracks",binx) 
      bkg2 = np.array(bkg1)
      bkg3 = np.square(0.5*bkg2)
      bkg = np.add(bkg2,bkg3)
      signif = sig/(np.sqrt(np.add(sig,bkg)))
      signig_err = (sig/(np.sqrt(np.add(sig,bkg))))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(4*np.add(sig,bkg))))
      peak = max(signif)
      peak_err = signig_err[np.argmax(signif)]
      peaks.append(peak)
      peak_errs.append(peak_err)
      labels.append("%s: %s%s"%(partType[part],lab1,cut[i]))

  print(peaks)   
  fig, axs = plt.subplots(1,1)
  axs.errorbar(peaks,labels,xerr=peak_errs,fmt="o")
  axs.set_xlabel("Peak Significance")
  fig.tight_layout()
  fig.savefig("Plots/peak/peaks_%s_%s.png"%(signal,eta_cuts))
  plt.close()


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

qcd_p = ID_p(qcd_df)  
qcd_pm = ID_pm(qcd_df) 
qcd_pmh = ID_pmh(qcd_df)  
qcd_pmht = ID_pmht(qcd_df)  
qcd_pmt = ID_pmt(qcd_df)  
qcd_t = ID_t(qcd_df)  
qcd_pmr = ID_ptRes(qcd_pm)  
qcd_pmz = ID_dz(qcd_pm)  
qcd_pz = ID_dz(qcd_p)  

df1000_p     =   ID_p(df1000) 
df1000_pm   =   ID_pm(df1000) 
df1000_pmh  =  ID_pmh(df1000) 
df1000_pmht = ID_pmht(df1000) 
df1000_pmt  =  ID_pmt(df1000) 
df1000_pmr  =  ID_ptRes(df1000_pm) 
df1000_pmz  =  ID_dz(df1000_pm) 
df1000_pz  =  ID_dz(df1000_p) 
df1000_t  =  ID_t(df1000) 

df750_p     =   ID_p(df750) 
df750_pm   =   ID_pm(df750) 
df750_pmh  =  ID_pmh(df750) 
df750_pmht = ID_pmht(df750) 
df750_pmt  =  ID_pmt(df750) 
df750_t  =  ID_t(df750) 
df750_pmr  =  ID_ptRes(df750_pm) 
df750_pmz  =  ID_dz(df750_pm) 
df750_pz  =  ID_dz(df750_p) 

df400_p     =   ID_p(df400) 
df400_pm   =   ID_pm(df400) 
df400_pmh  =  ID_pmh(df400) 
df400_pmht = ID_pmht(df400) 
df400_pmt  =  ID_pmt(df400) 
df400_t  =  ID_t(df400) 
df400_pmr  =  ID_ptRes(df400_pm) 
df400_pmz  =  ID_dz(df400_pm) 
df400_pz  =  ID_dz(df400_p) 

df300_p     =   ID_p(df300) 
df300_pm   =   ID_pm(df300) 
df300_pmh  =  ID_pmh(df300) 
df300_pmht = ID_pmht(df300) 
df300_pmt  =  ID_pmt(df300) 
df300_t  =  ID_t(df300) 
df300_pmr  =  ID_ptRes(df300_pm) 
df300_pmz  =  ID_dz(df300_pm) 
df300_pz  =  ID_dz(df300_p) 

df200_p     =   ID_p(df200) 
df200_pm   =   ID_pm(df200) 
df200_pmh  =  ID_pmh(df200) 
df200_pmht = ID_pmht(df200) 
df200_pmt  =  ID_pmt(df200) 
df200_t  =  ID_t(df200) 
df200_pmr  =  ID_ptRes(df200_pm) 
df200_pmz  =  ID_dz(df200_pm) 
df200_pz  =  ID_dz(df200_p) 

df1000_barrel = ID_barrel(df1000_pm)
df750_barrel = ID_barrel(df750_pm)
df400_barrel = ID_barrel(df400_pm)
df300_barrel = ID_barrel(df300_pm)
df200_barrel = ID_barrel(df200_pm)
qcd_barrel = ID_barrel(qcd_pm)
df1000_endcap = ID_endcap(df1000_pm)
df750_endcap = ID_endcap(df750_pm)
df400_endcap = ID_endcap(df400_pm)
df300_endcap = ID_endcap(df300_pm)
df200_endcap = ID_endcap(df200_pm)
qcd_endcap = ID_endcap(qcd_pm)

df1000_barrelHiPt = ID_barrel(df1000_pmt)
df750_barrelHiPt = ID_barrel(df750_pmt)
df400_barrelHiPt = ID_barrel(df400_pmt)
df300_barrelHiPt = ID_barrel(df300_pmt)
df200_barrelHiPt = ID_barrel(df200_pmt)
qcd_barrelHiPt = ID_barrel(qcd_pmt)
df1000_endcapHiPt = ID_endcap(df1000_pmt)
df750_endcapHiPt = ID_endcap(df750_pmt)
df400_endcapHiPt = ID_endcap(df400_pmt)
df300_endcapHiPt = ID_endcap(df300_pmt)
df200_endcapHiPt = ID_endcap(df200_pmt)
qcd_endcapHiPt = ID_endcap(qcd_pmt)

#df_mD1_T1_p   =   ID_p(df_mD1_T1)
df_mD1_T1_pm  =  ID_pm(df_mD1_T1)
df_mD1_T1_pmr   =   ID_ptRes(df_mD1_T1_pm)
df_mD1_T1_pmz   =   ID_dz(df_mD1_T1_pm)
#df_mD1_T1_pmq = ID_pmq(df_mD1_T1)
#df_mD1_T2_p   =   ID_p(df_mD1_T2)
df_mD1_T2_pm  =  ID_pm(df_mD1_T2)
df_mD1_T2_pmr   =   ID_ptRes(df_mD1_T2_pm)
df_mD1_T2_pmz   =   ID_dz(df_mD1_T2_pm)
#df_mD1_T2_pmq = ID_pmq(df_mD1_T2)
#df_mD1_T5_p   =   ID_p(df_mD1_T5)
df_mD1_T5_pm  =  ID_pm(df_mD1_T5)
df_mD1_T5_pmr   =   ID_ptRes(df_mD1_T5_pm)
df_mD1_T5_pmz   =   ID_dz(df_mD1_T5_pm)
#df_mD1_T5_pmq = ID_pmq(df_mD1_T5)
#df_mD2_T1_p   =   ID_p(df_mD2_T1)
df_mD2_T1_pm  =  ID_pm(df_mD2_T1)
df_mD2_T1_pmr   =   ID_ptRes(df_mD2_T1_pm)
df_mD2_T1_pmz   =   ID_dz(df_mD2_T1_pm)
#df_mD2_T1_pmq = ID_pmq(df_mD2_T1)
#df_mD2_T5_p   =   ID_p(df_mD2_T5)
df_mD2_T5_pm  =  ID_pm(df_mD2_T5)
df_mD2_T5_pmr   =   ID_ptRes(df_mD2_T5_pm)
df_mD2_T5_pmz   =   ID_dz(df_mD2_T5_pm)
#df_mD2_T5_pmq = ID_pmq(df_mD2_T5)
#df_mD5_T1_p   =   ID_p(df_mD5_T1)
df_mD5_T1_pm  =  ID_pm(df_mD5_T1)
df_mD5_T1_pmr   =   ID_ptRes(df_mD5_T1_pm)
df_mD5_T1_pmz   =   ID_dz(df_mD5_T1_pm)
#df_mD5_T1_pmq = ID_pmq(df_mD5_T1)
#df_mD5_T2_p   =   ID_p(df_mD5_T2)
df_mD5_T2_pm  =  ID_pm(df_mD5_T2)
df_mD5_T2_pmr   =   ID_ptRes(df_mD5_T2_pm)
df_mD5_T2_pmz   =   ID_dz(df_mD5_T2_pm)
#df_mD5_T2_pmq = ID_pmq(df_mD5_T2)
#df_mD5_T5_p   =   ID_p(df_mD5_T5)
df_mD5_T5_pm  =  ID_pm(df_mD5_T5)
df_mD5_T5_pmr   =   ID_ptRes(df_mD5_T5_pm)
df_mD5_T5_pmz   =   ID_dz(df_mD5_T5_pm)
#df_mD5_T5_pmq = ID_pmq(df_mD5_T5)


df_mD1_T1_pmrt   =   ID_t(df_mD1_T1_pmr)
df_mD1_T2_pmrt   =   ID_t(df_mD1_T2_pmr)
df_mD1_T5_pmrt   =   ID_t(df_mD1_T5_pmr)
df_mD2_T1_pmrt   =   ID_t(df_mD2_T1_pmr)
df_mD2_T5_pmrt   =   ID_t(df_mD2_T5_pmr)
df_mD5_T1_pmrt   =   ID_t(df_mD5_T1_pmr)
df_mD5_T2_pmrt   =   ID_t(df_mD5_T2_pmr)
df_mD5_T5_pmrt   =   ID_t(df_mD5_T5_pmr)
df1000_pmrt = ID_t(df1000_pmr)
df750_pmrt = ID_t(df750_pmr)
df400_pmrt = ID_t(df400_pmr)
df300_pmrt = ID_t(df300_pmr)
df200_pmrt = ID_t(df200_pmr)
qcd_pmrt = ID_t(qcd_pmr)

df_mD1_T1_pmrtx   =   ID_HiptRes(df_mD1_T1_pm)
df_mD1_T2_pmrtx   =   ID_HiptRes(df_mD1_T2_pm)
df_mD1_T5_pmrtx   =   ID_HiptRes(df_mD1_T5_pm)
df_mD2_T1_pmrtx   =   ID_HiptRes(df_mD2_T1_pm)
df_mD2_T5_pmrtx   =   ID_HiptRes(df_mD2_T5_pm)
df_mD5_T1_pmrtx   =   ID_HiptRes(df_mD5_T1_pm)
df_mD5_T2_pmrtx   =   ID_HiptRes(df_mD5_T2_pm)
df_mD5_T5_pmrtx   =   ID_HiptRes(df_mD5_T5_pm)
df1000_pmrtx = ID_HiptRes(df1000_pm)
df750_pmrtx = ID_HiptRes(df750_pm)
df400_pmrtx = ID_HiptRes(df400_pm)
df300_pmrtx = ID_HiptRes(df300_pm)
df200_pmrtx = ID_HiptRes(df200_pm)
qcd_pmrtx = ID_HiptRes(qcd_pm)

qcd_pm2 = ID_pm2(qcd_df) 
df1000_pm2 = ID_pm2(df1000)
df750_pm2 = ID_pm2(df750)
df400_pm2 = ID_pm2(df400)
df300_pm2 = ID_pm2(df300)
df200_pm2 = ID_pm2(df200)
qcd_pm2z  =  ID_dz(qcd_pm2) 
df1000_pm2z  =  ID_dz(df1000_pm2) 
df750_pm2z  =  ID_dz(df750_pm2) 
df400_pm2z  =  ID_dz(df400_pm2) 
df300_pm2z  =  ID_dz(df300_pm2) 
df200_pm2z  =  ID_dz(df200_pm2) 

qcd_pm2ze  =  ID_dzerr(qcd_pm2z) 
df1000_pm2ze  =  ID_dzerr(df1000_pm2z) 
df750_pm2ze  =  ID_dzerr(df750_pm2z) 
df400_pm2ze  =  ID_dzerr(df400_pm2z) 
df300_pm2ze  =  ID_dzerr(df300_pm2z) 
df200_pm2ze  =  ID_dzerr(df200_pm2z) 

qcd_pze  =  ID_dzerr(qcd_pm2z) 
df1000_pze  =  ID_dzerr(df1000_pz) 
df750_pze  =  ID_dzerr(df750_pz) 
df400_pze  =  ID_dzerr(df400_pz) 
df300_pze  =  ID_dzerr(df300_pz) 
df200_pze  =  ID_dzerr(df200_pz) 

pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50,200])
eta_bins = np.array(range(-250,250,25))/100.
phi_bins = np.array(range(-31,31,5))/10.

ideffs1 = []
ideffs2 = []
ideffs3 = []
ideffs4 = []
ideffs5 = []
ideffs1.append(mp.Process(target=make_eff, args=(df1000,df1000_p,gen_df1000[gen_df1000["pt"]>0.5],"pt",pt_bins,1,"sig1000")))
ideffs1.append(mp.Process(target=make_eff, args=(df1000,df1000_p,gen_df1000[gen_df1000["pt"]>0.5],"eta",eta_bins,1,"sig1000")))
ideffs1.append(mp.Process(target=make_eff, args=(df1000,df1000_p,gen_df1000[gen_df1000["pt"]>0.5],"phi",phi_bins,1,"sig1000")))
ideffs1.append(mp.Process(target=make_eff, args=(df750,df750_p,gen_df750[gen_df750["pt"]>0.5],"pt",pt_bins,1,"sig750")))
ideffs1.append(mp.Process(target=make_eff, args=(df750,df750_p,gen_df750[gen_df750["pt"]>0.5],"eta",eta_bins,1,"sig750")))
ideffs1.append(mp.Process(target=make_eff, args=(df750,df750_p,gen_df750[gen_df750["pt"]>0.5],"phi",phi_bins,1,"sig750")))
ideffs1.append(mp.Process(target=make_eff, args=(df400,df400_p,gen_df400[gen_df400["pt"]>0.5],"pt",pt_bins,1,"sig400")))
ideffs1.append(mp.Process(target=make_eff, args=(df400,df400_p,gen_df400[gen_df400["pt"]>0.5],"eta",eta_bins,1,"sig400")))
ideffs1.append(mp.Process(target=make_eff, args=(df400,df400_p,gen_df400[gen_df400["pt"]>0.5],"phi",phi_bins,1,"sig400")))
ideffs1.append(mp.Process(target=make_eff, args=(df300,df300_p,gen_df300[gen_df300["pt"]>0.5],"pt",pt_bins,1,"sig300")))
ideffs1.append(mp.Process(target=make_eff, args=(df300,df300_p,gen_df300[gen_df300["pt"]>0.5],"eta",eta_bins,1,"sig300")))
ideffs1.append(mp.Process(target=make_eff, args=(df300,df300_p,gen_df300[gen_df300["pt"]>0.5],"phi",phi_bins,1,"sig300")))
ideffs1.append(mp.Process(target=make_eff, args=(df200,df200_p,gen_df200[gen_df200["pt"]>0.5],"pt",pt_bins,1,"sig200")))
ideffs1.append(mp.Process(target=make_eff, args=(df200,df200_p,gen_df200[gen_df200["pt"]>0.5],"eta",eta_bins,1,"sig200")))
ideffs1.append(mp.Process(target=make_eff, args=(df200,df200_p,gen_df200[gen_df200["pt"]>0.5],"phi",phi_bins,1,"sig200")))

ideffs2.append(mp.Process(target=make_eff, args=(df1000,df1000_pm,gen_df1000[gen_df1000["pt"]>0.5],"pt",pt_bins,2,"sig1000")))
ideffs2.append(mp.Process(target=make_eff, args=(df1000,df1000_pm,gen_df1000[gen_df1000["pt"]>0.5],"eta",eta_bins,2,"sig1000")))
ideffs2.append(mp.Process(target=make_eff, args=(df1000,df1000_pm,gen_df1000[gen_df1000["pt"]>0.5],"phi",phi_bins,2,"sig1000")))
ideffs2.append(mp.Process(target=make_eff, args=(df750,df750_pm,gen_df750[gen_df750["pt"]>0.5],"pt",pt_bins,2,"sig750")))
ideffs2.append(mp.Process(target=make_eff, args=(df750,df750_pm,gen_df750[gen_df750["pt"]>0.5],"eta",eta_bins,2,"sig750")))
ideffs2.append(mp.Process(target=make_eff, args=(df750,df750_pm,gen_df750[gen_df750["pt"]>0.5],"phi",phi_bins,2,"sig750")))
ideffs2.append(mp.Process(target=make_eff, args=(df400,df400_pm,gen_df400[gen_df400["pt"]>0.5],"pt",pt_bins,2,"sig400")))
ideffs2.append(mp.Process(target=make_eff, args=(df400,df400_pm,gen_df400[gen_df400["pt"]>0.5],"eta",eta_bins,2,"sig400")))
ideffs2.append(mp.Process(target=make_eff, args=(df400,df400_pm,gen_df400[gen_df400["pt"]>0.5],"phi",phi_bins,2,"sig400")))
ideffs2.append(mp.Process(target=make_eff, args=(df300,df300_pm,gen_df300[gen_df300["pt"]>0.5],"pt",pt_bins,2,"sig300")))
ideffs2.append(mp.Process(target=make_eff, args=(df300,df300_pm,gen_df300[gen_df300["pt"]>0.5],"eta",eta_bins,2,"sig300")))
ideffs2.append(mp.Process(target=make_eff, args=(df300,df300_pm,gen_df300[gen_df300["pt"]>0.5],"phi",phi_bins,2,"sig300")))
ideffs2.append(mp.Process(target=make_eff, args=(df200,df200_pm,gen_df200[gen_df200["pt"]>0.5],"pt",pt_bins,2,"sig200")))
ideffs2.append(mp.Process(target=make_eff, args=(df200,df200_pm,gen_df200[gen_df200["pt"]>0.5],"eta",eta_bins,2,"sig200")))
ideffs2.append(mp.Process(target=make_eff, args=(df200,df200_pm,gen_df200[gen_df200["pt"]>0.5],"phi",phi_bins,2,"sig200")))

ideffs3.append(mp.Process(target=make_eff, args=(df1000,df1000_pm2,gen_df1000[gen_df1000["pt"]>0.5],"pt",pt_bins,9,"sig1000")))
ideffs3.append(mp.Process(target=make_eff, args=(df1000,df1000_pm2,gen_df1000[gen_df1000["pt"]>0.5],"eta",eta_bins,9,"sig1000")))
ideffs3.append(mp.Process(target=make_eff, args=(df1000,df1000_pm2,gen_df1000[gen_df1000["pt"]>0.5],"phi",phi_bins,9,"sig1000")))
ideffs3.append(mp.Process(target=make_eff, args=(df750,df750_pm2,gen_df750[gen_df750["pt"]>0.5],"pt",pt_bins,9,"sig750")))
ideffs3.append(mp.Process(target=make_eff, args=(df750,df750_pm2,gen_df750[gen_df750["pt"]>0.5],"eta",eta_bins,9,"sig750")))
ideffs3.append(mp.Process(target=make_eff, args=(df750,df750_pm2,gen_df750[gen_df750["pt"]>0.5],"phi",phi_bins,9,"sig750")))
ideffs3.append(mp.Process(target=make_eff, args=(df400,df400_pm2,gen_df400[gen_df400["pt"]>0.5],"pt",pt_bins,9,"sig400")))
ideffs3.append(mp.Process(target=make_eff, args=(df400,df400_pm2,gen_df400[gen_df400["pt"]>0.5],"eta",eta_bins,9,"sig400")))
ideffs3.append(mp.Process(target=make_eff, args=(df400,df400_pm2,gen_df400[gen_df400["pt"]>0.5],"phi",phi_bins,9,"sig400")))
ideffs3.append(mp.Process(target=make_eff, args=(df300,df300_pm2,gen_df300[gen_df300["pt"]>0.5],"pt",pt_bins,9,"sig300")))
ideffs3.append(mp.Process(target=make_eff, args=(df300,df300_pm2,gen_df300[gen_df300["pt"]>0.5],"eta",eta_bins,9,"sig300")))
ideffs3.append(mp.Process(target=make_eff, args=(df300,df300_pm2,gen_df300[gen_df300["pt"]>0.5],"phi",phi_bins,9,"sig300")))
ideffs3.append(mp.Process(target=make_eff, args=(df200,df200_pm2,gen_df200[gen_df200["pt"]>0.5],"pt",pt_bins,9,"sig200")))
ideffs3.append(mp.Process(target=make_eff, args=(df200,df200_pm2,gen_df200[gen_df200["pt"]>0.5],"eta",eta_bins,9,"sig200")))
ideffs3.append(mp.Process(target=make_eff, args=(df200,df200_pm2,gen_df200[gen_df200["pt"]>0.5],"phi",phi_bins,9,"sig200")))

ideffs4.append(mp.Process(target=make_eff, args=(df1000,df1000_pm2z,gen_df1000[gen_df1000["pt"]>0.5],"pt",pt_bins,10,"sig1000")))
ideffs4.append(mp.Process(target=make_eff, args=(df1000,df1000_pm2z,gen_df1000[gen_df1000["pt"]>0.5],"eta",eta_bins,10,"sig1000")))
ideffs4.append(mp.Process(target=make_eff, args=(df1000,df1000_pm2z,gen_df1000[gen_df1000["pt"]>0.5],"phi",phi_bins,10,"sig1000")))
ideffs4.append(mp.Process(target=make_eff, args=(df750,df750_pm2z,gen_df750[gen_df750["pt"]>0.5],"pt",pt_bins,10,"sig750")))
ideffs4.append(mp.Process(target=make_eff, args=(df750,df750_pm2z,gen_df750[gen_df750["pt"]>0.5],"eta",eta_bins,10,"sig750")))
ideffs4.append(mp.Process(target=make_eff, args=(df750,df750_pm2z,gen_df750[gen_df750["pt"]>0.5],"phi",phi_bins,10,"sig750")))
ideffs4.append(mp.Process(target=make_eff, args=(df400,df400_pm2z,gen_df400[gen_df400["pt"]>0.5],"pt",pt_bins,10,"sig400")))
ideffs4.append(mp.Process(target=make_eff, args=(df400,df400_pm2z,gen_df400[gen_df400["pt"]>0.5],"eta",eta_bins,10,"sig400")))
ideffs4.append(mp.Process(target=make_eff, args=(df400,df400_pm2z,gen_df400[gen_df400["pt"]>0.5],"phi",phi_bins,10,"sig400")))
ideffs4.append(mp.Process(target=make_eff, args=(df300,df300_pm2z,gen_df300[gen_df300["pt"]>0.5],"pt",pt_bins,10,"sig300")))
ideffs4.append(mp.Process(target=make_eff, args=(df300,df300_pm2z,gen_df300[gen_df300["pt"]>0.5],"eta",eta_bins,10,"sig300")))
ideffs4.append(mp.Process(target=make_eff, args=(df300,df300_pm2z,gen_df300[gen_df300["pt"]>0.5],"phi",phi_bins,10,"sig300")))
ideffs4.append(mp.Process(target=make_eff, args=(df200,df200_pm2z,gen_df200[gen_df200["pt"]>0.5],"pt",pt_bins,10,"sig200")))
ideffs4.append(mp.Process(target=make_eff, args=(df200,df200_pm2z,gen_df200[gen_df200["pt"]>0.5],"eta",eta_bins,10,"sig200")))
ideffs4.append(mp.Process(target=make_eff, args=(df200,df200_pm2z,gen_df200[gen_df200["pt"]>0.5],"phi",phi_bins,10,"sig200")))

ideffs5.append(mp.Process(target=make_eff, args=(df1000,df1000_pm2ze,gen_df1000[gen_df1000["pt"]>0.5],"pt",pt_bins,11,"sig1000")))
ideffs5.append(mp.Process(target=make_eff, args=(df1000,df1000_pm2ze,gen_df1000[gen_df1000["pt"]>0.5],"eta",eta_bins,11,"sig1000")))
ideffs5.append(mp.Process(target=make_eff, args=(df1000,df1000_pm2ze,gen_df1000[gen_df1000["pt"]>0.5],"phi",phi_bins,11,"sig1000")))
ideffs5.append(mp.Process(target=make_eff, args=(df750,df750_pm2ze,gen_df750[gen_df750["pt"]>0.5],"pt",pt_bins,11,"sig750")))
ideffs5.append(mp.Process(target=make_eff, args=(df750,df750_pm2ze,gen_df750[gen_df750["pt"]>0.5],"eta",eta_bins,11,"sig750")))
ideffs5.append(mp.Process(target=make_eff, args=(df750,df750_pm2ze,gen_df750[gen_df750["pt"]>0.5],"phi",phi_bins,11,"sig750")))
ideffs5.append(mp.Process(target=make_eff, args=(df400,df400_pm2ze,gen_df400[gen_df400["pt"]>0.5],"pt",pt_bins,11,"sig400")))
ideffs5.append(mp.Process(target=make_eff, args=(df400,df400_pm2ze,gen_df400[gen_df400["pt"]>0.5],"eta",eta_bins,11,"sig400")))
ideffs5.append(mp.Process(target=make_eff, args=(df400,df400_pm2ze,gen_df400[gen_df400["pt"]>0.5],"phi",phi_bins,11,"sig400")))
ideffs5.append(mp.Process(target=make_eff, args=(df300,df300_pm2ze,gen_df300[gen_df300["pt"]>0.5],"pt",pt_bins,11,"sig300")))
ideffs5.append(mp.Process(target=make_eff, args=(df300,df300_pm2ze,gen_df300[gen_df300["pt"]>0.5],"eta",eta_bins,11,"sig300")))
ideffs5.append(mp.Process(target=make_eff, args=(df300,df300_pm2ze,gen_df300[gen_df300["pt"]>0.5],"phi",phi_bins,11,"sig300")))
ideffs5.append(mp.Process(target=make_eff, args=(df200,df200_pm2ze,gen_df200[gen_df200["pt"]>0.5],"pt",pt_bins,11,"sig200")))
ideffs5.append(mp.Process(target=make_eff, args=(df200,df200_pm2ze,gen_df200[gen_df200["pt"]>0.5],"eta",eta_bins,11,"sig200")))
ideffs5.append(mp.Process(target=make_eff, args=(df200,df200_pm2ze,gen_df200[gen_df200["pt"]>0.5],"phi",phi_bins,11,"sig200")))

#for idtype in [11,13,211]:
#  make_eff(df1000[abs(df1000["gen_id"]) == idtype],gen_df1000[abs(gen_df1000["gen_id"]) == idtype],qcd_df[abs(qcd_df["gen_id"]) == idtype],gen_qcddf[abs(gen_qcddf["gen_id"]) == idtype],"pt",pt_bins,idtype)
#  make_eff(df1000[abs(df1000["gen_id"]) == idtype],gen_df1000[abs(gen_df1000["gen_id"]) == idtype],qcd_df[abs(qcd_df["gen_id"]) == idtype],gen_qcddf[abs(gen_qcddf["gen_id"]) == idtype],"eta",eta_bins,idtype)
#  make_eff(df1000[abs(df1000["gen_id"]) == idtype],gen_df1000[abs(gen_df1000["gen_id"]) == idtype],qcd_df[abs(qcd_df["gen_id"]) == idtype],gen_qcddf[abs(gen_qcddf["gen_id"]) == idtype],"phi",phi_bins,idtype)
#
#
#make_eff(df1000[(abs(df1000["gen_id"]) != 211) & (abs(df1000["gen_id"]) > 100)],gen_df1000[(abs(gen_df1000["gen_id"]) != 211) & (abs(gen_df1000["gen_id"]) > 100)],qcd_df[(abs(qcd_df["gen_id"]) != 211) & (abs(qcd_df["gen_id"]) > 100)],gen_qcddf[(abs(gen_qcddf["gen_id"]) != 211) & (abs(gen_qcddf["gen_id"]) > 100)],"pt",pt_bins,100)
#make_eff(df1000[(abs(df1000["gen_id"]) != 211) & (abs(df1000["gen_id"]) > 100)],gen_df1000[(abs(gen_df1000["gen_id"]) != 211) & (abs(gen_df1000["gen_id"]) > 100)],qcd_df[(abs(qcd_df["gen_id"]) != 211) & (abs(qcd_df["gen_id"]) > 100)],gen_qcddf[(abs(gen_qcddf["gen_id"]) != 211) & (abs(gen_qcddf["gen_id"]) > 100)],"eta",eta_bins,100)
#make_eff(df1000[(abs(df1000["gen_id"]) != 211) & (abs(df1000["gen_id"]) > 100)],gen_df1000[(abs(gen_df1000["gen_id"]) != 211) & (abs(gen_df1000["gen_id"]) > 100)],qcd_df[(abs(qcd_df["gen_id"]) != 211) & (abs(qcd_df["gen_id"]) > 100)],gen_qcddf[(abs(gen_qcddf["gen_id"]) != 211) & (abs(gen_qcddf["gen_id"]) > 100)],"phi",phi_bins,100)
#
processes = []
processes2 = []

processes.append( mp.Process(target=trk_var, args=(df1000,qcd_df,"sig1000",0)))
processes.append( mp.Process(target=trk_var, args=(df750,qcd_df,"sig750",0)))
processes.append( mp.Process(target=trk_var, args=(df400,qcd_df,"sig400",0)))
processes.append( mp.Process(target=trk_var, args=(df300,qcd_df,"sig300",0)))
processes.append( mp.Process(target=trk_var, args=(df200,qcd_df,"sig200",0)))

processes.append( mp.Process(target=trk_var, args=(df1000_p,qcd_p,"sig1000",1)))
processes.append( mp.Process(target=trk_var, args=(df750_p,qcd_p,"sig750",1)))
processes.append( mp.Process(target=trk_var, args=(df400_p,qcd_p,"sig400",1)))
processes.append( mp.Process(target=trk_var, args=(df300_p,qcd_p,"sig300",1)))
processes.append( mp.Process(target=trk_var, args=(df200_p,qcd_p,"sig200",1)))

processes.append( mp.Process(target=trk_var, args=(df1000_pm,qcd_pm,"sig1000",2)))
processes.append( mp.Process(target=trk_var, args=(df750_pm,qcd_pm,"sig750",2)))
processes.append( mp.Process(target=trk_var, args=(df400_pm,qcd_pm,"sig400",2)))
processes.append( mp.Process(target=trk_var, args=(df300_pm,qcd_pm,"sig300",2)))
processes.append( mp.Process(target=trk_var, args=(df200_pm,qcd_pm,"sig200",2)))

processes2.append( mp.Process(target=trk_var, args=(df1000_pm2,qcd_pm2,"sig1000",9)))
processes2.append( mp.Process(target=trk_var, args=(df750_pm2,qcd_pm2,"sig750",9)))
processes2.append( mp.Process(target=trk_var, args=(df400_pm2,qcd_pm2,"sig400",9)))
processes2.append( mp.Process(target=trk_var, args=(df300_pm2,qcd_pm2,"sig300",9)))
processes2.append( mp.Process(target=trk_var, args=(df200_pm2,qcd_pm2,"sig200",9)))

processes2.append( mp.Process(target=trk_var, args=(df1000_pm2z,qcd_pm2z,"sig1000",10)))
processes2.append( mp.Process(target=trk_var, args=(df750_pm2z,qcd_pm2z,"sig750",10)))
processes2.append( mp.Process(target=trk_var, args=(df400_pm2z,qcd_pm2z,"sig400",10)))
processes2.append( mp.Process(target=trk_var, args=(df300_pm2z,qcd_pm2z,"sig300",10)))
processes2.append( mp.Process(target=trk_var, args=(df200_pm2z,qcd_pm2z,"sig200",10)))

processes2.append( mp.Process(target=trk_var, args=(df1000_pm2ze,qcd_pm2ze,"sig1000",11)))
processes2.append( mp.Process(target=trk_var, args=(df750_pm2ze,qcd_pm2ze,"sig750",11)))
processes2.append( mp.Process(target=trk_var, args=(df400_pm2ze,qcd_pm2ze,"sig400",11)))
processes2.append( mp.Process(target=trk_var, args=(df300_pm2ze,qcd_pm2ze,"sig300",11)))
processes2.append( mp.Process(target=trk_var, args=(df200_pm2ze,qcd_pm2ze,"sig200",11)))


combos = []
combos2 = []
combos3 = []
combos4 = []
#
#combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000, 0,65)))
#combos.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750, 0,55)))
#combos.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400, 0,45)))
#combos.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300, 0,45)))
#combos.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200, 0,30)))

combos.append(mp.Process(target=make_eff_combo, args=(df1000_p,qcd_p,1000, 1,65)))
combos.append(mp.Process(target=make_eff_combo, args=(df750_p,qcd_p,750, 1,55)))
combos.append(mp.Process(target=make_eff_combo, args=(df400_p,qcd_p,400, 1,45)))
combos.append(mp.Process(target=make_eff_combo, args=(df300_p,qcd_p,300, 1,45)))
combos.append(mp.Process(target=make_eff_combo, args=(df200_p,qcd_p,200, 1,30)))

combos.append(mp.Process(target=make_eff_combo, args=(df1000_pm,qcd_pm,1000,2 ,65)))
combos.append(mp.Process(target=make_eff_combo, args=(df750_pm,qcd_pm,750,2 ,55)))
combos.append(mp.Process(target=make_eff_combo, args=(df400_pm,qcd_pm,400,2 ,45)))
combos.append(mp.Process(target=make_eff_combo, args=(df300_pm,qcd_pm,300,2 ,45)))
combos.append(mp.Process(target=make_eff_combo, args=(df200_pm,qcd_pm,200,2 ,30)))

combos2.append(mp.Process(target=make_eff_combo, args=(df1000_pm2,qcd_pm2,1000,9,65)))
combos2.append(mp.Process(target=make_eff_combo, args=(df750_pm2,qcd_pm2,750,9,55)))
combos2.append(mp.Process(target=make_eff_combo, args=(df400_pm2,qcd_pm2,400,9,45)))
combos2.append(mp.Process(target=make_eff_combo, args=(df300_pm2,qcd_pm2,300,9,45)))
combos2.append(mp.Process(target=make_eff_combo, args=(df200_pm2,qcd_pm2,200,9,30)))

combos2.append(mp.Process(target=make_eff_combo, args=(df1000_pm2z,qcd_pm2z,1000,10 ,65)))
combos2.append(mp.Process(target=make_eff_combo, args=(df750_pm2z,qcd_pm2z, 750,10 ,55)))
combos2.append(mp.Process(target=make_eff_combo, args=(df400_pm2z,qcd_pm2z, 400,10 ,45)))
combos2.append(mp.Process(target=make_eff_combo, args=(df300_pm2z,qcd_pm2z, 300,10 ,45)))
combos2.append(mp.Process(target=make_eff_combo, args=(df200_pm2z,qcd_pm2z, 200,10 ,30)))

combos3.append(mp.Process(target=make_eff_combo, args=(df1000_pm2z,qcd_pm2z,1000,10 ,65,1)))
combos3.append(mp.Process(target=make_eff_combo, args=(df750_pm2z,qcd_pm2z, 750,10 ,55,1)))
combos3.append(mp.Process(target=make_eff_combo, args=(df400_pm2z,qcd_pm2z, 400,10 ,45,1)))
combos3.append(mp.Process(target=make_eff_combo, args=(df300_pm2z,qcd_pm2z, 300,10 ,45,1)))
combos3.append(mp.Process(target=make_eff_combo, args=(df200_pm2z,qcd_pm2z, 200,10 ,30,1)))

combos3.append(mp.Process(target=make_eff_combo, args=(df1000_pm2ze,qcd_pm2ze,1000, 11,65)))
combos3.append(mp.Process(target=make_eff_combo, args=(df750_pm2ze,qcd_pm2ze, 750,11 ,55)))
combos3.append(mp.Process(target=make_eff_combo, args=(df400_pm2ze,qcd_pm2ze, 400,11 ,45)))
combos3.append(mp.Process(target=make_eff_combo, args=(df300_pm2ze,qcd_pm2ze, 300,11 ,45)))
combos3.append(mp.Process(target=make_eff_combo, args=(df200_pm2ze,qcd_pm2ze, 200,11 ,30)))

combos4.append(mp.Process(target=make_eff_combo, args=(df1000_pm2ze,qcd_pm2ze,1000, 11,65,1)))
combos4.append(mp.Process(target=make_eff_combo, args=(df750_pm2ze,qcd_pm2ze, 750,11 ,55,1)))
combos4.append(mp.Process(target=make_eff_combo, args=(df400_pm2ze,qcd_pm2ze, 400,11 ,45,1)))
combos4.append(mp.Process(target=make_eff_combo, args=(df300_pm2ze,qcd_pm2ze, 300,11 ,45,1)))
combos4.append(mp.Process(target=make_eff_combo, args=(df200_pm2ze,qcd_pm2ze, 200,11 ,30,1)))

matched = []

matched.append(mp.Process(target=pfMatched, args=(df1000_p,qcd_p,"sig1000",1)))
matched.append(mp.Process(target=pfMatched, args=( df750_p,qcd_p, "sig750",1)))
matched.append(mp.Process(target=pfMatched, args=( df400_p,qcd_p, "sig400",1)))
matched.append(mp.Process(target=pfMatched, args=( df300_p,qcd_p, "sig300",1)))
matched.append(mp.Process(target=pfMatched, args=( df200_p,qcd_p, "sig200",1)))

matched.append(mp.Process(target=pfMatched, args=(df1000_pz,qcd_pz,"sig1000",12)))
matched.append(mp.Process(target=pfMatched, args=( df750_pz,qcd_pz, "sig750",12)))
matched.append(mp.Process(target=pfMatched, args=( df400_pz,qcd_pz, "sig400",12)))
matched.append(mp.Process(target=pfMatched, args=( df300_pz,qcd_pz, "sig300",12)))
matched.append(mp.Process(target=pfMatched, args=( df200_pz,qcd_pz, "sig200",12)))

matched.append(mp.Process(target=pfMatched, args=(df1000_pze,qcd_pze,"sig1000",13)))
matched.append(mp.Process(target=pfMatched, args=( df750_pze,qcd_pze, "sig750",13)))
matched.append(mp.Process(target=pfMatched, args=( df400_pze,qcd_pze, "sig400",13)))
matched.append(mp.Process(target=pfMatched, args=( df300_pze,qcd_pze, "sig300",13)))
matched.append(mp.Process(target=pfMatched, args=( df200_pze,qcd_pze, "sig200",13)))

#for p in matched:
#  p.start()
#for p in matched:
#  p.join()

#print("var studies")
#for p in processes:
#  p.start()
#for p in processes:
#  p.join()
#for p in processes2:
#  p.start()
#for p in processes2:
#  p.join()
#
#print("id efficiency")
#for p in ideffs1:
#  p.start()
#for p in ideffs1:
#  p.join()
#for p in ideffs2:
#  p.start()
#for p in ideffs2:
#  p.join()
#for p in ideffs3:
#  p.start()
#for p in ideffs3:
#  p.join()
#for p in ideffs4:
#  p.start()
#for p in ideffs4:
#  p.join()
#for p in ideffs5:
#  p.start()
#for p in ideffs5:
#  p.join()

print("nTracks") 
for p in combos:
  p.start()
for p in combos:
  p.join()
#for p in combos2:
#  p.start()
#for p in combos2:
#  p.join()
#for p in combos3:
#  p.start()
#for p in combos3:
#  p.join()
#for p in combos4:
#  p.start()
#for p in combos4:
#  p.join()
#print("2d plots")
#make_2d_correlation(df1000, "trk_matched",[0,1,2], "qOverp",[x*0.001 for x in range(0,44440)])
#make_2d_correlation(df1000, "trk_pv",[0,1,2,3,4], "qOverp",[x*0.001 for x in range(0,40)])
#make_2d_correlation(df1000, "trk_matched",[0,1,2], "trk_quality",[0,1,2,3,4,5,6])
#make_2d_correlation(df1000, "eta",np.array(range(-250,250,25))/100., "trk_dzErrorPV0",[x/100 for x in range(0,100)])
#make_2d_correlation(qcd_pm2z, "eta",np.array(range(-250,250,25))/100., "trk_dzErrorPV0",[x/100 for x in range(0,100)])
#
#make_peak_sig([df1000_p,df1000_pm2,df1000_pm2z,df1000_pm2ze],[qcd_p,qcd_pm2,qcd_pm2z,qcd_pm2ze], 1000,[1,9,10,11],65)
#make_peak_sig([df750_p,df750_pm2,df750_pm2z,df750_pm2ze],[qcd_p,qcd_pm2,qcd_pm2z,qcd_pm2ze], 750,[1,9,10,11],55)
#make_peak_sig([df400_p,df400_pm2,df400_pm2z,df400_pm2ze],[qcd_p,qcd_pm2,qcd_pm2z,qcd_pm2ze], 400,[1,9,10,11],45)
#make_peak_sig([df300_p,df300_pm2,df300_pm2z,df300_pm2ze],[qcd_p,qcd_pm2,qcd_pm2z,qcd_pm2ze], 300,[1,9,10,11],45)
#make_peak_sig([df200_p,df200_pm2,df200_pm2z,df200_pm2ze],[qcd_p,qcd_pm2,qcd_pm2z,qcd_pm2ze], 200,[1,9,10,11],30)
##
#make_peak_sig([df1000_p,df1000_pm2,df1000_pm2z,df1000_pm2ze],[qcd_p,qcd_pm2,qcd_pm2z,qcd_pm2ze], 1000,[1,9,10,11],65,1)
#make_peak_sig([df750_p,df750_pm2,df750_pm2z,df750_pm2ze],[qcd_p,qcd_pm2,qcd_pm2z,qcd_pm2ze], 750,[1,9,10,11],55,1)
#make_peak_sig([df400_p,df400_pm2,df400_pm2z,df400_pm2ze],[qcd_p,qcd_pm2,qcd_pm2z,qcd_pm2ze], 400,[1,9,10,11],45,1)
#make_peak_sig([df300_p,df300_pm2,df300_pm2z,df300_pm2ze],[qcd_p,qcd_pm2,qcd_pm2z,qcd_pm2ze], 300,[1,9,10,11],45,1)
#make_peak_sig([df200_p,df200_pm2,df200_pm2z,df200_pm2ze],[qcd_p,qcd_pm2,qcd_pm2z,qcd_pm2ze], 200,[1,9,10,11],30,1)
##
#print("PFMatching")
#pfMatched(df1000_p,qcd_p,"sig1000",1)
#pfMatched(df750_p,qcd_p,"sig750",1)
#pfMatched(df400_p,qcd_p,"sig400",1)
#pfMatched(df300_p,qcd_p,"sig300",1)
#pfMatched(df200_p,qcd_p,"sig200",1)
#pfMatched(df1000_pz,qcd_pz,"sig1000",12)
#pfMatched(df750_pz,qcd_pz,"sig750",12)
#pfMatched(df400_pz,qcd_pz,"sig400",12)
#pfMatched(df300_pz,qcd_pz,"sig300",12)
#pfMatched(df200_pz,qcd_pz,"sig200",12)
#pfMatched(df1000_pze,qcd_pze,"sig1000",13)
#pfMatched(df750_pze,qcd_pze,"sig750",13)
#pfMatched(df400_pze,qcd_pze,"sig400",13)
#pfMatched(df300_pze,qcd_pze,"sig300",13)
#pfMatched(df200_pze,qcd_pze,"sig200",13)


