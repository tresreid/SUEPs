from utils import *

cuts = ["Cut 0: No Cut:","Cut 1: Trigger", "Cut 2: $\HT > 560 \GeV$","Cut 3: AK15 Jets $>2$","Cut 4a: \\nSUEPConstituents $>%d$"%region_cuts_tracks[0],"Cut 5a: \\boostedSphericity $>0.%s$"%region_cuts_sphere[0],"Cut 4b: \\nSUEPConstituents $>%d$"%region_cuts_tracks[1],"Cut 5b: \\boostedSphericity $>0.%s$"%region_cuts_sphere[1],"Cut 4c: \\nSUEPConstituents $>%d$"%region_cuts_tracks[2],"Cut 5c:\\boostedSphericity $>0.%s$"%region_cuts_sphere[2],"Cut 4d: \\nSUEPConstituents $>%d$"%region_cuts_tracks[3],"Cut 5d:\\boostedSphericity $>0.%s$"%region_cuts_sphere[3]]

def make_cutflow(samples,var):
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
  for SR in [0,1,2,3]:
    x1 = region_cuts_tracks[SR]
    y1 = region_cuts_sphere[SR]/100.
    b3 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
    for (k,b) in b3.items():
      cutflow["QCD"].append(b.sum())
      cutflow_releff["QCD"].append(100*b.sum()/cutflow["QCD"][3])
    b4 = qcdscaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
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
        for SR in [0,1,2,3]:
          x1 = region_cuts_tracks[SR]
          y1 = region_cuts_sphere[SR]/100.
          s3 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(0,1)).values()
          for (k,s) in s3.items():
            cutflow[sample].append(s.sum())
            cutflow_releff[sample].append(100*s.sum()/cutflow[sample][3])
            cutflow_sig[sample].append(s.sum()/np.sqrt(s.sum()+cutflow["QCD"][4+2*SR]+(cutflow["QCD"][4+2*SR]**2)))

          s4 = scaled["SR1_suep_3"].integrate("nPFCand",slice(x1,300)).integrate("eventBoostedSphericity",slice(y1,1)).values()
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
    print("%s & %.2e & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],yields["QCD"][i],yields["sig125"][i],yields["sig200"][i],yields["sig300"][i],yields["sig400"][i],yields["sig700"][i],yields["sig1000"][i]))
    if i == 3 or i==5 or i==7 or i==9 or i==11:
      print("\\hline")
  print("##################  RelEff  ################")
  for i in releff.index:
    print("%s & %.2e & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i+1],releff["QCD"][i],releff["sig125"][i],releff["sig200"][i],releff["sig300"][i],releff["sig400"][i],releff["sig700"][i],releff["sig1000"][i]))
    if i+1 == 3 or i+1==5 or i+1==7 or i+1==9 or i+1==11:
      print("\\hline")
  print("##################  SIGS  ################")
  for i in sigs.index:
    print("%s & %.2e & %.2e & %.2e & %.2e & %.2e & %.2e \\\\"%(cuts[i],sigs["sig125"][i],sigs["sig200"][i],sigs["sig300"][i],sigs["sig400"][i],sigs["sig700"][i],sigs["sig1000"][i]))
    if i == 3 or i==5 or i==7 or i==9 or i==11:
      print("\\hline")

def make_systematics(samples,var,systematics1="",systematics2=""):
  name = "dist_%s"%var
  final_cut = 35 # 50 bins -> 35= 0.7 cut
  higgs = False
  if systematics2 =="higgsdown":
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
        print("%s & %.2f & x & x & x & x & x \\\\"%(cuts[i],(yields["sig125"][i]-yields["sig125%s"%(systematics1)][i])/yields["sig125"][i]))
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
        print("%s & %.2f & x & x & x & x & x \\\\"%(cuts[i],(yields["sig125%s"%(systematics1)][i]-yields["sig125%s"%(systematics2)][i])/yields["sig125"][i]))
        if i == 3 or i==5 or i==7 or i==9 or i == 11:
          print("\\hline")
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
        print("%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],(yields["sig125"][i]-yields["sig125%s"%(systematics1)][i])/yields["sig125"][i],(yields["sig200"][i]-yields["sig200%s"%(systematics1)][i])/yields["sig200"][i],(yields["sig300"][i]-yields["sig300%s"%(systematics1)][i])/yields["sig300"][i],(yields["sig400"][i]-yields["sig400%s"%(systematics1)][i])/yields["sig400"][i],(yields["sig700"][i]-yields["sig700%s"%(systematics1)][i])/yields["sig700"][i],(yields["sig1000"][i]-yields["sig1000%s"%(systematics1)][i])/yields["sig1000"][i]))
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
        print("%s & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\"%(cuts[i],(yields["sig125%s"%(systematics1)][i]-yields["sig125%s"%(systematics2)][i])/yields["sig125"][i],(yields["sig200%s"%(systematics1)][i]-yields["sig200%s"%(systematics2)][i])/yields["sig200"][i],(yields["sig300%s"%(systematics1)][i]-yields["sig300%s"%(systematics2)][i])/yields["sig300"][i],(yields["sig400%s"%(systematics1)][i]-yields["sig400%s"%(systematics2)][i])/yields["sig400"][i],(yields["sig700%s"%(systematics1)][i]-yields["sig700%s"%(systematics2)][i])/yields["sig700"][i],(yields["sig1000%s"%(systematics1)][i]-yields["sig1000%s"%(systematics2)][i])/yields["sig1000"][i]))
        if i == 3 or i==5 or i==7 or i==9 or i == 11:
          print("\\hline")



def makeCombineHistograms(samples,var,cut):
  f = ROOT.TFile.Open("combineInput.root","RECREATE")
  #makeQCD = True
  for sample in samples:
    #for systematic in ["m2t0p5", "m2t1", "m2t2", "m2t3", "m2t4", "m3t1p5", "m3t3", "m3t6", "m5t1", "m5t5", "m5t10"]:
    for systematic in ["","killtrk","AK4up","AK4down","trigup","trigdown","PUup","PUdown"]:
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
      txt = "$M_{\phi}$ = 2 GeV\n T= 2 GeV"
    else:
      xsec1 = xsecs["sig400"]
      f = ROOT.TFile.Open(dirx+"higgsCombineTest.AsymptoticLimits.%s.root"%sig)
      txt = "$M_s$ = 400 GeV\n $M_{\phi}$ = %s GeV"%scan
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

