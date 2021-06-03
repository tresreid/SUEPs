import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import gc
#from pathlib import Path

lumi = 59.74*1000
sig1000dr =[]
sig750dr =[]
sig400dr =[]
sig300dr =[]
sig200dr =[]
qcddr =[]
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
          "entry":int(cols[23])
          })
  df = pd.DataFrame(dr)
  del dr
  df["phi"] = df["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
  return df

df_mD1_T1 = openReco("track_mDark1_temp1_v0",5.9)
df_mD1_T2 = openReco("track_mDark1_temp2_v0",5.9)
df_mD1_T5 = openReco("track_mDark1_temp5_v0",5.9)
df_mD2_T1 = openReco("track_mDark2_temp1_v0",5.9)
df_mD2_T5 = openReco("track_mDark2_temp5_v0",5.9)
df_mD5_T1 = openReco("track_mDark5_temp1_v0",5.9)
df_mD5_T2 = openReco("track_mDark5_temp2_v0",5.9)
df_mD5_T5 = openReco("track_mDark5_temp5_v0",5.9)

#with open('data/track_sig_1000_v0.txt') as f:
#    xsec = 0.17
#    for line in f.readlines():
#      if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
#        continue
#      cols = line.rstrip().split(' ')
#      sig1000dr.append({
#        "min_dR":float(cols[3]),"is_isr":int(cols[6]),"wgt":xsec*lumi/10000,
#        "pt":float(cols[7]),"eta":float(cols[8]),"phi":float(cols[9]),
#        "trk_pv":int(cols[13]),
#        "trk_matched":int(cols[14]),
#        "trk_foundHits":int(cols[15]),
#        "trk_lostHits":int(cols[16]),
#        "trk_chi2":float(cols[17]),
#        "trk_nHits":int(cols[18]),
#        "trk_nPHits":int(cols[19]),
#        "trk_quality":int(cols[20]),
#        "gen_id":int(cols[21]),
#        "size":int(cols[22]),
#        "entry":int(cols[23])
#        })
#df1000 = pd.DataFrame(sig1000dr)
#del sig1000dr
#with open('data/track_sig_750_v0.txt') as f:
#    xsec = 0.5 
#    for line in f.readlines():
#      if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
#        continue
#      cols = line.rstrip().split(' ')
#      sig750dr.append({
#        "min_dR":float(cols[3]),"is_isr":int(cols[6]),"wgt":xsec*lumi/10000,
#        "pt":float(cols[7]),"eta":float(cols[8]),"phi":float(cols[9]),
#        "trk_pv":int(cols[13]),
#        "trk_matched":int(cols[14]),
#        "trk_foundHits":int(cols[15]),
#        "trk_lostHits":int(cols[16]),
#        "trk_chi2":float(cols[17]),
#        "trk_nHits":int(cols[18]),
#        "trk_nPHits":int(cols[19]),
#        "trk_quality":int(cols[20]),
#        "gen_id":int(cols[21]),
#        "size":int(cols[22]),
#        "entry":int(cols[23])
#        })
#df750 = pd.DataFrame(sig750dr)
#del sig750dr
#with open('data/track_sig_400_v0.txt') as f:
#    xsec = 5.9
#    for line in f.readlines():
#      if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
#        continue
#      cols = line.rstrip().split(' ')
#      sig400dr.append({
#        "min_dR":float(cols[3]),"is_isr":int(cols[6]),"wgt":xsec*lumi/10000,
#        "pt":float(cols[7]),"eta":float(cols[8]),"phi":float(cols[9]),
#        "trk_pv":int(cols[13]),
#        "trk_matched":int(cols[14]),
#        "trk_foundHits":int(cols[15]),
#        "trk_lostHits":int(cols[16]),
#        "trk_chi2":float(cols[17]),
#        "trk_nHits":int(cols[18]),
#        "trk_nPHits":int(cols[19]),
#        "trk_quality":int(cols[20]),
#        "gen_id":int(cols[21]),
#        "size":int(cols[22]),
#        "entry":int(cols[23])
#        })
#df400 = pd.DataFrame(sig400dr)
#del sig400dr
#with open('data/track_sig_300_v0.txt') as f:
#    xsec = 8.9
#    for line in f.readlines():
#      if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
#        continue
#      cols = line.rstrip().split(' ')
#      sig300dr.append({
#        "min_dR":float(cols[3]),"is_isr":int(cols[6]),"wgt":xsec*lumi/10000,
#        "pt":float(cols[7]),"eta":float(cols[8]),"phi":float(cols[9]),
#        "trk_pv":int(cols[13]),
#        "trk_matched":int(cols[14]),
#        "trk_foundHits":int(cols[15]),
#        "trk_lostHits":int(cols[16]),
#        "trk_chi2":float(cols[17]),
#        "trk_nHits":int(cols[18]),
#        "trk_nPHits":int(cols[19]),
#        "trk_quality":int(cols[20]),
#        "gen_id":int(cols[21]),
#        "size":int(cols[22]),
#        "entry":int(cols[23])
#        })
#df300 = pd.DataFrame(sig300dr)
#del sig300dr
#
#with open('data/track_sig_200_v0.txt') as f:
#    xsec = 13.6
#    for line in f.readlines():
#      if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
#        continue
#      cols = line.rstrip().split(' ')
#      sig200dr.append({
#        "min_dR":float(cols[3]),"is_isr":int(cols[6]),"wgt":xsec*lumi/10000,
#        "pt":float(cols[7]),"eta":float(cols[8]),"phi":float(cols[9]),
#        "trk_pv":int(cols[13]),
#        "trk_matched":int(cols[14]),
#        "trk_foundHits":int(cols[15]),
#        "trk_lostHits":int(cols[16]),
#        "trk_chi2":float(cols[17]),
#        "trk_nHits":int(cols[18]),
#        "trk_nPHits":int(cols[19]),
#        "trk_quality":int(cols[20]),
#        "gen_id":int(cols[21]),
#        "size":int(cols[22]),
#        "entry":int(cols[23])
#        })
#df200 = pd.DataFrame(sig200dr)
#del sig200dr
gc.collect()
          
#xsecs = [311900,29070,5962,1207,119.9,25.24] # signal xsec are (125,34.8),(300,8.9), (400,5.9), (750,0.5), (1000,0.17)
#files = [300,500,700,1000,1500,2000]
xsecs = [5962,1207,119.9,25.24] # signal xsec are (125,34.8),(300,8.9), (400,5.9), (750,0.5), (1000,0.17)
files = [700,1000,1500,2000]
qcdi=0 # don;t overlap entries from different files
for xsec,f1 in zip(xsecs,files):
#with open('data/track_qcd_1000_v0.txt') as f:
  f=open("data/track_qcd_%s_v0.txt"%f1)
  print(f1)
  for line in f.readlines():
    if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
      continue
    cols = line.rstrip().split(' ')
    #if (int(cols[14]) == 0) or (int(cols[20]) <= 0) or (int(cols[13]) <= 1) or (int(cols[19]) <= 1) or (int(cols[15]) == 0): #part of fake id
    #if (int(cols[14]) == 0) or (int(cols[13]) <= 1):# or (float(cols[7]) < 1.0): 
    #  continue
#    if int(cols[23]) > 1000:
#      break
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
      "entry":int(cols[23]) + 100000*qcdi
      })
  qcdi = qcdi+1
qcd_df = pd.DataFrame(qcddr)
del qcddr
#gc.collect()
################GEN INFO
gen1000 =[]
gen750 =[]
gen400 =[]
gen300 =[]
gen200 =[]
qcdgen =[]
print("opening gen")
#with open('track.txt') as f:

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

#with open('data/gentrack_sig_1000_v0.txt') as f:
#    xsec = 0.17
#    for line in f.readlines():
#      if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
#        continue
#      cols = line.rstrip().split(' ')
#      gen1000.append({
#        "wgt":xsec*lumi/10000,
#        "pt":float(cols[0]),"eta":float(cols[1]),"phi":float(cols[2]),"gen_id":int(cols[3]),"is_isr":int(cols[4]),
#        "suep_size":int(cols[5]), "isr_size":int(cols[6]),"entry":int(cols[7])
#        })
#gen_df1000 = pd.DataFrame(gen1000)
#del gen1000
#with open('data/gentrack_sig_750_v0.txt') as f:
#    xsec = 0.5
#    for line in f.readlines():
#      if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
#        continue
#      cols = line.rstrip().split(' ')
#      gen750.append({
#        "wgt":xsec*lumi/10000,
#        "pt":float(cols[0]),"eta":float(cols[1]),"phi":float(cols[2]),"gen_id":int(cols[3]),"is_isr":int(cols[4]),
#        "suep_size":int(cols[5]), "isr_size":int(cols[6]),"entry":int(cols[7])
#        })
#gen_df750 = pd.DataFrame(gen750)
#del gen750
#with open('data/gentrack_sig_400_v0.txt') as f:
#    xsec = 5.9 
#    for line in f.readlines():
#      if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
#        continue
#      cols = line.rstrip().split(' ')
#      gen400.append({
#        "wgt":xsec*lumi/10000,
#        "pt":float(cols[0]),"eta":float(cols[1]),"phi":float(cols[2]),"gen_id":int(cols[3]),"is_isr":int(cols[4]),
#        "suep_size":int(cols[5]), "isr_size":int(cols[6]),"entry":int(cols[7])
#        })
#gen_df400 = pd.DataFrame(gen400)
#del gen400
#with open('data/gentrack_sig_300_v0.txt') as f:
#    xsec = 8.9 
#    for line in f.readlines():
#      if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
#        continue
#      cols = line.rstrip().split(' ')
#      gen300.append({
#        "wgt":xsec*lumi/10000,
#        "pt":float(cols[0]),"eta":float(cols[1]),"phi":float(cols[2]),"gen_id":int(cols[3]),"is_isr":int(cols[4]),
#        "suep_size":int(cols[5]), "isr_size":int(cols[6]),"entry":int(cols[7])
#        })
#gen_df300 = pd.DataFrame(gen300)
#del gen300
##gc.collect()
#with open('data/gentrack_sig_200_v0.txt') as f:
#    xsec = 13.6
#    for line in f.readlines():
#      if "No" in line or "Starting" in line or "sample" in line or "entry" in line:
#        continue
#      cols = line.rstrip().split(' ')
#      gen200.append({
#        "wgt":xsec*lumi/10000,
#        "pt":float(cols[0]),"eta":float(cols[1]),"phi":float(cols[2]),"gen_id":int(cols[3]),"is_isr":int(cols[4]),
#        "suep_size":int(cols[5]), "isr_size":int(cols[6]),"entry":int(cols[7])
#        })
#gen_df200 = pd.DataFrame(gen200)
#del gen200
gc.collect()
          
#xsecs = [311900,29070,5962,1207,119.9,25.24] # signal xsec are (125,34.8), (400,5.9), (750,0.5), (1000,0.17)
#files = [300,500,700,1000,1500,2000]
xsecs = [5962,1207,119.9,25.24] # signal xsec are (125,34.8), (400,5.9), (750,0.5), (1000,0.17)
files = [700,1000,1500,2000]
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
#df1000 = pd.DataFrame(sig1000dr)
#df200 = pd.DataFrame(sig200dr)
#qcd_df = pd.DataFrame(qcddr)
#gen_df1000 = pd.DataFrame(gen1000)
#gen_df200 = pd.DataFrame(gen200)
#gen_qcddf = pd.DataFrame(qcdgen)

#df1000["phi"] = df1000["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
#df750["phi"] = df750["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
#df400["phi"] = df400["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
#df300["phi"] = df300["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
#df200["phi"] = df200["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
qcd_df["phi"] = qcd_df["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
#gen_df1000["phi"] = gen_df1000["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
#gen_df750["phi"] = gen_df750["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
#gen_df400["phi"] = gen_df400["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
#gen_df300["phi"] = gen_df300["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
#gen_df200["phi"] = gen_df200["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
gen_qcddf["phi"] = gen_qcddf["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
#print(gen_df)



print("plotting")
def trk_var(df,qcd_df,name,idtype):
  fig, ax = plt.subplots(2,2)
  partType = {0:"all",11:"electron",13:"muon",22:"photon",211:"pion",100:"hadron",1:"pv >= 2",2:"pv >=2; matched==1",3:"pv >= 2; matched==1; quality > 0",4:"pv >= 2; matched==1; pt > 1"}
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
  ax[1,1].hist(df[df["min_dR"] < 0.05]["trk_chi2"]    ,bins=10,range=[0,200],density=False, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,1].hist(df[df["min_dR"] >= 0.05]["trk_chi2"]   ,bins=10,range=[0,200],density=False, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,1].hist(qcd_df["trk_chi2"]                     ,bins=10,range=[0,200],density=False, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  
  ax[0,0].legend()
  ax[1,0].legend()
  ax[0,1].legend()
  ax[1,1].legend()
  fig.tight_layout()
  fig.savefig("Plots/var/matched_distribtuion_trks1_%s_%s.png"%(name,idtype))
#  fig.clear()
  plt.close()
  fig, ax = plt.subplots(2,2)
  partType = {0:"all",11:"electron",13:"muon",22:"photon",211:"pion",100:"hadron",1:"pv >= 2",2:"pv >=2; matched==1",3:"pv >= 2; matched==1; quality > 0",4:"pv >= 2; matched==1; pt > 1"}
  fig.suptitle("%s: "%(name)+partType[idtype],y=1.0)
  
  ax[0,0].set_xlabel("trk PV")    
  ax[1,0].set_xlabel("trk Quality")    
  ax[0,1].set_xlabel("matched")    
  ax[1,1].set_xlabel("chi2")    
  #ax[0,0].set_yscale('log')
  #ax[0,1].set_yscale('log')
  #ax[1,0].set_yscale('log')
  #ax[1,1].set_yscale('log')
  
  ax[0,0].hist(df[df["min_dR"] < 0.05]["trk_pv"]      ,bins=4,range=[0,4],   density=True, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,0].hist(df[df["min_dR"] >= 0.05]["trk_pv"]     ,bins=4,range=[0,4],   density=True, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,0].hist(qcd_df["trk_pv"]                       ,bins=4,range=[0,4],   density=True, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,0].hist(df[df["min_dR"] < 0.05]["trk_quality"] ,bins=8,range=[-2,6],  density=True, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,0].hist(df[df["min_dR"] >= 0.05]["trk_quality"],bins=8,range=[-2,6],  density=True, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,0].hist(qcd_df["trk_quality"]                  ,bins=8,range=[-2,6],  density=True, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[0,1].hist(df[df["min_dR"] < 0.05]["trk_matched"] ,bins=2,range=[0,2],   density=True, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,1].hist(df[df["min_dR"] >= 0.05]["trk_matched"],bins=2,range=[0,2],   density=True, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,1].hist(qcd_df["trk_matched"]                  ,bins=2,range=[0,2],   density=True, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,1].hist(df[df["min_dR"] < 0.05]["trk_chi2"]    ,bins=10,range=[0,200],density=True, histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,1].hist(df[df["min_dR"] >= 0.05]["trk_chi2"]   ,bins=10,range=[0,200],density=True, histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,1].hist(qcd_df["trk_chi2"]                     ,bins=10,range=[0,200],density=True, histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  
  ax[0,0].legend()
  ax[1,0].legend()
  ax[0,1].legend()
  ax[1,1].legend()
  fig.tight_layout()
  fig.savefig("Plots/var/matched_distribtuion_trks1_%s_%s_norm.png"%(name,idtype))
#  fig.clear()
  plt.close()
  
  
  fig, ax = plt.subplots(2,2)
  fig.suptitle("%s: "%(name)+partType[idtype],y=1.0)
  
  ax[0,0].set_xlabel("found Hits")    
  ax[1,0].set_xlabel("lost Hits")    
  ax[0,1].set_xlabel("nHits")    
  ax[1,1].set_xlabel("nPixelHits")    
  ax[0,0].set_yscale('log')
  ax[0,1].set_yscale('log')
  ax[1,0].set_yscale('log')
  ax[1,1].set_yscale('log')
  
  ax[0,0].hist(df[df["min_dR"] < 0.05]["trk_foundHits"], bins=50,range=[0,50],density=False,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,0].hist(df[df["min_dR"] >= 0.05]["trk_foundHits"],bins=50,range=[0,50],density=False,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,0].hist(qcd_df["trk_foundHits"],                  bins=50,range=[0,50],density=False,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,0].hist(df[df["min_dR"] < 0.05]["trk_lostHits"],  bins=5,range=[-1,1], density=False,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,0].hist(df[df["min_dR"] >= 0.05]["trk_lostHits"], bins=5,range=[-1,1], density=False,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,0].hist(qcd_df["trk_lostHits"],                   bins=5,range=[-1,1], density=False,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[0,1].hist(df[df["min_dR"] < 0.05]["trk_nHits"],     bins=50,range=[0,50],density=False,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,1].hist(df[df["min_dR"] >= 0.05]["trk_nHits"],    bins=50,range=[0,50],density=False,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,1].hist(qcd_df["trk_nHits"],                      bins=50,range=[0,50],density=False,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,1].hist(df[df["min_dR"] < 0.05]["trk_nPHits"],    bins=12,range=[0,12],density=False,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,1].hist(df[df["min_dR"] >= 0.05]["trk_nPHits"],   bins=12,range=[0,12],density=False,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,1].hist(qcd_df["trk_nPHits"],                     bins=12,range=[0,12],density=False,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  
  ax[0,0].legend()
  ax[1,0].legend()
  ax[0,1].legend()
  ax[1,1].legend()
  fig.tight_layout()
  fig.savefig("Plots/var/matched_distribtuion_trks2_%s_%s.png"%(name,idtype))
  plt.close()
  fig, ax = plt.subplots(2,2)
  fig.suptitle("%s: "%(name)+partType[idtype],y=1.0)
  
  ax[0,0].set_xlabel("found Hits")    
  ax[1,0].set_xlabel("lost Hits")    
  ax[0,1].set_xlabel("nHits")    
  ax[1,1].set_xlabel("nPixelHits")    
  #ax[0,0].set_yscale('log')
  #ax[0,1].set_yscale('log')
  #ax[1,0].set_yscale('log')
  #ax[1,1].set_yscale('log')
  
  ax[0,0].hist(df[df["min_dR"] < 0.05]["trk_foundHits"], bins=50,range=[0,50],density=True,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,0].hist(df[df["min_dR"] >= 0.05]["trk_foundHits"],bins=50,range=[0,50],density=True,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,0].hist(qcd_df["trk_foundHits"],                  bins=50,range=[0,50],density=True,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,0].hist(df[df["min_dR"] < 0.05]["trk_lostHits"],  bins=5,range=[-1,1], density=True,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,0].hist(df[df["min_dR"] >= 0.05]["trk_lostHits"], bins=5,range=[-1,1], density=True,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,0].hist(qcd_df["trk_lostHits"],                   bins=5,range=[-1,1], density=True,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[0,1].hist(df[df["min_dR"] < 0.05]["trk_nHits"],     bins=50,range=[0,50],density=True,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[0,1].hist(df[df["min_dR"] >= 0.05]["trk_nHits"],    bins=50,range=[0,50],density=True,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[0,1].hist(qcd_df["trk_nHits"],                      bins=50,range=[0,50],density=True,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  ax[1,1].hist(df[df["min_dR"] < 0.05]["trk_nPHits"],    bins=12,range=[0,12],density=True,histtype=u'step',weights=df[df["min_dR"] < 0.05]["wgt"],color="blue",label="true")
  ax[1,1].hist(df[df["min_dR"] >= 0.05]["trk_nPHits"],   bins=12,range=[0,12],density=True,histtype=u'step',weights=df[df["min_dR"] >= 0.05]["wgt"],color="red",label="false")
  ax[1,1].hist(qcd_df["trk_nPHits"],                     bins=12,range=[0,12],density=True,histtype=u'step',weights=qcd_df["wgt"],color="black",label="qcd")
  
  ax[0,0].legend()
  ax[1,0].legend()
  ax[0,1].legend()
  ax[1,1].legend()
  fig.tight_layout()
  fig.savefig("Plots/var/matched_distribtuion_trks2_%s_%s_norm.png"%(name,idtype))
  plt.close()


def make_eff(df,dfID,gen_df,var,bins,idtype,sample):
  print("running %s eff"%var)
  fig, ax = plt.subplots(2,sharex=True)
  
  partType = {0:"all",11:"electron",13:"muon",22:"photon",211:"pion",100:"hadron",1:"pv >= 2",2:"pv >=2; matched==1",3:"pv >= 2; matched==1; quality > 0",4:"pv >= 2; matched==1; pt > 1"}
  fig.suptitle("%s: "%(sample)+partType[idtype])
  ax[0].set_ylabel("events")    
  ax[1].set_ylabel("efficiency")    
  if "pt" in var:
    ax[0].set_yscale('log')
    ax[0].set_xscale('log')
    ax[1].set_xscale('log')
  
  ax[0].hist(df[(df["min_dR"] < 0.05)][var], bins=bins,histtype=u'step',weights=df[(df["min_dR"] < 0.05)]["wgt"],color="blue",label="matched")
  ax[0].hist(df[(df["min_dR"] >= 0.05)][var],bins=bins,histtype=u'step',weights=df[(df["min_dR"] >= 0.05)]["wgt"],color="red",label="!matched")
  ax[0].hist(dfID[(dfID["min_dR"] < 0.05)][var], bins=bins,histtype=u'step',weights=dfID[(dfID["min_dR"] < 0.05)]["wgt"],color="green",label="matched+ID")
  ax[0].hist(dfID[(dfID["min_dR"] >= 0.05)][var], bins=bins,histtype=u'step',weights=dfID[(dfID["min_dR"] >= 0.05)]["wgt"],color="cyan",label="!matched+ID")
  ax[0].hist(df[var], bins=bins,histtype=u'step',weights=df["wgt"],color="black",label="all reco")
  ax[0].hist(gen_df[var], bins=bins,histtype=u'step',weights=gen_df["wgt"],color="magenta",label="gen")
  all_group = df.groupby(pd.cut(df[var],bins))["wgt"].sum().to_numpy()
  reco_group = df[(df["min_dR"] < 0.05)].groupby(pd.cut(df[(df["min_dR"] < 0.05)][var],bins))["wgt"].sum().to_numpy()
  fake_group = df[(df["min_dR"] >= 0.05)].groupby(pd.cut(df[(df["min_dR"] >= 0.05)][var],bins))["wgt"].sum().to_numpy()
  ID_group = dfID[(dfID["min_dR"] < 0.05)].groupby(pd.cut(dfID[(dfID["min_dR"] < 0.05)][var],bins))["wgt"].sum().to_numpy()
  fakeID_group = dfID[(dfID["min_dR"] >= 0.05)].groupby(pd.cut(dfID[(dfID["min_dR"] >= 0.05)][var],bins))["wgt"].sum().to_numpy()
  gen_group = gen_df.groupby(pd.cut(gen_df[var],bins))["wgt"].sum().to_numpy()

  
  eff = pd.DataFrame()
  eff["range"] = (bins[1:]-bins[:-1])/2.
  eff["recoeff"] = (reco_group/gen_group) #reco matched/ all gen
  eff["reco_yerr"]=(reco_group/gen_group)*np.sqrt((1/reco_group)+(1/gen_group))
  eff["IDeff"] = (ID_group/reco_group) # reco-matched ID / reco-matched
  eff["ID_yerr"]=(ID_group/reco_group)*np.sqrt((1/reco_group)+(1/ID_group))
  eff["fakeRate"] = (fake_group/all_group) # reco-matched ID / reco-matched
  eff["fake_yerr"]=(fake_group/all_group)*np.sqrt((1/fake_group)+(1/all_group))
  eff["purity"] = (reco_group/all_group) # reco-matched ID / reco-matched
  eff["pure_yerr"]=(reco_group/all_group)*np.sqrt((1/reco_group)+(1/all_group))
  eff["fakeIDeff"] = (fakeID_group/all_group) # reco-matched ID / reco-matched
  eff["fakeID_yerr"]=(fakeID_group/all_group)*np.sqrt((1/all_group)+(1/fakeID_group))
  eff["totaleff"] = (ID_group/gen_group) #reco matched/ all gen
  eff["total_yerr"]=(ID_group/gen_group)*np.sqrt((1/reco_group)+(1/gen_group))
  
  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["recoeff"].to_numpy(),eff["reco_yerr"].to_numpy(),xerr=eff["range"],ls='none',label="reco eff",color="blue")
  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["IDeff"].to_numpy(),eff["ID_yerr"].to_numpy(),xerr=eff["range"],ls='none',label="ID eff",color="green")
  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["fakeRate"].to_numpy(),eff["fake_yerr"].to_numpy(),xerr=eff["range"],ls='none',label="fake Rate",color="red")
  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["purity"].to_numpy(),eff["pure_yerr"].to_numpy(),xerr=eff["range"],ls='none',label="purity",color="cyan")
  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["fakeIDeff"].to_numpy(),eff["fakeID_yerr"].to_numpy(),xerr=eff["range"],ls='none',label="fake ID Rate",color="orange")
  ax[1].errorbar(eff["range"].to_numpy()+bins[:-1],eff["totaleff"].to_numpy(),eff["total_yerr"].to_numpy(),xerr=eff["range"],ls='none',label="Total Eff",color="black")
  
  ax[1].set_ylim([0,1.01])
  ax[1].set_xlabel(var)
  ax[0].set_xlabel(var)
  ax[0].legend()
  ax[1].legend()
  fig.tight_layout()
  fig.savefig("Plots/eff/efficiency_%s_%s_%s.png"%(var,idtype,sample))
  plt.close()


def get_sig(df_sig,df_bkg,var,binx):
  sig = []
  bkg = []
  tot_sig = df_sig["wgt"].sum()
  tot_bkg = df_bkg["wgt"].sum()
  for i in range(0,binx*10,10):
    sig.append(df_sig[df_sig[var] > i]["wgt"].sum())
    bkg.append(df_bkg[df_bkg[var] > i]["wgt"].sum()+0.000001)
  return(sig,tot_sig,bkg,tot_bkg)

plot_id=0
def make_eff_combo(reco_id,qcd_id,idx,binx,pt_cut):
  global plot_id
  fig, ax = plt.subplots(1,1)

  ax.set_title(idx)    
  ax.set_ylabel("Events")
  ax2 = ax.twinx()
  if(pt_cut):
    pt = [0.1,0.5,.75,1.0,2.0]
  else:
    pt = [200,50,20,10,5]
  colors = ["red","green","blue","black","magenta"]
  for i in [0,1,2,3,4]:
    if(pt_cut):
      reco_id = reco_id[reco_id["pt"] > pt[i]]
      qcd_id = qcd_id[qcd_id["pt"] > pt[i]]
      lab1 = ">"
    else:
      reco_id = reco_id[reco_id["pt"] < pt[i]]
      qcd_id = qcd_id[qcd_id["pt"] < pt[i]]
      lab1 = "<"
    reco_group = reco_id.groupby(['entry']).first()
    reco_group['nTracks'] = reco_id.groupby(['entry']).size()
    #gen_group = gen_df.groupby(['entry']).first()
    #gen_group['nTracks'] = gen_df.groupby(['entry']).size()
    qcd_group = qcd_id.groupby(['entry']).first()
    qcd_group['nTracks'] = qcd_id.groupby(['entry']).size()
    sig,tot_sig,bkg,tot_bkg = get_sig(reco_group,qcd_group,"nTracks",binx) 
#    ax.plot([],[],' ',label="max sig: %.2f"%(np.max((sig/(np.sqrt(np.add(sig,bkg)))))))
    #ax.hist(gen_group["nTracks"],   bins=120,histtype=u'step',range=[0,1200],weights=gen_group["wgt"],color="green",label="gen")
    ax.hist(reco_group["nTracks"],  bins=binx,histtype=u'step',range=[0,binx*10],weights=reco_group["wgt"],color=colors[i],linestyle="solid",label="sig:pt%s%.2f"%(lab1,pt[i]))
    ax.hist(qcd_group["nTracks"],   bins=binx,histtype=u'step',range=[0,binx*10],weights=qcd_group["wgt"],color=colors[i],linestyle="dashed",label="qcd:pt%s%.2f"%(lab1,pt[i]))
    ax2.errorbar(range(0,binx*10,10),sig/(np.sqrt(np.add(sig,bkg))),(sig/(np.sqrt(np.add(sig,bkg))))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(4*np.add(sig,bkg)))),ecolor=colors[i],label="signif: pt%s%.2f"%(lab1,pt[i]),color=colors[i],linestyle="dashdot",errorevery=2)
  ax2.set_ylabel("Significance")
  #ax3 = ax.twinx()
  #ax3.spines["right"].set_position(("axes",1.2))
  #ax3.errorbar(range(0,1200,10),sig/tot_sig,(sig/tot_sig)*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(tot_sig))),ecolor='lightblue',label="sig_eff",color="blue",errorevery=10)
  #ax3.errorbar(range(0,1200,10),bkg/tot_bkg,(bkg/tot_bkg)*np.sqrt(np.add(np.reciprocal(bkg),np.reciprocal(tot_bkg))),ecolor='indianred',label="bkg_eff",color="red",errorevery=10)
  #ax3.set_ylabel("Efficiency")
  lin1,lab1 = ax.get_legend_handles_labels()
  lin2,lab2 = ax2.get_legend_handles_labels()
  #lin3,lab3 = ax3.get_legend_handles_labels()
  lin = lin1+lin2#+lin3
  lab = lab1+lab2#+lab3
  ax.legend(lin,lab)
  ax.set_yscale('log')
  plot_id = plot_id + 1
  fig.tight_layout()
  fig.savefig("Plots/nTracks/nTracks_%s_%s.png"%(plot_id,pt_cut))
  plt.close()


# Get IDs
print("making IDs")
#df1000_p = df1000[(df1000["trk_pv"] >=2)]
#df1000_pm = df1000[(df1000["trk_pv"] >=2) & (df1000["trk_matched"]==1)]
#df1000_pmt = df1000[(df1000["trk_pv"] >=2) & (df1000["trk_matched"]==1) & (df1000["pt"]>1)]
#df1000_pmq = df1000[(df1000["trk_pv"] >=2) & (df1000["trk_matched"]==1) & (df1000["trk_quality"]>0)]
#df750_p   = df750[(df750["trk_pv"] >=2)]
#df750_pm  = df750[(df750["trk_pv"] >=2) & (df750["trk_matched"]==1)]
#df750_pmt = df750[(df750["trk_pv"] >=2) & (df750["trk_matched"]==1) & (df750["pt"]>1)]
#df750_pmq = df750[(df750["trk_pv"] >=2) & (df750["trk_matched"]==1) & (df750["trk_quality"]>0)]
#df400_p   = df400[(df400["trk_pv"] >=2)]
#df400_pm  = df400[(df400["trk_pv"] >=2) & (df400["trk_matched"]==1)]
#df400_pmt = df400[(df400["trk_pv"] >=2) & (df400["trk_matched"]==1) & (df400["pt"]>1)]
#df400_pmq = df400[(df400["trk_pv"] >=2) & (df400["trk_matched"]==1) & (df400["trk_quality"]>0)]
#df300_p   = df300[(df300["trk_pv"] >=2)]
#df300_pm  = df300[(df300["trk_pv"] >=2) & (df300["trk_matched"]==1)]
#df300_pmt = df300[(df300["trk_pv"] >=2) & (df300["trk_matched"]==1) & (df300["pt"]>1)]
#df300_pmq = df300[(df300["trk_pv"] >=2) & (df300["trk_matched"]==1) & (df300["trk_quality"]>0)]
#df200_p = df200[(df200["trk_pv"] >=2)]
#df200_pm = df200[(df200["trk_pv"] >=2) & (df200["trk_matched"]==1)]
#df200_pmt = df200[(df200["trk_pv"] >=2) & (df200["trk_matched"]==1) & (df200["pt"]>1)]
#df200_pmq = df200[(df200["trk_pv"] >=2) & (df200["trk_matched"]==1) & (df200["trk_quality"]>0)]
#qcd_p = qcd_df[(qcd_df["trk_pv"] >=2)]
#qcd_pm = qcd_df[(qcd_df["trk_pv"] >=2) & (qcd_df["trk_matched"]==1)]
#qcd_pmt = qcd_df[(qcd_df["trk_pv"] >=2) & (qcd_df["trk_matched"]==1) & (qcd_df["pt"]>1)]
#qcd_pmq = qcd_df[(qcd_df["trk_pv"] >=2) & (qcd_df["trk_matched"]==1) & (qcd_df["trk_quality"]>0)]

def ID_p(df):
  return df[(df["trk_pv"] >=2)]
def ID_pm(df):
  return df[(df["trk_pv"] >=2) & (df["trk_matched"]==1)]
def ID_pmq(df):
  return df[(df["trk_pv"] >=2) & (df["trk_matched"]==1) & (df["trk_quality"]>0)]
qcd_p = ID_p(qcd_df)  
qcd_pm = ID_pm(qcd_df)  
qcd_pmq = ID_pmq(qcd_df)  
df_mD1_T1_p   =   ID_p(df_mD1_T1)
df_mD1_T1_pm  =  ID_pm(df_mD1_T1)
df_mD1_T1_pmq = ID_pmq(df_mD1_T1)
df_mD1_T2_p   =   ID_p(df_mD1_T2)
df_mD1_T2_pm  =  ID_pm(df_mD1_T2)
df_mD1_T2_pmq = ID_pmq(df_mD1_T2)
df_mD1_T5_p   =   ID_p(df_mD1_T5)
df_mD1_T5_pm  =  ID_pm(df_mD1_T5)
df_mD1_T5_pmq = ID_pmq(df_mD1_T5)
df_mD2_T1_p   =   ID_p(df_mD2_T1)
df_mD2_T1_pm  =  ID_pm(df_mD2_T1)
df_mD2_T1_pmq = ID_pmq(df_mD2_T1)
df_mD2_T5_p   =   ID_p(df_mD2_T5)
df_mD2_T5_pm  =  ID_pm(df_mD2_T5)
df_mD2_T5_pmq = ID_pmq(df_mD2_T5)
df_mD5_T1_p   =   ID_p(df_mD5_T1)
df_mD5_T1_pm  =  ID_pm(df_mD5_T1)
df_mD5_T1_pmq = ID_pmq(df_mD5_T1)
df_mD5_T2_p   =   ID_p(df_mD5_T2)
df_mD5_T2_pm  =  ID_pm(df_mD5_T2)
df_mD5_T2_pmq = ID_pmq(df_mD5_T2)
df_mD5_T5_p   =   ID_p(df_mD5_T5)
df_mD5_T5_pm  =  ID_pm(df_mD5_T5)
df_mD5_T5_pmq = ID_pmq(df_mD5_T5)
#print("id efficiency")
#pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50,200])
#eta_bins = np.array(range(-250,250,25))/100.
#phi_bins = np.array(range(-31,31,5))/10.
#make_eff(df1000,df1000,gen_df1000,"pt",pt_bins,0,"sig1000")
#make_eff(df1000,df1000,gen_df1000,"eta",eta_bins,0,"sig1000")
#make_eff(df1000,df1000,gen_df1000,"phi",phi_bins,0,"sig1000")
#
#make_eff(df1000,df1000_p,gen_df1000,"pt",pt_bins,1,"sig1000")
#make_eff(df1000,df1000_p,gen_df1000,"eta",eta_bins,1,"sig1000")
#make_eff(df1000,df1000_p,gen_df1000,"phi",phi_bins,1,"sig1000")
#
#make_eff(df1000,df1000_pm,gen_df1000,"pt",pt_bins,2,"sig1000")
#make_eff(df1000,df1000_pm,gen_df1000,"eta",eta_bins,2,"sig1000")
#make_eff(df1000,df1000_pm,gen_df1000,"phi",phi_bins,2,"sig1000")
#
#make_eff(df1000[df1000["pt"]>1],df1000_pmt,gen_df1000[gen_df1000["pt"]>1],"pt",pt_bins,4,"sig1000")
#make_eff(df1000[df1000["pt"]>1],df1000_pmt,gen_df1000[gen_df1000["pt"]>1],"eta",eta_bins,4,"sig1000")
#make_eff(df1000[df1000["pt"]>1],df1000_pmt,gen_df1000[gen_df1000["pt"]>1],"phi",phi_bins,4,"sig1000")
#
#make_eff(df750,df750,gen_df750,"pt",pt_bins,0,"sig750")
#make_eff(df750,df750,gen_df750,"eta",eta_bins,0,"sig750")
#make_eff(df750,df750,gen_df750,"phi",phi_bins,0,"sig750")
#
#make_eff(df750,df750_p,gen_df750,"pt",pt_bins,1,"sig750")
#make_eff(df750,df750_p,gen_df750,"eta",eta_bins,1,"sig750")
#make_eff(df750,df750_p,gen_df750,"phi",phi_bins,1,"sig750")
#
#make_eff(df750,df750_pm,gen_df750,"pt",pt_bins,2,"sig750")
#make_eff(df750,df750_pm,gen_df750,"eta",eta_bins,2,"sig750")
#make_eff(df750,df750_pm,gen_df750,"phi",phi_bins,2,"sig750")
#
#make_eff(df750[df750["pt"]>1],df750_pmt,gen_df750[gen_df750["pt"]>1],"pt",pt_bins,4,"sig750")
#make_eff(df750[df750["pt"]>1],df750_pmt,gen_df750[gen_df750["pt"]>1],"eta",eta_bins,4,"sig750")
#make_eff(df750[df750["pt"]>1],df750_pmt,gen_df750[gen_df750["pt"]>1],"phi",phi_bins,4,"sig750")
#
#make_eff(df400,df400,gen_df400,"pt",pt_bins,0,"sig400")
#make_eff(df400,df400,gen_df400,"eta",eta_bins,0,"sig400")
#make_eff(df400,df400,gen_df400,"phi",phi_bins,0,"sig400")
#
#make_eff(df400,df400_p,gen_df400,"pt",pt_bins,1,"sig1000")
#make_eff(df400,df400_p,gen_df400,"eta",eta_bins,1,"sig1000")
#make_eff(df400,df400_p,gen_df400,"phi",phi_bins,1,"sig1000")
#
#make_eff(df400,df400_pm,gen_df400,"pt",pt_bins,2,"sig1000")
#make_eff(df400,df400_pm,gen_df400,"eta",eta_bins,2,"sig1000")
#make_eff(df400,df400_pm,gen_df400,"phi",phi_bins,2,"sig1000")
#
#make_eff(df400[df400["pt"]>1],df400_pmt,gen_df400[gen_df400["pt"]>1],"pt",pt_bins,4,"sig400")
#make_eff(df400[df400["pt"]>1],df400_pmt,gen_df400[gen_df400["pt"]>1],"eta",eta_bins,4,"sig400")
#make_eff(df400[df400["pt"]>1],df400_pmt,gen_df400[gen_df400["pt"]>1],"phi",phi_bins,4,"sig400")
#
#make_eff(df300,df300,gen_df300,"pt",pt_bins,0,"sig300")
#make_eff(df300,df300,gen_df300,"eta",eta_bins,0,"sig300")
#make_eff(df300,df300,gen_df300,"phi",phi_bins,0,"sig300")
#
#make_eff(df300,df300_p,gen_df300,"pt",pt_bins,1,"sig300")
#make_eff(df300,df300_p,gen_df300,"eta",eta_bins,1,"sig300")
#make_eff(df300,df300_p,gen_df300,"phi",phi_bins,1,"sig300")
#
#make_eff(df300,df300_pm,gen_df300,"pt",pt_bins,2,"sig300")
#make_eff(df300,df300_pm,gen_df300,"eta",eta_bins,2,"sig300")
#make_eff(df300,df300_pm,gen_df300,"phi",phi_bins,2,"sig300")
#
#make_eff(df300[df300["pt"]>1],df300_pmt,gen_df300[gen_df300["pt"]>1],"pt",pt_bins,4,"sig300")
#make_eff(df300[df300["pt"]>1],df300_pmt,gen_df300[gen_df300["pt"]>1],"eta",eta_bins,4,"sig300")
#make_eff(df300[df300["pt"]>1],df300_pmt,gen_df300[gen_df300["pt"]>1],"phi",phi_bins,4,"sig300")
#
#make_eff(df200,df200,gen_df200,"pt",pt_bins,0,"sig200")
#make_eff(df200,df200,gen_df200,"eta",eta_bins,0,"sig200")
#make_eff(df200,df200,gen_df200,"phi",phi_bins,0,"sig200")
#
#make_eff(df200,df200_p,gen_df200,"pt",pt_bins,1,"sig200")
#make_eff(df200,df200_p,gen_df200,"eta",eta_bins,1,"sig200")
#make_eff(df200,df200_p,gen_df200,"phi",phi_bins,1,"sig200")
#
#make_eff(df200,df200_pm,gen_df200,"pt",pt_bins,2,"sig200")
#make_eff(df200,df200_pm,gen_df200,"eta",eta_bins,2,"sig200")
#make_eff(df200,df200_pm,gen_df200,"phi",phi_bins,2,"sig200")
#
#make_eff(df200[df200["pt"]>1],df200_pmt,gen_df200[gen_df200["pt"]>1],"pt",pt_bins,4,"sig200")
#make_eff(df200[df200["pt"]>1],df200_pmt,gen_df200[gen_df200["pt"]>1],"eta",eta_bins,4,"sig200")
#make_eff(df200[df200["pt"]>1],df200_pmt,gen_df200[gen_df200["pt"]>1],"phi",phi_bins,4,"sig200")
#
#
#make_eff(qcd_df,qcd_df,gen_qcddf,"pt",pt_bins,0,"qcd")
#make_eff(qcd_df,qcd_df,gen_qcddf,"eta",eta_bins,0,"qcd")
#make_eff(qcd_df,qcd_df,gen_qcddf,"phi",phi_bins,0,"qcd")
#
#make_eff(qcd_df,qcd_p,gen_qcddf,"pt",pt_bins,1,"qcd")
#make_eff(qcd_df,qcd_p,gen_qcddf,"eta",eta_bins,1,"qcd")
#make_eff(qcd_df,qcd_p,gen_qcddf,"phi",phi_bins,1,"qcd")
#
#make_eff(qcd_df,qcd_pm,gen_qcddf,"pt",pt_bins,2,"qcd")
#make_eff(qcd_df,qcd_pm,gen_qcddf,"eta",eta_bins,2,"qcd")
#make_eff(qcd_df,qcd_pm,gen_qcddf,"phi",phi_bins,2,"qcd")
#
#make_eff(qcd_df,qcd_pmt,gen_qcddf[gen_qcddf["pt"]>1],"pt",pt_bins,4,"qcd")
#make_eff(qcd_df,qcd_pmt,gen_qcddf[gen_qcddf["pt"]>1],"eta",eta_bins,4,"qcd")
#make_eff(qcd_df,qcd_pmt,gen_qcddf[gen_qcddf["pt"]>1],"phi",phi_bins,4,"qcd")
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
#print("var studies")
#trk_var(df1000,qcd_df,"sig1000",0)
#trk_var(df1000_p,qcd_p,"sig1000",1)
#trk_var(df1000_pm,qcd_pm,"sig1000",2)
#trk_var(df1000_pmt,qcd_pmt,"sig1000",4)
#trk_var(df750,qcd_df,"sig750",0)
#trk_var(df750_p,qcd_p,"sig750",1)
#trk_var(df750_pm,qcd_pm,"sig750",2)
#trk_var(df750_pmt,qcd_pmt,"sig750",4)
#trk_var(df400,qcd_df,"sig400",0)
#trk_var(df400_p,qcd_p,"sig400",1)
#trk_var(df400_pm,qcd_pm,"sig400",2)
#trk_var(df400_pmt,qcd_pmt,"sig400",4)
#trk_var(df300,qcd_df,"sig300",0)
#trk_var(df300_p,qcd_p,"sig300",1)
#trk_var(df300_pm,qcd_pm,"sig300",2)
#trk_var(df300_pmt,qcd_pmt,"sig300",4)
#trk_var(df200,qcd_df,"sig200",0)
#trk_var(df200_p,qcd_p,"sig200",1)
#trk_var(df200_pm,qcd_pm,"sig200",2)
#trk_var(df200_pmt,qcd_pmt,"sig200",4)
print("nTracks") 
make_eff_combo(df_mD1_T1_pm,qcd_pm,"mDark1T1",50,1)
make_eff_combo(df_mD1_T2_pm,qcd_pm,"mDark1T2",40,1)
make_eff_combo(df_mD1_T5_pm,qcd_pm,"mDark1T5",35,1)
make_eff_combo(df_mD2_T1_pm,qcd_pm,"mDark2T1",50,1)
make_eff_combo(df_mD2_T5_pm,qcd_pm,"mDark2T5",35,1)
make_eff_combo(df_mD5_T1_pm,qcd_pm,"mDark5T1",45,1)
make_eff_combo(df_mD5_T2_pm,qcd_pm,"mDark5T2",40,1)
make_eff_combo(df_mD5_T5_pm,qcd_pm,"mDark5T5",30,1)
#make_eff_combo(df1000_pm,qcd_pm,gen_df1000,"sig1000",60,1)
#make_eff_combo(df750_pm,qcd_pm,gen_df750,"sig750",55,1)
#make_eff_combo(df400_pm,qcd_pm,gen_df400,"sig400",40,1)
#make_eff_combo(df300_pm,qcd_pm,gen_df300,"sig300",35,1)
#make_eff_combo(df200_pm,qcd_pm,gen_df200,"sig200",25,1)
#make_eff_combo(df1000_pm,qcd_pm,gen_df1000,"sig1000",60,0)
#make_eff_combo(df750_pm,qcd_pm,gen_df750,"sig750",55,0)
#make_eff_combo(df400_pm,qcd_pm,gen_df400,"sig400",40,0)
#make_eff_combo(df300_pm,qcd_pm,gen_df300,"sig300",35,0)
#make_eff_combo(df200_pm,qcd_pm,gen_df200,"sig200",25,0)
#make_eff_combo(df1000_pm[df1000_pm["trk_nHits"]<30],qcd_pm[qcd_pm["trk_nHits"]<30],gen_df1000,"sig1000 (nHit<30)",55)
#make_eff_combo(df750_pm[df750_pm["trk_nHits"]<30],qcd_pm[qcd_pm["trk_nHits"]<30],gen_df750,"sig750 (nHit<30)",55)
#make_eff_combo(df400_pm[df400_pm["trk_nHits"]<30],qcd_pm[qcd_pm["trk_nHits"]<30],gen_df400,"sig400 (nHit<30)",55)
#make_eff_combo(df300_pm[df300_pm["trk_nHits"]<30],qcd_pm[qcd_pm["trk_nHits"]<30],gen_df300,"sig300 (nHit<30)",55)
#make_eff_combo(df200_pm[df200_pm["trk_nHits"]<30],qcd_pm[qcd_pm["trk_nHits"]<30],gen_df200,"sig200 (nHit<30)",25)

#make_eff_combo(df200,qcd_df,gen_df200,"sig200:no id")
##make_eff_combo(df200[(df200["min_dR"] < 0.001)],qcd_df[(qcd_df["min_dR"]< 0.001)],gen_df200,"sig200:min_dR<0.001")
##make_eff_combo(df200[(df200["min_dR"] < 0.05)],qcd_df[(qcd_df["min_dR"]< 0.05)],gen_df200,"sig200:min_dR<0.05")
#make_eff_combo(df200[(df200["trk_chi2"] <= 2)],qcd_df[(qcd_df["trk_chi2"] <= 2)],gen_df200,"sig200:trk_chi2 <= 2")
#make_eff_combo(df200[(df200["trk_matched"] == 1)],qcd_df[(qcd_df["trk_matched"] == 1)],gen_df200,"sig200:trk_matched == 1")
#make_eff_combo(df200[(df200["trk_pv"] >= 2)],qcd_df[(qcd_df["trk_pv"] >= 2)],gen_df200,"sig200:trk_Pv >= 2")
#make_eff_combo(df200[((df200["trk_matched"] == 1) &(df200["trk_pv"] >= 2) )],qcd_df[((qcd_df["trk_matched"] == 1) & (qcd_df["trk_pv"] >= 2))],gen_df200,"sig200:trk_matched == 1; trk_pv >=2")
#make_eff_combo(df200[((df200["trk_matched"] == 1) &(df200["trk_pv"] >= 2) & (df200["pt"] < 10) )],qcd_df[((qcd_df["trk_matched"] == 1) & (qcd_df["trk_pv"] >= 2) & (qcd_df["pt"] < 10))],gen_df200,"sig200:trk_matched == 1; trk_pv >=2; trk_pt < 10")
#make_eff_combo(df200[((df200["trk_matched"] == 1) &(df200["trk_quality"] > 0) &(df200["trk_pv"] >= 2) & (df200["pt"] < 10) )],qcd_df[((qcd_df["trk_matched"] == 1) &(qcd_df["trk_quality"] > 0)& (qcd_df["trk_pv"] >= 2) & (qcd_df["pt"] < 10))],gen_df200,"sig200:trk_matched == 1; trk_pv >=2;trk_quality>0 trk_pt < 10")
#print("sig 1000") 
#make_eff_combo(df1000,qcd_df,gen_df1000,"sig1000:no id")
##make_eff_combo(df1000[(df1000["min_dR"] < 0.001)],qcd_df[(qcd_df["min_dR"]< 0.001)],gen_df1000,"sig1000:min_dR<0.001")
##make_eff_combo(df1000[(df1000["min_dR"] < 0.05)],qcd_df[(qcd_df["min_dR"]< 0.05)],gen_df1000,"sig1000:min_dR<0.05")
#make_eff_combo(df1000[(df1000["trk_chi2"] <= 2)],qcd_df[(qcd_df["trk_chi2"] <= 2)],gen_df1000,"sig1000:trk_chi2 <= 2")
#make_eff_combo(df1000[(df1000["trk_matched"] == 1)],qcd_df[(qcd_df["trk_matched"] == 1)],gen_df1000,"sig1000:trk_matched == 1")
#make_eff_combo(df1000[(df1000["trk_pv"] >= 2)],qcd_df[(qcd_df["trk_pv"] >= 2)],gen_df1000,"sig1000:trk_Pv >= 2")
#make_eff_combo(df1000[((df1000["trk_matched"] == 1) &(df1000["trk_pv"] >= 2) )],qcd_df[((qcd_df["trk_matched"] == 1) & (qcd_df["trk_pv"] >= 2))],gen_df1000,"sig1000:trk_matched == 1; trk_pv >=2")
#make_eff_combo(df1000[((df1000["trk_matched"] == 1) &(df1000["trk_quality"] > 2) &(df1000["trk_pv"] >= 2) & (df1000["pt"] < 15) )],qcd_df[((qcd_df["trk_matched"] == 1) & (qcd_df["trk_pv"] >= 2) & (qcd_df["pt"] < 15))],gen_df1000,"sig1000:trk_matched == 1; trk_pv >=2; trk_pt < 15")
#make_eff_combo(df1000[((df1000["trk_matched"] == 1) &(df1000["trk_quality"] > 0) &(df1000["trk_pv"] >= 2) & (df1000["pt"] < 15) )],qcd_df[((qcd_df["trk_matched"] == 1) &(qcd_df["trk_quality"] > 0)& (qcd_df["trk_pv"] >= 2) & (qcd_df["pt"] < 15))],gen_df1000,"sig1000:trk_matched == 1; trk_pv >=2;trk_quality>0 trk_pt < 15")
