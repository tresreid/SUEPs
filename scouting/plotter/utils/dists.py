
from utils.utils import *

def make_threshold(samples,allmaxpoints,xs,xlab):
  fig, (ax1) = plt.subplots(
      nrows=1,
      ncols=1,
      figsize=(7,7),
  )
  fig.subplots_adjust(hspace=.07)
  for sample in samples:

      ax1.errorbar(xs,allmaxpoints["sig_%s"%sample],allmaxpoints["err_%s"%sample],ecolor=sigcolors[sample],color=sigcolors[sample],label=labels[sample],marker="+")

  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax1)
  ax1.set_xlabel(xlab)
  ax1.set_ylabel("s/sqrt(s+b+$b^{2}$)")
  ax1.legend()
  fig.savefig("Plots/threshold_%s_%s.%s"%(xlab.replace(" ", "_"),year,ext))
  plt.close()

def make_n1(samples,var,cut,maxpoints,xlab=None,shift_leg=False):
  name = "dist_%s"%var
  if(xlab==None):
    xlab= name[5:]
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)

  qcd = qcdscaled[name].integrate("cut",slice(cut,cut+1))
  qcd.label = "QCD"
  hx = hist.plot1d(
      qcd,
      ax=ax,
      stack=False,
      fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3),"color":"wheat"}
  )
  large_max = False
  large_max1 = False
  large_max2 = False
  large_max3 = False
  large_max4 = False
  for sample in samples:
    scaled = sigscaled[sample]
    s = scaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy()
    b = qcdscaled[name].integrate("cut",slice(cut,cut+1)).to_hist().to_numpy()

    xbin = xbins(s[1])
    sig, bkg = get_sig(s[0],b[0],xbin)
    sigbkg = np.add(np.add(sig,bkg),np.square(bkg))
    signifline = sig/np.sqrt(np.add(np.add(sig,bkg),np.square(bkg)))
    err = (signifline)*np.sqrt(np.add(np.reciprocal(sig),np.reciprocal(np.multiply(4,sigbkg))))
    ax1.errorbar(xbin,signifline,err,ecolor=sigcolors[sample],color=sigcolors[sample],label=labels[sample],marker="+")

    ax.step(s[1],np.append(s[0],s[0][-1]),color=sigcolors[sample],label=labels[sample],linestyle="--",where="post")
    if("fjn1" in name):
      maxpoints["sig_%s"%sample].append(signifline[3])
      maxpoints["err_%s"%sample].append(err[3])
      maxpoints["evt_%s"%sample].append(sum(s[0][2:]))
    else:
      maxpoints["sig_%s"%sample].append(np.nanmax(signifline))
      maxpoints["evt_%s"%sample].append(sum(s[0][np.nanargmax(signifline):]))
      maxpoints["err_%s"%sample].append(err[np.nanargmax(signifline)])
    if(np.nanmax(signifline) > 1):
      large_max = True
    if(np.nanmax(signifline) > 5):
      large_max1 = True
    if(np.nanmax(signifline) > 20):
      large_max2 = True
    if(np.nanmax(signifline) > 30):
      large_max3 = True
    if(np.nanmax(signifline) > 60):
      large_max4 = True
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
  ax.set_yscale("log")
  y1,y2 = ax.get_ylim()
  ax.set_ylim(y1,y2*10)
  ax.set_xlabel("")
  ax1.set_xlabel(xlab)
  ax1.set_ylabel("s/sqrt(s+b+$b^{2}$)")
  ax.set_ylabel("Events")
  leg1, leg = ax.get_legend_handles_labels()
  leg = [l.replace("None","QCD") for l in leg]
  if shift_leg:
    locx = "center left"
    locy = "lower left"
  else:
    locx = "upper right"
    locy = "right"

  if("fjn1" in var):
    ax.add_artist(AnchoredText("Selection:\n Trigger\n %s>560 GeV\n"%(r"$H_{t}$"),loc=locx))
  elif("PFcand_ncount" in var):
    ax.add_artist(AnchoredText("Selection:\n Trigger\n %s>560 GeV\n 2+ AK15 Jets\n sphericity > 0.7"%(r"$H_{t}$"),loc=locx))
  elif("FatJet_nconst" in var and cut ==4):
    ax.add_artist(AnchoredText("Selection:\n Trigger\n %s>560 GeV\n 2+ AK15 Jets\n sphericity > 0.7"%(r"$H_{t}$"),loc=locx))
  else:
    ax.add_artist(AnchoredText(selection[cut],loc=locx))
  ax.legend(leg,loc=locy)
  if large_max4:
    ax1.set_ylim([0,100])
  elif large_max3:
    ax1.set_ylim([0,60])
  elif large_max2:
    ax1.set_ylim([0,40])
  elif large_max1:
    ax1.set_ylim([0,20])
  elif large_max:
    ax1.set_ylim([0,5])
  #else:
  #  ax1.set_ylim([0,1])
  #ax.autoscale(axis='y', tight=True)
  fig.savefig("Plots/signif_%s_%s_%s.%s"%(var,cut,year,ext))
  plt.close()

  return maxpoints

def make_dists(sample):
  #skip = ["trigdist_ht20","trigdist_ht30","trigdist_ht40","trigdist_ht50","dist_event_sphericity","dist_Vertex_tracksSize0"]
  #skip = ["dist_Vertex_minZ","dist_Vertex_tracksSize0"]
  #run = ["dist_offline_trk_pt","dist_offline_trk_eta","dist_offline_trk_phi"]
  if "QCD" in sample:
    scaled = qcdscaled
  elif "RunA" in sample:
    scaled = datascaled
  else:
    scaled = sigscaled[sample]
  for name, h in scaled.items():
    if "SR1" in name or "trkID" in name or "2d" in name:
          continue
    #if name in skip:
    #      continue
    #if name not in run:
    #      continue
    print(name)

    fig, ax1 = plt.subplots()
    hx = hist.plot1d(
        scaled[name],
        ax=ax1,
        overlay="cut",
        stack=False,
        fill_opts={'alpha': .9, 'edgecolor': (0,0,0,0.3)}
    )
    hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2)
    if "trkID" not in name and "offline_trk" not in name:
      ax1.set_yscale("log")
      ax1.autoscale(axis='y', tight=True)
    if "_pt" in name and "res" not in name and "Dispersion" not in name and "offline" not in name:
      ax1.set_xscale("log")
      ax1.set_xlim([20,200])
      if "PFcand" in name or "gen" in name:
        ax1.set_xlim([0.3,100])
    if "dR" in name:
      ax1.set_yscale("log")
      ax1.axvline(x=0.02,color="grey",ls="--")
    fig.savefig("Plots/proccess_%s_%s_%s.%s"%(sample,name,year,ext))
    plt.close()

def make_overlapdists(samples,var,cut,xlab=None,make_ratio=True,vline=None,shift_leg=False,save_ratio=False):
  if make_ratio:
    fig, (ax,ax1) = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(7,7),
        gridspec_kw={"height_ratios": (3, 1)},
        sharex=True
    )
  else:
    fig, ax = plt.subplots()
  fig.subplots_adjust(hspace=.07)
  name = "dist_%s"%var
  if (xlab==None):
    xlab=name[5:]
  if "RunA" in samples:
    h1 = datascaled[name].integrate("cut",slice(cut,cut+1))
    if("ht" in name):
      h1 = h1.rebin("v1",hist.Bin("v1","ht",50,50,3500))
    h1_scale = h1.values(sumw2=True)[()]
    sdat = h1.to_hist().to_numpy()
    daterr = np.sqrt(h1_scale[1])
    xerr = xbins_err(sdat[1])
    xbin = np.array(xbins(sdat[1]))
    xerr_low = [(t - s) for s, t in zip(sdat[1], xbin)]
    xerr_high = [abs(t - s) for s, t in zip(sdat[1][1:], xbin)]
    ax.errorbar(xbin,sdat[0],yerr=daterr,xerr=[xerr_low,xerr_high],color=sigcolors["RunA"],label=labels["RunA"],zorder=6,ls="None",marker=".")
  if "QCD" in samples:
    h2x = qcddatascaled[name]
    h2= h2x.integrate("cut",slice(cut,cut+1))
    if("ht" in name):
      h2 = h2.rebin("v1",hist.Bin("v1","ht",50,50,3500))
    h2_scale = h2.values(sumw2=True)[()]
    s = h2.to_hist().to_numpy()
    s_err = np.sqrt(h2_scale[1])
    xbin = xbins(s[1])
    ## append an extra point at the end because the post doesn't work without it for the last bin. it needs to know where to go next
    ax.fill_between(s[1],np.append(s[0],s[0][-1]),color=sigcolors["QCD"],alpha=0.8,label=labels["QCD"],zorder=0,linestyle="-",step="post")#,)
    ax.errorbar(s[1],np.append(s[0],s[0][-1]),yerr=np.append(s_err,0),color=sigcolors["QCD"],zorder=1,ls='none')
    if(make_ratio):
      hist.plotratio(
      h1,h2,
      ax=ax1,
      clear=False,
      error_opts={'color': sigcolors["RunA"], 'marker': '+'},
      unc='num'
      )

  for sample in samples:
    if "sig" in sample:
      fil = directory+"myhistos_%s_2.p"%sample
      scaled = sigscaled[sample]
      s = scaled[name].integrate("cut",slice(cut,cut+1))#.to_hist().to_numpy()
      if("ht" in name):
        s = s.rebin("v1",hist.Bin("v1","ht",50,50,3500))
      s_scale = s.values(sumw2=True)[()]
      s1= s.to_hist().to_numpy()
      xbin = xbins(s1[1])
      ## append an extra point at the end because the post doesn't work without it for the last bin. it needs to know where to go next
      ax.step(s1[1],np.append(s1[0],s1[0][-1]),color=sigcolors[sample],label=labels[sample],linestyle="--",where="post",zorder=2)
      ax.set_xlabel("")
  if(vline):
    for v in vline:
      ax.axvline(x=v,color="grey",ls="--")
      if(make_ratio):
        ax1.axvline(x=v,color="grey",ls="--")

  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
  if("res" in var):
    ax.set_yscale("linear")
    y1,y2 = ax.get_ylim()
    ax.set_ylim(y1,y2*1.50)
  else:
    ax.set_yscale("log")
    y1,y2 = ax.get_ylim()
    ax.set_ylim(y1,y2*100)
  if("ht" in var):
    ax.set_xlim([0,3500])
  if("PFcand_pt" in var):
    ax.set_xscale("log")
    ax.set_xlim([0.6,50])
  if("FatJet_pt" in var):
    ax.set_xlim([50,1000])
  ax.set_ylabel("Events")
  if make_ratio:
    ax1.set_xlabel(xlab)
    ax1.set_ylim(0.5,1.5)
    #ax1.set_ylim(0.0,1.5)
    ax1.set_ylabel("Data/QCD")
    ax1.axhline(y=1,color="grey",ls="--")
    if save_ratio:
      rat_vals = np.divide(h1.to_hist().to_numpy()[0],h2.to_hist().to_numpy()[0])
      print(rat_vals)
      np.savetxt("../systematics/triggers/track_multiplicity_ratio_2018.txt",np.nan_to_num(rat_vals), delimiter=",") 
  else:
    ax.set_xlabel(xlab)
  if "res" in var:
    selcut = 3
  else:
    selcut = cut
  if shift_leg:
    ax.add_artist(AnchoredText(selection[selcut],loc="lower left",prop=dict(size=15)))
    ax.legend(loc="center left")
  else:
    ax.add_artist(AnchoredText(selection[selcut],loc="upper right",prop=dict(size=15)))
    ax.legend(loc="right")
  fig.savefig("Plots/overlap_dist_%s_cut%s_%s.%s"%(var,cut,year,ext))
  plt.close()

