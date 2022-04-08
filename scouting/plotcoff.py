import awkward as ak
from coffea import hist, processor
import uproot
from coffea.nanoevents import NanoEventsFactory, BaseSchema
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import uproot
import pickle

#with open("myhistos_sig400_0.p", "rb") as pkl_file:
lumi = 59.74*1000
qcdscaled = {}
with open("outhists/myhistos_HT2000_0.p", "rb") as pkl_file:
#with open("outhists/myhistos_QCD.p", "rb") as pkl_file:
    out = pickle.load(pkl_file)
    for name, h in out.items():
      if isinstance(h, hist.Hist):
        qcdscaled[name] = h.copy()

def make_dists(sample, xsec):
  with open("outhists/myhistos_%s.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      print(out)
      if xsec ==0:
        scale = 1
      else:
        scale= lumi*xsec/out["sumw"]["sig400"]
      scaled = {}
      for name, h in out.items():
        if "SR" in name:
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
          fig.savefig("Plots/proccess_%s"%(name))
          plt.close()
  
      fig, ax1 = plt.subplots()
      
#      #Trigger plots
#      hx = hist.plotratio(
#          out["trigdist_ht"].integrate("cut",slice(2,3)),out["trigdist_ht"].integrate("cut",slice(0,1)),
#          ax=ax1,
#          error_opts={'color': 'k', 'marker': '.'},
#          unc='clopper-pearson'
#      )
#      ax1.set_ylim(0,1.1)
#      hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
#      fig.savefig("Plots/trigHtnoref_%s"%("ht"))
#      plt.close()
#      fig, ax1 = plt.subplots()
#      
#      hx = hist.plotratio(
#          out["trigdist_ht"].integrate("cut",slice(1,2)),out["trigdist_ht"].integrate("cut",slice(0,1)),
#          ax=ax1,
#          error_opts={'color': 'k', 'marker': '.'},
#          unc='clopper-pearson'
#      )
#      ax1.set_ylim(0,1.1)
#      hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
#      fig.savefig("Plots/trigMunoref_%s"%("ht"))
#      plt.close()
#      fig, ax1 = plt.subplots()
#      
#      hx = hist.plotratio(
#          out["trigdist_ht"].integrate("cut",slice(2,3)),out["trigdist_ht"].integrate("cut",slice(1,2)),
#          ax=ax1,
#          error_opts={'color': 'k', 'marker': '.'},
#          unc='clopper-pearson'
#      )
#      ax1.set_ylim(0,1.1)
#      hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
#      fig.savefig("Plots/trigHtMu_%s"%("ht"))
#      plt.close()


colors = ["red","green","orange","blue","black","magenta"]
cuts=["0:None","1:HTTrig","2:HT>=600","3:FJ>=2","4:nPFCand>=100"]

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
      print(out)
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
            #print(len(s[0]),len(s[1]))
            sig, sigbkg = get_sig(s[0],sb[0],s[1][:-1])
            ax1.errorbar(s[1][:-1],sig/np.sqrt(sigbkg),(sig/(np.sqrt(sigbkg)))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(np.multiply(4,sigbkg)))),ecolor=colors[cut],color=colors[cut],label=cuts[cut],marker="+")
            #ax1.errorbar(s[1][:-1],s[0]/np.sqrt(sb[0]),(s[0]/(np.sqrt(sb[0])))*np.sqrt(np.add(np.reciprocal(s[0]),np.reciprocal(4*sb[0]))),ecolor=colors[cut],color=colors[cut],label=cuts[cut],marker="+")
            #print(s)
            #hist.plotratio(
            #    #scaled[name].integrate("cut",slice(cut,cut+1)),scaled[name].integrate("cut",slice(cut,cut+1)),
            #    scaled[name].integrate("cut",slice(cut,cut+1)),qcdscaled[name].integrate("cut",slice(cut,cut+1)) + scaled[name].integrate("cut",slice(cut,cut+1)),
            #    ax=ax1,
            #    error_opts={'color': colors[cut], 'marker': '+'},
            #    clear=False,
            #    label=cuts[cut],
            #    unc='clopper-pearson'
            #)
          ax1.legend()
          ax1.set_xlabel(name[5:])
          ax1.set_ylabel("s/sqrt(s+b)")
          hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
          fig.savefig("Plots/signif_%s"%(name))
          plt.close()



def make_n1(sample,xsec,var,cut):
#  qcdscaled = {}
#  with open("outhists/myhistos_QCD.p", "rb") as pkl_file:
#      out = pickle.load(pkl_file)
#      for name, h in out.items():
#        if isinstance(h, hist.Hist):
#          qcdscaled[name] = h.copy()
  with open("outhists/myhistos_%s_2.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      print(out)
      scale= lumi*xsec/out["sumw"][sample]
      scaled = {}
      for name, h in out.items():
        if var not in name:
          continue
        if isinstance(h, hist.Hist):
          scaled[name] = h.copy()
          scaled[name].scale(scale)
      
      
          s = scaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy()
          b = (qcdscaled[name].integrate("cut",slice(cut,cut+1)) + scaled[name].integrate("cut",slice(cut,cut+1))).to_hist().to_numpy()
          fig, ax = plt.subplots()
          ax.step(s[1][:-1],s[0],color="black",label="Dist: Sig400")
          ax.step(s[1][:-1],b[0],color="blue" ,label="Dist: QCD"   )

          ax1 = ax.twinx()
          #for cut in [0,1,2,3,4]:
          sig, sigbkg = get_sig(s[0],(s+b)[0],s[1][:-1])
          ax1.errorbar(s[1][:-1],sig/np.sqrt(sigbkg),(sig/(np.sqrt(sigbkg)))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(np.multiply(4,sigbkg)))),ecolor="red",color="red",label="Signif",marker="+")
          lins1, labs1 = ax.get_legend_handles_labels()
          lins2, labs2 = ax1.get_legend_handles_labels()
          ax.legend(lins1+lins2, labs1+labs2)
          ax.set_yscale("log")
          ax1.set_xlabel(name[5:])
          ax1.set_ylabel("s/sqrt(s+b)")
          hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
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
def makeSR(sample,xsec):
  with open("outhists/myhistos_%s_2.p"%sample, "rb") as pkl_file:
      out = pickle.load(pkl_file)
      print(out)
      scale= lumi*xsec/out["sumw"][sample]
      scaled = {}
      var = "SR"
      for name, h in out.items():
        if var not in name:
          continue
        if isinstance(h, hist.Hist):
          scaled[name] = h.copy()
          scaled[name].scale(scale)
          s = scaled[name].to_hist().to_numpy()#[0][0]) #.integrate("cut",slice(cut,cut+1)).to_hist().to_numpy())
          b = qcdscaled[name].to_hist().to_numpy()#[0][0]) #.integrate("cut",slice(cut,cut+1)).to_hist().to_numpy())
          sig, sigbkg = get_sig2d(s[0][0],(s+b)[0][0],s[2][:-1],s[3][:-1])
          signif = sig/ np.sqrt(sigbkg)
          print(signif)
          print(len(s[2]),len(s[3]),len(signif))
          
          fig, ax = plt.subplots()
          shw = ax.imshow(signif, interpolation='none',origin="lower",cmap="autumn")
          bar = plt.colorbar(shw)
          bar.set_label("Significance")
          ax.set_ylabel("nPFCand")
          ax.set_xlabel("eventBoosted_Sphericity")
          #ax.pcolor = (s[2],s[3],signif)
          #X,Y = np.meshgrid(s[2][:-1],s[3][:-1])
          #plt.pcolor(X,Y,signif)
          #plt.pcolor(X,Y,signif.reshape(100,50))
          
          #ax1.errorbar(s[1][:-1],sig/np.sqrt(sigbkg),(sig/(np.sqrt(sigbkg)))*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(np.multiply(4,sigbkg)))),ecolor="red",color="red",label="Signif",marker="+")
          #lins1, labs1 = ax.get_legend_handles_labels()
          #lins2, labs2 = ax1.get_legend_handles_labels()
          #ax.legend(lins1+lins2, labs1+labs2)
          #ax.set_yscale("log")
          #ax1.set_xlabel(name[5:])
          #ax1.set_ylabel("s/sqrt(s+b)")
          hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
          fig.savefig("Plots/signif2d_%s"%(var))
          plt.close()
          fig, ax1 = plt.subplots()
      
          hx = hist.plot2d(
              scaled[name].integrate("axis",slice(0,1)),
              "nPFCand",
              ax=ax1,
              #overlay="cut",
              #stack=False,
              #fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
          )
          hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
          fig.savefig("Plots/SR_sig_%s"%(name))
          plt.close()
        
          fig, ax1 = plt.subplots()
      
          hx = hist.plot2d(
              qcdscaled[name].integrate("axis",slice(0,1)),
              "nPFCand",
              ax=ax1,
              #overlay="cut",
              #stack=False,
              #fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
          )
          hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)
          fig.savefig("Plots/SR_bkg_%s"%(name))
          plt.close()
        
          




xsec = [0.17,0.5,5.9,8.9,13.6] #1000-200
#make_signif("sig400",5.9)
make_dists("QCD",0)
make_dists("sig400_2",5.9)
make_dists("sig200_2",13.6)

#make_n1("sig400",5.9,"FatJet_pt",2)
#make_n1("sig400",5.9,"n_fatjet",2)
#make_n1("sig400",5.9,"n_pfcand",3)
#make_n1("sig400",5.9,"eventBoosted_sphericity",4)
makeSR("sig400",5.9)
makeSR("sig200",13.6)
