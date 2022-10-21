from utils import *

def make_trkeff(sample,name,xlab,runPV=0):
#  with open(directory+"myhistos_%s.p"%sample, "rb") as pkl_file:
#      out = pickle.load(pkl_file)
#      sample = sample.split("_")[0]
#      xsec = xsecs[sample.split("_")[0]]
#      if xsec ==0:
#        scale = 1
#      else:
#        scale= lumi*xsec/out["sumw"][sample]
#      #out[name].scale(scale)
#
#
      out = sigscaled[sample]
      if("IDFK" in name):
        ###############FAKE
        numFK = out[name].integrate("v2",slice(0.02,0.3)).copy()
        denom = out[name].integrate("v2").copy()
        fig, ax1 = plt.subplots()
        ### note that the cut order goes 0,10,1,2,3,... so cut 10 is actually number 1 and all others are shifted +1 except 10. dumb dumb dumb
        for i,cut in enumerate([3,4,5,8,1]):
          hx1 = hist.plotratio(
              numFK.integrate("cut",slice(cut,1+cut)),denom.integrate("cut",slice(cut,1+cut)),
              ax=ax1,
              clear=False,
              error_opts={'color': colors[i], 'marker': '+'},
              unc='clopper-pearson'
          )

        #ax1.set_ylim(0,0.5)
        if "_pt" in name:
          ax1.set_xscale("log")
          ax1.set_xlim([20,200])
          if "PFcand" in name or "gen" in name:
            ax1.set_xlim([0.5,100])
        ax1.legend(["q != 0","PV =0","pt > 0.5","pt >0.75","pt >1.0",],loc="lower right")
        ax1.set_xlabel(xlab)
        ax1.set_ylabel("Fake Rate")
        #ax1.legend(["no cut", "|eta| < 2.4","q != 0","PV =0","pt > 0.5","pt >0.6","pt >0.7","pt >0.75","pt >0.8","pt >0.9","pt >1.0",],loc="lower right")
        fig.suptitle("Track Fake Rate: %s"%sample)
        hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
        fig.savefig("Plots/track_fake_%s_%s_%s.%s"%(sample,name,year,ext))
        plt.close()
      else:
        num = out[name].integrate("v3",slice(0,4)).integrate("v2",slice(0,0.02)).copy()
        denom = out[name].integrate("v3",slice(0,4)).integrate("v2").copy()
        numPV = out[name].integrate("v3",slice(0,1)).integrate("v2",slice(0,0.02)).copy()
        denomPV = out[name].integrate("v3",slice(0,1)).integrate("v2").copy()
        fig, ax1 = plt.subplots()
        cuts = [1,4,6]
        leg = ["pt >0.6","pt >0.8","pt >1.0"]
        #leg = ["pt >0.6","PV==0 + pt >0.6","pt >0.8","PV==0 + pt >0.8","pt >1.0","PV==0 + pt >1.0"]
        if "_pt" in name:
          cuts=[0]
          leg = ["pt> 0.5","PV==0 + pt >0.5"]
          ax1.set_xscale("log")
          ax1.set_xlim([20,200])
          if "PFcand" in name or "gen" in name:
            ax1.set_xlim([0.5,100])
        #ax1.legend(["pt > 0.5","pt >0.6","pt >0.7","pt >0.75","pt >0.8","pt >0.9","pt >1.0",],loc="lower right")
        for i,cut in enumerate(cuts):
          if(runPV==0):
            hx = hist.plotratio(
                num.integrate("cut",slice(1+cut,2+cut)),denom.integrate("cut",slice(1+cut,2+cut)),
                ax=ax1,
                clear=False,
                error_opts={'color': colors[i], 'marker': '+'},
                unc='clopper-pearson'
            )
          if(runPV==1):
            hxPV = hist.plotratio(
                numPV.integrate("cut",slice(1+cut,2+cut)),denomPV.integrate("cut",slice(1+cut,2+cut)),
                ax=ax1,
                clear=False,
                error_opts={'color': colors[i], 'marker': 'x'},
                unc='clopper-pearson'
            )
          if(runPV==2):
            hx = hist.plotratio(
                num.integrate("cut",slice(1+cut,2+cut)),denom.integrate("cut",slice(1+cut,2+cut)),
                ax=ax1,
                clear=False,
                error_opts={'color': colors[i], 'marker': '+'},
                unc='clopper-pearson'
            )
            hxPV = hist.plotratio(
                numPV.integrate("cut",slice(1+cut,2+cut)),denomPV.integrate("cut",slice(1+cut,2+cut)),
                ax=ax1,
                clear=False,
                error_opts={'color': colors[i], 'marker': 'x'},
                unc='clopper-pearson'
            )

        ax1.legend(leg,loc="lower right")
        ax1.set_ylim(0.7,1.01)
        ax1.set_xlabel(xlab)
        ax1.set_ylabel("Efficiency")
        fig.suptitle("Track Efficiency: %s"%sample)
        hep.cms.label('',data=False,lumi=lumi/1000,year=2018,loc=2)
        fig.savefig("Plots/track_eff_%s_%s_%d_%s.%s"%(sample,name,runPV,year,ext))
        plt.close()
