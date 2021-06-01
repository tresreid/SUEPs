import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import gc
import matplotlib.colors as colors



lumi = 59.74*1000

jets_1000 = []
jets_400 = []
jets_750 = []
jets_300 = []
jets_200 = []
jets_qcd = []
for qcd in [0,1,2,3,4,5]:
  xsecs = [311900,29070,5962,1207,119.9,25.24] # signal xsec are (125,34.8), (400,5.9), (750,0.5), (1000,0.17)
  files = [300,500,700,1000,1500,2000]
  if qcd == 0:
    for xsec,f in  zip(xsecs,files):
      #fname = "data/qcd%s_comparisonsx.txt"%f
      fname = "../macros/data/qcd_%s_v0.txt"%f
      try:
        firstfile = open(fname)
      except IOError:
        print("file %s doesn't exist"%fname)
        continue
      qcd_tit = "QCD"
      next(firstfile)
      events = 0
      for line in firstfile.readlines():
        events += xsec
        cols = line.rstrip().split(' ')
        jets_qcd.append({"Event":int(cols[0]), "Jet_algo": int(cols[1]), "R":float(cols[2]),"jet_id":int(cols[3]),
          "pt":float(cols[4]), "eta":float(cols[5]), "phi":float(cols[6]), "nTracks":int(cols[7]), "girth":float(cols[8]), "mass":float(cols[9]),"xsec":xsec*lumi/10000,
           "trackpt":float(cols[10]),"medpt":float(cols[11]),"suep_tracks":int(cols[12]), "isr_tracks":int(cols[13]), "total_suep":int(cols[14]), "total_isr":int(cols[15]),
            "NVtx":int(cols[16]),"Num_Interactions":int(cols[17]),"scalardR":float(cols[18]),"scalarpt":float(cols[19]),"scalareta":float(cols[20]),"scalarphi":float(cols[21]), 
            "suep_ptwgt":float(cols[22]),"scalarmass":float(cols[23]),"beta":float(cols[24]),"scalarbeta":float(cols[25]), 
            "pt_dispersion":float(cols[26]),"lesHouches":float(cols[27]),"thrust":float(cols[28]),
            "t1":float(cols[29]),"t2":float(cols[30]),"t3":float(cols[31]),"e2":float(cols[32]),"e3":float(cols[33])
            })
      print("QCD %d Events: %d"%(f,events))
      print(len(jets_qcd))
  elif qcd == 1:
    firstfile = open('../macros/data/sig_1000_v0.txt')
    qcd_tit = "Sig"
    next(firstfile)
    events = 0
    xsec = 0.17
    for line in firstfile.readlines():
      events += 1
      cols = line.rstrip().split(' ')
      jets_1000.append({"Event":int(cols[0]), "Jet_algo": int(cols[1]), "R":float(cols[2]),"jet_id":int(cols[3]), 
      "pt":float(cols[4]), "eta":float(cols[5]), "phi":float(cols[6]), "nTracks":int(cols[7]), "girth":float(cols[8]), "mass":float(cols[9]),"xsec":xsec*lumi/10000,
           "trackpt":float(cols[10]),"medpt":float(cols[11]),"suep_tracks":int(cols[12]), "isr_tracks":int(cols[13]), "total_suep":int(cols[14]), "total_isr":int(cols[15]),
            "NVtx":int(cols[16]),"Num_Interactions":int(cols[17]),"scalardR":float(cols[18]),"scalarpt":float(cols[19]),"scalareta":float(cols[20]),"scalarphi":float(cols[21]),
            "suep_ptwgt":float(cols[22]),"scalarmass":float(cols[23]),"beta":float(cols[24]),"scalarbeta":float(cols[25]), 
            "pt_dispersion":float(cols[26]),"lesHouches":float(cols[27]),"thrust":float(cols[28]),
            "t1":float(cols[29]),"t2":float(cols[30]),"t3":float(cols[31]),"e2":float(cols[32]),"e3":float(cols[33])
            })
    print("Signal Events: %d"%(events))
  elif qcd == 2:
    firstfile = open('../macros/data/sig_400_v0.txt')
    qcd_tit = "Sig400"
    next(firstfile)
    events = 0
    xsec = 5.9
    for line in firstfile.readlines():
      events += 1
      cols = line.rstrip().split(' ')
      jets_400.append({"Event":int(cols[0]), "Jet_algo": int(cols[1]), "R":float(cols[2]),"jet_id":int(cols[3]), 
      "pt":float(cols[4]), "eta":float(cols[5]), "phi":float(cols[6]), "nTracks":int(cols[7]), "girth":float(cols[8]), "mass":float(cols[9]),"xsec":xsec*lumi/10000,
           "trackpt":float(cols[10]),"medpt":float(cols[11]),"suep_tracks":int(cols[12]), "isr_tracks":int(cols[13]), "total_suep":int(cols[14]), "total_isr":int(cols[15]),
            "NVtx":int(cols[16]),"Num_Interactions":int(cols[17]),"scalardR":float(cols[18]),"scalarpt":float(cols[19]),"scalareta":float(cols[20]),"scalarphi":float(cols[21]),
            "suep_ptwgt":float(cols[22]),"scalarmass":float(cols[23]),"beta":float(cols[24]),"scalarbeta":float(cols[25]), 
            "pt_dispersion":float(cols[26]),"lesHouches":float(cols[27]),"thrust":float(cols[28]),
            "t1":float(cols[29]),"t2":float(cols[30]),"t3":float(cols[31]),"e2":float(cols[32]),"e3":float(cols[33])
            })
    print("Signal 400 Events: %d"%(events))
  elif qcd == 3:
    firstfile = open('../macros/data/sig_750_v0.txt')
    qcd_tit = "Sig750"
    next(firstfile)
    events = 0
    xsec = 0.5
    for line in firstfile.readlines():
      events += 1
      cols = line.rstrip().split(' ')
      jets_750.append({"Event":int(cols[0]), "Jet_algo": int(cols[1]), "R":float(cols[2]),"jet_id":int(cols[3]), 
      "pt":float(cols[4]), "eta":float(cols[5]), "phi":float(cols[6]), "nTracks":int(cols[7]), "girth":float(cols[8]), "mass":float(cols[9]),"xsec":xsec*lumi/10000,
           "trackpt":float(cols[10]),"medpt":float(cols[11]),"suep_tracks":int(cols[12]), "isr_tracks":int(cols[13]), "total_suep":int(cols[14]), "total_isr":int(cols[15]),
            "NVtx":int(cols[16]),"Num_Interactions":int(cols[17]),"scalardR":float(cols[18]),"scalarpt":float(cols[19]),"scalareta":float(cols[20]),"scalarphi":float(cols[21]),
            "suep_ptwgt":float(cols[22]),"scalarmass":float(cols[23]),"beta":float(cols[24]),"scalarbeta":float(cols[25]), 
            "pt_dispersion":float(cols[26]),"lesHouches":float(cols[27]),"thrust":float(cols[28]),
            "t1":float(cols[29]),"t2":float(cols[30]),"t3":float(cols[31]),"e2":float(cols[32]),"e3":float(cols[33])
            })
    print("Signal 750 Events: %d"%(events))
  elif qcd == 4:
    firstfile = open('../macros/data/sig_200_v0.txt')
    qcd_tit = "Sig200"
    next(firstfile)
    events = 0
    xsec = 13.6
    for line in firstfile.readlines():
      events += 1
      cols = line.rstrip().split(' ')
      jets_200.append({"Event":int(cols[0]), "Jet_algo": int(cols[1]), "R":float(cols[2]),"jet_id":int(cols[3]), 
      "pt":float(cols[4]), "eta":float(cols[5]), "phi":float(cols[6]), "nTracks":int(cols[7]), "girth":float(cols[8]), "mass":float(cols[9]),"xsec":xsec*lumi/10000,
           "trackpt":float(cols[10]),"medpt":float(cols[11]),"suep_tracks":int(cols[12]), "isr_tracks":int(cols[13]), "total_suep":int(cols[14]), "total_isr":int(cols[15]),
            "NVtx":int(cols[16]),"Num_Interactions":int(cols[17]),"scalardR":float(cols[18]),"scalarpt":float(cols[19]),"scalareta":float(cols[20]),"scalarphi":float(cols[21]),
            "suep_ptwgt":float(cols[22]),"scalarmass":float(cols[23]),"beta":float(cols[24]),"scalarbeta":float(cols[25]), 
            "pt_dispersion":float(cols[26]),"lesHouches":float(cols[27]),"thrust":float(cols[28]),
            "t1":float(cols[29]),"t2":float(cols[30]),"t3":float(cols[31]),"e2":float(cols[32]),"e3":float(cols[33])
            })
    print("Signal 200 Events: %d"%(events))
  elif qcd == 5:
    firstfile = open('../macros/data/sig_300_v0.txt')
    qcd_tit = "Sig300"
    next(firstfile)
    events = 0
    xsec = 8.9 
    for line in firstfile.readlines():
      events += 1
      cols = line.rstrip().split(' ')
      jets_300.append({"Event":int(cols[0]), "Jet_algo": int(cols[1]), "R":float(cols[2]),"jet_id":int(cols[3]), 
      "pt":float(cols[4]), "eta":float(cols[5]), "phi":float(cols[6]), "nTracks":int(cols[7]), "girth":float(cols[8]), "mass":float(cols[9]),"xsec":xsec*lumi/10000,
           "trackpt":float(cols[10]),"medpt":float(cols[11]),"suep_tracks":int(cols[12]), "isr_tracks":int(cols[13]), "total_suep":int(cols[14]), "total_isr":int(cols[15]),
            "NVtx":int(cols[16]),"Num_Interactions":int(cols[17]),"scalardR":float(cols[18]),"scalarpt":float(cols[19]),"scalareta":float(cols[20]),"scalarphi":float(cols[21]),
            "suep_ptwgt":float(cols[22]),"scalarmass":float(cols[23]),"beta":float(cols[24]),"scalarbeta":float(cols[25]), 
            "pt_dispersion":float(cols[26]),"lesHouches":float(cols[27]),"thrust":float(cols[28]),
            "t1":float(cols[29]),"t2":float(cols[30]),"t3":float(cols[31]),"e2":float(cols[32]),"e3":float(cols[33])
            })
    print("Signal 300 Events: %d"%(events))

print("starting pandas")  
df_jets1000 = pd.DataFrame(jets_1000)
df_jets400 = pd.DataFrame(jets_400)
df_jetsqcd = pd.DataFrame(jets_qcd)
#df_jets1000['pt_rank'] = df_jets1000.groupby(["Event","Jet_algo","R"])["pt"].rank(method="first",ascending=False)
#df_jets1000['multi_rank'] = df_jets1000.groupby(["Event","Jet_algo","R"])["nTracks"].rank(method="first",ascending=False)
#df_jets400['pt_rank'] = df_jets400.groupby(["Event","Jet_algo","R"])["pt"].rank(method="first",ascending=False)
#df_jets400['multi_rank'] = df_jets400.groupby(["Event","Jet_algo","R"])["nTracks"].rank(method="first",ascending=False)
#df_jetsqcd['pt_rank'] = df_jetsqcd.groupby(["Event","Jet_algo","R"])["pt"].rank(method="first",ascending=False)
#df_jetsqcd['multi_rank'] = df_jetsqcd.groupby(["Event","Jet_algo","R"])["nTracks"].rank(method="first",ascending=False)

df_jets750 = pd.DataFrame(jets_750)
df_jets300 = pd.DataFrame(jets_300)
df_jets200 = pd.DataFrame(jets_200)
#df_jets750['pt_rank'] = df_jets750.groupby(["Event","Jet_algo","R"])["pt"].rank(method="first",ascending=False)
#df_jets750['multi_rank'] = df_jets750.groupby(["Event","Jet_algo","R"])["nTracks"].rank(method="first",ascending=False)
#df_jets300 = pd.DataFrame(jets_300)
#df_jets300['pt_rank'] = df_jets300.groupby(["Event","Jet_algo","R"])["pt"].rank(method="first",ascending=False)
#df_jets300['multi_rank'] = df_jets300.groupby(["Event","Jet_algo","R"])["nTracks"].rank(method="first",ascending=False)
#df_jets200 = pd.DataFrame(jets_200)
#df_jets200['pt_rank'] = df_jets200.groupby(["Event","Jet_algo","R"])["pt"].rank(method="first",ascending=False)
#df_jets200['multi_rank'] = df_jets200.groupby(["Event","Jet_algo","R"])["nTracks"].rank(method="first",ascending=False)

#print(df_jets1000[["suep_tracks","total_suep","suep_frac"]].loc[df_jets1000["suep_frac"]>1]) # can have frac greater than 1 due to false matching from tracks
#df_jets1000["suep_frac"] = df_jets1000["suep_frac"].clip(upper=1)
#df_jets400["suep_frac"] = df_jets400["suep_frac"].clip(upper=1)
#print(df_jets1000)

#df_jetsqcd = df_jetsqcd[df_jetsqcd['multi_rank'] == 1]
#df_jets1000 = df_jets1000[df_jets1000['multi_rank'] == 1]
#df_jets400 = df_jets400[df_jets400['multi_rank'] == 1]
#df_jets750 = df_jets750[df_jets750['multi_rank'] == 1]
#df_jets300 = df_jets300[df_jets300['multi_rank'] == 1]
#df_jets200 = df_jets200[df_jets200['multi_rank'] == 1]
#df_jetsqcd = df_jetsqcd[(df_jetsqcd["mass"] > 150) & (df_jetsqcd["trackpt"] < 0.01) & (df_jetsqcd['multi_rank'] == 1)]
#df_jets1000 = df_jets1000[(df_jets1000["nTracks"] > 85) & (df_jets1000["mass"] > 150) & (df_jets1000["trackpt"] < 0.05) & (df_jets1000['multi_rank'] == 1)]
#df_jets400 = df_jets400[(df_jets400["mass"] > 150) & (df_jets400["trackpt"] < 0.01) & ( df_jets400['multi_rank'] == 1)]

#df_jetsqcd = df_jetsqcd[df_jetsqcd['pt_rank'] == 1]
#df_jets1000 = df_jets1000[df_jets1000['pt_rank'] == 1]
#df_jets400 = df_jets400[df_jets400['pt_rank'] == 1]

gc.collect()
df_jets1000["suep_frac"] = df_jets1000["suep_tracks"]/df_jets1000["total_suep"]
df_jets1000["suep_purity"] = df_jets1000["suep_tracks"]/(df_jets1000["isr_tracks"]+df_jets1000["suep_tracks"])
df_jets1000["is_suep"] = df_jets1000["suep_purity"].apply(lambda x: 1 if x > 0.8 else 0) 
df_jets400["suep_frac"] = df_jets400["suep_tracks"]/df_jets400["total_suep"]
df_jets400["suep_purity"] = df_jets400["suep_tracks"]/(df_jets400["isr_tracks"]+df_jets400["suep_tracks"])
df_jets400["is_suep"] = df_jets400["suep_purity"].apply(lambda x: 1 if x > 0.8 else 0) 
df_jetsqcd["suep_frac"] = 0
df_jetsqcd["suep_purity"] = 0
df_jetsqcd["is_suep"] = 0
df_jets750["suep_frac"] = df_jets750["suep_tracks"]/df_jets750["total_suep"]
df_jets750["suep_purity"] = df_jets750["suep_tracks"]/(df_jets750["isr_tracks"]+df_jets750["suep_tracks"])
df_jets750["is_suep"] = df_jets750["suep_purity"].apply(lambda x: 1 if x > 0.8 else 0) 
df_jets300["suep_frac"] = df_jets300["suep_tracks"]/df_jets300["total_suep"]
df_jets300["suep_purity"] = df_jets300["suep_tracks"]/(df_jets300["isr_tracks"]+df_jets300["suep_tracks"])
df_jets300["is_suep"] = df_jets300["suep_purity"].apply(lambda x: 1 if x > 0.8 else 0) 
df_jets200["suep_frac"] = df_jets200["suep_tracks"]/df_jets200["total_suep"]
df_jets200["suep_purity"] = df_jets200["suep_tracks"]/(df_jets200["isr_tracks"]+df_jets200["suep_tracks"])
df_jets200["is_suep"] = df_jets200["suep_purity"].apply(lambda x: 1 if x > 0.8 else 0) 

df_jets1000["phi"] = df_jets1000["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x) 
df_jets400["phi"] = df_jets400["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x) 
df_jetsqcd["phi"] = df_jetsqcd["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x) 
df_jets750["phi"] = df_jets750["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x) 
df_jets300["phi"] = df_jets300["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x) 
df_jets200["phi"] = df_jets200["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x) 

df_jets1000["pt_res"] = (df_jets1000["pt"] - df_jets1000["scalarpt"])/df_jets1000["scalarpt"]
df_jets1000["mass_res"] = (df_jets1000["mass"] - df_jets1000["scalarmass"])/df_jets1000["scalarmass"]
df_jets1000["beta_res"] = (df_jets1000["beta"] - df_jets1000["scalarbeta"])/df_jets1000["scalarbeta"]
df_jets400["pt_res"] = (df_jets400["pt"] - df_jets400["scalarpt"])/df_jets400["scalarpt"]
df_jets400["mass_res"] = (df_jets400["mass"] - df_jets400["scalarmass"])/df_jets400["scalarmass"]
df_jets400["beta_res"] = (df_jets400["beta"] - df_jets400["scalarbeta"])/df_jets400["scalarbeta"]
df_jetsqcd["pt_res"] = (df_jetsqcd["pt"] - df_jetsqcd["scalarpt"])/df_jetsqcd["scalarpt"]
df_jetsqcd["mass_res"] = (df_jetsqcd["mass"] - df_jetsqcd["scalarmass"])/df_jetsqcd["scalarmass"]
df_jetsqcd["beta_res"] = (df_jetsqcd["beta"] - df_jetsqcd["scalarbeta"])/df_jetsqcd["scalarbeta"]
df_jets750["pt_res"] = (df_jets750["pt"] - df_jets750["scalarpt"])/df_jets750["scalarpt"]
df_jets750["mass_res"] = (df_jets750["mass"] - df_jets750["scalarmass"])/df_jets750["scalarmass"]
df_jets750["beta_res"] = (df_jets750["beta"] - df_jets750["scalarbeta"])/df_jets750["scalarbeta"]
df_jets300["pt_res"] = (df_jets300["pt"] - df_jets300["scalarpt"])/df_jets300["scalarpt"]
df_jets300["mass_res"] = (df_jets300["mass"] - df_jets300["scalarmass"])/df_jets300["scalarmass"]
df_jets300["beta_res"] = (df_jets300["beta"] - df_jets300["scalarbeta"])/df_jets300["scalarbeta"]
df_jets200["pt_res"] = (df_jets200["pt"] - df_jets200["scalarpt"])/df_jets200["scalarpt"]
df_jets200["mass_res"] = (df_jets200["mass"] - df_jets200["scalarmass"])/df_jets200["scalarmass"]
df_jets200["beta_res"] = (df_jets200["beta"] - df_jets200["scalarbeta"])/df_jets200["scalarbeta"]

df_jets1000["t21"] = df_jets1000["t2"]/ df_jets1000["t1"]
df_jets1000["t32"] = df_jets1000["t3"]/ df_jets1000["t2"]
df_jets200["t21"] = df_jets200["t2"]/ df_jets200["t1"]
df_jets200["t32"] = df_jets200["t3"]/ df_jets200["t2"]
df_jets300["t21"] = df_jets300["t2"]/ df_jets300["t1"]
df_jets300["t32"] = df_jets300["t3"]/ df_jets300["t2"]
df_jets400["t21"] = df_jets400["t2"]/ df_jets400["t1"]
df_jets400["t32"] = df_jets400["t3"]/ df_jets400["t2"]
df_jets750["t21"] = df_jets750["t2"]/ df_jets750["t1"]
df_jets750["t32"] = df_jets750["t3"]/ df_jets750["t2"]
df_jetsqcd["t21"] = df_jetsqcd["t2"]/ df_jetsqcd["t1"]
df_jetsqcd["t32"] = df_jetsqcd["t3"]/ df_jetsqcd["t2"]
#isr_id = df_jets1000[(df_jets1000["girth"] >0.34) & (df_jets1000["mass"] > 60) & (df_jets1000["trackpt"] < 0.08) & (df_jets1000["nTracks"] > 135) & (df_jets1000["medpt"]<0.7)]

gc.collect()
#all_signifs = []
#for algo in [-1,0,1]:
#  for Ri in [0.8,1.0,1.5,2.0]:
#    sig_id_specific = df_jets1000[(df_jets1000["Jet_algo"] == algo) & (df_jets1000["R"] == Ri)]
#    bkg_id_specific = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algo) & (df_jetsqcd["R"] == Ri)]
#    print(algo,Ri)
#    for igirth in [0]:#[x*0.001 for x in range(0,50,1)]:
#      sig_girth = sig_id_specific[sig_id_specific["girth"] > igirth]
#      bkg_girth = bkg_id_specific[bkg_id_specific["girth"] > igirth]
#      for imass in [x for x in range(150,200,5)]:
#        print(igirth,imass)
#        sig_mass = sig_girth[sig_girth["mass"] > imass]
#        bkg_mass = bkg_girth[bkg_girth["mass"] > imass]
#        for itrkpt in [x*0.001 for x in range(0,50,1)]:#[.01]
#          sig_trkpt = sig_mass[sig_mass["trackpt"]< itrkpt]
#          bkg_trkpt = bkg_mass[bkg_mass["trackpt"]< itrkpt]
#          for imedpt in [.04]:#][x*0.001 for x in range(0,20,1)]:
#            sig_medpt = sig_trkpt[sig_trkpt["medpt"] < imedpt]
#            bkg_medpt = bkg_trkpt[bkg_trkpt["medpt"] < imedpt]
#            for itrk in [x for x in range(80,200,5)]: 
#              sig_trk = sig_medpt[sig_medpt["nTracks"]> itrk]
#              bkg_trk = bkg_medpt[bkg_medpt["nTracks"]> itrk]
#              #sig_trk = sig_id_specific[(sig_id_specific["girth"] > igirth)  & (sig_id_specific["mass"] > imass) & (sig_id_specific["trackpt"]< itrkpt) & (sig_id_specific["medpt"] < imedpt) & (sig_id_specific["nTracks"] > itrk)]
#              #bkg_trk = bkg_id_specific[(bkg_id_specific["girth"] > igirth)  & (bkg_id_specific["mass"] > imass) & (bkg_id_specific["trackpt"]< itrkpt) & (bkg_id_specific["medpt"] < imedpt) & (bkg_id_specific["nTracks"] > itrk)]
#              sig_id = sig_trk["xsec"].sum()
#              bkg_id = bkg_trk["xsec"].sum()
#              signif = sig_id/np.sqrt(sig_id+bkg_id)
#              all_signifs.append({"algo":algo,"R":Ri,"signif":signif,"signal":sig_id,"background":bkg_id,"girth":igirth,"mass":imass,"trkpt":itrkpt,"medpt":imedpt,"nTracks":itrk})
#              #print("%d %.1f %f %f %f [%f %f %f %f %f]"%(algo,Ri,signif,sig_id,bkg_id,igirth,imass,itrkpt,imedpt,itrk))
#df_signifs = pd.DataFrame(all_signifs)
#print(df_signifs[(df_signifs["algo"] == -1) & (df_signifs["R"] == 0.8)].nlargest(50,"signif"))
#print(df_signifs[(df_signifs["algo"] == -1) & (df_signifs["R"] == 1.0)].nlargest(50,"signif"))
#print(df_signifs[(df_signifs["algo"] == -1) & (df_signifs["R"] == 1.5)].nlargest(50,"signif"))
#print(df_signifs[(df_signifs["algo"] == -1) & (df_signifs["R"] == 2.0)].nlargest(50,"signif"))
#print(df_signifs[(df_signifs["algo"] == 0) & (df_signifs["R"] == 0.8)].nlargest(50,"signif"))
#print(df_signifs[(df_signifs["algo"] == 0) & (df_signifs["R"] == 1.0)].nlargest(50,"signif"))
#print(df_signifs[(df_signifs["algo"] == 0) & (df_signifs["R"] == 1.5)].nlargest(50,"signif"))
#print(df_signifs[(df_signifs["algo"] == 0) & (df_signifs["R"] == 2.0)].nlargest(50,"signif"))
#print(df_signifs[(df_signifs["algo"] == 1) & (df_signifs["R"] == 0.8)].nlargest(50,"signif"))
#print(df_signifs[(df_signifs["algo"] == 1) & (df_signifs["R"] == 1.0)].nlargest(50,"signif"))
#print(df_signifs[(df_signifs["algo"] == 1) & (df_signifs["R"] == 1.5)].nlargest(50,"signif"))
#print(df_signifs[(df_signifs["algo"] == 1) & (df_signifs["R"] == 2.0)].nlargest(50,"signif"))
sig_offset = 5
def get_sig(algo,R,var,steps):
  jet1_df = df_jets1000[(df_jets1000["Jet_algo"] == algo) & (df_jets1000["R"] == R) & (df_jets1000["is_suep"] == 1)]
  jet2_df = df_jets400[(df_jets400["Jet_algo"] == algo) & (df_jets400["R"] == R) & (df_jets400["is_suep"] == 1)]
  jet3_df = df_jets750[(df_jets750["Jet_algo"] == algo) & (df_jets750["R"] == R) & (df_jets750["is_suep"] == 1)]
  jet4_df = df_jets300[(df_jets300["Jet_algo"] == algo) & (df_jets300["R"] == R) & (df_jets300["is_suep"] == 1)]
  jet5_df = df_jets200[(df_jets200["Jet_algo"] == algo) & (df_jets200["R"] == R) & (df_jets200["is_suep"] == 1)]

  sig1 = []
  sig2 = []
  sig3 = []
  sig4 = []
  sig5 = []
  tot_sig1 = jet1_df["xsec"].sum() 
  tot_sig2 = jet2_df["xsec"].sum() 
  tot_sig3 = jet3_df["xsec"].sum() 
  tot_sig4 = jet4_df["xsec"].sum() 
  tot_sig5 = jet5_df["xsec"].sum() 
  for i in steps: 
    if 'trackpt' in var or 'medpt' or 'pt_dispersion' or 'lesHouches' or 'thrust' in var:
      sig1.append(jet1_df[jet1_df[var] < i]["xsec"].sum()) 
      sig2.append(jet2_df[jet2_df[var] < i]["xsec"].sum()) 
      sig3.append(jet3_df[jet3_df[var] < i]["xsec"].sum()) 
      sig4.append(jet4_df[jet4_df[var] < i]["xsec"].sum()) 
      sig5.append(jet5_df[jet5_df[var] < i]["xsec"].sum()) 
    else:
      sig1.append(jet1_df[jet1_df[var] > i]["xsec"].sum()) 
      sig2.append(jet2_df[jet2_df[var] > i]["xsec"].sum()) 
      sig3.append(jet3_df[jet3_df[var] > i]["xsec"].sum()) 
      sig4.append(jet4_df[jet4_df[var] > i]["xsec"].sum()) 
      sig5.append(jet5_df[jet5_df[var] > i]["xsec"].sum()) 
  return(sig1,sig2,sig3,sig4,sig5,tot_sig1,tot_sig2,tot_sig3,tot_sig4,tot_sig5)
def get_bkg(algo,R,var,steps):
  jet1_df = df_jets1000[(df_jets1000["Jet_algo"] == algo) & (df_jets1000["R"] == R) & (df_jets1000["is_suep"] == 0)]
  jet2_df = df_jets400[(df_jets400["Jet_algo"] == algo) & (df_jets400["R"] == R) & (df_jets400["is_suep"] == 0)]
  qcd_df = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algo) & (df_jetsqcd["R"] == R)]

  isr1 = []
  isr2 = []
  qcd = []
  bkg1 = []
  bkg2 = []
  tot_isr1 = jet1_df["xsec"].sum() 
  tot_isr2 = jet2_df["xsec"].sum() 
  tot_qcd  = qcd_df["xsec"].sum() 
  tot_bkg1 = qcd_df["xsec"].sum() + jet1_df["xsec"].sum() 
  tot_bkg2 = qcd_df["xsec"].sum() + jet2_df["xsec"].sum() 
  for i in steps: 
    if 'trackpt' in var or 'medpt' or 'pt_dispersion' or 'lesHouches' or 'thrust' in var:
      isr1.append(jet1_df[jet1_df[var] < i]["xsec"].sum()) 
      isr2.append(jet2_df[jet2_df[var] < i]["xsec"].sum()) 
      qcd.append(qcd_df[qcd_df[var] < i]["xsec"].sum())
      bkg1.append((qcd_df[qcd_df[var] < i]["xsec"].sum())+(jet1_df[jet1_df[var] < i]["xsec"].sum()))
      bkg2.append((qcd_df[qcd_df[var] < i]["xsec"].sum())+(jet2_df[jet2_df[var] < i]["xsec"].sum()))
    else:
      isr1.append(jet1_df[jet1_df[var] > i]["xsec"].sum()) 
      isr2.append(jet2_df[jet2_df[var] > i]["xsec"].sum()) 
      qcd.append((qcd_df[qcd_df[var] > i]["xsec"].sum()))
      bkg1.append((qcd_df[qcd_df[var] > i]["xsec"].sum())+(jet1_df[jet1_df[var] > i]["xsec"].sum()))
      bkg2.append((qcd_df[qcd_df[var] > i]["xsec"].sum())+(jet2_df[jet2_df[var] > i]["xsec"].sum()))
  return(qcd,isr1,isr2,bkg1,bkg2,tot_qcd,tot_isr1,tot_isr2,tot_bkg1,tot_bkg2)

def make_all_sig(var,steps):
  algo_set = []
  #for algo in ["AKT","KT","CA"]:
  for algo in [-1,0,1]:
    R_set = []
    for R in [0.8,1.0,1.5,2.0]:
      R_set.append(get_sig(algo,R,var,steps))
    algo_set.append(R_set)
  return algo_set
def make_all_bkg(var,steps):
  algo_set = []
  #for algo in ["AKT","KT","CA"]:
  for algo in [-1,0,1]:
    R_set = []
    for R in [0.8,1.0,1.5,2.0]:
      R_set.append(get_bkg(algo,R,var,steps))
    algo_set.append(R_set)
  return algo_set

def make_eff_algo_roc(var,steps,xtitle):
  sig_set = make_all_sig(var,steps)
  bkg_set = make_all_bkg(var,steps)
  alg_name = ["AKT","CA","KT"]
  #algs = [-1,0,1]
  Rs = [0.8,1.0,1.5,2.0]
  sigs = ["Sig1000","Sig400","Sig750","Sig300","Sig200"]
  bkgs = ["qcd","isr","bkg"]
  for bkg in [0]:#,1,2]: only do qcd for now. no ISR
    for sig in [0,1,2,3,4]:
      for i in [0,1,2]:
        if bkg == 0:
          bkg_x=0
        if bkg == 1:
          bkg_x=1+sig
        if bkg == 2:
          bkg_x=3+sig
        fig, (ax1,ax2) = plt.subplots(1,2)
        fig.suptitle("%s %s %s: %s"%(sigs[sig],bkgs[bkg],alg_name[i],var))
        ax1.set_xlabel(xtitle)
        ax1.set_ylabel("S/sqrt(S+B)")


        ax1.errorbar(steps,sig_set[i][0][sig]/(np.sqrt(np.add(sig_set[i][0][sig],bkg_set[i][0][bkg_x]))),(sig_set[i][0][sig]/(np.sqrt(np.add(sig_set[i][0][sig],bkg_set[i][0][bkg_x]))))*(np.sqrt(np.add(np.reciprocal(sig_set[i][0][sig]),np.reciprocal(4*np.add(sig_set[i][0][sig],bkg_set[i][0][bkg_x]))))),errorevery=int(len(steps)/20),ecolor='lightblue', label="R=0.8", color="blue")
        ax1.errorbar(steps,sig_set[i][1][sig]/(np.sqrt(np.add(sig_set[i][1][sig],bkg_set[i][1][bkg_x]))),(sig_set[i][1][sig]/(np.sqrt(np.add(sig_set[i][1][sig],bkg_set[i][1][bkg_x]))))*(np.sqrt(np.add(np.reciprocal(sig_set[i][1][sig]),np.reciprocal(4*np.add(sig_set[i][1][sig],bkg_set[i][1][bkg_x]))))),errorevery=int(len(steps)/20),ecolor='coral', label="R=1.0", color="orange")
        ax1.errorbar(steps,sig_set[i][2][sig]/(np.sqrt(np.add(sig_set[i][2][sig],bkg_set[i][2][bkg_x]))),(sig_set[i][2][sig]/(np.sqrt(np.add(sig_set[i][2][sig],bkg_set[i][2][bkg_x]))))*(np.sqrt(np.add(np.reciprocal(sig_set[i][2][sig]),np.reciprocal(4*np.add(sig_set[i][2][sig],bkg_set[i][2][bkg_x]))))),errorevery=int(len(steps)/20),ecolor='lightgreen', label="R=1.5", color="green")
        ax1.errorbar(steps,sig_set[i][3][sig]/(np.sqrt(np.add(sig_set[i][3][sig],bkg_set[i][3][bkg_x]))),(sig_set[i][3][sig]/(np.sqrt(np.add(sig_set[i][3][sig],bkg_set[i][3][bkg_x]))))*(np.sqrt(np.add(np.reciprocal(sig_set[i][3][sig]),np.reciprocal(4*np.add(sig_set[i][3][sig],bkg_set[i][3][bkg_x]))))),errorevery=int(len(steps)/20),ecolor='indianred', label="R=2.0", color="red")
        ax1.legend(loc="upper left")

        ax2.set_xlabel(xtitle)
        ax2.set_ylabel("Efficiency")
        ax2.errorbar(steps,sig_set[i][0][sig]/sig_set[i][0][sig+sig_offset],(sig_set[i][0][sig]/sig_set[i][0][sig+sig_offset])*np.sqrt(np.add(np.reciprocal(sig_set[i][0][sig]),np.reciprocal(sig_set[i][0][sig+sig_offset]))), label="Sig R=0.8",errorevery=int(len(steps)/10),ecolor='lightblue', color="blue", linestyle="-")
        ax2.errorbar(steps,sig_set[i][1][sig]/sig_set[i][1][sig+sig_offset],(sig_set[i][1][sig]/sig_set[i][1][sig+sig_offset])*np.sqrt(np.add(np.reciprocal(sig_set[i][1][sig]),np.reciprocal(sig_set[i][1][sig+sig_offset]))), label="Sig R=1.0",errorevery=int(len(steps)/10),ecolor='coral', color="orange", linestyle="-")
        ax2.errorbar(steps,sig_set[i][2][sig]/sig_set[i][2][sig+sig_offset],(sig_set[i][2][sig]/sig_set[i][2][sig+sig_offset])*np.sqrt(np.add(np.reciprocal(sig_set[i][2][sig]),np.reciprocal(sig_set[i][2][sig+sig_offset]))), label="Sig R=1.5",errorevery=int(len(steps)/10),ecolor='lightgreen', color="green", linestyle="-")
        ax2.errorbar(steps,sig_set[i][3][sig]/sig_set[i][3][sig+sig_offset],(sig_set[i][3][sig]/sig_set[i][3][sig+sig_offset])*np.sqrt(np.add(np.reciprocal(sig_set[i][3][sig]),np.reciprocal(sig_set[i][3][sig+sig_offset]))), label="Sig R=2.0",errorevery=int(len(steps)/10),ecolor='indianred', color="red", linestyle="-")


        ax2.errorbar(steps,bkg_set[i][0][bkg_x]/bkg_set[i][0][bkg_x+5],(bkg_set[i][0][bkg_x]/bkg_set[i][0][bkg_x+5])*np.sqrt(np.add(np.reciprocal(bkg_set[i][0][bkg_x]),np.reciprocal(bkg_set[i][0][bkg_x+5]))), errorevery=int(len(steps)/10),ecolor='lightblue', label="Bkg R=0.8", color="blue", linestyle=":")
        ax2.errorbar(steps,bkg_set[i][1][bkg_x]/bkg_set[i][1][bkg_x+5],(bkg_set[i][1][bkg_x]/bkg_set[i][1][bkg_x+5])*np.sqrt(np.add(np.reciprocal(bkg_set[i][1][bkg_x]),np.reciprocal(bkg_set[i][1][bkg_x+5]))), errorevery=int(len(steps)/10),ecolor='coral', label="Bkg R=1.0", color="orange", linestyle=":")
        ax2.errorbar(steps,bkg_set[i][2][bkg_x]/bkg_set[i][2][bkg_x+5],(bkg_set[i][2][bkg_x]/bkg_set[i][2][bkg_x+5])*np.sqrt(np.add(np.reciprocal(bkg_set[i][2][bkg_x]),np.reciprocal(bkg_set[i][2][bkg_x+5]))), errorevery=int(len(steps)/10),ecolor='lightgreen', label="Bkg R=1.5", color="green", linestyle=":")
        ax2.errorbar(steps,bkg_set[i][3][bkg_x]/bkg_set[i][3][bkg_x+5],(bkg_set[i][3][bkg_x]/bkg_set[i][3][bkg_x+5])*np.sqrt(np.add(np.reciprocal(bkg_set[i][3][bkg_x]),np.reciprocal(bkg_set[i][3][bkg_x+5]))), errorevery=int(len(steps)/10),ecolor='indianred', label="Bkg R=2.0", color="red", linestyle=":")
        ax2.legend(loc="upper right")
        fig.tight_layout()
        Path("Plots/ROC/bkg_%s/%s"%(bkgs[bkg],var)).mkdir(parents=True,exist_ok=True)
        fig.savefig("Plots/ROC/bkg_%s/%s/%s_%s.png"%(bkgs[bkg],var,sigs[sig],alg_name[i]))
        plt.close()

      for i in [0,1,2,3]:
        fig, (ax1,ax2) = plt.subplots(1,2)
        fig.suptitle("%s R%s: %s"%(sigs[sig],Rs[i],var))
        ax1.set_xlabel(xtitle)
        ax1.set_ylabel("S/sqrt(S+B)")
        ax1.errorbar(steps,sig_set[0][i][sig]/(np.sqrt(np.add(sig_set[0][i][sig],bkg_set[0][i][bkg_x]))),(sig_set[0][i][sig]/(np.sqrt(np.add(sig_set[0][i][sig],bkg_set[0][i][bkg_x]))))*(np.sqrt(np.add(np.reciprocal(sig_set[0][i][sig]),np.reciprocal(4*np.add(sig_set[0][i][sig],bkg_set[0][i][bkg_x]))))),errorevery=int(len(steps)/20),ecolor='lightblue', label="AKT", color="blue")
        ax1.errorbar(steps,sig_set[1][i][sig]/(np.sqrt(np.add(sig_set[1][i][sig],bkg_set[1][i][bkg_x]))),(sig_set[1][i][sig]/(np.sqrt(np.add(sig_set[1][i][sig],bkg_set[1][i][bkg_x]))))*(np.sqrt(np.add(np.reciprocal(sig_set[1][i][sig]),np.reciprocal(4*np.add(sig_set[1][i][sig],bkg_set[1][i][bkg_x]))))),errorevery=int(len(steps)/20),ecolor='coral', label="CA", color="orange")
        ax1.errorbar(steps,sig_set[2][i][sig]/(np.sqrt(np.add(sig_set[2][i][sig],bkg_set[2][i][bkg_x]))),(sig_set[2][i][sig]/(np.sqrt(np.add(sig_set[2][i][sig],bkg_set[2][i][bkg_x]))))*(np.sqrt(np.add(np.reciprocal(sig_set[2][i][sig]),np.reciprocal(4*np.add(sig_set[2][i][sig],bkg_set[2][i][bkg_x]))))),errorevery=int(len(steps)/20),ecolor='lightgreen', label="KT", color="green")
        ax1.legend(loc="upper left")

        ax2.set_xlabel(xtitle)
        ax2.set_ylabel("Efficiency")
        ax2.errorbar(steps,sig_set[0][i][sig]/sig_set[0][i][sig+sig_offset],(sig_set[0][i][sig]/sig_set[0][i][sig+sig_offset])*np.sqrt(np.add(np.reciprocal(sig_set[0][i][sig]),np.reciprocal(sig_set[0][i][sig+sig_offset]))), errorevery=int(len(steps)/10),ecolor='lightblue', label="Sig AKT", color="blue", linestyle="-")
        ax2.errorbar(steps,sig_set[1][i][sig]/sig_set[1][i][sig+sig_offset],(sig_set[1][i][sig]/sig_set[1][i][sig+sig_offset])*np.sqrt(np.add(np.reciprocal(sig_set[1][i][sig]),np.reciprocal(sig_set[1][i][sig+sig_offset]))), errorevery=int(len(steps)/10),ecolor='coral', label="Sig CA", color="orange", linestyle="-")
        ax2.errorbar(steps,sig_set[2][i][sig]/sig_set[2][i][sig+sig_offset],(sig_set[2][i][sig]/sig_set[2][i][sig+sig_offset])*np.sqrt(np.add(np.reciprocal(sig_set[2][i][sig]),np.reciprocal(sig_set[2][i][sig+sig_offset]))), errorevery=int(len(steps)/10),ecolor='lightgreen', label="Sig KT", color="green", linestyle="-")

        ax2.errorbar(steps,bkg_set[0][i][bkg_x]/bkg_set[0][i][bkg_x+5],(bkg_set[0][i][bkg_x]/bkg_set[0][i][bkg_x+5])*np.sqrt(np.add(np.reciprocal(bkg_set[0][i][bkg_x]),np.reciprocal(bkg_set[0][i][bkg_x+5]))), errorevery=int(len(steps)/10),ecolor='lightblue', label="Bkg AKT", color="blue", linestyle=":")
        ax2.errorbar(steps,bkg_set[1][i][bkg_x]/bkg_set[1][i][bkg_x+5],(bkg_set[1][i][bkg_x]/bkg_set[1][i][bkg_x+5])*np.sqrt(np.add(np.reciprocal(bkg_set[1][i][bkg_x]),np.reciprocal(bkg_set[1][i][bkg_x+5]))), errorevery=int(len(steps)/10),ecolor='coral', label="Bkg CA", color="orange", linestyle=":")
        ax2.errorbar(steps,bkg_set[2][i][bkg_x]/bkg_set[2][i][bkg_x+5],(bkg_set[2][i][bkg_x]/bkg_set[2][i][bkg_x+5])*np.sqrt(np.add(np.reciprocal(bkg_set[2][i][bkg_x]),np.reciprocal(bkg_set[2][i][bkg_x+5]))), errorevery=int(len(steps)/10),ecolor='lightgreen', label="Bkg KT", color="green", linestyle=":")
        ax2.legend(loc="upper right")
        fig.tight_layout()
        Path("Plots/ROC/bkg_%s/%s"%(bkgs[bkg],var)).mkdir(parents=True,exist_ok=True)
        fig.savefig("Plots/ROC/bkg_%s/%s/%s_%s.png"%(bkgs[bkg],var,sigs[sig],Rs[i]))
        plt.close()


def make_eff_algo_combo(var,steps,xtitle):
  sig_set = make_all_sig(var,steps)
  bkg_set = make_all_bkg(var,steps)
  alg_name = ["AKT","CA","KT"]
  algs = [-1,0,1]
  Rs = [0.8,1.0,1.5,2.0]
  sigs = ["Sig1000","Sig400","Sig750","Sig300","Sig200"]
  bkgs = ["qcd","isr","bkg"]
  for bkg in [0]:#,1,2]:
    for sig in [0,1,2,3,4]:
      for i in [0,1,2]:
        for r in [0,1,2,3]:
          if sig == 0:
            jet1_df = df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[r]) & (df_jets1000["is_suep"] == 1)]
            isr_df = df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[r]) & (df_jets1000["is_suep"] == 0)]
          if sig == 1:
            jet1_df = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[r]) & (df_jets400["is_suep"] == 1)]
            isr_df = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[r]) & (df_jets400["is_suep"] == 0)]
          if sig == 2:
            jet1_df = df_jets750[(df_jets750["Jet_algo"] == algs[i]) & (df_jets750["R"] == Rs[r]) & (df_jets750["is_suep"] == 1)]
            isr_df = df_jets750[(df_jets750["Jet_algo"] == algs[i]) & (df_jets750["R"] == Rs[r]) & (df_jets750["is_suep"] == 0)]
          if sig == 3:
            jet1_df = df_jets300[(df_jets300["Jet_algo"] == algs[i]) & (df_jets300["R"] == Rs[r]) & (df_jets300["is_suep"] == 1)]
            isr_df = df_jets300[(df_jets300["Jet_algo"] == algs[i]) & (df_jets300["R"] == Rs[r]) & (df_jets300["is_suep"] == 0)]
          if sig == 4:
            jet1_df = df_jets200[(df_jets200["Jet_algo"] == algs[i]) & (df_jets200["R"] == Rs[r]) & (df_jets200["is_suep"] == 1)]
            isr_df = df_jets200[(df_jets200["Jet_algo"] == algs[i]) & (df_jets200["R"] == Rs[r]) & (df_jets200["is_suep"] == 0)]
          if bkg == 0:
            bkg_df = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[r])] 
            bkg_x=0
          if bkg == 1:
            bkg_df = isr_df
            bkg_x=1+sig
          if bkg == 2:
            bkg_df = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[r])].append(isr_df) 
            bkg_x=3+sig

          fig, (ax1,ax2) = plt.subplots(1,2)
          fig.suptitle("%s %s %s %s: %s"%(sigs[sig],bkgs[bkg],alg_name[i],Rs[r],var))
          ax1.set_xlabel(xtitle)
          ax1.set_ylabel("S/sqrt(S+B)")


          ax1.errorbar(steps,sig_set[i][r][sig]/(np.sqrt(np.add(sig_set[i][r][sig],bkg_set[i][r][bkg_x]))),(sig_set[i][r][sig]/(np.sqrt(np.add(sig_set[i][r][sig],bkg_set[i][r][bkg_x]))))*(np.sqrt(np.add(np.reciprocal(sig_set[i][r][sig]),np.reciprocal(4*np.add(sig_set[i][r][sig],bkg_set[i][r][bkg_x]))))),errorevery=int(len(steps)/20),ecolor='lightblue', label="R=%s"%Rs[r], color="blue")
          ax1x = ax1.twinx()
          plt.yscale('log')
          ax1x.set_ylabel('Events')
          ax1x.hist(jet1_df[var],range=[steps[0],steps[-1]],weights=jet1_df['xsec'],bins=20,alpha=0.2,color='blue',label=sigs[sig])
          ax1x.hist(bkg_df[var],range=[steps[0],steps[-1]],weights=bkg_df['xsec'],bins=20,alpha=0.2,color='red',label=bkgs[bkg])
          ax1x.legend(loc="upper right")

          ax2.set_xlabel(xtitle)
          ax2.set_ylabel("Efficiency")
          ax2.errorbar(steps,sig_set[i][r][sig]/sig_set[i][r][sig+sig_offset],(sig_set[i][r][sig]/sig_set[i][r][sig+sig_offset])*np.sqrt(np.add(np.reciprocal(sig_set[i][r][sig]),np.reciprocal(sig_set[i][r][sig+sig_offset]))), label="Sig R=%s"%Rs[r],errorevery=int(len(steps)/10),ecolor='lightblue', color="blue", linestyle="-")
          ax2.errorbar(steps,bkg_set[i][r][bkg_x]/bkg_set[i][r][bkg_x+5],(bkg_set[i][r][bkg_x]/bkg_set[i][r][bkg_x+5])*np.sqrt(np.add(np.reciprocal(bkg_set[i][r][bkg_x]),np.reciprocal(bkg_set[i][r][bkg_x+5]))), errorevery=int(len(steps)/10),ecolor='lightblue', label="Bkg R=%s"%Rs[r], color="blue", linestyle=":")
          ax2x = ax2.twinx()
          ax2x.set_ylabel('A.U.')
          ax2x.hist(jet1_df[var],range=[steps[0],steps[-1]],weights=np.ones_like(jet1_df[var])/len(jet1_df[var]),bins=20,alpha=0.2,color='blue')
          ax2x.hist(bkg_df[var],range=[steps[0],steps[-1]],weights=np.ones_like(bkg_df[var])/len(bkg_df[var]),bins=20,alpha=0.2,color='red')
          ax2.legend(loc="upper right")
          fig.tight_layout()
          Path("Plots/COMBO/bkg_%s/%s"%(bkgs[bkg],var)).mkdir(parents=True,exist_ok=True)
          fig.savefig("Plots/COMBO/bkg_%s/%s/%s_%s_%s.png"%(bkgs[bkg],var,sigs[sig],alg_name[i],Rs[r]))
          plt.close()

def make_eff_algo_dist(var,steps,xtitle):
  #algo_set = make_all(var,steps)
  alg_name = ["AKT","CA","KT"]
  algs = [-1,0,1]
  Rs = [0.8,1.0,1.5,2.0]
  sigs = ["Sig1000","Sig400","Sig750","Sig300","Sig200","qcd"]#,"isr1000","isr400","bkg1000","bkg400"]
  for sig in [0,1,2,3,4,5]:#,6]:
    if ((("suep" in var) or ("NVtx" in var) or ("Num" in var) or ("scalar" in var)) and sig >= 2):
      continue
    if sig == 0:
      df_jets = df_jets1000
    if sig == 1:
      df_jets = df_jets400
    if sig == 2:
      df_jets = df_jets750
    if sig == 3:
      df_jets = df_jets300
    if sig == 4:
      df_jets = df_jets200
    if sig == 5:
      df_jets = df_jetsqcd
    for i in [0,1,2]:
        if "suep" in var or "scalar" in var:
          jet1_df_1 = df_jets[(df_jets["Jet_algo"] == algs[i]) & (df_jets["R"] == Rs[0])]
          jet1_df_2 = df_jets[(df_jets["Jet_algo"] == algs[i]) & (df_jets["R"] == Rs[1])]
          jet1_df_3 = df_jets[(df_jets["Jet_algo"] == algs[i]) & (df_jets["R"] == Rs[2])]
          jet1_df_4 = df_jets[(df_jets["Jet_algo"] == algs[i]) & (df_jets["R"] == Rs[3])]
        else:
          jet1_df_1 = df_jets[(df_jets["Jet_algo"] == algs[i]) & (df_jets["R"] == Rs[0]) & (df_jets["is_suep"] == 1)]
          jet1_df_2 = df_jets[(df_jets["Jet_algo"] == algs[i]) & (df_jets["R"] == Rs[1]) & (df_jets["is_suep"] == 1)]
          jet1_df_3 = df_jets[(df_jets["Jet_algo"] == algs[i]) & (df_jets["R"] == Rs[2]) & (df_jets["is_suep"] == 1)]
          jet1_df_4 = df_jets[(df_jets["Jet_algo"] == algs[i]) & (df_jets["R"] == Rs[3]) & (df_jets["is_suep"] == 1)]
#        if sig == 1:
#          if "suep" in var or "scalar" in var:
#            jet1_df_1 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[0])]
#            jet1_df_2 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[1])]
#            jet1_df_3 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[2])]
#            jet1_df_4 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[3])]
#          else:
#            jet1_df_1 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[0]) & (df_jets400["is_suep"] == 1)]
#            jet1_df_2 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[1]) & (df_jets400["is_suep"] == 1)]
#            jet1_df_3 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[2]) & (df_jets400["is_suep"] == 1)]
#            jet1_df_4 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[3]) & (df_jets400["is_suep"] == 1)]
#        if sig == 2:
#          jet1_df_1 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[0])]
#          jet1_df_2 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[1])]
#          jet1_df_3 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[2])]
#          jet1_df_4 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[3])]
#        if sig == 3:
#          jet1_df_1 = df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[0]) & (df_jets1000["is_suep"] == 0)]
#          jet1_df_2 = df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[1]) & (df_jets1000["is_suep"] == 0)]
#          jet1_df_3 = df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[2]) & (df_jets1000["is_suep"] == 0)]
#          jet1_df_4 = df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[3]) & (df_jets1000["is_suep"] == 0)]
#        if sig == 4:
#          jet1_df_1 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[0]) & (df_jets400["is_suep"] == 0)]
#          jet1_df_2 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[1]) & (df_jets400["is_suep"] == 0)]
#          jet1_df_3 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[2]) & (df_jets400["is_suep"] == 0)]
#          jet1_df_4 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[3]) & (df_jets400["is_suep"] == 0)]
#        if sig == 5:
#          jet1_df_1 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[0])].append(df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[0]) & (df_jets1000["is_suep"] == 0)])
#          jet1_df_2 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[1])].append(df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[1]) & (df_jets1000["is_suep"] == 0)])
#          jet1_df_3 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[2])].append(df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[2]) & (df_jets1000["is_suep"] == 0)])
#          jet1_df_4 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[3])].append(df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[3]) & (df_jets1000["is_suep"] == 0)])
#        if sig == 6:
#          jet1_df_1 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[0])].append(df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[0]) & (df_jets400["is_suep"] == 0)])
#          jet1_df_2 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[1])].append(df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[1]) & (df_jets400["is_suep"] == 0)])
#          jet1_df_3 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[2])].append(df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[2]) & (df_jets400["is_suep"] == 0)])
#          jet1_df_4 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[3])].append(df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[3]) & (df_jets400["is_suep"] == 0)])

        fig, (ax1,ax2) = plt.subplots(1,2)
        fig.suptitle("%s %s: %s"%(sigs[sig],alg_name[i],var))
        ax1.set_xlabel(xtitle)
        plt.yscale('log')
        ax1.set_ylabel('Events')
        ax1.hist(jet1_df_1[var],range=[steps[0],steps[-1]],weights=jet1_df_1['xsec'],bins=20,histtype=u'step',color='blue',label="R=0.8")
        ax1.hist(jet1_df_2[var],range=[steps[0],steps[-1]],weights=jet1_df_2['xsec'],bins=20,histtype=u'step',color='orange',label="R=1.0")
        ax1.hist(jet1_df_3[var],range=[steps[0],steps[-1]],weights=jet1_df_3['xsec'],bins=20,histtype=u'step',color='green',label="R=1.5")
        ax1.hist(jet1_df_4[var],range=[steps[0],steps[-1]],weights=jet1_df_4['xsec'],bins=20,histtype=u'step',color='red',label="R=2.0")
        

        ax2.set_xlabel(xtitle)
        ax2.set_ylabel('A.U.')
        ax2.hist(jet1_df_1[var],range=[steps[0],steps[-1]],weights=np.ones_like(jet1_df_1[var])/len(jet1_df_1[var]),bins=20,histtype=u'step',color='blue',label="R=0.8")
        ax2.hist(jet1_df_2[var],range=[steps[0],steps[-1]],weights=np.ones_like(jet1_df_2[var])/len(jet1_df_2[var]),bins=20,histtype=u'step',color='orange',label="R=1.0")
        ax2.hist(jet1_df_3[var],range=[steps[0],steps[-1]],weights=np.ones_like(jet1_df_3[var])/len(jet1_df_3[var]),bins=20,histtype=u'step',color='green',label="R=1.5")
        ax2.hist(jet1_df_4[var],range=[steps[0],steps[-1]],weights=np.ones_like(jet1_df_4[var])/len(jet1_df_4[var]),bins=20,histtype=u'step',color='red',label="R=2.0")
        ax2.legend(loc="upper right")
        fig.tight_layout()
        Path("Plots/DIST/%s"%(var)).mkdir(parents=True,exist_ok=True)
        fig.savefig("Plots/DIST/%s/%s_%s.png"%(var,sigs[sig],alg_name[i]))
        plt.close()

        figbox, boxax1 = plt.subplots(1,1)
        figbox.suptitle("%s %s: %s"%(sigs[sig],alg_name[i],var))
        boxax1.boxplot([jet1_df_1[var],jet1_df_2[var],jet1_df_3[var],jet1_df_4[var]],notch=1,positions=[0,1,2,3],labels=["0.8","1.0","1.5","2.0"], sym='',vert=1)
        Path("Plots/box/%s"%(var)).mkdir(parents=True,exist_ok=True)
        figbox.savefig("Plots/box/%s/%s_%s.png"%(var,sigs[sig],alg_name[i]))
        plt.close()
    for i in [0,1,2,3]:
        #if sig == 0:
        if "suep" in var:
          jet1_df_1 = df_jets[(df_jets["Jet_algo"] == algs[0]) & (df_jets["R"] == Rs[i])]
          jet1_df_2 = df_jets[(df_jets["Jet_algo"] == algs[1]) & (df_jets["R"] == Rs[i])]
          jet1_df_3 = df_jets[(df_jets["Jet_algo"] == algs[2]) & (df_jets["R"] == Rs[i])]
        else:
          jet1_df_1 = df_jets[(df_jets["Jet_algo"] == algs[0]) & (df_jets["R"] == Rs[i]) & (df_jets["is_suep"] == 1)]
          jet1_df_2 = df_jets[(df_jets["Jet_algo"] == algs[1]) & (df_jets["R"] == Rs[i]) & (df_jets["is_suep"] == 1)]
          jet1_df_3 = df_jets[(df_jets["Jet_algo"] == algs[2]) & (df_jets["R"] == Rs[i]) & (df_jets["is_suep"] == 1)]
#        if sig == 1:
#          if "suep" in var:
#            jet1_df_1 = df_jets400[(df_jets400["Jet_algo"] == algs[0]) & (df_jets400["R"] == Rs[i])]
#            jet1_df_2 = df_jets400[(df_jets400["Jet_algo"] == algs[1]) & (df_jets400["R"] == Rs[i])]
#            jet1_df_3 = df_jets400[(df_jets400["Jet_algo"] == algs[2]) & (df_jets400["R"] == Rs[i])]
#          else:
#            jet1_df_1 = df_jets400[(df_jets400["Jet_algo"] == algs[0]) & (df_jets400["R"] == Rs[i]) & (df_jets400["is_suep"] == 1)]
#            jet1_df_2 = df_jets400[(df_jets400["Jet_algo"] == algs[1]) & (df_jets400["R"] == Rs[i]) & (df_jets400["is_suep"] == 1)]
#            jet1_df_3 = df_jets400[(df_jets400["Jet_algo"] == algs[2]) & (df_jets400["R"] == Rs[i]) & (df_jets400["is_suep"] == 1)]
#        if sig == 2:
#          jet1_df_1 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[0]) & (df_jetsqcd["R"] == Rs[i])]
#          jet1_df_2 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[1]) & (df_jetsqcd["R"] == Rs[i])]
#          jet1_df_3 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[2]) & (df_jetsqcd["R"] == Rs[i])]
#        if sig == 3:
#          jet1_df_1 = df_jets1000[(df_jets1000["Jet_algo"] == algs[0]) & (df_jets1000["R"] == Rs[i]) & (df_jets1000["is_suep"] == 0)]
#          jet1_df_2 = df_jets1000[(df_jets1000["Jet_algo"] == algs[1]) & (df_jets1000["R"] == Rs[i]) & (df_jets1000["is_suep"] == 0)]
#          jet1_df_3 = df_jets1000[(df_jets1000["Jet_algo"] == algs[2]) & (df_jets1000["R"] == Rs[i]) & (df_jets1000["is_suep"] == 0)]
#        if sig == 4:
#          jet1_df_1 = df_jets400[(df_jets400["Jet_algo"] == algs[0]) & (df_jets400["R"] == Rs[i]) & (df_jets400["is_suep"] == 0)]
#          jet1_df_2 = df_jets400[(df_jets400["Jet_algo"] == algs[1]) & (df_jets400["R"] == Rs[i]) & (df_jets400["is_suep"] == 0)]
#          jet1_df_3 = df_jets400[(df_jets400["Jet_algo"] == algs[2]) & (df_jets400["R"] == Rs[i]) & (df_jets400["is_suep"] == 0)]
#        if sig == 5:
#          jet1_df_1 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[0]) & (df_jetsqcd["R"] == Rs[i])].append(df_jets1000[(df_jets1000["Jet_algo"] == algs[0]) & (df_jets1000["R"] == Rs[i]) & (df_jets1000["is_suep"] == 0)])
#          jet1_df_2 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[1]) & (df_jetsqcd["R"] == Rs[i])].append(df_jets1000[(df_jets1000["Jet_algo"] == algs[1]) & (df_jets1000["R"] == Rs[i]) & (df_jets1000["is_suep"] == 0)])
#          jet1_df_3 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[2]) & (df_jetsqcd["R"] == Rs[i])].append(df_jets1000[(df_jets1000["Jet_algo"] == algs[2]) & (df_jets1000["R"] == Rs[i]) & (df_jets1000["is_suep"] == 0)])
#        if sig == 6:
#          jet1_df_1 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[0]) & (df_jetsqcd["R"] == Rs[i])].append(df_jets400[(df_jets400["Jet_algo"] == algs[0]) & (df_jets400["R"] == Rs[i]) & (df_jets400["is_suep"] == 0)])
#          jet1_df_2 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[1]) & (df_jetsqcd["R"] == Rs[i])].append(df_jets400[(df_jets400["Jet_algo"] == algs[1]) & (df_jets400["R"] == Rs[i]) & (df_jets400["is_suep"] == 0)])
#          jet1_df_3 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[2]) & (df_jetsqcd["R"] == Rs[i])].append(df_jets400[(df_jets400["Jet_algo"] == algs[2]) & (df_jets400["R"] == Rs[i]) & (df_jets400["is_suep"] == 0)])

        fig, (ax1,ax2) = plt.subplots(1,2)
        fig.suptitle("%s %s: %s"%(sigs[sig],Rs[i],var))
        ax1.set_xlabel(xtitle)
        plt.yscale('log')
        ax1.set_ylabel('Events')
        ax1.hist(jet1_df_1[var],range=[steps[0],steps[-1]],weights=jet1_df_1['xsec'],bins=20,histtype=u'step',color='blue',label="AKT")
        ax1.hist(jet1_df_2[var],range=[steps[0],steps[-1]],weights=jet1_df_2['xsec'],bins=20,histtype=u'step',color='orange',label="CA")
        ax1.hist(jet1_df_3[var],range=[steps[0],steps[-1]],weights=jet1_df_3['xsec'],bins=20,histtype=u'step',color='green',label="KT")

        ax2.set_xlabel(xtitle)
        ax2.set_ylabel('A.U.')
        ax2.hist(jet1_df_1[var],range=[steps[0],steps[-1]],weights=np.ones_like(jet1_df_1[var])/len(jet1_df_1[var]),bins=20,histtype=u'step',color='blue',label="AKT")
        ax2.hist(jet1_df_2[var],range=[steps[0],steps[-1]],weights=np.ones_like(jet1_df_2[var])/len(jet1_df_2[var]),bins=20,histtype=u'step',color='orange',label="CA")
        ax2.hist(jet1_df_3[var],range=[steps[0],steps[-1]],weights=np.ones_like(jet1_df_3[var])/len(jet1_df_3[var]),bins=20,histtype=u'step',color='green',label="KT")
        ax2.legend(loc="upper right")
        fig.tight_layout()
        Path("Plots/DIST/%s"%(var)).mkdir(parents=True,exist_ok=True)
        fig.savefig("Plots/DIST/%s/%s_%s.png"%(var,sigs[sig],Rs[i]))
        plt.close()

        #figbox, boxax1 = plt.subplots(1,1)
        #figbox.suptitle("%s %s: %s"%(sigs[sig],Rs[i],var))
        #boxax1.boxplot([jet1_df_1[var],jet1_df_2[var],jet1_df_3[var]],notch=1,positions=[0,1,2],labels=["AKT","CA","KT"], sym='',vert=1)
        #Path("Plots/box/%s"%(var)).mkdir(parents=True,exist_ok=True)
        #figbox.savefig("Plots/box/%s/%s_%s.png"%(var,sigs[sig],Rs[i]))
        #plt.close()

def make_eff_algo_res(var1,var2,steps,xtitle):
  #algo_set = make_all(var,steps)
  alg_name = ["AKT","CA","KT"]
  algs = [-1,0,1]
  Rs = [0.8,1.0,1.5,2.0]
  sigs = ["Sig1000","Sig400","Sig750","Sig300","Sig200","qcd"]#,"isr1000","isr400","bkg1000","bkg400"]
  for sig in [0,1,2,3,4,5]:#,6]:
    if sig == 0:
      df_jets = df_jets1000
    if sig == 1:
      df_jets = df_jets400
    if sig == 2:
      df_jets = df_jets750
    if sig == 3:
      df_jets = df_jets300
    if sig == 4:
      df_jets = df_jets200
    if sig == 5:
      df_jets = df_jetsqcd
    for i in [0,1,2]:
        #if sig == 0:
          #if "suep" in var1 or "scalar" in var1:
        jet1_df_1 = df_jets[(df_jets["Jet_algo"] == algs[i]) & (df_jets["R"] == Rs[0])]
        jet1_df_2 = df_jets[(df_jets["Jet_algo"] == algs[i]) & (df_jets["R"] == Rs[1])]
        jet1_df_3 = df_jets[(df_jets["Jet_algo"] == algs[i]) & (df_jets["R"] == Rs[2])]
        jet1_df_4 = df_jets[(df_jets["Jet_algo"] == algs[i]) & (df_jets["R"] == Rs[3])]
          #else:
          #  jet1_df_1 = df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[0]) & (df_jets1000["is_suep"] == 1)]
          #  jet1_df_2 = df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[1]) & (df_jets1000["is_suep"] == 1)]
          #  jet1_df_3 = df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[2]) & (df_jets1000["is_suep"] == 1)]
          #  jet1_df_4 = df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[3]) & (df_jets1000["is_suep"] == 1)]
#        if sig == 1:
#          #if "suep" in var1 or "scalar" in var1:
#            jet1_df_1 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[0])]
#            jet1_df_2 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[1])]
#            jet1_df_3 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[2])]
#            jet1_df_4 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[3])]
#          #else:
#          #  jet1_df_1 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[0]) & (df_jets400["is_suep"] == 1)]
#          #  jet1_df_2 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[1]) & (df_jets400["is_suep"] == 1)]
#          #  jet1_df_3 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[2]) & (df_jets400["is_suep"] == 1)]
#          #  jet1_df_4 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[3]) & (df_jets400["is_suep"] == 1)]
#        if sig == 2:
#          jet1_df_1 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[0])]
#          jet1_df_2 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[1])]
#          jet1_df_3 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[2])]
#          jet1_df_4 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[3])]

        figres, (ax1res,ax2res) = plt.subplots(1,2)
        figres.suptitle("%s %s: %s"%(sigs[sig],alg_name[i],var1))
        ax1res.set_xlabel(xtitle)
        plt.yscale('log')
        ax1res.set_ylabel('Events')
        ax1res.hist((jet1_df_1[var1]-jet1_df_1[var2])/jet1_df_1[var2],range=[steps[0],steps[-1]],weights=jet1_df_1['xsec'],bins=20,histtype=u'step',color='blue',label="R=0.8")
        ax1res.hist((jet1_df_2[var1]-jet1_df_2[var2])/jet1_df_2[var2],range=[steps[0],steps[-1]],weights=jet1_df_2['xsec'],bins=20,histtype=u'step',color='orange',label="R=1.0")
        ax1res.hist((jet1_df_3[var1]-jet1_df_3[var2])/jet1_df_3[var2],range=[steps[0],steps[-1]],weights=jet1_df_3['xsec'],bins=20,histtype=u'step',color='green',label="R=1.5")
        ax1res.hist((jet1_df_4[var1]-jet1_df_4[var2])/jet1_df_4[var2],range=[steps[0],steps[-1]],weights=jet1_df_4['xsec'],bins=20,histtype=u'step',color='red',label="R=2.0")

        ax2res.set_xlabel(xtitle)
        ax2res.set_ylabel('Events')
        ax2res.hist((jet1_df_1[var1]-jet1_df_1[var2])/jet1_df_1[var2],range=[steps[0],steps[-1]],weights=jet1_df_1['xsec'],bins=20,histtype=u'step',color='blue',label="R=0.8")
        ax2res.hist((jet1_df_2[var1]-jet1_df_2[var2])/jet1_df_2[var2],range=[steps[0],steps[-1]],weights=jet1_df_2['xsec'],bins=20,histtype=u'step',color='orange',label="R=1.0")
        ax2res.hist((jet1_df_3[var1]-jet1_df_3[var2])/jet1_df_3[var2],range=[steps[0],steps[-1]],weights=jet1_df_3['xsec'],bins=20,histtype=u'step',color='green',label="R=1.5")
        ax2res.hist((jet1_df_4[var1]-jet1_df_4[var2])/jet1_df_4[var2],range=[steps[0],steps[-1]],weights=jet1_df_4['xsec'],bins=20,histtype=u'step',color='red',label="R=2.0")
        ax2res.legend(loc="upper right")
        figres.tight_layout()
        Path("Plots/RES/%s"%(var1)).mkdir(parents=True,exist_ok=True)
        figres.savefig("Plots/RES/%s/%s_%s.png"%(var1,sigs[sig],alg_name[i]))
        plt.close()
    for i in [0,1,2,3]:
        #if sig == 0:
          #if "suep" in var1:
        jet1_df_1 = df_jets[(df_jets["Jet_algo"] == algs[0]) & (df_jets["R"] == Rs[i])]
        jet1_df_2 = df_jets[(df_jets["Jet_algo"] == algs[1]) & (df_jets["R"] == Rs[i])]
        jet1_df_3 = df_jets[(df_jets["Jet_algo"] == algs[2]) & (df_jets["R"] == Rs[i])]
          #else:
          #  jet1_df_1 = df_jets1000[(df_jets1000["Jet_algo"] == algs[0]) & (df_jets1000["R"] == Rs[i]) & (df_jets1000["is_suep"] == 1)]
          #  jet1_df_2 = df_jets1000[(df_jets1000["Jet_algo"] == algs[1]) & (df_jets1000["R"] == Rs[i]) & (df_jets1000["is_suep"] == 1)]
          #  jet1_df_3 = df_jets1000[(df_jets1000["Jet_algo"] == algs[2]) & (df_jets1000["R"] == Rs[i]) & (df_jets1000["is_suep"] == 1)]
#        if sig == 1:
#          #if "suep" in var1:
#            jet1_df_1 = df_jets400[(df_jets400["Jet_algo"] == algs[0]) & (df_jets400["R"] == Rs[i])]
#            jet1_df_2 = df_jets400[(df_jets400["Jet_algo"] == algs[1]) & (df_jets400["R"] == Rs[i])]
#            jet1_df_3 = df_jets400[(df_jets400["Jet_algo"] == algs[2]) & (df_jets400["R"] == Rs[i])]
#          #else:
#          #  jet1_df_1 = df_jets400[(df_jets400["Jet_algo"] == algs[0]) & (df_jets400["R"] == Rs[i]) & (df_jets400["is_suep"] == 1)]
#          #  jet1_df_2 = df_jets400[(df_jets400["Jet_algo"] == algs[1]) & (df_jets400["R"] == Rs[i]) & (df_jets400["is_suep"] == 1)]
#          #  jet1_df_3 = df_jets400[(df_jets400["Jet_algo"] == algs[2]) & (df_jets400["R"] == Rs[i]) & (df_jets400["is_suep"] == 1)]
#        if sig == 2:
#          jet1_df_1 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[0]) & (df_jetsqcd["R"] == Rs[i])]
#          jet1_df_2 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[1]) & (df_jetsqcd["R"] == Rs[i])]
#          jet1_df_3 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[2]) & (df_jetsqcd["R"] == Rs[i])]

        figres, (ax1res,ax2res) = plt.subplots(1,2)
        figres.suptitle("%s %s: %s"%(sigs[sig],Rs[i],var1))
        ax1res.set_xlabel(xtitle)
        plt.yscale('log')
        ax1res.set_ylabel('Events')
        ax1res.hist((jet1_df_1[var1]-jet1_df_1[var2])/jet1_df_1[var2],range=[steps[0],steps[-1]],weights=jet1_df_1['xsec'],bins=20,histtype=u'step',color='blue',label="AKT")
        ax1res.hist((jet1_df_2[var1]-jet1_df_2[var2])/jet1_df_2[var2],range=[steps[0],steps[-1]],weights=jet1_df_2['xsec'],bins=20,histtype=u'step',color='orange',label="CA")
        ax1res.hist((jet1_df_3[var1]-jet1_df_3[var2])/jet1_df_3[var2],range=[steps[0],steps[-1]],weights=jet1_df_3['xsec'],bins=20,histtype=u'step',color='green',label="KT")

        ax2res.set_xlabel(xtitle)
        ax2res.set_ylabel('Events')
        ax2res.hist((jet1_df_1[var1]-jet1_df_1[var2])/jet1_df_1[var2],range=[steps[0],steps[-1]],weights=jet1_df_1['xsec'],bins=20,histtype=u'step',color='blue',label="AKT")
        ax2res.hist((jet1_df_2[var1]-jet1_df_2[var2])/jet1_df_2[var2],range=[steps[0],steps[-1]],weights=jet1_df_2['xsec'],bins=20,histtype=u'step',color='orange',label="CA")
        ax2res.hist((jet1_df_3[var1]-jet1_df_3[var2])/jet1_df_3[var2],range=[steps[0],steps[-1]],weights=jet1_df_3['xsec'],bins=20,histtype=u'step',color='green',label="KT")
        ax2res.legend(loc="upper right")
        figres.tight_layout()
        Path("Plots/RES/%s"%(var1)).mkdir(parents=True,exist_ok=True)
        figres.savefig("Plots/RES/%s/%s_%s.png"%(var1,sigs[sig],Rs[i]))
        plt.close()
        
def make_eff_algo_dist_2d(var1,steps1,xtitle1,var2,steps2,xtitle2):
  #algo_set = make_all(var2,steps2)
  alg_name = ["AKT","CA","KT"]
  algs = [-1,0,1]
  Rs = [0.8,1.0,1.5,2.0]
  sigs = ["Sig1000","Sig400","Sig750","Sig300","Sig200"]
  for sig in [0,1,2,3,4,2,3,4]:
    for i in [0,1,2]:
      for r in [0,1,2,3]:
        if sig == 0:
          jet1_df_1 = df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[r])]
        if sig == 1:
          jet1_df_1 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[r])]
        if sig == 2:
          jet1_df_1 = df_jets750[(df_jets750["Jet_algo"] == algs[i]) & (df_jets750["R"] == Rs[r])]
        if sig == 3:
          jet1_df_1 = df_jets300[(df_jets300["Jet_algo"] == algs[i]) & (df_jets300["R"] == Rs[r])]
        if sig == 4:
          jet1_df_1 = df_jets200[(df_jets200["Jet_algo"] == algs[i]) & (df_jets200["R"] == Rs[r])]

        def func(x,y):
          value = 0 
          bin_width = (steps1[-1] - steps1[0])/len(steps1)
          if "trackpt" in var2 or "medpt" or 'pt_dispersion' or 'lesHouches' or 'thrust' in var2:
            value = value + jet1_df_1[(jet1_df_1[var2] < y) & (jet1_df_1[var1] >= x ) & (jet1_df_1[var1] < x+bin_width)]["xsec"].sum()
          else:
            value = value + jet1_df_1[(jet1_df_1[var2] > y) & (jet1_df_1[var1] >= x ) & (jet1_df_1[var1] < x+bin_width)]["xsec"].sum()
          if value == 0:
            return np.nan
          return value
    

        Xm,Ym = np.meshgrid(steps1,steps2)
        Z = np.zeros((len(steps2),len(steps1)))
        for xi,x in enumerate(steps1):
          for yi,y in enumerate(steps2):
            Z[yi,xi] = func(x,y)
        fig, (ax1,ax2) = plt.subplots(1,2)
        fig.set_size_inches(12.8,7.2)
        fig.suptitle("%s %s %s: %s vs %s"%(sigs[sig],alg_name[i],Rs[r],var1,var2))
        c = ax1.pcolormesh(Xm,Ym,Z,cmap="RdBu",shading="flat")
        fig.colorbar(c,ax=ax1) 
        ax1.set_xlabel(xtitle1)
        ax1.set_ylabel(xtitle2)
       
         
        d = ax2.hist2d(jet1_df_1[var1],jet1_df_1[var2],range=[[steps1[0],steps1[-1]],[steps2[0],steps2[-1]]],bins=[100,100],weights=jet1_df_1['xsec'],cmin=0.0000001)
        fig.colorbar(d[3],ax=ax2)
        ax2.set_xlabel(xtitle1)
        ax2.set_ylabel(xtitle2)
        Path("Plots/DIST2d/%s_%s"%(var1,var2)).mkdir(parents=True,exist_ok=True)
        fig.savefig("Plots/DIST2d/%s_%s/%s_%s_%s.png"%(var1,var2,sigs[sig],alg_name[i],Rs[r]))
        plt.close()
def make_signif_2d(var1,steps1,xtitle1,var2,steps2,xtitle2):
  #algo_set = make_all(var2,steps2)
  alg_name = ["AKT","CA","KT"]
  algs = [-1,0,1]
  Rs = [0.8,1.0,1.5,2.0]
  sigs = ["Sig1000","Sig400","Sig750","Sig300","Sig200"]
  for sig in [0,1,2,3,4,2,3,4]:
    for i in [0,1,2]:
      for r in [0,1,2,3]:
        if sig == 0:
          jet1_df_1 = df_jets1000[(df_jets1000["Jet_algo"] == algs[i]) & (df_jets1000["R"] == Rs[r])]
        if sig == 1:
          jet1_df_1 = df_jets400[(df_jets400["Jet_algo"] == algs[i]) & (df_jets400["R"] == Rs[r])]
        if sig == 2:
          jet1_df_1 = df_jets750[(df_jets750["Jet_algo"] == algs[i]) & (df_jets750["R"] == Rs[r])]
        if sig == 3:
          jet1_df_1 = df_jets300[(df_jets300["Jet_algo"] == algs[i]) & (df_jets300["R"] == Rs[r])]
        if sig == 4:
          jet1_df_1 = df_jets200[(df_jets200["Jet_algo"] == algs[i]) & (df_jets200["R"] == Rs[r])]
        bkg_df_1 = df_jetsqcd[(df_jetsqcd["Jet_algo"] == algs[i]) & (df_jetsqcd["R"] == Rs[r])]

        def func(x,y):
          value = 0 
          value_bkg = 0 
          bin_width = (steps1[-1] - steps1[0])/len(steps1)
          bin_widthy = (steps2[-1] - steps2[0])/len(steps2)
          if "trackpt" in var2 or "medpt" or 'pt_dispersion' or 'lesHouches' or 'thrust' in var2:
            value = value + jet1_df_1[(jet1_df_1[var2] < y) & (jet1_df_1[var1] >= x ) ]["xsec"].sum()
            value_bkg = value_bkg + bkg_df_1[(bkg_df_1[var2] < y) &  (bkg_df_1[var1] >= x )]["xsec"].sum()
          else:
            value = value + jet1_df_1[(jet1_df_1[var2] > y) & (jet1_df_1[var1] >= x )]["xsec"].sum()
            value_bkg = value_bkg + bkg_df_1[(bkg_df_1[var2] > y) & (bkg_df_1[var1] >= x )]["xsec"].sum()
          if value+value_bkg == 0:
            return np.nan
          return value/(np.sqrt(value+value_bkg))
    

        Xm,Ym = np.meshgrid(steps1,steps2)
        Z = np.zeros((len(steps2),len(steps1)))
        for xi,x in enumerate(steps1):
          for yi,y in enumerate(steps2):
            Z[yi,xi] = func(x,y)
        #fig, (ax1,ax2) = plt.subplots(1,2)
        fig, ax1 = plt.subplots(1,1)
        fig.set_size_inches(12.8,7.2)
        fig.suptitle("%s %s %s: %s vs %s"%(sigs[sig],alg_name[i],Rs[r],var1,var2))
        c = ax1.pcolormesh(Xm,Ym,Z,cmap="brg",shading="flat",norm=colors.Normalize(vmin=0,vmax=70))
        fig.colorbar(c,ax=ax1) 
        ax1.set_xlabel(xtitle1)
        ax1.set_ylabel(xtitle2)
       
         
        #d = ax2.hist2d(jet1_df_1[var1],jet1_df_1[var2],range=[[steps1[0],steps1[-1]],[steps2[0],steps2[-1]]],bins=[100,100],weights=jet1_df_1['xsec'],cmin=0.0000001)
        #fig.colorbar(d[3],ax=ax2)
        #ax2.set_xlabel(xtitle1)
        #ax2.set_ylabel(xtitle2)
        Path("Plots/SIGNIF2d/%s_%s"%(var1,var2)).mkdir(parents=True,exist_ok=True)
        fig.savefig("Plots/SIGNIF2d/%s_%s/%s_%s_%s.png"%(var1,var2,sigs[sig],alg_name[i],Rs[r]))
        plt.close()

def make_box(var,xtitle,yrange):
  sigs = ["Sig1000","Sig400","Sig750","Sig300","Sig200"]#,"qcd","isr1000","isr400","bkg1000","bkg400"]
  for sig in [0,1,2,3,4]:
        if sig == 0:
            df_jets = df_jets1000
            #jet1_df_akt8 = df_jets1000[(df_jets1000["Jet_algo"] == -1) & (df_jets1000["R"] == 0.8)]
            #jet1_df_akt10 = df_jets1000[(df_jets1000["Jet_algo"] == -1) & (df_jets1000["R"] == 1.0)]
            #jet1_df_akt15 = df_jets1000[(df_jets1000["Jet_algo"] == -1) & (df_jets1000["R"] == 1.5)]
            #jet1_df_akt20 = df_jets1000[(df_jets1000["Jet_algo"] == -1) & (df_jets1000["R"] == 2.0)]
            #jet1_df_ca8 = df_jets1000[(df_jets1000["Jet_algo"] == 0) & (df_jets1000["R"] == 0.8)]
            #jet1_df_ca10 = df_jets1000[(df_jets1000["Jet_algo"] == 0) & (df_jets1000["R"] == 1.0)]
            #jet1_df_ca15 = df_jets1000[(df_jets1000["Jet_algo"] == 0) & (df_jets1000["R"] == 1.5)]
            #jet1_df_ca20 = df_jets1000[(df_jets1000["Jet_algo"] == 0) & (df_jets1000["R"] == 2.0)]
            #jet1_df_kt8 = df_jets1000[(df_jets1000["Jet_algo"] == 1) & (df_jets1000["R"] == 0.8)]
            #jet1_df_kt10 = df_jets1000[(df_jets1000["Jet_algo"] == 1) & (df_jets1000["R"] == 1.0)]
            #jet1_df_kt15 = df_jets1000[(df_jets1000["Jet_algo"] == 1) & (df_jets1000["R"] == 1.5)]
            #jet1_df_kt20 = df_jets1000[(df_jets1000["Jet_algo"] == 1) & (df_jets1000["R"] == 2.0)]
        if sig == 1:
            df_jets = df_jets400
        if sig == 2:
            df_jets = df_jets750
        if sig == 3:
            df_jets = df_jets300
        if sig == 4:
            df_jets = df_jets200
        jet1_df_akt8 = df_jets[(df_jets["Jet_algo"] == -1) &(df_jets["R"] == 0.8)]
        jet1_df_akt10 =df_jets[(df_jets["Jet_algo"] == -1) &(df_jets["R"] == 1.0)]
        jet1_df_akt15 =df_jets[(df_jets["Jet_algo"] == -1) &(df_jets["R"] == 1.5)]
        jet1_df_akt20 =df_jets[(df_jets["Jet_algo"] == -1) &(df_jets["R"] == 2.0)]
        jet1_df_ca8 =  df_jets[(df_jets["Jet_algo"] == 0) & (df_jets["R"] == 0.8)]
        jet1_df_ca10 = df_jets[(df_jets["Jet_algo"] == 0) & (df_jets["R"] == 1.0)]
        jet1_df_ca15 = df_jets[(df_jets["Jet_algo"] == 0) & (df_jets["R"] == 1.5)]
        jet1_df_ca20 = df_jets[(df_jets["Jet_algo"] == 0) & (df_jets["R"] == 2.0)]
        jet1_df_kt8 =  df_jets[(df_jets["Jet_algo"] == 1) & (df_jets["R"] == 0.8)]
        jet1_df_kt10 = df_jets[(df_jets["Jet_algo"] == 1) & (df_jets["R"] == 1.0)]
        jet1_df_kt15 = df_jets[(df_jets["Jet_algo"] == 1) & (df_jets["R"] == 1.5)]
        jet1_df_kt20 = df_jets[(df_jets["Jet_algo"] == 1) & (df_jets["R"] == 2.0)]

        figbox, boxax1 = plt.subplots(1,1)
        figbox.suptitle("%s %s"%(sigs[sig],var))
        boxax1.set_ylabel(xtitle)
        boxax1.set_ylim(yrange)

        boxax1.boxplot([
        jet1_df_akt8[var],jet1_df_ca8[var],jet1_df_kt8[var],
        jet1_df_akt10[var],jet1_df_ca10[var],jet1_df_kt10[var],
        jet1_df_akt15[var],jet1_df_ca15[var],jet1_df_kt15[var],
        jet1_df_akt20[var],jet1_df_ca20[var],jet1_df_kt20[var]
        ],
        notch=1,positions=[0,1,2,3,4,5,6,7,8,9,10,11],labels=[
        "akt8","ca8","kt8",
        "akt10","ca10","kt10",
        "akt15","ca15","kt15",
        "akt20","ca20","kt20",
        ], sym='',vert=1)
        Path("Plots/fullbox/%s"%(var)).mkdir(parents=True,exist_ok=True)
        figbox.savefig("Plots/fullbox/%s/%s.png"%(var,sigs[sig]))
        plt.close()

#print("Starting combo") 
#make_eff_algo_combo("nTracks",range(0,500,1),"nTracks")
#make_eff_algo_combo("pt",range(0,1000,10),"Pt [GeV]")
#make_eff_algo_combo("trackpt",[0.005 * x for x in range(0,20,1)],"<track Pt/ jet pt>")
#make_eff_algo_combo("medpt",[0.005 * x for x in range(0,20,1)]," median track Pt/ jet pt")
#make_eff_algo_combo("mass",range(0,1000,1),"Mass [GeV")
#make_eff_algo_combo("beta",[0.01*x for x in range(0,100,1)],"beta")
#make_eff_algo_combo("girth",[0.01 *x for x in range(0,100,1)],"$1/Pt \Sigma_{i} (Pt_{i} * \Delta R_{i,jet}/R)$")
#make_eff_algo_combo("pt_dispersion",[0.0001 *x for x in range(0,100,1)],"$1/Pt^{2} \Sigma_{i} (Pt_{i}^{2})$")
#make_eff_algo_combo("lesHouches",[0.0005 *x for x in range(0,100,1)],"$1/Pt \Sigma_{i} (Pt_{i} * (\Delta R_{i,jet}/R)^{0.5})$")
#make_eff_algo_combo("thrust",[0.0005 *x for x in range(0,100,1)],"$1/Pt \Sigma_{i} (Pt_{i} * (\Delta R_{i,jet}/R)^{2})$")
#make_eff_algo_combo("e2",[0.01*x for x in range(0,100,1)],"e2")
#make_eff_algo_combo("e3",[0.01*x for x in range(0,100,1)],"e3")
#make_eff_algo_combo("t1",[0.01*x for x in range(0,100,1)],"t1")
#make_eff_algo_combo("t2",[0.01*x for x in range(0,100,1)],"t2")
#make_eff_algo_combo("t3",[0.01*x for x in range(0,100,1)],"t3")
#make_eff_algo_combo("t21",[0.01*x for x in range(0,100,1)],"t2/t1")
#make_eff_algo_combo("t32",[0.01*x for x in range(0,100,1)],"t3/t2")
#
#print("Starting roc")
#make_eff_algo_roc("nTracks",range(0,500,1),"nTracks")
#make_eff_algo_roc("pt",range(0,1000,10),"Pt [GeV]")
#make_eff_algo_roc("trackpt",[0.005 * x for x in range(0,20,1)],"<track Pt/ jet pt>")
#make_eff_algo_roc("medpt",[0.005 * x for x in range(0,20,1)],"median Pt/ jet pt")
#make_eff_algo_roc("mass",range(0,1000,1),"Mass [GeV")
#make_eff_algo_roc("girth",[0.01 *x for x in range(0,200,1)],"$1/Pt \Sigma_{i} (Pt_{i} * \Delta R_{i,jet})$")
#make_eff_algo_roc("beta",[0.01*x for x in range(0,100,1)],"beta")
#make_eff_algo_roc("girth",[0.01 *x for x in range(0,100,1)],"$1/Pt \Sigma_{i} (Pt_{i} * \Delta R_{i,jet}/R)$")
#make_eff_algo_roc("pt_dispersion",[0.0001 *x for x in range(0,100,1)],"$1/Pt^{2} \Sigma_{i} (Pt_{i}^{2})$")
#make_eff_algo_roc("lesHouches",[0.0005 *x for x in range(0,100,1)],"$1/Pt \Sigma_{i} (Pt_{i} * (\Delta R_{i,jet}/R)^{0.5})$")
#make_eff_algo_roc("thrust",[0.0005 *x for x in range(0,100,1)],"$1/Pt \Sigma_{i} (Pt_{i} * (\Delta R_{i,jet}/R)^{2})$")
#make_eff_algo_roc("e2",[0.01*x for x in range(0,100,1)],"e2")
#make_eff_algo_roc("e3",[0.01*x for x in range(0,100,1)],"e3")
#make_eff_algo_roc("t1",[0.01*x for x in range(0,100,1)],"t1")
#make_eff_algo_roc("t2",[0.01*x for x in range(0,100,1)],"t2")
#make_eff_algo_roc("t3",[0.01*x for x in range(0,100,1)],"t3")
#make_eff_algo_roc("t21",[0.01*x for x in range(0,100,1)],"t2/t1")
#make_eff_algo_roc("t32",[0.01*x for x in range(0,100,1)],"t3/t2")
#print("Starting dist")
#make_eff_algo_dist("nTracks",range(0,500,1),"nTracks")
#make_eff_algo_dist("pt",range(0,1000,10),"Pt [GeV]")
#make_eff_algo_dist("trackpt",[0.005 * x for x in range(0,20,1)],"<track Pt/ jet pt>")
#make_eff_algo_dist("medpt",[0.005 * x for x in range(0,20,1)],"median track Pt/ jet pt")
#make_eff_algo_dist("mass",range(0,1500,1),"Mass [GeV]")
###make_eff_algo_dist("vec4mass",range(0,1000,1),"Mass (4vec) [GeV]")
#make_eff_algo_dist("girth",[0.01 *x for x in range(0,200,1)],"$1/Pt \Sigma_{i} (Pt_{i} * \Delta R_{i,jet})$")
#make_eff_algo_dist("suep_purity",[0.01*x for x in range(0,100,2)],"purity")
#make_eff_algo_dist("suep_frac",[0.01*x for x in range(0,100,2)],"Suep Fraction")
#make_eff_algo_dist("scalardR",[0.01*x for x in range(0,100,2)],"dR(scalar,jet)")
#make_eff_algo_dist("beta",[0.01*x for x in range(0,100,1)],"beta")
#make_eff_algo_dist("girth",[0.01 *x for x in range(0,100,1)],"$1/Pt \Sigma_{i} (Pt_{i} * \Delta R_{i,jet}/R)$")
#make_eff_algo_dist("pt_dispersion",[0.0001 *x for x in range(0,100,1)],"$1/Pt^{2} \Sigma_{i} (Pt_{i}^{2})$")
#make_eff_algo_dist("lesHouches",[0.0005 *x for x in range(0,100,1)],"$1/Pt \Sigma_{i} (Pt_{i} * (\Delta R_{i,jet}/R)^{0.5})$")
#make_eff_algo_dist("thrust",[0.0005 *x for x in range(0,100,1)],"$1/Pt \Sigma_{i} (Pt_{i} * (\Delta R_{i,jet}/R)^{2})$")
#make_eff_algo_dist("e2",[0.01*x for x in range(0,100,1)],"e2")
#make_eff_algo_dist("e3",[0.01*x for x in range(0,100,1)],"e3")
#make_eff_algo_dist("t1",[0.01*x for x in range(0,100,1)],"t1")
#make_eff_algo_dist("t2",[0.01*x for x in range(0,100,1)],"t2")
#make_eff_algo_dist("t3",[0.01*x for x in range(0,100,1)],"t3")
#make_eff_algo_dist("t21",[0.01*x for x in range(0,100,1)],"t2/t1")
#make_eff_algo_dist("t32",[0.01*x for x in range(0,100,1)],"t3/t2")
#print("starting box")
#make_box("suep_purity","purity",[0.8,1.0])
##make_box("suep_ptwgt",[0.01*x for x in range(0,100,2)],"purity (pt weight)")
#make_box("suep_frac","Suep Fraction",[0.7,1.0])
#make_box("scalardR","dR(scalar,jet)",[0,0.5])
#make_box("pt_res","(Pt_Jet - Pt_Gen)/Pt_Gen",[-0.75,0.25])
#make_box("mass_res","(Mass_Jet - Mass_Gen)/Mass_Gen",[-1,1])
#make_box("beta_res","(Beta_Jet - Beta_Gen)/Beta_Gen",[-0.25,0.35])
#print("starting resolution plots")
#make_eff_algo_res("pt","scalarpt",[0.001*x for x in range(-1000,1000,10)],"(Pt_Jet - Pt_Gen)/Pt_Gen")
#make_eff_algo_res("mass","scalarmass",[0.001*x for x in range(-1000,1000,10)],"(Mass_Jet - Mass_Gen)/Mass_Gen")
#make_eff_algo_res("beta","scalarbeta",[0.001*x for x in range(-1000,1000,10)],"(Beta_Jet - Beta_Gen)/Beta_Gen")
#print("starting 2d significance plots:trkpt")
#make_signif_2d("nTracks",range(50,250,10),"nTracks","trackpt",[0.0001 * x for x in range(0,200,1)],"<track Pt/ jet pt>")
#print("starting 2d significance plots:pt")
#make_signif_2d("nTracks",range(50,250,10),"nTracks","pt",range(0,1000,50),"Pt [GeV]")
#print("starting 2d significance plots:mass")
#make_signif_2d("nTracks",range(50,250,10),"nTracks","mass",range(0,1000,50),"Mass [GeV]")
#print("starting 2d significance plots:medpt")
#make_signif_2d("nTracks",range(50,250,10),"nTracks","medpt",[0.0001 * x for x in range(0,200,1)],"median track Pt/ jet pt")
#
#print("starting 2d significance plots:girth")
#make_signif_2d("nTracks",range(50,250,10),"nTracks","girth",[0.01 *x for x in range(0,100,1)],"$1/Pt \Sigma_{i} (Pt_{i} * \Delta R_{i,jet}/R)$")
#print("starting 2d significance plots:pt dispersion")
#make_signif_2d("nTracks",range(50,250,10),"nTracks","pt_dispersion",[0.0001 *x for x in range(0,100,1)],"$1/Pt^{2} \Sigma_{i} (Pt_{i}^{2})$")
#print("starting 2d significance plots:lesHouches")
#make_signif_2d("nTracks",range(50,250,10),"nTracks","lesHouches",[0.0005 *x for x in range(0,100,1)],"$1/Pt \Sigma_{i} (Pt_{i} * (\Delta R_{i,jet}/R)^{0.5})$")
#print("starting 2d significance plots:thrust")
#make_signif_2d("nTracks",range(50,250,10),"nTracks","thrust",[0.0005 *x for x in range(0,100,1)],"$1/Pt \Sigma_{i} (Pt_{i} * (\Delta R_{i,jet}/R)^{2})$")
#
#print("starting 2d significance plots:t1")
#make_signif_2d("nTracks",range(50,250,10),"nTracks","t1",[0.01*x for x in range(0,100,1)],"t1")
#print("starting 2d significance plots:t2")
#make_signif_2d("nTracks",range(50,250,10),"nTracks","t2",[0.01*x for x in range(0,100,1)],"t2")
#print("starting 2d significance plots:t3")
#make_signif_2d("nTracks",range(50,250,10),"nTracks","t3",[0.01*x for x in range(0,100,1)],"t3")
print("starting 2d significance plots:t2/t1")
make_signif_2d("nTracks",range(50,250,10),"nTracks","t21",[0.01*x for x in range(0,100,1)],"t2/t1")
print("starting 2d significance plots:t3/t2")
make_signif_2d("nTracks",range(50,250,10),"nTracks","t32",[0.01*x for x in range(0,100,1)],"t3/t2")
print("starting 2d significance plots:e2")
make_signif_2d("nTracks",range(50,250,10),"nTracks","e2",[0.01*x for x in range(0,100,1)],"e2")
print("starting 2d significance plots:e3")
make_signif_2d("nTracks",range(50,250,10),"nTracks","e3",[0.01*x for x in range(0,100,1)],"e3")
#print("starting scalar 2d plots")
#make_eff_algo_dist_2d("scalarpt",range(0,1000,50),"Pt [GeV]","pt",range(0,1000,50),"Pt [GeV]")
#make_eff_algo_dist_2d("scalareta",[0.1*x for x in range(-25,25,1)],"Eta","eta",[0.1*x for x in range(-25,25,1)],"Eta")
#make_eff_algo_dist_2d("scalarphi",[0.1*x for x in range(-32,32,1)],"Phi","phi",[0.1*x for x in range(-32,32,1)],"Phi")
#make_eff_algo_dist_2d("suep_purity",[0.01*x for x in range(0,100,2)],"purity","suep_frac",[0.01*x for x in range(0,100,2)],"Suep Fraction")
#make_eff_algo_dist("NVtx",range(0,100,1),"NVtx")
#make_eff_algo_dist("Num_Interactions",range(0,100,1),"Num Interactions")

#print("starting purity 2d plots")
#make_eff_algo_dist_2d("suep_purity",[0.01*x for x in range(0,100,2)],"purity","nTracks",range(0,500,25),"nTracks")
#make_eff_algo_dist_2d("suep_purity",[0.01*x for x in range(0,100,2)],"purity","pt",range(0,1000,50),"Pt [GeV]")
#make_eff_algo_dist_2d("suep_purity",[0.01*x for x in range(0,100,2)],"purity","trackpt",[0.005 * x for x in range(0,20,1)],"<track Pt/ jet pt>")
#make_eff_algo_dist_2d("suep_purity",[0.01*x for x in range(0,100,2)],"purity","mass",range(0,1000,50),"Mass [GeV]")
#make_eff_algo_dist_2d("suep_purity",[0.01*x for x in range(0,100,2)],"purity","girth",[0.01 *x for x in range(0,200,20)],"$1/Pt \Sigma_{i} (Pt_{i} * \Delta R_{i,jet})$")
#make_eff_algo_dist_2d("suep_purity",[0.01*x for x in range(0,100,2)],"purity","NVtx",range(0,100,1),"NVtx")
#make_eff_algo_dist_2d("suep_purity",[0.01*x for x in range(0,100,2)],"purity","Num_Interactions",range(0,100,1),"Num Interactions")
#print("starting frac 2d plots")
#make_eff_algo_dist_2d("suep_frac",[0.01*x for x in range(0,100,2)],"Suep Fraction","nTracks",range(0,500,25),"nTracks")
#make_eff_algo_dist_2d("suep_frac",[0.01*x for x in range(0,100,2)],"Suep Fraction","pt",range(0,1000,50),"Pt [GeV]")
#make_eff_algo_dist_2d("suep_frac",[0.01*x for x in range(0,100,2)],"Suep Fraction","trackpt",[0.005 * x for x in range(0,20,1)],"<track Pt/ jet pt>")
#make_eff_algo_dist_2d("suep_frac",[0.01*x for x in range(0,100,2)],"Suep Fraction","mass",range(0,1000,50),"Mass [GeV]")
#make_eff_algo_dist_2d("suep_frac",[0.01*x for x in range(0,100,2)],"Suep Fraction","girth",[0.01 *x for x in range(0,200,20)],"$1/Pt \Sigma_{i} (Pt_{i} * \Delta R_{i,jet})$")
#make_eff_algo_dist_2d("suep_frac",[0.01*x for x in range(0,100,2)],"Suep Fraction","NVtx",range(0,100,1),"NVtx")
#make_eff_algo_dist_2d("suep_frac",[0.01*x for x in range(0,100,2)],"Suep Fraction","Num_Interactions",range(0,100,1),"Num Interactions")
#print("starting nvtx 2d plots")
#make_eff_algo_dist_2d("NVtx",range(0,100,1),"NVtx","nTracks",range(0,500,25),"nTracks")
#make_eff_algo_dist_2d("NVtx",range(0,100,1),"NVtx","pt",range(0,1000,50),"Pt [GeV]")
#make_eff_algo_dist_2d("NVtx",range(0,100,1),"NVtx","trackpt",[0.005 * x for x in range(0,20,1)],"<track Pt/ jet pt>")
#make_eff_algo_dist_2d("NVtx",range(0,100,1),"NVtx","mass",range(0,1000,50),"Mass [GeV]")
#make_eff_algo_dist_2d("NVtx",range(0,100,1),"NVtx","girth",[0.01 *x for x in range(0,200,20)],"$1/Pt \Sigma_{i} (Pt_{i} * \Delta R_{i,jet})$")
#print("starting num interactions 2d plots")
#make_eff_algo_dist_2d("Num_Interactions",range(0,100,1),"Num Interactions","nTracks",range(0,500,25),"nTracks")
#make_eff_algo_dist_2d("Num_Interactions",range(0,100,1),"Num Interactions","pt",range(0,1000,50),"Pt [GeV]")
#make_eff_algo_dist_2d("Num_Interactions",range(0,100,1),"Num Interactions","trackpt",[0.005 * x for x in range(0,20,1)],"<track Pt/ jet pt>")
#make_eff_algo_dist_2d("Num_Interactions",range(0,100,1),"Num Interactions","mass",range(0,1000,50),"Mass [GeV]")
#make_eff_algo_dist_2d("Num_Interactions",range(0,100,1),"Num Interactions","girth",[0.01 *x for x in range(0,200,20)],"$1/Pt \Sigma_{i} (Pt_{i} * \Delta R_{i,jet})$")
##
