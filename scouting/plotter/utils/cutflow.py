from utils.utils import *
from scipy.optimize import curve_fit

def linearFunc(x,intercept,slope):
    y = intercept + slope * x
    return y

cuts = ["Cut 0: No Cut:","Cut 1: Trigger", "Cut 2: $\HT > 560 \GeV$","Cut 3: AK15 Jets $>2$","Cut 4a: \\nSUEPConstituents $>%d$"%region_cuts_tracks[0],"Cut 5a: \\boostedSphericity $>0.%s$"%region_cuts_sphere[0],"Cut 4b: \\nSUEPConstituents $>%d$"%region_cuts_tracks[1],"Cut 5b: \\boostedSphericity $>0.%s$"%region_cuts_sphere[1],"Cut 4c: \\nSUEPConstituents $>%d$"%region_cuts_tracks[2],"Cut 5c:\\boostedSphericity $>0.%s$"%region_cuts_sphere[2],"Cut 4d: \\nSUEPConstituents $>%d$"%region_cuts_tracks[3],"Cut 5d:\\boostedSphericity $>0.%s$"%region_cuts_sphere[3]]

def make_cutflow(samples,var):
  region_cuts_tracksx = region_cuts_tracks + [250,300]
  region_cuts_spherex = region_cuts_sphere + [50,50]
  cutsx = cuts+ ["Cut 4e: \\nSUEPConstituents $>%d$"%region_cuts_tracksx[4],"Cut 5e:\\boostedSphericity $>0.%s$"%region_cuts_spherex[4]]
  name1 = "dist_%s"%var
  final_cut = 35 # 50 bins -> 35= 0.7 cut
  cutflow = {"QCD":[],"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  cutflow_sig = {"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  cutflow_releff = {"QCD":[],"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  for cut in [0,1,2]:
    b1 = qcdscaled[name1].integrate("cut",slice(cut,cut+1)).values()
    for (k,b) in b1.items():
      cutflow["QCD"].append(b.sum())
      if(cut >0):
        cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][cut-1])
  b2 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(0,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
  for (k,b) in b2.items():
    cutflow["QCD"].append(b.sum())
    cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][2])
  for SR in [0,1,2,3,4]:
    x1 = region_cuts_tracksx[SR]
    y1 = region_cuts_spherex[SR]/100.
    if SR==0:
      x2 = region_cuts_tracksx[-1]
      y2 = region_cuts_spherex[-1]/100.
    else:
      x2 = region_cuts_tracksx[SR+1]
      y2 = region_cuts_spherex[SR+1]/100.
    b3 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(x1,x2)).integrate("eventBoostedSphericity",slice(0,1)).values()
    #b3 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
    for (k,b) in b3.items():
      cutflow["QCD"].append(b.sum())
      cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][3])
    b4 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(x1,x2)).integrate("eventBoostedSphericity",slice(y1,1)).values()
    #b4 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
    for (k,b) in b4.items():
      cutflow["QCD"].append(b.sum())
      cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][4+2*SR])

  for sample in samples:
        scaled = sigscaled[sample]
        for cut in [0,1,2]:#,3,4]:
          s1 = scaled[name1].integrate("cut",slice(cut,cut+1)).values()
          for (k,s) in s1.items():
            cutflow[sample].append(s.sum())
            sigb = cutflow["QCD"][cut]
            signif = s.sum()/np.sqrt(s.sum()+sigb+(sigb**2))
            cutflow_sig[sample].append(signif)
            if(cut >0):
              cutflow_releff[sample].append(100*s.sum()/cutflow[sample][cut-1])
        s2 = scaled["SR1_suep_3"].integrate("nPFCand",slice(0,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
        for (k,s) in s2.items():
          cutflow[sample].append(s.sum())
          cutflow_releff[sample].append(100*s.sum()/cutflow[sample][2])
          cutflow_sig[sample].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][3]+(cutflow["QCD"][3]**2)))
        for SR in [0,1,2,3,4]:
          x1 = region_cuts_tracksx[SR]
          y1 = region_cuts_spherex[SR]/100.
          if SR==0:
            x2 = region_cuts_tracksx[-1]
            y2 = region_cuts_spherex[-1]/100.
          else:
            x2 = region_cuts_tracksx[SR+1]
            y2 = region_cuts_spherex[SR+1]/100.
          s3 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,x2)).integrate("eventBoostedSphericity",slice(0,1)).values()
          #s3 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
          for (k,s) in s3.items():
            cutflow[sample].append(s.sum())
            cutflow_releff[sample].append(100*s.sum()/cutflow[sample][3])
            cutflow_sig[sample].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][4+2*SR]+(cutflow["QCD"][4+2*SR]**2)))

          s4 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,x2)).integrate("eventBoostedSphericity",slice(y1,1)).values()
          #s4 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
          for (k,s) in s4.items():
            cutflow[sample].append(s.sum())
            cutflow_releff[sample].append(100*s.sum()/cutflow[sample][4+2*SR])
            cutflow_sig[sample].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][5+2*SR]+(cutflow["QCD"][5+2*SR]**2)))

  print(pd.DataFrame(cutflow))
  print(pd.DataFrame(cutflow_sig))
  pd.set_option('display.float_format', lambda x: '%.2f' % x)
  releff = pd.DataFrame(cutflow_releff)
  yields = pd.DataFrame(cutflow)
  sigs = pd.DataFrame(cutflow_sig)
  print("##################  Yields  ################")
  for i in yields.index:
    print("%s & %.2e & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cutsx[i],yields["QCD"][i],yields["sig125"][i],yields["sig200"][i],yields["sig300"][i],yields["sig400"][i],yields["sig700"][i],yields["sig1000"][i]))
    if i == 3 or i==5 or i==7 or i==9 or i==11:
      print("\\hline")
  print("##################  RelEff  ################")
  for i in releff.index:
    print("%s & %.2e & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cutsx[i+1],releff["QCD"][i],releff["sig125"][i],releff["sig200"][i],releff["sig300"][i],releff["sig400"][i],releff["sig700"][i],releff["sig1000"][i]))
    if i+1 == 3 or i+1==5 or i+1==7 or i+1==9 or i+1==11:
      print("\\hline")
  print("##################  SIGS  ################")
  for i in sigs.index:
    print("%s & %.2e & %.2e & %.2e & %.2e & %.2e & %.2e \\\\"%(cutsx[i],sigs["sig125"][i],sigs["sig200"][i],sigs["sig300"][i],sigs["sig400"][i],sigs["sig700"][i],sigs["sig1000"][i]))
    if i == 3 or i==5 or i==7 or i==9 or i==11:
      print("\\hline")

def make_systematics(samples,var,allsys,sysname="",systematics1="",systematics2=""):
  name = "dist_%s"%var
  final_cut = 35 # 50 bins -> 35= 0.7 cut
  higgs = False
  if systematics2 =="_higgs_weights_down":
    cutflow = {"sig125":[],"sig125%s"%(systematics1):[],"sig125%s"%(systematics2):[]}
    syslist = ["",systematics1,systematics2]
    higgs = True
  elif systematics2 =="":
    cutflow = {"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[],"sig125%s"%(systematics1):[],"sig200%s"%(systematics1):[],"sig300%s"%(systematics1):[],"sig400%s"%(systematics1):[],"sig700%s"%(systematics1):[],"sig1000%s"%(systematics1):[]}
    syslist = ["",systematics1]
  else:
    cutflow = {"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[],"sig125%s"%(systematics1):[],"sig200%s"%(systematics1):[],"sig300%s"%(systematics1):[],"sig400%s"%(systematics1):[],"sig700%s"%(systematics1):[],"sig1000%s"%(systematics1):[],"sig125%s"%(systematics2):[],"sig200%s"%(systematics2):[],"sig300%s"%(systematics2):[],"sig400%s"%(systematics2):[],"sig700%s"%(systematics2):[],"sig1000%s"%(systematics2):[]}
    syslist = ["",systematics1,systematics2]
  for sample in samples:
    for systematic in syslist:
      scaled = sigscaled_sys[sample][systematic] 
      #with open(directory+"myhistos_%s_2%s.p"%(sample,systematic), "rb") as pkl_file:
      #    out = pickle.load(pkl_file)
      #    scale= lumi*xsecs[sample]/out["sumw"][sample]
      #    for name, h in out.items():
      #      if isinstance(h, hist.Hist):
      #        scaled[name] = h.copy()
      #        scaled[name].scale(scale)

      for cut in [0,1,2]:#,3,4]:
        s1 = scaled[name].integrate("cut",slice(cut,cut+1)).values()
        for (k,s) in s1.items():
          print("%s %d %s %.2f"%(sample,cut,name,s.sum()))
          cutflow[sample+systematic].append(s.sum())
      s2 = scaled["SR1_suep_3"].integrate("nPFCand",slice(0,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
      for (k,s) in s2.items():
        cutflow[sample+systematic].append(s.sum())
####  ######SR 
      for SR in [0,1,2,3]:
        x1 = region_cuts_tracks[SR]
        y1 = region_cuts_sphere[SR]/100.
        s3 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
        for (k,s) in s3.items():
          cutflow[sample+systematic].append(s.sum())

        s4 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
        for (k,s) in s4.items():
          cutflow[sample+systematic].append(s.sum())
  print(cutflow)
  print(pd.DataFrame(cutflow))
  pd.set_option('display.float_format', lambda x: '%.2f' % x)
  yields = pd.DataFrame(cutflow)
  if higgs:
    print("##################  Yields  ################")
    for i in yields.index:
      print("%s & %.2f & x & x & x & x & x \\\\"%(cuts[i],yields["sig125"][i]))
      if i == 3 or i==5 or i==7 or i==9 or i == 11:
        print("\\hline")
    print("##################  New Yields 1 ################")
    for i in yields.index:
      print("%s & %.2f & x & x & x & x & x \\\\"%(cuts[i],yields["sig125%s"%(systematics1)][i]))
      if i == 3 or i==5 or i==7 or i==9 or i == 11:
        print("\\hline")
    if systematics2 == "":
      print("##################  Uncertainty  ################")
      for i in yields.index:
        print("%s & %.2f & x & x & x & x & x \\\\"%(cuts[i],100*(yields["sig125"][i]-yields["sig125%s"%(systematics1)][i])/yields["sig125"][i]))
        if i == 3 or i==5 or i==7 or i==9 or i == 11:
          print("\\hline")
    else:
      print("##################  New Yields 2 ################")
      for i in yields.index:
        print("%s & %.2f & x & x & x & x & x \\\\"%(cuts[i],yields["sig125%s"%(systematics2)][i]))
        if i == 3 or i==5 or i==7 or i==9 or i == 11:
          print("\\hline")
      print("##################  Uncertainty  ################")
      for i in yields.index:
        print("%s & %.2f & x & x & x & x & x \\\\"%(cuts[i],100*(yields["sig125%s"%(systematics1)][i]-yields["sig125%s"%(systematics2)][i])/yields["sig125"][i]))
        if i == 3 or i==5 or i==7 or i==9 or i == 11:
          print("\\hline")
    i=5
    allsys.append("%s\t & %.2f & N/A & N/A & N/A & N/A & N/A \\\\"%(sysname,100*abs(yields["sig125%s"%(systematics1)][i]-yields["sig125%s"%(systematics2)][i])/yields["sig125"][i]))
  else:
    print("##################  Yields  ################")
    for i in yields.index:
      print("%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],yields["sig125"][i],yields["sig200"][i],yields["sig300"][i],yields["sig400"][i],yields["sig700"][i],yields["sig1000"][i]))
      if i == 3 or i==5 or i==7 or i==9 or i == 11:
        print("\\hline")
    print("##################  New Yields 1 ################")
    for i in yields.index:
      print("%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],yields["sig125%s"%(systematics1)][i],yields["sig200%s"%(systematics1)][i],yields["sig300%s"%(systematics1)][i],yields["sig400%s"%(systematics1)][i],yields["sig700%s"%(systematics1)][i],yields["sig1000%s"%(systematics1)][i]))
      if i == 3 or i==5 or i==7 or i==9 or i == 11:
        print("\\hline")
    if systematics2 == "":
      print("##################  Uncertainty  ################")
      for i in yields.index:
        print("%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],100*(yields["sig125"][i]-yields["sig125%s"%(systematics1)][i])/yields["sig125"][i],100*(yields["sig200"][i]-yields["sig200%s"%(systematics1)][i])/yields["sig200"][i],100*(yields["sig300"][i]-yields["sig300%s"%(systematics1)][i])/yields["sig300"][i],100*(yields["sig400"][i]-yields["sig400%s"%(systematics1)][i])/yields["sig400"][i],100*(yields["sig700"][i]-yields["sig700%s"%(systematics1)][i])/yields["sig700"][i],100*(yields["sig1000"][i]-yields["sig1000%s"%(systematics1)][i])/yields["sig1000"][i]))
        if i == 3 or i==5 or i==7 or i==9 or i == 11:
          print("\\hline")
    else:
      print("##################  New Yields 2 ################")
      for i in yields.index:
        print("%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],yields["sig125%s"%(systematics2)][i],yields["sig200%s"%(systematics2)][i],yields["sig300%s"%(systematics2)][i],yields["sig400%s"%(systematics2)][i],yields["sig700%s"%(systematics2)][i],yields["sig1000%s"%(systematics2)][i]))
        if i == 3 or i==5 or i==7 or i==9 or i == 11:
          print("\\hline")
      print("##################  Uncertainty  ################")
      for i in yields.index:
        print("%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],100*(yields["sig125%s"%(systematics1)][i]-yields["sig125%s"%(systematics2)][i])/yields["sig125"][i],100*(yields["sig200%s"%(systematics1)][i]-yields["sig200%s"%(systematics2)][i])/yields["sig200"][i],100*(yields["sig300%s"%(systematics1)][i]-yields["sig300%s"%(systematics2)][i])/yields["sig300"][i],100*(yields["sig400%s"%(systematics1)][i]-yields["sig400%s"%(systematics2)][i])/yields["sig400"][i],100*(yields["sig700%s"%(systematics1)][i]-yields["sig700%s"%(systematics2)][i])/yields["sig700"][i],100*(yields["sig1000%s"%(systematics1)][i]-yields["sig1000%s"%(systematics2)][i])/yields["sig1000"][i]))
        if i == 3 or i==5 or i==7 or i==9 or i == 11:
          print("\\hline")

    i=5
    if systematics2== "":
      allsys.append("%s\t & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(sysname,100*abs(yields["sig125"][i]-yields["sig125%s"%(systematics1)][i])/yields["sig125"][i],100*abs(yields["sig200"][i]-yields["sig200%s"%(systematics1)][i])/yields["sig200"][i],100*abs(yields["sig300"][i]-yields["sig300%s"%(systematics1)][i])/yields["sig300"][i],100*abs(yields["sig400"][i]-yields["sig400%s"%(systematics1)][i])/yields["sig400"][i],100*abs(yields["sig700"][i]-yields["sig700%s"%(systematics1)][i])/yields["sig700"][i],100*abs(yields["sig1000"][i]-yields["sig1000%s"%(systematics1)][i])/yields["sig1000"][i]))
    else:
      allsys.append("%s\t & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(sysname,100*abs(yields["sig125%s"%(systematics1)][i]-yields["sig125%s"%(systematics2)][i])/yields["sig125"][i],100*abs(yields["sig200%s"%(systematics1)][i]-yields["sig200%s"%(systematics2)][i])/yields["sig200"][i],100*abs(yields["sig300%s"%(systematics1)][i]-yields["sig300%s"%(systematics2)][i])/yields["sig300"][i],100*abs(yields["sig400%s"%(systematics1)][i]-yields["sig400%s"%(systematics2)][i])/yields["sig400"][i],100*abs(yields["sig700%s"%(systematics1)][i]-yields["sig700%s"%(systematics2)][i])/yields["sig700"][i],100*abs(yields["sig1000%s"%(systematics1)][i]-yields["sig1000%s"%(systematics2)][i])/yields["sig1000"][i]))


def makeCombineHistograms(samples,var,cut):
  f = ROOT.TFile.Open("combineInput_%s.root"%year,"RECREATE")
  #makeQCD = True
  #systematics_list1 = ["","killtrk","AK4up","AK4down","trigup","trigdown","PUup","PUdown","PSup","PSdown","Prefireup","Prefiredown"]#,"JESup","JESdown"]#,"killtrk2","higgsup","higgsdown","PSdown2","PSup2"]
  systematics_list1 = ["","_track_up","_JES_up","_JES_down","_JER_up","_JER_down","_trigSF_up","_trigSF_down","_puweights_up","_puweights_down","_PSWeight_ISR_up","_PSWeight_FSR_up","_PSWeight_ISR_down","_PSWeight_FSR_down","_prefire_up","_prefire_down"]
  for sample in samples:
    if "125" in sample:
      systematics_list = systematics_list1 +["_higgs_weights_up","_higgs_weights_down"]
    else:
      systematics_list = systematics_list1
    #for systematic in ["m2t0p5", "m2t1", "m2t2", "m2t3", "m2t4", "m3t1p5", "m3t3", "m3t6", "m5t1", "m5t5", "m5t10"]:
    for systematic in systematics_list:
      #with open(directory+"myhistos_%s_2%s.p"%(sample,systematic), "rb") as pkl_file:
      #with open(directory+"myhistos_%s_%s.p"%(sample,systematic), "rb") as pkl_file:
      #    out = pickle.load(pkl_file)
      #    scale= lumi*xsecs[sample]/out["sumw"][sample]
      #    scaled = {}
      scaled = sigscaled_sys[sample][systematic]
      name = var+"_%s"%cut
      xvar = "SUEP Jet Track Multiplicity"
     #     for name, h in out.items():
     #       if var2 not in name:
     #         continue
     #       if isinstance(h, hist.Hist):
     #         scaled[name] = h.copy()
     #         scaled[name].scale(scale)
      s = scaled[name].to_hist().to_numpy()
      if systematic == "":
        b = qcdscaled[name].to_hist().to_numpy()
      else:
        systematic = "_"+systematic #for aesthetic purposes

      x1 = 0
      x2 = inner_tracks
      x3 = region_cuts_tracks[0]
      x4 = 300
      y1 = 30
      y2 = inner_sphere
      y3 = region_cuts_sphere[0]
      y4 = 100
      if sample == "sig200" or sample == "sig125":
        point=1
      if sample == "sig300" or sample == "sig400":
        point=2
      if sample == "sig700" or sample == "sig1000":
        point=3
      x0 = region_cuts_tracks[0]
      y0 = region_cuts_sphere[0] #use only gap point
      region_sum = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"SR":0,"ALL":0}
      region_sumqcd = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"SR":0,"ALL":0}
      for region in ["A","B","C","D","E","F","G","H","SR","ALL"]:
        if region == "A":
          xx = x1
          xxx = x2
          yy = y1
          yyy = y2
        elif region == "B":
          xx = x2
          xxx = x3
          yy = y1
          yyy = y2
        elif region == "C":
          xx = x0
          xxx = x4
          yy = y1
          yyy = y2
        elif region == "D":
          xx = x1
          xxx = x2
          yy = y2
          yyy = y3
        elif region == "E":
          xx = x2
          xxx = x3
          yy = y2
          yyy = y3
        elif region == "F":
          xx = x0
          xxx = x4
          yy = y2
          yyy = y3
        elif region == "G":
          xx = x1
          xxx = x2
          yy = y0
          yyy = y4
        elif region == "H":
          xx = x2
          xxx = x3
          yy = y0
          yyy = y4
        elif region == "SR":
          xx = x0
          xxx = x4
          yy = y0
          yyy = y4
        elif region == "ALL":
          xx = 0
          xxx = x4
          yy = 0
          yyy = y4
        else:
          print("what happened")
          pass
        #h = ROOT.TH2F("%s_%s"%(systematic,region),"%s_%s"%(systematic,region),300,0,300,100,0,1)
        h = ROOT.TH2F("%s_%s%s"%(sample,region,systematic),"%s_%s%s"%(sample,region,systematic),300,0,300,100,0,1)
        if systematic == "":
          hb = ROOT.TH2F("QCD_%s_%s"%(sample,region),"QCD_%s_%s"%(sample,region),300,0,300,100,0,1)
        for x in range(xx,xxx):
          for y in range(yy,yyy):
            region_sum[region] = region_sum[region] + s[0][0][x][y]
            h.Fill(s[2][x],s[3][y],s[0][0][x][y])
            if systematic == "":
              region_sum[region] = region_sum[region] + s[0][0][x][y]
              region_sumqcd[region] = region_sumqcd[region] + b[0][0][x][y]
              hb.Fill(b[2][x],b[3][y],b[0][0][x][y])
        h.Write()
        if systematic == "":
          hb.Write()
      if systematic == "":
        print(sample)
        print(region_sum)
        print(region_sumqcd)
  f.Close()

def makeCombineHistogramsOffline(var,cut,samplename="test",temp="",phi="",load_ondemand=False,fullscan=False,unblind=False):
  if not (temp=="" and phi==""):
    scan = "_T%s_phi%s"%(temp,phi) 
  else:
    scan = ""
  f = ROOT.TFile.Open("combineHist/%s%s_%s.root"%(samplename,scan,year),"RECREATE")
  if samplename == "QCD" or samplename == "Data":
    systematics_list = [""]
  else:
    systematics_list = ["","_track_up","_JES_up","_JES_down","_JER_up","_JER_down","_trigSF_up","_trigSF_down","_puweights_up","_puweights_down","_PSWeight_ISR_up","_PSWeight_FSR_up","_PSWeight_ISR_down","_PSWeight_FSR_down","_prefire_up","_prefire_down","_track_down"]
  if "125" in samplename:
    systematics_list = systematics_list + ["_higgs_weights_up","_higgs_weights_down"]
  for systematic in systematics_list:
    if samplename == "QCD":
      scaled = qcdscaled#.to_hist().to_numpy()
    elif samplename == "Data":
      scaled = datafullscaled#.to_hist().to_numpy()
      h1 = datafullscaled["SR1_suep_3"].integrate("axis",slice(0,1))
      lowx =0
      lowy = 30
      highx3 = 300
      highy3 = 100
      highx1 = inner_tracks #region_cuts_tracks[0]#20
      highy1 = inner_sphere #region_cuts_sphere[0]#38
      highx2 = region_cuts_tracks[0]
      highy2 = region_cuts_sphere[0]
      varx = "nPFCand"
      gapx = region_cuts_tracks[0]
      gapy = region_cuts_sphere[0]
      abin = h1.integrate("eventBoostedSphericity",slice( lowy/100.,  highy1/100.)).integrate(  varx,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100.,  highy1/100.)).integrate(  varx,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100.,  highy1/100.)).integrate(  varx,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100., gapy/100.)).integrate(  varx,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100., gapy/100.)).integrate(  varx,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100., gapy/100.)).integrate(  varx,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100., highy3/100.)).integrate(  varx,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100., highy3/100.)).integrate(  varx,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100.,highy3/100.)).integrate(  varx,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      abinx = abin[0]
      bbinx = bbin[0]
      cbinx = cbin[0]
      dbinx = dbin[0]
      ebinx = ebin[0]
      fbinx = fbin[0]
      gbinx = gbin[0]
      hbinx = hbin[0]
      SRbinx = SRbin[0]
      ratx = fbinx*((hbinx*dbinx*bbinx)**2)/((gbinx*cbinx*abinx)*(ebinx**4))
    else:
      #if load_ondemand:
      if "track_down" in systematic:
        scaled = load_samples(samplename+"_2",year,"_track_up",temp=temp,phi=phi,fullscan=fullscan)
      else:
        scaled = load_samples(samplename+"_2",year,systematic,temp=temp,phi=phi,fullscan=fullscan)
      #else:
      #  if "higgs" in systematic and "125" not in samplename: 
      #    scaled = sigscaled_sys[sample][""]
      #  elif "track_down" in systematic:
      #    scaled = sigscaled_sys[sample]["_track_up"]
      #  else:
      #    scaled = sigscaled_sys[sample][systematic]
    name = var+"_%s"%cut
    xvar = "SUEP Jet Track Multiplicity"
    s = scaled[name].to_hist().to_numpy()

    x1 = 0
    x2 = inner_tracks
    x3 = region_cuts_tracks[0]
    x4 = 300
    y1 = 30
    y2 = inner_sphere
    y3 = region_cuts_sphere[0]
    y4 = 100
    #if sample == "sig200" or sample == "sig125":
    #  point=1
    #if sample == "sig300" or sample == "sig400":
    #  point=2
    #if sample == "sig700" or sample == "sig1000":
    #  point=3
    x0 = region_cuts_tracks[0]
    y0 = region_cuts_sphere[0] #use only gap point
    #region_sum = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"ALL":0}
    #region_sumqcd = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"ALL":0}
    #C_array = [0]*x4 #arrays for F/C comparison
    #F_array = [0]*x4
    for region in ["A","B","C","D","E","F","G","H","I","ALL"]:
      if region == "A":
        xx = x1
        xxx = x2
        yy = y1
        yyy = y2
      elif region == "B":
        xx = x2
        xxx = x3
        yy = y1
        yyy = y2
      elif region == "C":
        xx = x0
        xxx = x4
        yy = y1
        yyy = y2
      elif region == "D":
        xx = x1
        xxx = x2
        yy = y2
        yyy = y3
      elif region == "E":
        xx = x2
        xxx = x3
        yy = y2
        yyy = y3
      elif region == "F":
        xx = x0
        xxx = x4
        yy = y2
        yyy = y3
      elif region == "G":
        xx = x1
        xxx = x2
        yy = y0
        yyy = y4
      elif region == "H":
        xx = x2
        xxx = x3
        yy = y0
        yyy = y4
      elif region == "I":
        if(samplename == "Data" and not unblind): #repeat region F for data to do expected scaling
          xx = x0
          xxx = x4
          yy = y2
          yyy = y3
        else:
          xx = x0
          xxx = x4
          yy = y0
          yyy = y4
      elif region == "ALL":
        xx = 0
        xxx = x4
        yy = 0
        yyy = y4
      else:
        print("what happened")
        pass
      h = ROOT.TH1D("%s_SUEP_nconst_Cluster70%s"%(region,systematic),"%s_SUEP_nconst_Cluster70%s"%(region,systematic),300,0,300)
      for x in range(xx,xxx):
        for y in range(yy,yyy):
          #region_sum[region] = region_sum[region] + s[0][0][x][y]
          if(samplename == "Data" and region == "I" and not unblind): 
          #  h.Fill(s[2][x],0)
            h.Fill(s[2][x],ratx*s[0][0][x][y])
          else:
            if (region == "I"):
              h.Fill(s[2][x],s[0][0][x][y])
            else:
              h.Fill(s[2][x],s[0][0][x][y])
          #if(region == "F"): 
          #  print("F: ",s[2][x],s[0][0][x][y])
          #  F_array[int(s[2][x])] = F_array[int(s[2][x])] + s[0][0][x][y]
          #if(region == "C"):
          #  print("C: ",s[2][x],s[0][0][x][y])
          #  C_array[int(s[2][x])] = C_array[int(s[2][x])] + s[0][0][x][y]
          #  #C_array.append(s[0][0][x][y])
      h.Write()
    #print(F_array)
    #print(C_array)
    #F_err =np.sqrt(np.nan_to_num(F_array))
    #C_err =np.sqrt(np.nan_to_num(C_array))
    #print(F_err)
    #print(C_err)
    #FC_array = np.nan_to_num(np.divide(F_array,C_array))
    #FC_array[FC_array > 1000] = np.nan
    #print(FC_array)
    #FC_err = FC_array * np.sqrt( (F_err/F_array)**2 + (C_err/C_array)**2)
    #print(FC_err)
    #fig, (ax, ax1) = plt.subplots(
    #nrows=2,
    #ncols=1,
    #figsize=(7,7),
    #gridspec_kw={"height_ratios": (3, 1)},
    #sharex=True
    #)
    #fig.subplots_adjust(hspace=.07)
    #ax.errorbar(range(0,110),np.nan_to_num(F_array[:110]),xerr=1,yerr=F_err[:110],color="b",ls='none',label= "F")
    #ax.errorbar(range(0,110),np.nan_to_num(C_array[:110]),xerr=1,yerr=C_err[:110],color="r",ls='none',label = "C")
    ##ax1.errorbar(range(0,300),FC_array,yerr=1,color="r",ls='none',label = "F/C")
    #plt.legend()
    #ax1.errorbar(range(0,110),FC_array[:110],yerr=FC_err[:110],color="r",ls='none',label = "F/C")

    #valid = ~(np.isnan(FC_array) | np.isnan(FC_err))
    #a_fit,cov=curve_fit(linearFunc,np.array(range(0,300))[valid],FC_array[valid],sigma=FC_err[valid],absolute_sigma=False)
    #inter = a_fit[0]
    #slope = a_fit[1]
    #d_inter = np.sqrt(cov[0][0])
    #d_slope = np.sqrt(cov[1][1])
    #print(inter, slope, d_inter, d_slope)
    #yfit = inter + slope*range(50,80)
    ##ax1.plot(range(50,80),yfit,color="black")
    #ax1.plot(range(50,80),yfit,color="black",label="best fit:\n y = (%.3f$\pm$%.3f) *x\n + (%.1f$\pm$%.1f)"%(slope,d_slope,inter,d_inter))
    #plt.legend()
    #ax1.set_xlabel("SUEP Track Multiplicity")
    #ax1.set_ylabel("F/C")
    #ax.set_ylabel("Events")
    #ax1.set_ylim(0.0,20)
    #fig.suptitle("F/C %s"%(sample))
    #fig.savefig("Plots/FC_%s_%s.%s"%(sample,year,ext))
    #plt.close()

  f.Close()

#def makeCombineHistograms(samples,var,cut):
#  f = ROOT.TFile.Open("combineInputscan.root","RECREATE")
#  #makeQCD = True
#  for sample in samples:
#    for systematic in ["m2t0p5", "m2t1", "m2t2", "m2t3", "m2t4", "m3t1p5", "m3t3", "m3t6", "m5t1", "m5t5", "m5t10"]:
#    #for systematic in ["","killtrk","AK4up","AK4down","trigup","trigdown","PUup","PUdown"]:
#      #with open(directory+"myhistos_%s_2%s.p"%(sample,systematic), "rb") as pkl_file:
#      with open(directory+"myhistos_%s_%s.p"%(sample,systematic), "rb") as pkl_file:
#          out = pickle.load(pkl_file)
#          scale= lumi*xsecs[sample]/out["sumw"][sample]
#          scaled = {}
#          var2 = var+"_%s"%cut
#          xvar = "SUEP Jet Track Multiplicity"
#          for name, h in out.items():
#            if var2 not in name:
#              continue
#            if isinstance(h, hist.Hist):
#              scaled[name] = h.copy()
#              scaled[name].scale(scale)
#              s = scaled[name].to_hist().to_numpy()
#              #if systematic == "":
#              b = qcdscaled[name].to_hist().to_numpy()
#              #else:
#              #  systematic = "_"+systematic #for aesthetic purposes
#
#              x1 = 0
#              x2 = inner_tracks
#              x3 = region_cuts_tracks[0]
#              x4 = 300
#              y1 = 30
#              y2 = inner_sphere
#              y3 = region_cuts_sphere[0]
#              y4 = 100
#              if sample == "sig200" or sample == "sig125":
#                point=1
#              if sample == "sig300" or sample == "sig400":
#                point=2
#              if sample == "sig700" or sample == "sig1000":
#                point=3
#              x0 = region_cuts_tracks[0]
#              y0 = region_cuts_sphere[0] #use only gap point
#              region_sum = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"SR":0,"ALL":0}
#              region_sumqcd = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"SR":0,"ALL":0}
#              for region in ["A","B","C","D","E","F","G","H","SR","ALL"]:
#                if region == "A":
#                  xx = x1
#                  xxx = x2
#                  yy = y1
#                  yyy = y2
#                elif region == "B":
#                  xx = x2
#                  xxx = x3
#                  yy = y1
#                  yyy = y2
#                elif region == "C":
#                  xx = x0
#                  xxx = x4
#                  yy = y1
#                  yyy = y2
#                elif region == "D":
#                  xx = x1
#                  xxx = x2
#                  yy = y2
#                  yyy = y3
#                elif region == "E":
#                  xx = x2
#                  xxx = x3
#                  yy = y2
#                  yyy = y3
#                elif region == "F":
#                  xx = x0
#                  xxx = x4
#                  yy = y2
#                  yyy = y3
#                elif region == "G":
#                  xx = x1
#                  xxx = x2
#                  yy = y0
#                  yyy = y4
#                elif region == "H":
#                  xx = x2
#                  xxx = x3
#                  yy = y0
#                  yyy = y4
#                elif region == "SR":
#                  xx = x0
#                  xxx = x4
#                  yy = y0
#                  yyy = y4
#                elif region == "ALL":
#                  xx = 0
#                  xxx = x4
#                  yy = 0
#                  yyy = y4
#                else:
#                  print("what happened")
#                  pass
#                h = ROOT.TH2F("%s_%s"%(systematic,region),"%s_%s"%(systematic,region),300,0,300,100,0,1)
#                #h = ROOT.TH2F("%s_%s%s"%(sample,region,systematic),"%s_%s%s"%(sample,region,systematic),300,0,300,100,0,1)
#                #if systematic == "":
#                hb = ROOT.TH2F("QCD_%s_%s"%(sample,region),"QCD_%s_%s"%(sample,region),300,0,300,100,0,1)
#                for x in range(xx,xxx):
#                  for y in range(yy,yyy):
#                    region_sum[region] = region_sum[region] + s[0][0][x][y]
#                    h.Fill(s[2][x],s[3][y],s[0][0][x][y])
#                    #if systematic == "":
#                    region_sum[region] = region_sum[region] + s[0][0][x][y]
#                    region_sumqcd[region] = region_sumqcd[region] + b[0][0][x][y]
#                    hb.Fill(b[2][x],b[3][y],b[0][0][x][y])
#                h.Write()
#                #if systematic == "":
#                hb.Write()
#              if systematic == "":
#                print(sample)
#                print(region_sum)
#                print(region_sumqcd)
#  f.Close()


def make_limits(scan=0):
  dirx = "/uscms/home/mreid/nobackup/sueps/analysis/SUEPs/limits/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/"
  values = {0:[],1:[],2:[],3:[],4:[],5:[]}
  xlab = "$Temp$ [GeV]"
  if scan == 0 :
    sigs = [125,200,300,400,700,1000]
    xs = sigs
    xlab = "$m_{s}$ [GeV]"
  elif scan == 2:
    sigs = ["m2t0p5", "m2t1", "m2t2", "m2t3", "m2t4"]
    xs = [0.5,1,2,3,4]
  elif scan == 3:
    sigs = ["m3t1p5", "m3t3", "m3t6"]
    xs = [1.5,3,5]
  elif scan == 5:
    sigs = ["m5t1", "m5t5", "m5t10"]
    xs = [1,5,10]
  xsec=[]
  for sig in sigs:
    if scan == 0:
      xsec1 = xsecs["sig%s"%sig]
      f = ROOT.TFile.Open(dirx+"higgsCombineTest.AsymptoticLimits.mH%s.root"%sig)
      txt = "$m_{\phi}$ = 2 GeV\n T= 2 GeV"
    else:
      xsec1 = xsecs["sig400"]
      f = ROOT.TFile.Open(dirx+"higgsCombineTest.AsymptoticLimits.%s.root"%sig)
      txt = "$m_s$ = 400 GeV\n $m_{\phi}$ = %s GeV"%scan
    xsec.append(xsec1)
    tree = f.Get("limit")
    for i in range(0,6):
      tree.GetEntry(i)
      values[i].append(tree.limit * xsec1)

  print(values)
  fig, ax = plt.subplots()
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
  ax.add_artist(AnchoredText(txt,loc="upper center",prop=dict(size=10)))
  ax.fill_between(xs,values[0],values[4],color="yellow",label="Expected $\pm 2 \sigma$") # 2 sigma band
  ax.fill_between(xs,values[1],values[3],color="lime",label="Expected $\pm 1 \sigma$") # 1 sigma band
  ax.plot(xs,values[2],color="black",label = "Median Expected",marker=".",linestyle="--") #median band
  ax.plot(xs,xsec,color="blue",label = "Theory",marker=".",linestyle="--") #theory band
  ax.set_xlabel(xlab)
  ax.set_ylabel("Cross Section (pb)")
  ax.set_yscale("log")
  ax.legend()
  fig.tight_layout()
  fig.savefig("/uscms/home/mreid/nobackup/sueps/analysis/SUEPs/scouting/plotter/Plots/limits_%s_%s.%s"%(scan,year,ext))
  plt.close()

