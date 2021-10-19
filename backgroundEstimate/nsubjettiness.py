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
          "rho0_50":float(cols[11]),"rho1_50":float(cols[12]),"rho2_50":float(cols[13]),
          "rho0_20":float(cols[14]),"rho1_20":float(cols[15]),"rho2_20":float(cols[16]),
          "rho0_10":float(cols[17]),"rho1_10":float(cols[18]),"rho2_10":float(cols[19]),
          "rho0_05":float(cols[20]),"rho1_05":float(cols[21]),"rho2_05":float(cols[22]),
          "rho0_15":float(cols[23]),"rho1_15":float(cols[24]),"rho2_15":float(cols[25]),
          "rho0_30":float(cols[26]),"rho1_30":float(cols[27]),"rho2_30":float(cols[28]),
          "sphericity":float(cols[29]),"sphericity_b":float(cols[30]),"sphericity_b2":float(cols[31]),
          "C":float(cols[32]),"C_b":float(cols[33]),"C_b2":float(cols[34]),
          "D":float(cols[35]),"D_b":float(cols[36]),"D_b2":float(cols[37]),
          "aPlanarity":float(cols[38]),"aPlanarity_b":float(cols[39]),"aPlanarity_b2":float(cols[40])
          })
  df = pd.DataFrame(dr)
  del dr
  df["phi"] = df["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
  return df

df1000 =openReco("variables_sig_1000_v0",0.17)
df750 = openReco("variables_sig_750_v0",0.5)
df400 = openReco("variables_sig_400_v0",5.9)
df300 = openReco("variables_sig_300_v0",8.9)
df200 = openReco("variables_sig_200_v0",13.6)

gc.collect()
          
#xsecs = [311900,29070,5962,1207,119.9,25.24] # signal xsec are (125,34.8),(300,8.9), (400,5.9), (750,0.5), (1000,0.17)
#files = [300,500,700,1000,1500,2000]
smallest_wgt = 25.24*lumi/100000
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
          "rho0_50":float(cols[11]),"rho1_50":float(cols[12]),"rho2_50":float(cols[13]),
          "rho0_20":float(cols[14]),"rho1_20":float(cols[15]),"rho2_20":float(cols[16]),
          "rho0_10":float(cols[17]),"rho1_10":float(cols[18]),"rho2_10":float(cols[19]),
          "rho0_05":float(cols[20]),"rho1_05":float(cols[21]),"rho2_05":float(cols[22]),
          "rho0_15":float(cols[23]),"rho1_15":float(cols[24]),"rho2_15":float(cols[25]),
          "rho0_30":float(cols[26]),"rho1_30":float(cols[27]),"rho2_30":float(cols[28]),
          "sphericity":float(cols[29]),"sphericity_b":float(cols[30]),"sphericity_b2":float(cols[31]),
          "C":float(cols[32]),"C_b":float(cols[33]),"C_b2":float(cols[34]),
          "D":float(cols[35]),"D_b":float(cols[36]),"D_b2":float(cols[37]),
          "aPlanarity":float(cols[38]),"aPlanarity_b":float(cols[39]),"aPlanarity_b2":float(cols[40])
      })
  qcdi = qcdi+1
qcd_df = pd.DataFrame(qcddr)
#print(qcd_df)
del qcddr
#print(qcd_df)
qcd_df["phi"] = qcd_df["phi"].apply(lambda x: x-2*np.pi if x> np.pi else x)
#gc.collect()


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
def closure(var1,binx,var2,biny,SR_D,gauss,sel1,sel2):
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
      bkgA = df_bkg[(df_bkg[var1] < i) & (df_bkg[var2] < j)]["wgt"].sum() #lower left
      bkgB = df_bkg[(df_bkg[var1] < i) & (df_bkg[var2] > j)]["wgt"].sum() # upper left
      bkgC = df_bkg[(df_bkg[var1] > i) & (df_bkg[var2] < j)]["wgt"].sum() # lower right
      bkgD = df_bkg[(df_bkg[var1] > i) & (df_bkg[var2] > j)]["wgt"].sum() # upper right
      bkgC_evts = len(df_bkg[(df_bkg[var1] > i) & (df_bkg[var2] < j)]) # lower right
      bkgD_evts = len(df_bkg[(df_bkg[var1] > i) & (df_bkg[var2] > j)]) # upper right

      bkgA_err = np.sqrt((df_bkg[(df_bkg[var1] < i) & (df_bkg[var2] < j)]["wgt"]**2).sum()) #lower left
      bkgB_err = np.sqrt((df_bkg[(df_bkg[var1] < i) & (df_bkg[var2] > j)]["wgt"]**2).sum()) # upper left
      bkgC_err = np.sqrt((df_bkg[(df_bkg[var1] > i) & (df_bkg[var2] < j)]["wgt"]**2).sum()) # lower right
      bkgD_err = np.sqrt((df_bkg[(df_bkg[var1] > i) & (df_bkg[var2] > j)]["wgt"]**2).sum()) # upper right

      sig_1000A= sig1000[(sig1000[var1] < i) & (sig1000[var2] < j)]["wgt"].sum()
      sig_750A = sig750[(sig750[var1] < i) & (sig750[var2] < j)]["wgt"].sum()
      sig_400A = sig400[(sig400[var1] < i) & (sig400[var2] < j)]["wgt"].sum()
      sig_300A = sig300[(sig300[var1] < i) & (sig300[var2] < j)]["wgt"].sum()
      sig_200A = sig200[(sig200[var1] < i) & (sig200[var2] < j)]["wgt"].sum()

      sig_1000B= sig1000[(sig1000[var1] < i) & (sig1000[var2] > j)]["wgt"].sum()
      sig_750B = sig750[(sig750[var1] < i) & (sig750[var2] > j)]["wgt"].sum()
      sig_400B = sig400[(sig400[var1] < i) & (sig400[var2] > j)]["wgt"].sum()
      sig_300B = sig300[(sig300[var1] < i) & (sig300[var2] > j)]["wgt"].sum()
      sig_200B = sig200[(sig200[var1] < i) & (sig200[var2] > j)]["wgt"].sum()

      sig_1000C= sig1000[(sig1000[var1] > i) & (sig1000[var2] < j)]["wgt"].sum()
      sig_750C = sig750[(sig750[var1] > i) & (sig750[var2] < j)]["wgt"].sum()
      sig_400C = sig400[(sig400[var1] > i) & (sig400[var2] < j)]["wgt"].sum()
      sig_300C = sig300[(sig300[var1] > i) & (sig300[var2] < j)]["wgt"].sum()
      sig_200C = sig200[(sig200[var1] > i) & (sig200[var2] < j)]["wgt"].sum()

      sig_1000D= sig1000[(sig1000[var1] > i) & (sig1000[var2] > j)]["wgt"].sum()
      sig_750D = sig750[(sig750[var1] > i) & (sig750[var2] > j)]["wgt"].sum()
      sig_400D = sig400[(sig400[var1] > i) & (sig400[var2] > j)]["wgt"].sum()
      sig_300D = sig300[(sig300[var1] > i) & (sig300[var2] > j)]["wgt"].sum()
      sig_200D = sig200[(sig200[var1] > i) & (sig200[var2] > j)]["wgt"].sum()
      if SR_D:
        sig_1000= sig_1000D 
        sig_750 = sig_750D 
        sig_400 = sig_400D 
        sig_300 = sig_300D 
        sig_200 = sig_200D 

        #sig_1000x = sig1000[(sig1000[var1] < i) | (sig1000[var2] < j)]["wgt"].sum()
        #sig_750x = sig750[(sig750[var1] < i) | (sig750[var2] < j)]["wgt"].sum()
        #sig_400x = sig400[(sig400[var1] < i) | (sig400[var2] < j)]["wgt"].sum()
        #sig_300x = sig300[(sig300[var1] < i) | (sig300[var2] < j)]["wgt"].sum()
        #sig_200x = sig200[(sig200[var1] < i) | (sig200[var2] < j)]["wgt"].sum()
        bkg = bkgD
        bkg_evts = bkgD_evts
        predicted_err_stat = bkgD_err
        bkgx = bkgA+bkgB+bkgC
        predicted = bkgB*bkgC/bkgA
        #predicted_err_stat = bkgB_err*bkgC_err/bkgA_err
        predicted_err_sys = predicted * np.sqrt((bkgA_err/bkgA)**2 + (bkgC_err/bkgC)**2 + (bkgB_err/bkgB)**2)
        predicted_contam1000 =(bkgB+sig_1000B)*(bkgC+sig_1000C)/(bkgA+sig_1000A)
        predicted_contam750 = (bkgB+sig_750B)*(bkgC+sig_750C)/(bkgA+sig_750A)
        predicted_contam400 = (bkgB+sig_400B)*(bkgC+sig_400C)/(bkgA+sig_400A)
        predicted_contam300 = (bkgB+sig_300B)*(bkgC+sig_300C)/(bkgA+sig_300A)
        predicted_contam200 = (bkgB+sig_200B)*(bkgC+sig_200C)/(bkgA+sig_200A)
      else:
        sig_1000= sig_1000C 
        sig_750 = sig_750C 
        sig_400 = sig_400C 
        sig_300 = sig_300C 
        sig_200 = sig_200C 

        #sig_1000x= sig1000[(sig1000[var1] < i) | (sig1000[var2] > j)]["wgt"].sum()
        #sig_750x = sig750[(sig750[var1] < i) | (sig750[var2] > j)]["wgt"].sum()
        #sig_400x = sig400[(sig400[var1] < i) | (sig400[var2] > j)]["wgt"].sum()
        #sig_300x = sig300[(sig300[var1] < i) | (sig300[var2] > j)]["wgt"].sum()
        #sig_200x = sig200[(sig200[var1] < i) | (sig200[var2] > j)]["wgt"].sum()
        bkg = bkgC
        bkg_evts = bkgC_evts
        predicted_err_stat = bkgC_err
        bkgx = bkgA+bkgB+bkgD
        predicted = bkgA*bkgD/bkgB
        #predicted_err_stat = bkgA_err*bkgD_err/bkgB_err
        predicted_err_sys = predicted * np.sqrt((bkgA_err/bkgA)**2 + (bkgD_err/bkgD)**2 + (bkgB_err/bkgB)**2)
        predicted_contam1000 = (bkgA+sig_1000A)*(bkgD+sig_1000D)/(bkgB+sig_1000B)
        predicted_contam750 = (bkgA+sig_750A)*(bkgD+sig_750D)/(bkgB+sig_750B)
        predicted_contam400 = (bkgA+sig_400A)*(bkgD+sig_400D)/(bkgB+sig_400B)
        predicted_contam300 = (bkgA+sig_300A)*(bkgD+sig_300D)/(bkgB+sig_300B)
        predicted_contam200 = (bkgA+sig_200A)*(bkgD+sig_200D)/(bkgB+sig_200B)

      
      #predicted_err_sys = predicted * (1/bkgA + 1/bkgB + 1/bkg)**(0.5)
      #predicted_err_stat = (predicted)**(0.5)
      if bkg == 0:
        predicted_err_stat = smallest_wgt
      signif_10 = sig_1000/(sig_1000+predicted+(0.5*predicted)**2)**(0.5) 
      signif_7 = sig_750/(sig_750+predicted+(0.9*predicted)**2)**(0.5) 
      signif_4 = sig_400/(sig_400+predicted+(0.9*predicted)**2)**(0.5) 
      signif_3 = sig_300/(sig_300+predicted+(0.9*predicted)**2)**(0.5) 
      signif_2 = sig_200/(sig_200+predicted+(0.9*predicted)**2)**(0.5) 
      signifcontam_10 = sig_1000/(sig_1000+predicted_contam1000+(0.5*predicted_contam1000)**2)**(0.5) 
      signifcontam_7 = sig_750/(sig_750+predicted_contam750+(0.5*predicted_contam750)**2)**(0.5) 
      signifcontam_4 = sig_400/(sig_400+predicted_contam400+(0.5*predicted_contam400)**2)**(0.5) 
      signifcontam_3 = sig_300/(sig_300+predicted_contam300+(0.5*predicted_contam300)**2)**(0.5) 
      signifcontam_2 = sig_200/(sig_200+predicted_contam200+(0.5*predicted_contam200)**2)**(0.5) 
      contam1000 =(predicted_contam1000-predicted)/predicted
      contam750 = (predicted_contam750-predicted)/predicted
      contam400 = (predicted_contam400-predicted)/predicted
      contam300 = (predicted_contam300-predicted)/predicted
      contam200 = (predicted_contam200-predicted)/predicted

      if predicted == 0:
        closure = float("nan")
        nonclosure = float("nan")
        pull = float("nan")
      else:
        closure = (predicted-bkg)/predicted
        nonclosure = max(abs(predicted-bkg)-(predicted_err_stat+predicted_err_sys),0)/((predicted+bkg)/2)
        pull = (predicted-bkg)/(predicted_err_stat+predicted_err_sys)
      closed = 1 #abs(nonclosure) < 0.5
      all_closure.append(closure)
      #closed = (predicted - predicted_err_sys -predicted_err_stat) + (bkgC + bkgC**(0.5)) < 0
#      if closed:
  #      print("%d %.2f %d %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %d"%(i,j,SR,bkgA,bkgB,bkgC,bkgD,predicted,predicted_err_sys,predicted_err_stat,sig_1000,sig_1000/tot_sig10,signif_10,sig_750,sig_750/tot_sig7,signif_7,sig_400,sig_400/tot_sig4,signif_4,sig_300,sig_300/tot_sig3,signif_3,sig_200,sig_200/tot_sig2,signif_2,closure, closed)) 

      dr_close.append({"i":i, "j":j, 
      "bkgA":bkgA, "bkgB":bkgB, "bkgC":bkgC, "bkgD":bkgD,"bkgEvents":bkg_evts, 
      "predicted":predicted, "predicted_err_sys":predicted_err_sys, "predicted_err_stat":predicted_err_stat, 
      "sig_1000":sig_1000, "eff_1000":sig_1000/tot_sig10, "signif_1000":signif_10,"predicted_w/sig1000":predicted_contam1000,"contamination_sig1000": contam1000,"signifcontam_1000":signifcontam_10,
      "sig_750":sig_750, "eff_750":sig_750/tot_sig7, "signif_750":signif_7, "predicted_w/sig750":predicted_contam750,"contamination_sig750": contam750,"signifcontam_750":signifcontam_7, 
      "sig_400":sig_400, "eff_400":sig_400/tot_sig4, "signif_400":signif_4, "predicted_w/sig400":predicted_contam400,"contamination_sig400": contam400,"signifcontam_400":signifcontam_4,
      "sig_300":sig_300, "eff_300":sig_300/tot_sig3, "signif_300":signif_3, "predicted_w/sig300":predicted_contam300,"contamination_sig300": contam300,"signifcontam_300":signifcontam_3,
      "sig_200":sig_200, "eff_200":sig_200/tot_sig2, "signif_200":signif_2, "predicted_w/sig200":predicted_contam200,"contamination_sig200": contam200,"signifcontam_200":signifcontam_2,
      "closure":closure,"nonclosure":nonclosure, "pull": pull
      #"bkgx":bkgx,#"contamination_1000":sig_1000x/float(sig_1000x+bkgx),"contamination_750":sig_750x/float(sig_750x+bkgx),"contamination_400":sig_400x/float(sig_400x+bkgx),"contamination_300":sig_300x/float(sig_300x+bkgx),"contamination_200":sig_200x/float(sig_200x+bkgx)
        })
  df_close = pd.DataFrame(dr_close)      
  Path("Plots/closure").mkdir(parents=True,exist_ok=True)
  df_close.to_csv("Plots/closure/table_%s_%s_%s.csv"%(SR_D,var1,var2))

  fig, ax1 = plt.subplots(1,1)
  SR_tit = ["C","D"]
  fig.suptitle("closure SR %s: %s %s "%(SR_tit[SR_D],var1,var2),y=1.0)
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
  fig.savefig("Plots/closure/closure_%s_%s_%s"%(SR_D,var1,var2))
  plt.close()

  fig, ax2 = plt.subplots(1,1)
  fig.suptitle("closuremap SR %s: %s %s "%(SR_tit[SR_D],var1,var2),y=1.0)
  piv = df_close.pivot("j","i","closure")
  ax2 = sns.heatmap(piv,cmap="seismic",center=0.0)
  ax2.invert_yaxis()
  ax2.set_yticklabels(['{:.2f}'.format(float(t.get_text())) for t in ax2.get_yticklabels()])
  ax2.set_xlabel("%s Cut"%var1)
  ax2.set_ylabel("%s Cut"%var2)
  fig.tight_layout()
  Path("Plots/closure").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/closure/closuremap_%s_%s_%s"%(SR_D,var1,var2))
  plt.close()

  fig, ax1 = plt.subplots(1,1)
  fig.suptitle("nonclosure SR %s: %s %s "%(SR_tit[SR_D],var1,var2),y=1.0)
  ax1.hist(df_close["nonclosure"],bins=100)
  ax1.set_xlabel("nonclosure")
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
  fig.savefig("Plots/closure/nonclosure_%s_%s_%s"%(SR_D,var1,var2))
  plt.close()

  fig, ax2 = plt.subplots(1,1)
  fig.suptitle("nonclosure map SR %s: %s %s "%(SR_tit[SR_D],var1,var2),y=1.0)
  piv = df_close.pivot("j","i","nonclosure")
  ax2 = sns.heatmap(piv,cmap="seismic",center=0.0)
  ax2.invert_yaxis()
  ax2.set_yticklabels(['{:.2f}'.format(float(t.get_text())) for t in ax2.get_yticklabels()])
  ax2.set_xlabel("%s Cut"%var1)
  ax2.set_ylabel("%s Cut"%var2)
  fig.tight_layout()
  Path("Plots/closure").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/closure/nonclosuremap_%s_%s_%s"%(SR_D,var1,var2))
  plt.close()

  fig, ax1 = plt.subplots(1,1)
  fig.suptitle("pull SR %s: %s %s "%(SR_tit[SR_D],var1,var2),y=1.0)
  ax1.hist(df_close["pull"],bins=100)
  ax1.set_xlabel("pull")
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
  fig.savefig("Plots/closure/pull_%s_%s_%s"%(SR_D,var1,var2))
  plt.close()

  fig, ax2 = plt.subplots(1,1)
  fig.suptitle("pullmap SR %s: %s %s "%(SR_tit[SR_D],var1,var2),y=1.0)
  piv = df_close.pivot("j","i","pull")
  ax2 = sns.heatmap(piv,cmap="seismic",center=0.0)
  ax2.invert_yaxis()
  ax2.set_yticklabels(['{:.2f}'.format(float(t.get_text())) for t in ax2.get_yticklabels()])
  ax2.set_xlabel("%s Cut"%var1)
  ax2.set_ylabel("%s Cut"%var2)
  fig.tight_layout()
  Path("Plots/closure").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/closure/pullmap_%s_%s_%s"%(SR_D,var1,var2))
  plt.close()

  fig, ax2 = plt.subplots(1,1)
  fig.suptitle("SR %s: %s %s "%(SR_tit[SR_D],var1,var2),y=1.0)
  piv = df_close.pivot("j","i","predicted")
  ax2 = sns.heatmap(piv,cmap="seismic")
  ax2.invert_yaxis()
  ax2.set_yticklabels(['{:.2f}'.format(float(t.get_text())) for t in ax2.get_yticklabels()])
  ax2.set_xlabel("%s Cut"%var1)
  ax2.set_ylabel("%s Cut"%var2)
  fig.tight_layout()
  Path("Plots/yieldmap").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/yieldmap/predictedmap_%s_QCD_%s_%s"%(SR_D,var1,var2))
  plt.close()


  for sig in [1000,750,400,300,200]:
    contamination = "contamination_sig%s"%sig
    fig, ax4 = plt.subplots(1,1)
    fig.suptitle("SR %s: %s %s "%(SR_tit[SR_D],var1,var2),y=1.0)
    piv = df_close.pivot("j","i",contamination)
    ax2 = sns.heatmap(piv,cmap="seismic",center=0.0)
    ax2.invert_yaxis()
    ax2.set_yticklabels(['{:.2f}'.format(float(t.get_text())) for t in ax2.get_yticklabels()])
    ax2.set_xlabel("%s Cut"%var1)
    ax2.set_ylabel("%s Cut"%var2)
    fig.tight_layout()
    Path("Plots/contamination").mkdir(parents=True,exist_ok=True)
    fig.savefig("Plots/contamination/contaminationmap_%s_%s_%s_%s"%(SR_D,sig,var1,var2))
    plt.close()

    signif = "signif_%s"%sig
    fig, ax3 = plt.subplots(1,1)
    fig.suptitle("signif SR %s sig%s: %s %s "%(SR_tit[SR_D],sig,var1,var2),y=1.0)
    #piv = df_close[abs(df_close["closure"]) <= 0.5].pivot("j","i",signif)
    piv = df_close.pivot("j","i",signif)
    ax3 = sns.heatmap(piv,cmap="winter")
    ax3.invert_yaxis()
    ax3.set_yticklabels(['{:.2f}'.format(float(t.get_text())) for t in ax3.get_yticklabels()])
    ax3.set_xlabel("%s Cut"%var1)
    ax3.set_ylabel("%s Cut"%var2)
    fig.tight_layout()
    Path("Plots/signifmap").mkdir(parents=True,exist_ok=True)
    fig.savefig("Plots/signifmap/signifmap_%s_%s_%s_%s"%(SR_D,sig,var1,var2))
    plt.close()

    signif = "signifcontam_%s"%sig
    fig, ax3 = plt.subplots(1,1)
    fig.suptitle("contaminated signif SR %s sig%s: %s %s "%(SR_tit[SR_D],sig,var1,var2),y=1.0)
    #piv = df_close[abs(df_close["closure"]) <= 0.5].pivot("j","i",signif)
    piv = df_close.pivot("j","i",signif)
    ax3 = sns.heatmap(piv,cmap="winter")
    ax3.invert_yaxis()
    ax3.set_yticklabels(['{:.2f}'.format(float(t.get_text())) for t in ax3.get_yticklabels()])
    ax3.set_xlabel("%s Cut"%var1)
    ax3.set_ylabel("%s Cut"%var2)
    fig.tight_layout()
    Path("Plots/signifmap").mkdir(parents=True,exist_ok=True)
    fig.savefig("Plots/signifmap/signifcontammap_%s_%s_%s_%s"%(SR_D,sig,var1,var2))
    plt.close()

    sigs = "sig_%s"%sig
    fig, ax4 = plt.subplots(1,1)
    fig.suptitle("SR %s sig%s: %s %s "%(SR_tit[SR_D],sig,var1,var2),y=1.0)
    #piv = df_close[abs(df_close["closure"]) <= 0.5].pivot("j","i",sigs)
    piv = df_close.pivot("j","i",sigs)
    ax4 = sns.heatmap(piv,cmap="seismic")
    ax4.invert_yaxis()
    ax4.set_yticklabels(['{:.2f}'.format(float(t.get_text())) for t in ax4.get_yticklabels()])
    ax4.set_xlabel("%s Cut"%var1)
    ax4.set_ylabel("%s Cut"%var2)
    fig.tight_layout()
    Path("Plots/yieldmap").mkdir(parents=True,exist_ok=True)
    fig.savefig("Plots/yieldmap/yieldmap_%s_%s_%s_%s"%(SR_D,sig,var1,var2))
    plt.close()

    sigs = "predicted_w/sig%s"%sig
    fig, ax4 = plt.subplots(1,1)
    SR_tit = ["C","D"]
    fig.suptitle("SR %s sig%s: %s %s "%(SR_tit[SR_D],sig,var1,var2),y=1.0)
    #piv = df_close[abs(df_close["closure"]) <= 0.5].pivot("j","i",sigs)
    piv = df_close.pivot("j","i",sigs)
    ax4 = sns.heatmap(piv,cmap="seismic")
    ax4.invert_yaxis()
    ax4.set_yticklabels(['{:.2f}'.format(float(t.get_text())) for t in ax4.get_yticklabels()])
    ax4.set_xlabel("%s Cut"%var1)
    ax4.set_ylabel("%s Cut"%var2)
    fig.tight_layout()
    Path("Plots/yieldmap").mkdir(parents=True,exist_ok=True)
    fig.savefig("Plots/yieldmap/predictedmap_%s_%s_%s_%s"%(SR_D,sig,var1,var2))
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
  h1= ax1.hist2d(qcd_df[var1],qcd_df[var2],bins=[len(steps1)-1,len(steps2)-1],range=[[steps1[0],steps1[-1]],[steps2[0],steps2[-1]]],norm=matplotlib.colors.LogNorm(),cmap=matplotlib.cm.spring,weights=qcd_df["wgt"])
  fig.colorbar(h1[3], ax=ax1)
  h= ax1.hist2d(sub_df[var1],sub_df[var2],bins=[len(steps1)-1,len(steps2)-1],range=[[steps1[0],steps1[-1]],[steps2[0],steps2[-1]]],norm=matplotlib.colors.LogNorm(),cmap=matplotlib.cm.winter,weights=sub_df["wgt"])
  fig.colorbar(h[3], ax=ax1)
  ax1.set_xlabel(var1)
  ax1.set_ylabel(var2)
  ax1.axvline(x=xline,linestyle=':',color='black')
  ax1.axhline(y=yline,linestyle=':',color='black')


  #bin_means1 = binned_statistic(qcd_df[var1],qcd_df[var2],"mean",bins=20,range=[0,140])
  #bin_std1 = binned_statistic(qcd_df[var1],qcd_df[var2],"std",bins=20,range=[0,140])
  #bin_x1 = bin_means1[1][1:]
  #bin_x2 = bin_means1[1][:-1]
  #bin_x = [(x1+x2)/2 for x1,x2 in zip(bin_x1,bin_x2)]
  #mask1 = np.isfinite(bin_means1[0])
  #ax1.errorbar(np.array(bin_x)[mask1],np.array(bin_means1[0])[mask1],yerr=np.array(bin_std1[0])[mask1],color="k",fmt=".",errorevery=1)

  #bin_means2 = binned_statistic(qcd_df[var2],qcd_df[var1],"mean",bins=20,range=[steps2[0],steps2[-1]])
  #bin_std2 = binned_statistic(qcd_df[var2],qcd_df[var1],"std",bins=20,range=[steps2[0],steps2[-1]])
  #bin_y1 = bin_means2[1][1:]
  #bin_y2 = bin_means2[1][:-1]
  #bin_y = [(y1+y2)/2 for y1,y2 in zip(bin_y1,bin_y2)]
  #mask2 = np.isfinite(bin_means2[0])
  #ax1.errorbar(np.array(bin_means2[0])[mask2],np.array(bin_y)[mask2],xerr=np.array(bin_std2[0])[mask2],color="navy",fmt=".",errorevery=1)

  fig.tight_layout()
  Path("Plots/2d").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/2d/2dSR_%s_%s_%s.png"%(sig,var1,var2))
  plt.close()

def binned_dist(df,var1,var2,binx,biny):
    
  fig, (ax1) = plt.subplots(1,1,figsize=(21,7))
  fig2, (ax2) = plt.subplots(1,1,figsize=(21,7))
  ax1.set_title("%s binned by %s"%(var1,var2))
  colors = ["red","green","orange","blue","black","magenta"]
  if "jetTracks" in var1:
    rg = [0,100]
  elif "rho" in var1:
    rg = [0.25,2]
  else:
    rg=[0.10,1.0]
  for x in range(len(biny)-1): 
    subdf =df[(df[var2] >= biny[x]) & (df[var2] < biny[x+1])]
    lab="[%s,%s)"%(biny[x],biny[x+1])
    n, bins, _ = ax1.hist(subdf[var1],bins=binx,range=rg,histtype=u'step',density=True,weights=subdf["wgt"],linestyle="solid",color=colors[x], label=lab) 
    n1, bins1, _ = ax2.hist(subdf[var1],bins=binx,range=rg)#,histtype=u'step',weights=subdf["wgt"],linestyle="solid",color=colors[x], label=lab) 
    mid = 0.5*(bins[1:] + bins[:-1])
    tot = sum(n1)*np.diff(bins1)
    if tot.all() == 0:
      tot=1
    #print(n,sum(n))
    errs = np.sqrt(n1)/tot
    #plt.clf()
    ax1.errorbar(mid, n, yerr=errs, fmt='none',color=colors[x], label=lab)

  ax1.legend()
  ax1.set_xlabel(var1)
  ax1.set_ylabel("normalized events")
  fig.tight_layout()
  Path("Plots/2d").mkdir(parents=True,exist_ok=True)
  fig.savefig("Plots/2d/binnedDist_%s_%s.png"%(var1,var2))
  plt.close()


def make_eff_combo(reco_group,qcd_group,signal, var, binx, eta_cuts=0):
  fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(21,7))
  

  fig.suptitle("sig%s"%(signal)) 
 
  colors = ["red","green","orange","blue","black","magenta"]
  sig,tot_sig,bkg1,tot_bkg = get_sig(reco_group,qcd_group,var,binx) 
  bkg2 = np.array(bkg1)
  bkg3 = np.square(0.5*bkg2)
  bkg = np.add(bkg2,bkg3)
#  sigr,tot_sigr,bkg1r,tot_bkgr = get_sig(reco_group,qcd_group,var,binx,True) 
#  bkg2r = np.array(bkg1r)
#  bkg3r = np.square(0.5*bkg2r)
#  bkgr = np.add(bkg2r,bkg3r)

  ax1.hist(reco_group[var],  bins=binx,histtype=u'step',density=True,color="r",linestyle="solid",label="sig")
  ax1.hist(qcd_group[var],   bins=binx,histtype=u'step',density=True,color="black",linestyle="dashed",label="qcd")
  #ax1.hist(reco_group[var],  bins=binx,histtype=u'step',density=True,weights=reco_group["wgt"],color="r",linestyle="solid",label="sig")
  #ax1.hist(qcd_group[var],   bins=binx,histtype=u'step',density=True,weights=qcd_group["wgt"],color="black",linestyle="dashed",label="qcd")

  ax2.errorbar(binx,sig/(np.sqrt(np.add(sig,bkg))),(sig/(np.sqrt(np.add(sig,bkg))))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(4*np.add(sig,bkg)))),ecolor="r",label="signif",color="r",linestyle="dashdot",errorevery=1)
#  ax2.errorbar(binx,sigr/(np.sqrt(np.add(sigr,bkgr))),(sigr/(np.sqrt(np.add(sigr,bkgr))))*np.sqrt(np.add(np.reciprocal(sigr),np.reciprocal(4*np.add(sigr,bkgr)))),ecolor="b",label="signif_reverse",color="b",linestyle="dashdot",errorevery=1)

  ax3.errorbar(binx,np.multiply(bkg1,1./tot_bkg),np.multiply(bkg1,1./tot_bkg)*np.sqrt(np.add(np.reciprocal(bkg1),np.reciprocal(tot_bkg))),ecolor="black",label="bkg_eff",color="black",linestyle="dashed",errorevery=1)
#  ax3.errorbar(binx,np.multiply(bkg1r,1./tot_bkgr),np.multiply(bkg1r,1./tot_bkgr)*np.sqrt(np.add(np.reciprocal(bkg1r),np.reciprocal(tot_bkgr))),ecolor="m",label="bkg_eff_reverse",color="m",linestyle="dashed",errorevery=1)
  ax3.errorbar(binx,np.multiply(sig,1./tot_sig),np.multiply(sig,1./tot_sig)*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(tot_sig))),ecolor="r",label="sig_eff",color="r",linestyle="solid",errorevery=1)
#  ax3.errorbar(binx,np.multiply(sigr,1./tot_sigr),np.multiply(sigr,1./tot_sigr)*np.sqrt(np.add(np.reciprocal(sigr),np.reciprocal(tot_sigr))),ecolor="b",label="sig_eff_reverse",color="b",linestyle="solid",errorevery=1)

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
  ax2.set_yscale('log')
  ax2.set_ylim(1e-6,2)
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



pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50,200])
eta_bins = np.array(range(-250,250,25))/100.
phi_bins = np.array(range(-31,31,5))/10.
#print("2d plots tau")
#make_2d_correlation(qcd_df, "jetTracks",range(0,500), "t21",tau_bins)
#make_2d_correlation(qcd_df, "jetTracks",range(0,500), "t32",tau_bins)
#print("2d plots rho")
#make_2d_correlation(qcd_df, "jetTracks",range(0,500), "rho1",rho_bins)
#make_2d_correlation(qcd_df, "jetTracks",range(0,500), "rho2",rho_bins)
#make_2d_correlation(qcd_df, "jetTracks",range(0,500), "rho0",rho_bins)



combos = []
combos2 = []
combos3 = []
combos4 = []
combos5 = []
combos6 = []
combos7 = []
combos8 = []
#
tau_bins = [0.01*x for x in range(0,100,1)]
rho_bins = [.01*x for x in range(0,500,5)]
combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"jetTracks",range(0,300,5))))
combos.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "jetTracks",range(0,300,5))))
combos.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "jetTracks",range(0,300,5))))
combos.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "jetTracks",range(0,300,5))))
combos.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "jetTracks",range(0,300,5))))

combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000, "t21",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750, "t21",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400, "t21",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300, "t21",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200, "t21",tau_bins)))

combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000, "t32",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750, "t32",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400, "t32",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300, "t32",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200, "t32",tau_bins)))

combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"sphericity",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750,  "sphericity",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400,  "sphericity",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300,  "sphericity",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200,  "sphericity",tau_bins)))

combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"sphericity_b",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750,  "sphericity_b",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400,  "sphericity_b",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300,  "sphericity_b",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200,  "sphericity_b",tau_bins)))

combos.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"sphericity_b2",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750,  "sphericity_b2",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400,  "sphericity_b2",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300,  "sphericity_b2",tau_bins)))
combos.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200,  "sphericity_b2",tau_bins)))

combos8.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"C",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750,  "C",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400,  "C",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300,  "C",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200,  "C",tau_bins)))

combos8.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"C_b",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750,  "C_b",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400,  "C_b",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300,  "C_b",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200,  "C_b",tau_bins)))

combos8.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"C_b2",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750,  "C_b2",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400,  "C_b2",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300,  "C_b2",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200,  "C_b2",tau_bins)))

combos8.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"D",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750,  "D",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400,  "D",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300,  "D",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200,  "D",tau_bins)))

combos8.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"D_b",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750,  "D_b",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400,  "D_b",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300,  "D_b",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200,  "D_b",tau_bins)))

combos8.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"D_b2",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750,  "D_b2",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400,  "D_b2",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300,  "D_b2",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200,  "D_b2",tau_bins)))

combos8.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"aPlanarity",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750,  "aPlanarity",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400,  "aPlanarity",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300,  "aPlanarity",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200,  "aPlanarity",tau_bins)))

combos8.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"aPlanarity_b",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750,  "aPlanarity_b",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400,  "aPlanarity_b",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300,  "aPlanarity_b",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200,  "aPlanarity_b",tau_bins)))

combos8.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"aPlanarity_b2",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df750,qcd_df,750,  "aPlanarity_b2",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df400,qcd_df,400,  "aPlanarity_b2",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df300,qcd_df,300,  "aPlanarity_b2",tau_bins)))
combos8.append(mp.Process(target=make_eff_combo, args=(df200,qcd_df,200,  "aPlanarity_b2",tau_bins)))

#combos2.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho0_50",rho_bins)))
#combos2.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho0_50",rho_bins)))
#combos2.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho0_50",rho_bins)))
#combos2.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho0_50",rho_bins)))
#combos2.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho0_50",rho_bins)))
#
#combos2.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho1_50",rho_bins)))
#combos2.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho1_50",rho_bins)))
#combos2.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho1_50",rho_bins)))
#combos2.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho1_50",rho_bins)))
#combos2.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho1_50",rho_bins)))
#
#combos2.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho2_50",rho_bins)))
#combos2.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho2_50",rho_bins)))
#combos2.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho2_50",rho_bins)))
#combos2.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho2_50",rho_bins)))
#combos2.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho2_50",rho_bins)))
#
combos3.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho0_20",rho_bins)))
combos3.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho0_20",rho_bins)))
combos3.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho0_20",rho_bins)))
combos3.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho0_20",rho_bins)))
combos3.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho0_20",rho_bins)))

combos3.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho1_20",rho_bins)))
combos3.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho1_20",rho_bins)))
combos3.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho1_20",rho_bins)))
combos3.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho1_20",rho_bins)))
combos3.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho1_20",rho_bins)))

combos3.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho2_20",rho_bins)))
combos3.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho2_20",rho_bins)))
combos3.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho2_20",rho_bins)))
combos3.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho2_20",rho_bins)))
combos3.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho2_20",rho_bins)))
#
#combos4.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho0_10",rho_bins)))
#combos4.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho0_10",rho_bins)))
#combos4.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho0_10",rho_bins)))
#combos4.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho0_10",rho_bins)))
#combos4.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho0_10",rho_bins)))
#
#combos4.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho1_10",rho_bins)))
#combos4.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho1_10",rho_bins)))
#combos4.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho1_10",rho_bins)))
#combos4.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho1_10",rho_bins)))
#combos4.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho1_10",rho_bins)))
#
#combos4.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho2_10",rho_bins)))
#combos4.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho2_10",rho_bins)))
#combos4.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho2_10",rho_bins)))
#combos4.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho2_10",rho_bins)))
#combos4.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho2_10",rho_bins)))
#
#combos5.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho0_05",rho_bins)))
#combos5.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho0_05",rho_bins)))
#combos5.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho0_05",rho_bins)))
#combos5.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho0_05",rho_bins)))
#combos5.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho0_05",rho_bins)))
#
#combos5.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho1_05",rho_bins)))
#combos5.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho1_05",rho_bins)))
#combos5.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho1_05",rho_bins)))
#combos5.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho1_05",rho_bins)))
#combos5.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho1_05",rho_bins)))
#
#combos5.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho2_05",rho_bins)))
#combos5.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho2_05",rho_bins)))
#combos5.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho2_05",rho_bins)))
#combos5.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho2_05",rho_bins)))
#combos5.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho2_05",rho_bins)))
#
#combos6.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho0_30",rho_bins)))
#combos6.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho0_30",rho_bins)))
#combos6.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho0_30",rho_bins)))
#combos6.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho0_30",rho_bins)))
#combos6.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho0_30",rho_bins)))
#
#combos6.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho1_30",rho_bins)))
#combos6.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho1_30",rho_bins)))
#combos6.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho1_30",rho_bins)))
#combos6.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho1_30",rho_bins)))
#combos6.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho1_30",rho_bins)))
#
#combos6.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho2_30",rho_bins)))
#combos6.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho2_30",rho_bins)))
#combos6.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho2_30",rho_bins)))
#combos6.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho2_30",rho_bins)))
#combos6.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho2_30",rho_bins)))
#
#combos7.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho0_15",rho_bins)))
#combos7.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho0_15",rho_bins)))
#combos7.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho0_15",rho_bins)))
#combos7.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho0_15",rho_bins)))
#combos7.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho0_15",rho_bins)))
#
#combos7.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho1_15",rho_bins)))
#combos7.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho1_15",rho_bins)))
#combos7.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho1_15",rho_bins)))
#combos7.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho1_15",rho_bins)))
#combos7.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho1_15",rho_bins)))
#
#combos7.append(mp.Process(target=make_eff_combo, args=(df1000,qcd_df,1000,"rho2_15",rho_bins)))
#combos7.append(mp.Process(target=make_eff_combo, args=(df750, qcd_df,750, "rho2_15",rho_bins)))
#combos7.append(mp.Process(target=make_eff_combo, args=(df400, qcd_df,400, "rho2_15",rho_bins)))
#combos7.append(mp.Process(target=make_eff_combo, args=(df300, qcd_df,300, "rho2_15",rho_bins)))
#combos7.append(mp.Process(target=make_eff_combo, args=(df200, qcd_df,200, "rho2_15",rho_bins)))


tracksel = 20
tausel= 0.5
rho0sel=0.0
rho1sel=0.4
rho2sel=0.4
spheresel =0.2

SR_taus=[]
SR_taus.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "t21",tau_bins,qcd_df,1000,tracksel,tausel)))
SR_taus.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "t32",tau_bins,qcd_df,1000,tracksel,tausel)))
#SR_taus.append(mp.Process(target=make_2d_SR, args=(df750, "jetTracks",range(0,500), "t21",tau_bins,qcd_df,750,tracksel,tausel)))
#SR_taus.append(mp.Process(target=make_2d_SR, args=(df750, "jetTracks",range(0,500), "t32",tau_bins,qcd_df,750,tracksel,tausel)))
#SR_taus.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "t21",tau_bins,qcd_df,400,tracksel,tausel)))
#SR_taus.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "t32",tau_bins,qcd_df,400,tracksel,tausel)))
#SR_taus.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "t21",tau_bins,qcd_df,300,tracksel,tausel)))
#SR_taus.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "t32",tau_bins,qcd_df,300,tracksel,tausel)))
#SR_taus.append(mp.Process(target=make_2d_SR, args=(df200, "jetTracks",range(0,500), "t21",tau_bins,qcd_df,200,tracksel,tausel)))
#SR_taus.append(mp.Process(target=make_2d_SR, args=(df200, "jetTracks",range(0,500), "t32",tau_bins,qcd_df,200,tracksel,tausel)))

SR_rhos = []
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho0_50",rho_bins,qcd_df,1000,tracksel,rho0sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho1_50",rho_bins,qcd_df,1000,tracksel,rho1sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho2_50",rho_bins,qcd_df,1000,tracksel,rho2sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho0_20",rho_bins,qcd_df,1000,tracksel,rho0sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho1_20",rho_bins,qcd_df,1000,tracksel,rho1sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho2_20",rho_bins,qcd_df,1000,tracksel,rho2sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho0_10",rho_bins,qcd_df,1000,tracksel,rho0sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho1_10",rho_bins,qcd_df,1000,tracksel,rho1sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho2_10",rho_bins,qcd_df,1000,tracksel,rho2sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho0_05",rho_bins,qcd_df,1000,tracksel,rho0sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho1_05",rho_bins,qcd_df,1000,tracksel,rho1sel)))
SR_rhos.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho2_05",rho_bins,qcd_df,1000,tracksel,rho2sel)))
#SR_rhos.append(mp.Process(target=make_2d_SR, args=(df750, "jetTracks",range(0,500), "rho0",rho_bins,qcd_df,750,tracksel,rho0sel)))
#SR_rhos.append(mp.Process(target=make_2d_SR, args=(df750, "jetTracks",range(0,500), "rho1",rho_bins,qcd_df,750,tracksel,rho1sel)))
#SR_rhos.append(mp.Process(target=make_2d_SR, args=(df750, "jetTracks",range(0,500), "rho2",rho_bins,qcd_df,750,tracksel,rho2sel)))
#SR_rhos.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "rho0",rho_bins,qcd_df,400,tracksel,rho0sel)))
#SR_rhos.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "rho1",rho_bins,qcd_df,400,tracksel,rho1sel)))
#SR_rhos.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "rho2",rho_bins,qcd_df,400,tracksel,rho2sel)))
#SR_rhos.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "rho0",rho_bins,qcd_df,300,tracksel,rho0sel)))
#SR_rhos.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "rho1",rho_bins,qcd_df,300,tracksel,rho1sel)))
#SR_rhos.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "rho2",rho_bins,qcd_df,300,tracksel,rho2sel)))
#SR_rhos.append(mp.Process(target=make_2d_SR, args=(df200, "jetTracks",range(0,500), "rho0",rho_bins,qcd_df,200,tracksel,rho0sel)))
#SR_rhos.append(mp.Process(target=make_2d_SR, args=(df200, "jetTracks",range(0,500), "rho1",rho_bins,qcd_df,200,tracksel,rho1sel)))
#SR_rhos.append(mp.Process(target=make_2d_SR, args=(df200, "jetTracks",range(0,500), "rho2",rho_bins,qcd_df,200,tracksel,rho2sel)))
SR_rhos2 = []
#SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho0_30",rho_bins,qcd_df,1000,tracksel,rho0sel)))
#SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho1_30",rho_bins,qcd_df,1000,tracksel,rho1sel)))
#SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho2_30",rho_bins,qcd_df,1000,tracksel,rho2sel)))
#SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho0_15",rho_bins,qcd_df,1000,tracksel,rho0sel)))
#SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho1_15",rho_bins,qcd_df,1000,tracksel,rho1sel)))
#SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "rho2_15",rho_bins,qcd_df,1000,tracksel,rho2sel)))
SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "sphericity",tau_bins,qcd_df,1000,tracksel,spheresel)))
SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "sphericity_b",tau_bins,qcd_df,1000,tracksel,spheresel)))
SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "sphericity_b2",tau_bins,qcd_df,1000,tracksel,spheresel)))
SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "C",tau_bins,qcd_df,1000,tracksel,spheresel)))
SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "C_b",tau_bins,qcd_df,1000,tracksel,spheresel)))
SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "C_b2",tau_bins,qcd_df,1000,tracksel,spheresel)))
SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "D",tau_bins,qcd_df,1000,tracksel,spheresel)))
SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "D_b",tau_bins,qcd_df,1000,tracksel,spheresel)))
SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "D_b2",tau_bins,qcd_df,1000,tracksel,spheresel)))
SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "aPlanarity",tau_bins,qcd_df,1000,tracksel,spheresel)))
SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "aPlanarity_b",tau_bins,qcd_df,1000,tracksel,spheresel)))
SR_rhos2.append(mp.Process(target=make_2d_SR, args=(df1000, "jetTracks",range(0,500), "aPlanarity_b2",tau_bins,qcd_df,1000,tracksel,spheresel)))

SR_rhos3 = []
#SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "rho0_30",rho_bins,qcd_df,400,tracksel,rho0sel)))
#SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "rho1_30",rho_bins,qcd_df,400,tracksel,rho1sel)))
#SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "rho2_30",rho_bins,qcd_df,400,tracksel,rho2sel)))
#SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "rho0_15",rho_bins,qcd_df,400,tracksel,rho0sel)))
#SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "rho1_15",rho_bins,qcd_df,400,tracksel,rho1sel)))
#SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "rho2_15",rho_bins,qcd_df,400,tracksel,rho2sel)))
SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "sphericity",tau_bins,qcd_df,400,tracksel,spheresel)))
SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "sphericity_b",tau_bins,qcd_df,400,tracksel,spheresel)))
SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "sphericity_b2",tau_bins,qcd_df,400,tracksel,spheresel)))
SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "C",tau_bins,qcd_df,400,tracksel,spheresel)))
SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "C_b",tau_bins,qcd_df,400,tracksel,spheresel)))
SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "C_b2",tau_bins,qcd_df,400,tracksel,spheresel)))
SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "D",tau_bins,qcd_df,400,tracksel,spheresel)))
SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "D_b",tau_bins,qcd_df,400,tracksel,spheresel)))
SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "D_b2",tau_bins,qcd_df,400,tracksel,spheresel)))
SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "aPlanarity",tau_bins,qcd_df,400,tracksel,spheresel)))
SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "aPlanarity_b",tau_bins,qcd_df,400,tracksel,spheresel)))
SR_rhos3.append(mp.Process(target=make_2d_SR, args=(df400, "jetTracks",range(0,500), "aPlanarity_b2",tau_bins,qcd_df,400,tracksel,spheresel)))

SR_rhos4 = []
#SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "rho0_30",rho_bins,qcd_df,300,tracksel,rho0sel)))
#SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "rho1_30",rho_bins,qcd_df,300,tracksel,rho1sel)))
#SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "rho2_30",rho_bins,qcd_df,300,tracksel,rho2sel)))
#SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "rho0_15",rho_bins,qcd_df,300,tracksel,rho0sel)))
#SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "rho1_15",rho_bins,qcd_df,300,tracksel,rho1sel)))
#SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "rho2_15",rho_bins,qcd_df,300,tracksel,rho2sel)))
SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "sphericity",tau_bins,qcd_df,300,tracksel,spheresel)))
SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "sphericity_b",tau_bins,qcd_df,300,tracksel,spheresel)))
SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "sphericity_b2",tau_bins,qcd_df,300,tracksel,spheresel)))
SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "C",tau_bins,qcd_df,300,tracksel,spheresel)))
SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "C_b",tau_bins,qcd_df,300,tracksel,spheresel)))
SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "C_b2",tau_bins,qcd_df,300,tracksel,spheresel)))
SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "D",tau_bins,qcd_df,300,tracksel,spheresel)))
SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "D_b",tau_bins,qcd_df,300,tracksel,spheresel)))
SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "D_b2",tau_bins,qcd_df,300,tracksel,spheresel)))
SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "aPlanarity",tau_bins,qcd_df,300,tracksel,spheresel)))
SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "aPlanarity_b",tau_bins,qcd_df,300,tracksel,spheresel)))
SR_rhos4.append(mp.Process(target=make_2d_SR, args=(df300, "jetTracks",range(0,500), "aPlanarity_b2",tau_bins,qcd_df,300,tracksel,spheresel)))

sphere=[]
sphere.append(mp.Process(target=closure, args=("jetTracks",range(40,130,10),"sphericity",[0.01*x for x in range(30,100,5)],1,0,tracksel,spheresel)))
sphere.append(mp.Process(target=closure, args=("jetTracks",range(40,130,10),"sphericity_b",[0.01*x for x in range(30,100,5)],1,0,tracksel,spheresel)))
sphere.append(mp.Process(target=closure, args=("jetTracks",range(40,130,10),"C",[0.01*x for x in range(30,100,5)],1,0,tracksel,spheresel)))
sphere.append(mp.Process(target=closure, args=("jetTracks",range(40,130,10),"C_b",[0.01*x for x in range(30,100,5)],1,0,tracksel,spheresel)))
sphere.append(mp.Process(target=closure, args=("jetTracks",range(40,130,10),"D",[0.01*x for x in range(30,100,5)],1,0,tracksel,spheresel)))
sphere.append(mp.Process(target=closure, args=("jetTracks",range(40,130,10),"D_b",[0.01*x for x in range(30,100,5)],1,0,tracksel,spheresel)))
sphere.append(mp.Process(target=closure, args=("jetTracks",range(40,130,10),"aPlanarity",[0.01*x for x in range(30,100,5)],1,0,tracksel,spheresel)))
sphere.append(mp.Process(target=closure, args=("jetTracks",range(40,130,10),"aPlanarity_b",[0.01*x for x in range(30,100,5)],1,0,tracksel,spheresel)))

taus=[]
taus.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"t21",[0.01*x for x in range(60,100,2)],0,1,tracksel,tausel)))
taus.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"t21",[0.01*x for x in range(60,100,2)],1,1,tracksel,tausel)))
taus.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"t32",[0.01*x for x in range(60,100,2)],0,1,tracksel,tausel)))
taus.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"t32",[0.01*x for x in range(60,100,2)],1,1,tracksel,tausel)))

rhos = []
rhos.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho0_50",[0.01*x for x in range(50,150,2)],0,0,tracksel,rho0sel)))
rhos.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho0_50",[0.01*x for x in range(50,150,2)],1,0,tracksel,rho0sel)))
rhos.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho1_50",[0.01*x for x in range(50,150,2)],0,0,tracksel,rho1sel)))
rhos.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho1_50",[0.01*x for x in range(50,150,2)],1,0,tracksel,rho1sel)))
rhos.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho2_50",[0.01*x for x in range(0,100,5)],0,0,tracksel,rho2sel)))
rhos.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho2_50",[0.01*x for x in range(0,100,5)],1,0,tracksel,rho2sel)))
rhos2 = []
rhos2.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho0_20",[0.01*x for x in range(50,150,2)],0,0,tracksel,rho0sel)))
rhos2.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho0_20",[0.01*x for x in range(50,150,2)],1,0,tracksel,rho0sel)))
rhos2.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho1_20",[0.01*x for x in range(50,150,2)],0,0,tracksel,rho1sel)))
rhos2.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho1_20",[0.01*x for x in range(50,150,2)],1,0,tracksel,rho1sel)))
rhos2.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho2_20",[0.01*x for x in range(0,100,5)],0,0,tracksel,rho2sel)))
rhos2.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho2_20",[0.01*x for x in range(0,100,5)],1,0,tracksel,rho2sel)))
rhos3 = []
rhos3.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho0_10",[0.01*x for x in range(50,150,2)],0,0,tracksel,rho0sel)))
rhos3.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho0_10",[0.01*x for x in range(50,150,2)],1,0,tracksel,rho0sel)))
rhos3.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho1_10",[0.01*x for x in range(50,150,2)],0,0,tracksel,rho1sel)))
rhos3.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho1_10",[0.01*x for x in range(50,150,2)],1,0,tracksel,rho1sel)))
rhos3.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho2_10",[0.01*x for x in range(0,100,5)],0,0,tracksel,rho2sel)))
rhos3.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho2_10",[0.01*x for x in range(0,100,5)],1,0,tracksel,rho2sel)))
rhos4 = []
rhos4.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho0_05",[0.01*x for x in range(50,150,2)],0,0,tracksel,rho0sel)))
rhos4.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho0_05",[0.01*x for x in range(50,150,2)],1,0,tracksel,rho0sel)))
rhos4.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho1_05",[0.01*x for x in range(50,150,2)],0,0,tracksel,rho1sel)))
rhos4.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho1_05",[0.01*x for x in range(50,150,2)],1,0,tracksel,rho1sel)))
rhos4.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho2_05",[0.01*x for x in range(0,100,5)],0,0,tracksel,rho2sel)))
rhos4.append(mp.Process(target=closure, args=("jetTracks",range(80,100,2),"rho2_05",[0.01*x for x in range(0,100,5)],1,0,tracksel,rho2sel)))

binned1 = []
binned2 = []
binned3 = []
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","t21",50,[0,0.2,0.4,0.6,0.8,1.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","t32",50,[0,0.2,0.4,0.6,0.8,1.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho0_50",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho1_50",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho2_50",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho0_20",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho1_20",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho2_20",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho0_10",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho1_10",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho2_10",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho0_05",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho1_05",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned1.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho2_05",50,[0,0.4,0.8,1.2,1.6,2.0])))

binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"t21","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"t32","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"rho0_50","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"rho1_50","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"rho2_50","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"rho0_20","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"rho1_20","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"rho2_20","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"rho0_10","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"rho1_10","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"rho2_10","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"rho0_05","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"rho1_05","jetTracks",50,[0,10,20,50,100,150])))
binned2.append(mp.Process(target=binned_dist, args=(qcd_df,"rho2_05","jetTracks",50,[0,10,20,50,100,150])))

binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","sphericity",30,[0,0.2,0.4,0.6,0.8,1.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","sphericity_b",30,[0,0.2,0.4,0.6,0.8,1.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","C",30,[0,0.2,0.4,0.6,0.8,1.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","C_b",30,[0,0.2,0.4,0.6,0.8,1.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","D",30,[0,0.2,0.4,0.6,0.8,1.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","D_b",30,[0,0.2,0.4,0.6,0.8,1.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","aPlanarity",30,[0,0.2,0.4,0.6,0.8,1.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","aPlanarity_b",30,[0,0.2,0.4,0.6,0.8,1.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho0_30",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho1_30",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho2_30",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho0_15",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho1_15",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"jetTracks","rho2_15",50,[0,0.4,0.8,1.2,1.6,2.0])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"sphericity","jetTracks",30,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"sphericity_b","jetTracks",30,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"C","jetTracks",30,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"C_b","jetTracks",30,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"D","jetTracks",30,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"D_b","jetTracks",30,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"aPlanarity","jetTracks",30,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"aPlanarity_b","jetTracks",30,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"rho0_30","jetTracks",50,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"rho1_30","jetTracks",50,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"rho2_30","jetTracks",50,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"rho0_15","jetTracks",50,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"rho1_15","jetTracks",50,[0,10,20,50,100,150])))
binned3.append(mp.Process(target=binned_dist, args=(qcd_df,"rho2_15","jetTracks",50,[0,10,20,50,100,150])))
#print("binned")
#for p in binned1:
#  p.start()
#for p in binned1:
#  p.join()
#for p in binned2:
#  p.start()
#for p in binned2:
#  p.join()
#for p in binned3:
#  p.start()
#for p in binned3:
#  p.join()
print("nTracks") 
for p in combos:
  p.start()
for p in combos:
  p.join()
for p in combos2:
  p.start()
for p in combos2:
  p.join()
for p in combos3:
  p.start()
for p in combos3:
  p.join()
for p in combos4:
  p.start()
for p in combos4:
  p.join()
for p in combos5:
  p.start()
for p in combos5:
  p.join()
for p in combos6:
  p.start()
for p in combos6:
  p.join()
for p in combos7:
  p.start()
for p in combos7:
  p.join()
for p in combos8:
  p.start()
for p in combos8:
  p.join()
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
#for p in SR_rhos2:
#  p.start()
#for p in SR_rhos2:
#  p.join()
#for p in SR_rhos3:
#  p.start()
#for p in SR_rhos3:
#  p.join()
#for p in SR_rhos4:
#  p.start()
#for p in SR_rhos4:
#  p.join()
#print("closure sphere")
#for p in sphere:
#  p.start()
#for p in sphere:
#  p.join()
#print("closure tau")
#for p in taus:
#  p.start()
#for p in taus:
#  p.join()
#print("closure rho")
#for p in rhos:
#  p.start()
#for p in rhos:
#  p.join()
#for p in rhos2:
#  p.start()
#for p in rhos2:
#  p.join()
#for p in rhos3:
#  p.start()
#for p in rhos3:
#  p.join()
#for p in rhos4:
#  p.start()
#for p in rhos4:
#  p.join()
