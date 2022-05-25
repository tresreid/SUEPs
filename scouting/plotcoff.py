import awkward as ak
from coffea import hist, processor
import uproot
from coffea.nanoevents import NanoEventsFactory, BaseSchema
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import uproot
import pickle
import pandas as pd
from numpy import unravel_index
import heapq
from scipy.optimize import curve_fit
import scipy
from matplotlib.colors import LinearSegmentedColormap

#with open("myhistos_sig400_0.p", "rb") as pkl_file:
lumi = 59.74*1000
xsecs = {"QCD":0,"sig1000":0.17,"sig750":0.5,"sig400":5.9,"sig300":8.9,"sig200":13.6} #1000-200
colors = ["black","red","green","orange","blue","magenta","cyan","yellow","brown","grey"]
cuts=["0:None","1:HTTrig","2:HT>=600","3:FJ>=2","4:nPFCand>=140"]
sigcolors = {"sig1000":"red","sig750":"green","sig400":"blue","sig300":"orange","sig200":"magenta"}

qcdscaled = {}
#with open("outhists/myhistos_HT2000_0.p", "rb") as pkl_file:
with open("outhists/save/myhistos_QCD.p", "rb") as pkl_file:
    out = pickle.load(pkl_file)
    for name, h in out.items():
      if isinstance(h, hist.Hist):
        qcdscaled[name] = h.copy()

def make_overlapdists(samples,var,cut):
  name1 = "dist_%s"%var
  fig, (ax) = plt.subplots(
      nrows=1,
      ncols=1,
      figsize=(7,7),
      #gridspec_kw={"height_ratios": (3, 1)},
      #sharex=True
  )
  fig.subplots_adjust(hspace=.07)

  for sample in samples:
    with open("outhists/save/myhistos_%s_2.p"%sample, "rb") as pkl_file:
        out = pickle.load(pkl_file)
        #print(out)
        scale= lumi*xsecs[sample]/out["sumw"][sample]
        scaled = {}
        for name, h in out.items():
          if var not in name or "mu" in name or "trig" in name:
            continue
          if isinstance(h, hist.Hist):
            scaled[name] = h.copy()
            scaled[name].scale(scale)
        
        
            s = scaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy()
            b = qcdscaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy()
            ax.step(s[1][:-1],s[0],color=sigcolors[sample],label=sample,linestyle="--",where="post")
  hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2,ax=ax)
  ax.set_yscale("log")
  ax.set_xlabel(name1[5:])
  ax.set_ylabel("Events")
  ax.legend()
  ax.autoscale(axis='y', tight=True)
  fig.savefig("Plots/overlap_sigdist_%s_cut%s"%(var,cut))
  plt.close()
  


def make_dists(sample):
  with open("outhists/myhistos_%s.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      xsec = xsecs[sample.split("_")[0]]
#      print(out)
      if xsec ==0:
        scale = 1
      else:
        scale= lumi*xsec/out["sumw"][sample.split("_")[0]]
      scaled = {}
      for name, h in out.items():
        if "SR" in name or "trkID" in name:
          continue
        if isinstance(h, hist.Hist):
          scaled[name] = h.copy()
          scaled[name].scale(scale)
      
      
          fig, ax1 = plt.subplots()
      
          hx = hist.plot1d(
              scaled[name],
              ax=ax1,
              overlay="cut",
              stack=False,
              fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
          )
          hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
          if "trkID" not in name:
            ax1.set_yscale("log")
            ax1.autoscale(axis='y', tight=True)
          if "_pt" in name:
            ax1.set_xscale("log")
            ax1.set_xlim([20,200])
            if "PFcand" in name or "gen" in name:
              ax1.set_xlim([0.3,100])
            #ax1.autoscale(axis='x', tight=True)
          fig.savefig("Plots/proccess_%s_%s"%(sample,name))
          plt.close()
  
#      fig, ax1 = plt.subplots()
def func(x,a,b,c,d):
  return a*scipy.special.erf((x-b)/c)+d 
def make_trkeff(sample,name):
  with open("outhists/myhistos_%s.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      sample = sample.split("_")[0]
      xsec = xsecs[sample.split("_")[0]]
      if xsec ==0:
        scale = 1
      else:
        scale= lumi*xsec/out["sumw"][sample]
      out[name].scale(scale)
      
      num = out[name].integrate("v2",slice(0,0.05)).copy()
      numFK = out[name].integrate("v2",slice(0.05,0.3)).copy()
      denom = out[name].integrate("v2").copy()
      
      fig, ax1 = plt.subplots()
      for cut in range(7):
        hx = hist.plotratio(
            num.integrate("cut",slice(1+cut,2+cut)),denom.integrate("cut",slice(1+cut,2+cut)),
            ax=ax1,
            clear=False,
            error_opts={'color': colors[cut], 'marker': '+'},
            unc='clopper-pearson'
        )

      ax1.set_ylim(0,1.1)
      if "_pt" in name:
        ax1.set_xscale("log")
        ax1.set_xlim([20,200])
        if "PFcand" in name or "gen" in name:
          ax1.set_xlim([0.3,100])
      ax1.legend(["pt > 0.5","pt >0.6","pt >0.7","pt >0.75","pt >0.8","pt >0.9","pt >1.0",],loc="lower right")
      fig.suptitle("Track Efficiency: %s"%sample)
      hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
      fig.savefig("Plots/track_eff_%s_%s"%(sample,name))
      plt.close()

      ###############FAKE
      fig, ax1 = plt.subplots()
      for cut in range(7):
        hx1 = hist.plotratio(
            numFK.integrate("cut",slice(1+cut,2+cut)),denom.integrate("cut",slice(1+cut,2+cut)),
            ax=ax1,
            clear=False,
            error_opts={'color': colors[cut], 'marker': '+'},
            unc='clopper-pearson'
        )

      ax1.set_ylim(0,1.1)
      if "_pt" in name:
        ax1.set_xscale("log")
        ax1.set_xlim([20,200])
        if "PFcand" in name or "gen" in name:
          ax1.set_xlim([0.3,100])
      ax1.legend(["pt > 0.5","pt >0.6","pt >0.7","pt >0.75","pt >0.8","pt >0.9","pt >1.0",],loc="lower right")
      fig.suptitle("Track Efficiency: %s"%sample)
      hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
      fig.savefig("Plots/track_fake_%s_%s"%(sample,name))
      plt.close()
def make_trigs(sample):
  with open("outhists/myhistos_%s.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      sample = sample.split("_")[0]
      xsec = xsecs[sample.split("_")[0]]
      if xsec ==0:
        scale = 1
      else:
        scale= lumi*xsec/out["sumw"][sample]
      out["trigdist_ht"].scale(scale)
      
      
      fig, ax1 = plt.subplots()
      #Trigger plots
      s = out["trigdist_ht"].integrate("cut",slice(2,3)).to_hist().to_numpy()
      s1 = s[0]
      s2 = out["trigdist_ht"].integrate("cut",slice(0,1)).to_hist().to_numpy()[0]
      points = np.nan_to_num(s1/s2)
      popt, pcov = curve_fit(func,s[1][:-1],points,p0=[0.5,500,100,0.5])
      hx1 = hist.plotratio(
          qcdscaled["trigdist_ht"].integrate("cut",slice(2,3)),qcdscaled["trigdist_ht"].integrate("cut",slice(0,1)),
          ax=ax1,
          error_opts={'color': 'r', 'marker': '.'},
          unc='clopper-pearson'
      )
      hx = hist.plotratio(
          out["trigdist_ht"].integrate("cut",slice(2,3)),out["trigdist_ht"].integrate("cut",slice(0,1)),
          ax=ax1,
          clear=False,
          error_opts={'color': 'k', 'marker': '.'},
          unc='clopper-pearson'
      )
      xs = np.linspace(0,1500,100)
      p98sig = 1.65*popt[2]+popt[1]
      p90sig = 1.163*popt[2]+popt[1]
      ax1.plot(xs,func(xs,popt[0],popt[1],popt[2],popt[3]), color="black",label="Sig: 90:%d 98:%d "%(p90sig,p98sig))

      b = qcdscaled["trigdist_ht"].integrate("cut",slice(2,3)).to_hist().to_numpy()
      b1 = b[0]
      b2 = qcdscaled["trigdist_ht"].integrate("cut",slice(0,1)).to_hist().to_numpy()[0]
      points2 = np.nan_to_num(b1/b2)
      popt2, pcov2 = curve_fit(func,b[1][:-1],points2,p0=[0.5,500,100,0.5])
      p98bkg = 1.65*popt2[2]+popt2[1]
      p90bkg = 1.163*popt2[2]+popt2[1]
      ax1.plot(xs,func(xs,popt2[0],popt2[1],popt2[2],popt2[3]), color="red",label="QCD: 90:%d 98:%d"%(p90bkg,p98bkg))
      ax1.axvline(x=p98sig,color="black",ls="--")
      ax1.axvline(x=p90sig,color="black",ls=":")
      ax1.axvline(x=p98bkg,color="red",ls="--")
      ax1.axvline(x=p90bkg,color="red",ls=":")

      ax1.set_ylim(0,1.1)
      ax1.legend(loc="lower right")
      fig.suptitle("HT Trigger Efficiency no reference: %s"%sample)
      hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
      fig.savefig("Plots/trigHtnoref_%s"%(sample))
      plt.close()



def get_sig(s,sb,rangex):
  sig = []
  bkg = []
  #print(s)
  for i in range(len(rangex)):
    sig.append(np.sum(s[i:]))
    bkg.append(np.sum(sb[i:])) # + 1e-9)
  return(sig,bkg)

def make_signif(sample,xsec):
  qcdscaled = {}
  with open("outhists/myhistos_QCD.p", "rb") as pkl_file:
      out = pickle.load(pkl_file)
      for name, h in out.items():
        if isinstance(h, hist.Hist):
          qcdscaled[name] = h.copy()
  with open("outhists/myhistos_%s_0.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      scale= lumi*xsec/out["sumw"][sample]
      scaled = {}
      for name, h in out.items():
        if "trig" in name:
          continue
        if isinstance(h, hist.Hist):
          scaled[name] = h.copy()
          scaled[name].scale(scale)
      
      
          fig, ax1 = plt.subplots()
          for cut in [0,1,2,3,4]:
            s = scaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy()
            sb = (qcdscaled[name].integrate("cut",slice(cut,cut+1)) + scaled[name].integrate("cut",slice(cut,cut+1))).to_hist().to_numpy()
            sig, sigbkg = get_sig(s[0],sb[0],s[1][:-1])
            ax1.errorbar(s[1][:-1],sig/np.sqrt(sigbkg),(sig/(np.sqrt(sigbkg)))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(np.multiply(4,sigbkg)))),ecolor=colors[cut],color=colors[cut],label=cuts[cut],marker="+")
          ax1.legend()
          ax1.set_xlabel(name[5:])
          ax1.set_ylabel("s/sqrt(s+b+0.5$b^{2}$)")
          hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
          fig.savefig("Plots/signif_%s"%(name))
          plt.close()



def make_n1(samples,var,cut):
  name1 = "dist_%s"%var
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)

  qcd = qcdscaled[name1].integrate("cut",slice(cut,cut+1))
  qcd.label = "QCD"
  hx = hist.plot1d(
      qcd,
      ax=ax,
      #overlay="cut",
      stack=False,
      fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3),"color":"wheat"}
  )
  for sample in samples:
    with open("outhists/myhistos_%s_2.p"%sample, "rb") as pkl_file:
        out = pickle.load(pkl_file)
        #print(out)
        scale= lumi*xsecs[sample]/out["sumw"][sample]
        scaled = {}
        for name, h in out.items():
          if var not in name or "mu" in name:
            continue
          if isinstance(h, hist.Hist):
            scaled[name] = h.copy()
            scaled[name].scale(scale)
        
        
            s = scaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy()
            b = qcdscaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy()
            sb = np.add(np.add(s,b),0.5*np.square(b))
            #sb = np.add(qcdscaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy(), scaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy())
            #sb = (qcdscaled[name].integrate("cut",slice(cut,cut+1)) + scaled[name].integrate("cut",slice(cut,cut+1))).to_hist().to_numpy()

            sig, sigbkg = get_sig(s[0],(sb)[0],s[1][:-1])
            ax1.errorbar(s[1][:-1],sig/np.sqrt(sigbkg),(sig/(np.sqrt(sigbkg)))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(np.multiply(4,sigbkg)))),ecolor=sigcolors[sample],color=sigcolors[sample],label=sample,marker="+")

            #print(s[1])
            #print(s[1][:-1])
            ax.step(s[1][:-1],s[0],color=sigcolors[sample],label=sample,linestyle="--",where="post")
  hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2,ax=ax)
  ax.set_yscale("log")
  ax1.set_xlabel(name1[5:])
  ax1.set_ylabel("s/sqrt(s+b+0.5$b^{2}$)")
  ax.set_ylabel("Events")
  leg1, leg = ax.get_legend_handles_labels()
  leg = [l.replace("None","QCD") for l in leg]
  ax.legend(leg)
  ax1.legend()
  #ax1.set_ylim([0,1e-4])
  ax1.set_ylim([0,30])
  ax.autoscale(axis='y', tight=True)
  fig.savefig("Plots/signif_%s"%(var))
  plt.close()


def get_sig2d(s,sb,rangex,rangey):
  sig = []
  bkg = []
  #print(s)
  for i in range(len(rangex)):
    sig1 = []
    bkg1 = []
    for j in range(len(rangey)):
      sig1.append(np.sum(s[i:,j:]))
      bkg1.append(np.sum(sb[i:,j:])) # + 1e-9)
    sig.append(sig1)
    bkg.append(bkg1)
  return(sig,bkg)
def makeSR(sample,var):
  with open("outhists/myhistos_%s_2.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      #print(out)
      scale= lumi*xsecs[sample]/out["sumw"][sample]
      scaled = {}
#      var = "SR2"
      # get colormap
      ncolors = 2048
      color_array = plt.get_cmap('Blues')(range(ncolors))
      color_array2 = plt.get_cmap('Reds')(range(ncolors))
      
      # change alpha values
      color_array[:,-1] = np.linspace(0.0,1.0,ncolors)
      color_array2[:,-1] = np.linspace(0.0,1.0,ncolors)
      
      # create a colormap object
      map_object = LinearSegmentedColormap.from_list(name='blues_alpha',colors=color_array)
      map_object2 = LinearSegmentedColormap.from_list(name='reds_alpha',colors=color_array2)
      
      # register this new colormap with matplotlib
      plt.register_cmap(cmap=map_object)
      plt.register_cmap(cmap=map_object2)

      if var=="SR1":
        xvar = "nPFCand"
      else:
        xvar = "FatJet_nconst"
      for name, h in out.items():
        if var not in name:
          continue
        if isinstance(h, hist.Hist):
          scaled[name] = h.copy()
          scaled[name].scale(scale)
          s = scaled[name].to_hist().to_numpy()#[0][0] #.integrate("cut",slice(cut,cut+1)).to_hist().to_numpy())
          b = qcdscaled[name].to_hist().to_numpy()#[0][0] #.integrate("cut",slice(cut,cut+1)).to_hist().to_numpy())
          print(s)
          print(b)
          #sb =  (scaled[name]+qcdscaled[name]).to_hist().to_numpy()#[0][0]) #.integrate("cut",slice(cut,cut+1)).to_hist().to_numpy())
          sb = np.add(np.add(s[0][0],b[0][0]),0.5*np.square(b[0][0]))
          sig, sigbkg = get_sig2d(s[0][0],(sb),s[2][:-1],s[3][:-1])
          signif = sig/ np.sqrt(sigbkg)
          signif = np.nan_to_num(signif)
          #print(signif)
          maxi = np.max(signif)
          maxindex = unravel_index(np.argmax(signif),signif.shape)
          #print(maxi,maxindex)
          maxes = heapq.nlargest(5,range(len(signif.flatten())),signif.flatten().take)
          for m in maxes:
            u = unravel_index(m,signif.shape)
            #print(signif.flatten()[m],signif[u[0]][u[1]],u,s[2][u[0]],s[3][u[1]])
          
          fig, ax = plt.subplots()
          shw = ax.imshow(np.transpose(signif), interpolation='none',origin="lower",cmap="autumn")
          ax.set_xticks([0,50,100,150,200,250,300])
          ax.set_xticklabels([0,50,100,150,200,250,300])
          ax.set_yticks([0,20,40,60,80,100])
          ax.set_yticklabels([0,.20,.40,.60,.80,1])
          bar = plt.colorbar(shw)
          bar.set_label("Significance")
          ax.set_xlabel(xvar)
          ax.set_ylabel("eventBoosted_Sphericity")
          ax.text(maxindex[0],maxindex[1],"X=%.2f(%d,%.2f)"%(maxi,maxindex[0],maxindex[1]/100))
           
          #ax.autoscale(axis='x', tight=True)
          ax.set_aspect("auto")
          fig.suptitle("Significance: %s"%sample)
          hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
          fig.savefig("Plots/signif2d_%s_%s"%(sample,var))
          plt.close()
          fig, ax1 = plt.subplots()
      
          hx = hist.plot2d(
              scaled[name].integrate("axis",slice(0,1)),
              xvar,
              #"nPFCand",
              ax=ax1,
              #overlay="cut",
              #stack=False,
              #fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
          )
          hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
          fig.suptitle("SR: %s"%sample)
          fig.savefig("Plots/%s_sig_%s"%(var,sample))
          plt.close()
        
          fig, ax1 = plt.subplots()
      
          hx = hist.plot2d(
              qcdscaled[name].integrate("axis",slice(0,1)),
              xvar, 
              #"nPFCand",
              ax=ax1,
              #overlay="cut",
              #stack=False,
              #fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
          )
          fig.suptitle("SR: QCD")
          hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
          fig.savefig("Plots/%s_bkg"%var)
          plt.close()
        
          fig, ax1 = plt.subplots()
      
          h0 = hist.plot2d(
              scaled[name].integrate("axis",slice(0,1)),
              xvar, 
              #"nPFCand",
              ax=ax1,
          #    clear=False,
              #overlay="cut",
              #stack=False,
              #fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
              patch_opts={'cmap': 'blues_alpha',"vmin":0,"vmax":150}
          )
          h1 = hist.plot2d(
              qcdscaled[name].integrate("axis",slice(0,1)),
              xvar,
              #"nPFCand",
              ax=ax1,
              #clear=False,
              #overlay="cut",
              #stack=False,
              #fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
              patch_opts={'cmap': 'reds_alpha',"vmin":0,"vmax":80000}
          )
          h2 = hist.plot2d(
              scaled[name].integrate("axis",slice(0,1)),
              xvar,
              #"nPFCand",
              ax=ax1,
              clear=False,
              #overlay="cut",
              #stack=False,
              #fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
              patch_opts={'cmap': "blues_alpha","vmin":0,"vmax":150}
          )
          fig.suptitle("SR: QCD + %s"%sample)
          hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
          fig.savefig("Plots/SR_%s_%s_bkg"%(sample,var))
          plt.close()
          

def make_cutflow(samples,var):
  name1 = "dist_%s"%var
  cutflow = {"QCD":[],"sig200":[],"sig300":[],"sig400":[],"sig750":[],"sig1000":[]}
  for cut in [0,1,2,3,4]: 
    b1 = qcdscaled[name1].integrate("cut",slice(cut,cut+1)).values()
    for (k,b) in b1.items():
      print("QCD %d %s %.2f"%(cut,name1,b.sum()))
      cutflow["QCD"].append(b.sum())
  b1 = qcdscaled[name1].integrate("cut",slice(4,5)).values()
  for (k,b) in b1.items():
    print("QCD %d %s %.2f"%(cut,name1,b[30:].sum()))
    cutflow["QCD"].append(b[30:].sum())
  for sample in samples:
    with open("outhists/myhistos_%s_2.p"%sample, "rb") as pkl_file:
        out = pickle.load(pkl_file)
        #print(out)
        scale= lumi*xsecs[sample]/out["sumw"][sample]
        scaled = {}
        for name, h in out.items():
          if name1 not in name or "mu" in name or "trig" in name:
            continue
          if isinstance(h, hist.Hist):
            scaled[name] = h.copy()
            scaled[name].scale(scale)
        
            for cut in [0,1,2,3,4]: 
              s1 = scaled[name].integrate("cut",slice(cut,cut+1)).values()
              for (k,s) in s1.items():
                print("%s %d %s %.2f"%(sample,cut,name,s.sum()))
                cutflow[sample].append(s.sum())
            s1 = scaled[name].integrate("cut",slice(4,5)).values()
            #print(s1)
            for (k,s) in s1.items():
              print("%s %d %s %.2f"%(sample,cut,name,s[30:].sum()))
              cutflow[sample].append(s[30:].sum())
            
  print(pd.DataFrame(cutflow))


def make_correlation(SR):
  if SR == "SR1":
    var = "nPFCand"
    high1 = 100
  else:
    var = "FatJet_nconst"
    high1 = 80
  h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  fig, ax1 = plt.subplots()
 
  sphere = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
  #labs = []
  for i in range(len(sphere)-1): 
    h2 = h1.integrate("eventBoostedSphericity",slice(sphere[i],sphere[i+1])).to_hist().to_numpy()
    norm = np.linalg.norm(h2[0])
    ax1.step(h2[1][:-(high1+1)],h2[0][:-high1]/norm,color=colors[i],label="%s-%s"%(sphere[i],sphere[i+1]),linestyle="-",where="post")
  hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
  ax1.legend(title="Boosted\n Sphericity\n Bins")
  ax1.set_xlabel(var)
  ax1.set_ylabel("AU")
  ax1.set_yscale("log")
  ax1.set_xscale("log")
  ax1.autoscale(axis='y', tight=True)
  ax1.autoscale(axis='x', tight=True)
  fig.savefig("Plots/correlation_sphere_%s"%var)
  plt.close()
 
  #fig, ax1 = plt.subplots()
  #sphere = [0,20,40,60,80,100]
  #for i in range(len(sphere)-1): 
  # 
  #  h2 = h1.integrate(var,slice(sphere[i],sphere[i+1])).to_hist().to_numpy()
  #  norm = np.linalg.norm(h2[0])
  #  ax1.step(h2[1][:-1],h2[0]/norm,color=colors[i],label="%s-%s"%(sphere[i],sphere[i+1]),linestyle="-",where="post")
  #hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
  #ax1.legend()
  #ax1.set_yscale("log")
  #ax1.autoscale(axis='y', tight=True)
  #fig.savefig("Plots/correlation_npfcand_%s"%var)
  #plt.close()

  for cut in [0,15,20,25,30,35]:
    fig, ax1 = plt.subplots()
    sphere = [0,20,40,60,80,100]
    for i in range(len(sphere)-1): 

      h2 = h1.integrate(var,slice(sphere[i],sphere[i+1])).to_hist().to_numpy()
      norm = np.linalg.norm(h2[0][cut:])
      ax1.step(h2[1][cut:-1],h2[0][cut:]/norm,color=colors[i],label="%s-%s"%(sphere[i],sphere[i+1]),linestyle="-",where="post")
    
    hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
    ax1.legend(title="%s Bins"%var)
    ax1.set_xlabel("Boosted Sphericity")
    ax1.set_ylabel("AU")
    ax1.set_yscale("log")
    ax1.autoscale(axis='y', tight=True)
    fig.savefig("Plots/correlation_%s_cut_%s"%(var,cut))
    plt.close()

def make_closure(sample="qcd",SR="SR1"):
  if SR == "SR2":
    var = "FatJet_nconst"
    high1 = 80
    high2 = 51
  else:
    var = "nPFCand"
    high1 = 100
    high2 = 61
  if sample == "qcd":
    h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  else:
    with open("outhists/myhistos_%s_2.p"%sample, "rb") as pkl_file:
        out = pickle.load(pkl_file)
        scale= lumi*xsecs[sample]/out["sumw"][sample]
        scaled = {}
        for name, h in out.items():
          if SR not in name or "mu" in name or "trig" in name:
            continue
          if isinstance(h, hist.Hist):
            scaled[name] = h.copy()
            scaled[name].scale(scale)
            h1 = (scaled[SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
  low1 =0
  low2 = 30
  high1x = 300
  high2x = 100
  
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
  #h1 = h1.rebin("nPFCand",hist.Bin("nPFCand","nPFCand",150,0,300))
  abin = h1.integrate("eventBoostedSphericity",slice(low2/100,high2/100)).integrate(  var,slice(low1,high1)).sum().values(sumw2=True)[()]
  bbin = h1.integrate("eventBoostedSphericity",slice(high2/100,high2x/100)).integrate(var,slice(low1,high1)).sum().values(sumw2=True)[()]
  cbin = h1.integrate("eventBoostedSphericity",slice(low2/100,high2/100)).integrate(  var,slice(high1,high1x)).sum().values(sumw2=True)[()]
  dbin = h1.integrate("eventBoostedSphericity",slice(high2/100,high2x/100)).integrate(var,slice(high1,high1x)).sum().values(sumw2=True)[()]
  abinx = abin[0]
  bbinx = bbin[0]
  cbinx = cbin[0]
  dbinx = dbin[0]
  abin_err = abin[1]
  bbin_err = bbin[1]
  cbin_err = cbin[1]
  dbin_err = dbin[1]
  ratx = bbinx/abinx
  expected = ratx*cbinx
  #err = np.sqrt(1/abin_err+1/bbin_err+1/cbin_err)
  err = expected*np.sqrt(abin_err/(abinx*abinx)+bbin_err/(bbinx*bbinx)+cbin_err/(cbinx*cbinx))
  print(abinx,np.sqrt(abin_err),bbinx,cbinx,dbinx,ratx,expected,dbinx/expected,err)
  hx = hist.plot1d(
      h1.integrate("eventBoostedSphericity",slice(high2/100,high2x/100)),
      ax=ax,
      #overlay="cut",
      stack=False,
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"blue"}
  )
  h2 = h1.copy()
  h2.scale(ratx)
  hx2 = hist.plot1d(
      h2.integrate("eventBoostedSphericity",slice(low2/100,high2/100)),
      ax=ax,
      clear=False,
      #overlay="cut",
      stack=False,
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"red"}
  )
  #ax.plot([],[],"")
  #ax.plot([],[],"")
  #ax.plot([],[],"")
  leg = ["Observed %.2f +/- %.2f"%(dbinx,np.sqrt(dbin_err)),"Expected: %.2f +/- %.2f"%(ratx*cbinx,err)]
  ax.legend(leg)
  hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2,ax=ax)
  ax.set_yscale("log")
  ax.autoscale(axis='y', tight=True)
  hx1 = hist.plotratio(
      h1.integrate("eventBoostedSphericity",slice(high2/100,high2x/100)),h2.integrate("eventBoostedSphericity",slice(low2/100,high2/100)),
      ax=ax1,
     # label="QCD",
      error_opts={'color': 'r', 'marker': '+'},
      unc='num'
      #unc='clopper-pearson'
  )
  #hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
  ax1.set_xlim(high1,175)
  ax1.set_ylim(0.5,1.5)
  fig.savefig("Plots/closure_%s_%s"%(sample,var))
  plt.close()


#######################ORGANIZE BY SECTION #######################################



############################# HT Trigger
#### HT Distributions
make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"ht",0)
make_overlapdists(["sig1000","sig750","sig400","sig300","sig200"],"ht",1)
#### Trigger Efficiency
#make_trigs("sig400_2")
#make_trigs("sig200_2")
#make_trigs("sig300_2")
#make_trigs("sig1000_2")
#make_trigs("sig750_2")


########################### Track Selection
###### DR distributions
make_overlapdists(["sig400"],"gen_dR",2)
#make_overlapdists(["sig400"],"gen_alldR",2) ## TODO
##### TRK Eff and Fakes 
## TODO with and without PV and q(neutrals) cut and significange (at preselection level) with and without cuts for nPFcands
#make_trkeff("sig400_2","dist_trkID_PFcand_pt") ## TODO fix fake labels
#make_trkeff("sig400_2","dist_trkID_PFcand_phi")
#make_trkeff("sig400_2","dist_trkID_PFcand_eta")
#make_trkeff("sig400_2","dist_trkID_gen_pt") #TODO check why efficiency is so high?
#make_trkeff("sig400_2","dist_trkID_gen_phi")
#make_trkeff("sig400_2","dist_trkID_gen_eta")

#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount50",4)
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount75",4)
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount100",4)
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount150",4)
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount200",4)
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"PFcand_ncount300",4)
## TODO make single plot to show max significance wrt pt threshold


##########################  FatJet Selection
##TODO SUEP vs scalar resolution for pt, mass, dR, nconstituents
## TODO make single plot to show max significance (2+ jets) wrt pt threshold
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount30",4)
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount50",4)
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount100",4)
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount150",4)
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount200",4)
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount250",4)
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"fjn1_FatJet_ncount300",4) 

########################## BOOSTING and sphericity
## TODO ISR removal methods
#make_correlation("SR1") #TODO revisit correlation plots
#make_correlation("SR2")
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"FatJet_nconst",4) 
#make_n1(["sig1000","sig750","sig400","sig300","sig200"],"eventBoosted_sphericity",4)


######################### ABCD
#makeSR("sig400","SR1")
#makeSR("sig200","SR1")
#makeSR("sig300","SR1")
#makeSR("sig750","SR1")
#makeSR("sig1000","SR1")
#makeSR("sig400","SR2")
#makeSR("sig200","SR2")
#makeSR("sig300","SR2")
#makeSR("sig750","SR2")
#makeSR("sig1000","SR2")
#make_closure("qcd")
#make_closure("sig400")
#make_closure("sig200")
#make_closure("sig1000")
#make_closure("qcd","SR2")
#make_closure("sig400","SR2") 
#make_closure("sig200","SR2")
#make_closure("sig1000","SR2")

## TODO cutflow table and significance by cut
#make_cutflow(["sig1000","sig750","sig400","sig300","sig200"],"eventBoosted_sphericity")


############# EXTRA
#make_dists("QCD")
#
