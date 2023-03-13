from utils.utils import *

def make_correlation(SR,cut):
  if cut==0 or cut==1:
    high1 = 100
  else:
    high1 = 80
  var = "nPFCand"
  SR=SR+"_%s"%cut
  h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  fig, ax1 = plt.subplots()

  sphere = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
  #labs = []
  for i in range(len(sphere)-1):
    h2 = h1.integrate("eventBoostedSphericity",slice(sphere[i],sphere[i+1])).to_hist().to_numpy()
    norm = np.linalg.norm(h2[0])
    xbin = xbins(h2[1])
    ax1.step(xbin[:-high1],h2[0][:-high1]/norm,color=colors[i],label="%s-%s"%(sphere[i],sphere[i+1]),linestyle="-",where="mid")
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax1)
  ax1.legend(title="Boosted\n Sphericity\n Bins")
  ax1.set_xlabel(var)
  ax1.set_ylabel("AU")
  ax1.set_yscale("log")
  ax1.set_xscale("log")
  ax1.autoscale(axis='y', tight=True)
  ax1.autoscale(axis='x', tight=True)
  fig.savefig("Plots/correlation_sphere_%s_%s.%s"%(SR,year,ext))
  plt.close()


  sphere = [0,20,40,60,80,100]
  for cut in [0,15,20,25,30,35,40,45]:
    fig, ax1 = plt.subplots()
    for i in range(len(sphere)-1):

      h2 = h1.integrate(var,slice(sphere[i],sphere[i+1])).to_hist().to_numpy()
      norm = np.linalg.norm(h2[0][cut:])
      xbin = xbins(h2[1])
      ax1.step(xbin[cut:],h2[0][cut:]/norm,color=colors[i],label="%s-%s"%(sphere[i],sphere[i+1]),linestyle="-",where="mid")

    hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax1)
    ax1.legend(title="%s Bins"%var)
    ax1.set_xlabel("Boosted Sphericity")
    ax1.set_ylabel("AU")
    ax1.set_yscale("log")
    ax1.autoscale(axis='y', tight=True)
    fig.savefig("Plots/correlation_PFcand_%s_cut%s_%s.%s"%(SR,cut,year,ext))
    plt.close()
def chisqr(obs, exp, error):
    print(obs)
    print(exp)
    print(error)
    chisqr = 0
    for i in range(len(obs)):
        chisqr = chisqr + ((obs[i]-exp[i])**2)/(error[i]**2)
    return chisqr/(len(obs)-1)

def make_closure(sample="QCD",SR="SR1_suep",cut=0,point=0,yrange=1, chi=False):
  high1 = region_cuts_tracks[point]
  high2 = region_cuts_sphere[point]
  var = "nPFCand"
  SR = SR+"_%s"%cut
  if sample == "QCD":
     h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  elif sample == "RunA":
     h1 = datascaled[SR].integrate("axis",slice(0,1))
  elif sample == "Data":
     h1 = datafullscaled[SR].integrate("axis",slice(0,1))
  else:
    h1 = (sigscaled[sample][SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
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
  rel_err = (abin_err/(abinx*abinx)+bbin_err/(bbinx*bbinx)+cbin_err/(cbinx*cbinx))
  err = expected*np.sqrt(rel_err)
  print(abinx,np.sqrt(abin_err),bbinx,cbinx,dbinx,ratx,expected,dbinx/expected,err)
  hx = hist.plot1d(
      h1.integrate("eventBoostedSphericity",slice(high2/100,high2x/100)),
      ax=ax,
      stack=False,
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"blue"}
  )
  h2 = h1.copy()
  h2.scale(ratx)
  hx2 = hist.plot1d(
      h2.integrate("eventBoostedSphericity",slice(low2/100,high2/100)),
      ax=ax,
      clear=False,
      stack=False,
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"red"}
  )
  leg = ["Observed %.2f +/- %.2f"%(dbinx,np.sqrt(dbin_err)),"Predicted: %.2f +/- %.2f"%(ratx*cbinx,err),"point"]
  ax.legend(leg)
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
  ax.set_yscale("log")
  ax.autoscale(axis='y', tight=True)
  hx1 = hist.plotratio(
      h1.integrate("eventBoostedSphericity",slice(high2/100,high2x/100)),h2.integrate("eventBoostedSphericity",slice(low2/100,high2/100)),
      ax=ax1,
      error_opts={'color': 'r', 'marker': '+'},
      unc='num'
  )
#new ratio

  xbin = xbins(h1.integrate("eventBoostedSphericity",slice(high2/100,high2x/100)).to_hist().to_numpy()[1])
  b_rat1, b_err1 = h1.integrate("eventBoostedSphericity",slice(high2/100,high2x/100)).values(sumw2=True)[()]
  b_rat2, b_err2 = h2.integrate("eventBoostedSphericity",slice(low2/100,high2/100)).values(sumw2=True)[()]
  print(xbin)
  ratio = (b_rat1/b_rat2)
  ratio_err = ratio*np.sqrt( np.divide(b_err1,np.square(b_rat1)) +np.divide(b_err2,np.square(b_rat2)) + rel_err)#+(d1_err/d1)**2+(d2_err/d2)**2)
  if chi:
    select_ratio = np.nan_to_num(ratio)[int(high1/2):]
    select_err = np.nan_to_num(ratio_err)[int(high1/2):]
    reduced_chi = chisqr(select_ratio[select_err !=0],[1]*len(select_ratio[select_err != 0]),select_err[select_err !=0])
    ax.add_artist(AnchoredText("Boundary: (%s,%s)\n $\chi^{2}$/N = %.2f"%(high1,high2/100.,reduced_chi),loc="center right",prop=dict(size=12)))
  else:
    ax.add_artist(AnchoredText("Boundary: (%s,%s)"%(high1,high2/100.),loc="center right",prop=dict(size=12)))
  hx  = ax.errorbar(xbin,b_rat1,xerr=1,yerr=np.sqrt(b_err1),color="b",ls='none')
  hx2 = ax.errorbar(xbin,b_rat2,xerr=1,yerr=np.sqrt(b_err2+rel_err),color="r",ls='none')
  hxrat = ax1.errorbar(xbin,ratio,yerr=ratio_err,color="r",ls='none')
  ax1.set_xlim(high1,125)
  if yrange:
    ax1.set_ylim(0.5,1.5)
  else:
    ax1.set_ylim(0.5,5)
  if("isrsuep" in SR):
    ax1.set_xlabel("ISR Jet Track Multiplicity")
  else:
    if cut== 2 or cut ==3:
      ax1.set_xlabel("Suep Jet Track Multiplcity")
    else:
      ax1.set_xlabel("Event Tracks")
  ax1.axhline(y=1,color="gray",ls="--")
  ax.set_xlabel("")
  ax1.set_ylabel("Observed/Predicted")
  fig.suptitle("4 Bin Closure: %s"%(sample))
  fig.savefig("Plots/closure_%s_%s_%s.%s"%(sample,SR,year,ext))
  plt.close()

def make_closure_correction6(sample="QCD",SR="SR1_suep",cut=0,point=0,yrange=1,chi=False):
  highx1 = inner_tracks #region_cuts_tracks[0]
  highx2 = region_cuts_tracks[point]
  highy1 = region_cuts_sphere[point]
  var = "nPFCand"
  SR = SR+"_%s"%cut
  if sample == "QCD":
     h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  elif sample == "RunA":
     h1 = datascaled[SR].integrate("axis",slice(0,1))
  elif sample == "Data":
     h1 = datafullscaled[SR].integrate("axis",slice(0,1))
  else:
    h1 = (sigscaled[sample][SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
  lowx =0
  lowy = 30
  highx3 = 300
  highy2 = 100

  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
  abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  SRbin = h1.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]

  abinx = abin[0]
  bbinx = bbin[0]
  cbinx = cbin[0]
  dbinx = dbin[0]
  ebinx = ebin[0]
  SRbinx = SRbin[0]
  abin_err = abin[1]
  bbin_err = bbin[1]
  cbin_err = cbin[1]
  dbin_err = dbin[1]
  ebin_err = ebin[1]
  SRbin_err = SRbin[1]
  A_err  = np.sqrt(abin[1])/abinx
  B_err  = np.sqrt(bbin[1])/bbinx
  C_err  = np.sqrt(cbin[1])/cbinx
  D_err  = np.sqrt(dbin[1])/dbinx
  E_err  = np.sqrt(ebin[1])/ebinx
  ratx = ((ebinx**2)*abinx)/((bbinx**2)*dbinx)
  rel_err = ((D_err)**2 +(2*B_err)**2 +(C_err)**2 +(A_err)**2 + (2*E_err)**2)
  err = ratx*cbinx*np.sqrt(rel_err)
  hx = hist.plot1d(
      h1.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)),
      ax=ax,
      stack=False,
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"blue"}
  )
  h2 = h1.copy()
  h2.scale(ratx)
  hx2 = hist.plot1d(
      h2.integrate("eventBoostedSphericity",slice(lowy/100,highy1/100)),
      ax=ax,
      clear=False,
      stack=False,
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"red"}
  )
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
  ax.set_yscale("log")
  ax.autoscale(axis='y', tight=True)
  hx1 = hist.plotratio(
      h1.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)),h2.integrate("eventBoostedSphericity",slice(lowy/100,highy1/100)),
      ax=ax1,
      error_opts={'color': 'r', 'marker': '+'},
      unc='num'
  )
#new ratio

  xbin = xbins(h1.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)).to_hist().to_numpy()[1])
  b_rat1, b_err1 = h1.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)).values(sumw2=True)[()]
  b_rat2, b_err2 = h2.integrate("eventBoostedSphericity",slice(lowy/100,highy1/100)).values(sumw2=True)[()]
  ratio = (b_rat1/b_rat2)
  ratio_err = ratio*np.sqrt( np.divide(b_err1,np.square(b_rat1)) +np.divide(b_err2,np.square(b_rat2)) + rel_err)#+(d1_err/d1)**2+(d2_err/d2)**2)
  hx  = ax.errorbar(xbin,b_rat1,xerr=1,yerr=np.sqrt(b_err1),color="b",ls='none')
  hx2 = ax.errorbar(xbin,b_rat2,xerr=1,yerr=np.sqrt(b_err2+rel_err),color="r",ls='none')
  hxrat = ax1.errorbar(xbin,ratio,yerr=ratio_err,color="r",ls='none')
  if chi:
    select_ratio = np.nan_to_num(ratio)[int(highx2/2):]
    select_err = np.nan_to_num(ratio_err)[int(highx2/2):]
    reduced_chi = chisqr(select_ratio[select_err !=0],[1]*len(select_ratio[select_err != 0]),select_err[select_err !=0])
    ax.add_artist(AnchoredText("Boundary: (%s,%s)\n $\chi^{2}$/N = %.2f"%(highx2,highy1/100.,reduced_chi),loc="center right",prop=dict(size=12)))
  else:
    ax.add_artist(AnchoredText("Boundary: (%s,%s)"%(highx2,highy1/100.),loc="center right",prop=dict(size=12)))
  leg = ["Observed %.2f +/- %.2f"%(SRbinx,np.sqrt(SRbin_err)),"Predicted: %.2f +/- %.2f"%(ratx*cbinx,err)]
  ax.legend(leg)

  ax1.set_xlim(highx2,125)
  if yrange:
    ax1.set_ylim(0.5,1.5)
  if("isrsuep" in SR):
    ax1.set_xlabel("ISR Jet Track Multiplicity")
  else:
    if cut== 2 or cut ==3:
      ax1.set_xlabel("Suep Jet Track Multiplicity")
    else:
      ax1.set_xlabel("Event Tracks")
  ax.set_xlabel("")
  ax1.axhline(y=1,color="gray",ls="--")
  ax1.set_ylabel("Observed/Predicted")
  fig.suptitle("6 Bin Closure: %s"%(sample))
  fig.savefig("Plots/closure6_%s_%s_%s.%s"%(sample,SR,year,ext))
  plt.close()

def make_closure_correction9(sample="QCD",SR="SR1_suep",cut=0,point=0,gap=0,yrange=1,rebin=False,chi=False):
  highx1 = inner_tracks #region_cuts_tracks[0]#20
  highy1 = inner_sphere #region_cuts_sphere[0]#38
  highx2 = region_cuts_tracks[point]
  highy2 = region_cuts_sphere[point]
  var = "nPFCand"
  SR = SR+"_%s"%cut
  if sample == "QCD":
     h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  elif sample == "RunA":
     h1 = datascaled[SR].integrate("axis",slice(0,1))
  elif sample == "Data":
     h1 = datafullscaled[SR].integrate("axis",slice(0,1))
  else:
    h1 = (sigscaled[sample][SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
  if gap:
    gapx = region_cuts_tracks[0] 
    gapy = region_cuts_sphere[0]
  else:
    gapx = highx2
    gapy = highy2

  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  if not rebin:
    h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
  #abin = h1.integrate("eventBoostedSphericity",slice( lowy/100.,  highy1/100.)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  #bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100.,  highy1/100.)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  #cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100.,  highy1/100.)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  #dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100., highy2/100.)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  #ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100., highy2/100.)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  #fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100., highy2/100.)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  #gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100., highy3/100.)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  #hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100., highy3/100.)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  #SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100.,highy3/100.)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  abin = h1.integrate("eventBoostedSphericity",slice( lowy/100.,  highy1/100.)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100.,  highy1/100.)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
  cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100.,  highy1/100.)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100., gapy/100.)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100., gapy/100.)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
  fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100., gapy/100.)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100., highy3/100.)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100., highy3/100.)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
  SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100.,highy3/100.)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  abinx = abin[0]
  bbinx = bbin[0]
  cbinx = cbin[0]
  dbinx = dbin[0]
  ebinx = ebin[0]
  fbinx = fbin[0]
  gbinx = gbin[0]
  hbinx = hbin[0]
  SRbinx = SRbin[0]
  abin_err = abin[1]
  bbin_err = bbin[1]
  cbin_err = cbin[1]
  dbin_err = dbin[1]
  ebin_err = ebin[1]
  fbin_err = fbin[1]
  gbin_err = gbin[1]
  hbin_err = hbin[1]
  SRbin_err = SRbin[1]
  A_err  = np.sqrt(abin[1])/abinx
  B_err  = np.sqrt(bbin[1])/bbinx
  C_err  = np.sqrt(cbin[1])/cbinx
  D_err  = np.sqrt(dbin[1])/dbinx
  E_err  = np.sqrt(ebin[1])/ebinx
  F_err  = np.sqrt(fbin[1])/fbinx
  G_err  = np.sqrt(gbin[1])/gbinx
  H_err  = np.sqrt(hbin[1])/hbinx
  print("A: %s +/- %s"%(abinx,np.sqrt(abin_err)))
  print("B: %s +/- %s"%(bbinx,np.sqrt(bbin_err)))
  print("C: %s +/- %s"%(cbinx,np.sqrt(cbin_err)))
  print("D: %s +/- %s"%(dbinx,np.sqrt(dbin_err)))
  print("E: %s +/- %s"%(ebinx,np.sqrt(ebin_err)))
  print("F: %s +/- %s"%(fbinx,np.sqrt(fbin_err)))
  print("G: %s +/- %s"%(gbinx,np.sqrt(gbin_err)))
  print("H: %s +/- %s"%(hbinx,np.sqrt(hbin_err)))
  print("SR: %s +/- %s"%(SRbinx,np.sqrt(SRbin_err)))
  ratx = fbinx*((hbinx*dbinx*bbinx)**2)/((gbinx*cbinx*abinx)*(ebinx**4))
  rel_err = (2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2
  err = ratx*fbinx*np.sqrt(rel_err+F_err**2)
  if rebin:
    h1 = h1.rebin(var,hist.Bin(var,var,[x for x in range(0,highx1,2)] +[50,55,60,65,120,300]))
  hx = hist.plot1d(
      h1.integrate("eventBoostedSphericity",slice(highy2/100.,highy3/100.)),
      ax=ax,
      stack=False,
      error_opts={'color': 'r', 'marker': '+'},
      #unc='num',
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"blue"}
  )
  h2 = h1.copy()
  h2.scale(ratx)
  hx2 = hist.plot1d(
      h2.integrate("eventBoostedSphericity",slice(highy1/100.,highy2/100.)),
      ax=ax,
      clear=False,
      stack=False,
      error_opts={'color': 'r', 'marker': '+'},
      #unc='num',
      fill_opts={'alpha': .5, 'edgecolor': (0,0,0,0.3),"color":"red"}
  )
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
  ax.set_yscale("log")
  ax.autoscale(axis='y', tight=True)
  hx1 = hist.plotratio(
      h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)),h2.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)),
      ax=ax1,
      error_opts={'color': 'r', 'marker': '+'},
      unc='num'
  )
  #new ratio

  xbin = xbins(h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).to_hist().to_numpy()[1])
  b_rat1, b_err1 = h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).values(sumw2=True)[()]
  b_rat2, b_err2 = h2.integrate("eventBoostedSphericity",slice(highy1/100,highy2/100)).values(sumw2=True)[()]
  ratio = (b_rat1/b_rat2)
  ratio_err = ratio*np.sqrt( np.divide(b_err1,np.square(b_rat1)) +np.divide(b_err2,np.square(b_rat2)) + rel_err)#+(d1_err/d1)**2+(d2_err/d2)**2)
  hx  = ax.errorbar(xbin,b_rat1,xerr=1,yerr=np.sqrt(b_err1),color="b",ls='none')
  hx2 = ax.errorbar(xbin,b_rat2,xerr=1,yerr=np.sqrt(b_err2+rel_err),color="r",ls='none')
  hxrat = ax1.errorbar(xbin,ratio,yerr=ratio_err,color="r",ls='none')
  if (chi):
    select_ratio = np.nan_to_num(ratio)[int(highx2/2):]
    select_err = np.nan_to_num(ratio_err)[int(highx2/2):]
    reduced_chi = chisqr(select_ratio[select_err !=0],[1]*len(select_ratio[select_err != 0]),select_err[select_err !=0])
    ax.add_artist(AnchoredText("Boundary: (%s,%s)\n $\chi^{2}$/N = %.2f"%(highx2,highy2/100.,reduced_chi),loc="center right",prop=dict(size=12)))
  else:
    ax.add_artist(AnchoredText("Boundary: (%s,%s)"%(highx2,highy2/100.),loc="center right",prop=dict(size=12)))
  leg = ["Observed %.2f +/- %.2f"%(SRbinx,np.sqrt(SRbin_err)),"Predicted: %.2f +/- %.2f"%(ratx*fbinx,err)]
  ax.legend(leg)
######
  ax1.set_xlim(highx2,125)
  if yrange:
    ax1.set_ylim(0.0,2.0)
  if("isrsuep" in SR):
    ax1.set_xlabel("ISR Jet Track Multiplicity")
  else:
    if cut== 2 or cut ==3:
      ax1.set_xlabel("Suep Jet Track Multiplicity")
    else:
      ax1.set_xlabel("Event Tracks")
  ax.set_xlabel("")
  ax1.axhline(y=1,color="gray",ls="--")
  ax1.set_ylabel("Observed/Predicted")
  fig.suptitle("9 Bin Closure: %s"%(labels[sample]))
  if rebin:
    fig.savefig("Plots/closure9_%s_%s_%s_%s_rebin.%s"%(sample,SR,gap,year,ext))
  else:
    fig.savefig("Plots/closure9_%s_%s_%s_%s.%s"%(sample,SR,gap,year,ext))
  plt.close()

def cutflow_correction_binned(SR="SR1_suep",cut=3,point=0,gap=0):
  highx1 = inner_tracks
  highy1 = inner_sphere
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
  var = "nPFCand"
  SR = SR+"_%s"%cut
  predicted = {"QCD":[],"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  observed = {"QCD":[],"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  sigobserved = {"QCD":[],"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  signif = {"QCD":[],"sig125":[],"sig200":[],"sig300":[],"sig400":[],"sig700":[],"sig1000":[]}
  gapx = region_cuts_tracks[0]
  gapy = region_cuts_sphere[0]
  injected = False
  for sample in ["QCD","sig125","sig200","sig300","sig400","sig700","sig1000"]:
    if sample == "QCD":
       h1 = qcdscaled[SR].integrate("axis",slice(0,1))
    elif sample == "RunA":
       h1 = datascaled[SR].integrate("axis",slice(0,1))
    elif sample == "Data":
       h1 = datafullscaled[SR].integrate("axis",slice(0,1))
    else:
      h1 = (sigscaled[sample][SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
      h2 = (sigscaled[sample][SR]).integrate("axis",slice(0,1))

    for highx2, highy2 in zip(region_cuts_tracks,region_cuts_sphere):
      if gap == 0:
        gapx = highx2
        gapy = highy2
      if gap ==2:
        highy3 = highy2+10
        if highx2!=100:
          highx3 = highx2+10
      print(highx2,highy2)
      h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
      abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      if("sig" in sample):
        SRbinsig = h2.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
        sigobserved[sample].append(SRbinsig[0])
      else:
        sigobserved[sample].append(0)

      abinx = abin[0]
      bbinx = bbin[0]
      cbinx = cbin[0]
      dbinx = dbin[0]
      ebinx = ebin[0]
      fbinx = fbin[0]
      gbinx = gbin[0]
      hbinx = hbin[0]
      SRbinx = SRbin[0]
      abin_err = abin[1]
      bbin_err = bbin[1]
      cbin_err = cbin[1]
      dbin_err = dbin[1]
      ebin_err = ebin[1]
      fbin_err = fbin[1]
      gbin_err = gbin[1]
      hbin_err = hbin[1]
      SRbin_err = SRbin[1]
      A_err  = np.sqrt(abin[1])/abinx
      B_err  = np.sqrt(bbin[1])/bbinx
      C_err  = np.sqrt(cbin[1])/cbinx
      D_err  = np.sqrt(dbin[1])/dbinx
      E_err  = np.sqrt(ebin[1])/ebinx
      F_err  = np.sqrt(fbin[1])/fbinx
      G_err  = np.sqrt(gbin[1])/gbinx
      H_err  = np.sqrt(hbin[1])/hbinx
      SR_err  = np.sqrt(SRbin[1])/SRbinx
      ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2))
      err = ratx*fbinx*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2)
      err1 = (2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2
      predicted[sample].append(ratx*fbinx)
      observed[sample].append(SRbinx)
      signif[sample].append(SRbinx/(ratx*fbinx))
  pred = pd.DataFrame(predicted)
  obs = pd.DataFrame(observed)
  sobs = pd.DataFrame(sigobserved)
  signifi = pd.DataFrame(signif)
  for sample in ["QCD","sig125","sig200","sig300","sig400","sig700","sig1000"]:
    print("(%s,%s) %s & %.2f & %.2f & %.2f & %.2f  \\\\"%(region_cuts_tracks[0],region_cuts_sphere[0]/100.,sample,pred[sample][0],sobs[sample][0],obs[sample][0],signifi[sample][0]))
  print("\\hline")
  for sample in ["QCD","sig125","sig200","sig300","sig400","sig700","sig1000"]:
    print("(%s,%s) %s & %.2f & %.2f & %.2f & %.2f  \\\\"%(region_cuts_tracks[1],region_cuts_sphere[1]/100.,sample,pred[sample][1],sobs[sample][1],obs[sample][1],signifi[sample][1]))
  print("\\hline")
  for sample in ["QCD","sig125","sig200","sig300","sig400","sig700","sig1000"]:
    print("(%s,%s) %s & %.2f & %.2f & %.2f & %.2f  \\\\"%(region_cuts_tracks[2],region_cuts_sphere[2]/100.,sample,pred[sample][2],sobs[sample][2],obs[sample][2],signifi[sample][2]))
  print("\\hline")
  for sample in ["QCD","sig125","sig200","sig300","sig400","sig700","sig1000"]:
    print("(%s,%s) %s & %.2f & %.2f & %.2f & %.2f  \\\\"%(region_cuts_tracks[3],region_cuts_sphere[3]/100.,sample,pred[sample][3],sobs[sample][3],obs[sample][3],signifi[sample][3]))

def compareRegionData(SR="SR1_suep",cut=0,point=0,zoom=0):
  highx1 = inner_tracks#22
  highy1 = inner_sphere#42
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100

  var = "nPFCand"
  SR = SR+"_%s"%cut
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  for sample in ["QCD","Data"]:
    if sample == "QCD":
       h1 = qcdscaled[SR].integrate("axis",slice(0,1))
    elif sample == "RunA":
       h1 = datascaled[SR].integrate("axis",slice(0,1))
    elif sample == "Data":
       h1 = datafullscaled[SR].integrate("axis",slice(0,1))
    else:
      #with open(directory+"myhistos_%s_2.p"%sample, "rb") as pkl_file:
      #    out = pickle.load(pkl_file)
      #    scale= lumi*xsecs[sample]/out["sumw"][sample]
      #    scaled = {}
      #    for name, h in out.items():
      #      if SR not in name or "mu" in name or "trig" in name:
      #        continue
      #      if isinstance(h, hist.Hist):
      #        scaled[name] = h.copy()
      #        scaled[name].scale(scale)
      h1 = (sigscaled[sample][SR]+qcdscaled[SR]).integrate("axis",slice(0,1))


    gapx = region_cuts_tracks[0]#70
    gapy = region_cuts_sphere[0]#50
    highx2 = region_cuts_tracks[0]
    highy2 = region_cuts_sphere[0]
    h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
    abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
    bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
    cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
    dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
    ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
    fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
    gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
    hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
    abinx = abin[0]
    bbinx = bbin[0]
    cbinx = cbin[0]
    dbinx = dbin[0]
    ebinx = ebin[0]
    fbinx = fbin[0]
    gbinx = gbin[0]
    hbinx = hbin[0]
    #SRbinx = SRbin[0]
    abin_err = np.sqrt(abin[1])
    bbin_err = np.sqrt(bbin[1])
    cbin_err = np.sqrt(cbin[1])
    dbin_err = np.sqrt(dbin[1])
    ebin_err = np.sqrt(ebin[1])
    fbin_err = np.sqrt(fbin[1])
    gbin_err = np.sqrt(gbin[1])
    hbin_err = np.sqrt(hbin[1])
    #SRbin_err = SRbin[1]
    A_err  = abin_err/abinx
    B_err  = bbin_err/bbinx
    C_err  = cbin_err/cbinx
    D_err  = dbin_err/dbinx
    E_err  = ebin_err/ebinx
    F_err  = fbin_err/fbinx
    G_err  = gbin_err/gbinx
    H_err  = hbin_err/hbinx
    #SR_err  = np.sqrt(SRbin[1])/SRbinx
    ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2))
    err = ratx*fbinx*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2)
    err1 = (2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2
    #print("(%d,%f)"%(highx2,highy2/100),ratx*fbinx,SRbinx)
    if sample == "Data":
      dobserved = np.array([abinx,bbinx,cbinx,dbinx,ebinx,fbinx,gbinx,hbinx, ratx*fbinx],dtype=float)
      dobserved_err = np.array([ abin_err,bbin_err,cbin_err,dbin_err,ebin_err,fbin_err,gbin_err,hbin_err, err],dtype=float)
    else:
      observed = np.array([abinx,bbinx,cbinx,dbinx,ebinx,fbinx,gbinx,hbinx, ratx*fbinx],dtype=float)
      observed_err = np.array([ abin_err,bbin_err,cbin_err,dbin_err,ebin_err,fbin_err,gbin_err,hbin_err, err],dtype=float)
  points = ["A","B","C","D","E","F","G","H","Predicted SR"]
  ratio = np.divide(dobserved,observed)
  ratio_err = ratio * np.sqrt(np.square(observed_err/observed)+np.square(dobserved_err/dobserved))
  print(ratio)
  print(ratio_err)
  ax.errorbar(range(9),observed,yerr=observed_err,xerr=0.5,color="black",label=labels["QCD"],ls='none',marker=".")
  ax.errorbar(range(9),dobserved,yerr=dobserved_err,xerr=0.5,color="red",label=labels["Data"],ls='none',marker=".")
  ax1.errorbar(range(9),ratio,yerr=ratio_err,color="black",ls='none',marker="+")
  plt.xticks(range(9),points)#, rotation="-45")
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2)
  ax.legend()
  ax.set_yscale("log")
  y1, y2 = ax.get_ylim()
  ax.set_ylim(y1,y2*10)
  ax.set_ylabel("Events")
  ax1.axhline(y=1,color="gray",ls="--")
  fig.savefig("Plots/compareDataRegion_%s_%s_%s.%s"%(SR,zoom,year,ext))
  plt.close()
def make_closure_correction_binnedFull(samples,SR="SR1_suep",cut=0,point=0,gap=0,zoom=0):
  highx1 = inner_tracks#20
  highy1 = inner_sphere#38
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
  var = "nPFCand"
  SR = SR+"_%s"%cut
  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  for sample in samples:#["QCD","sig125","sig200","sig300","sig400","sig700","sig1000"]:
    if sample == "QCD":
       h1 = qcdscaled[SR].integrate("axis",slice(0,1))
    elif sample == "RunA":
       h1 = datascaled[SR].integrate("axis",slice(0,1))
    elif sample == "Data":
       h1 = datafullscaled[SR].integrate("axis",slice(0,1))
    else:
      h1 = (sigscaled[sample][SR]+qcdscaled[SR]).integrate("axis",slice(0,1))


    expected = []
    expected_err = []
    observed = []
    observed_err = []
    ratio = []
    ratio_err = []
    points = []
    gapx = region_cuts_tracks[0]
    gapy = region_cuts_sphere[0]
    for highx2 in [70,80,90,100]: #region_cuts_tracks: #[70,85,90,105]:
      for highy2 in [50,60,70,80,90]: #region_cuts_sphere: #[50,65,80]:
        if gap == 0:
          gapx = highx2
          gapy = highy2
        if gap ==2:
          highy3 = highy2+10
          if highx2!=100:
            highx3 = highx2+10
        h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
        abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
        bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
        cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
        dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
        ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
        fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
        gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
        hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
        SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]

        abinx = abin[0]
        bbinx = bbin[0]
        cbinx = cbin[0]
        dbinx = dbin[0]
        ebinx = ebin[0]
        fbinx = fbin[0]
        gbinx = gbin[0]
        hbinx = hbin[0]
        SRbinx = SRbin[0]
        abin_err = abin[1]
        bbin_err = bbin[1]
        cbin_err = cbin[1]
        dbin_err = dbin[1]
        ebin_err = ebin[1]
        fbin_err = fbin[1]
        gbin_err = gbin[1]
        hbin_err = hbin[1]
        SRbin_err = SRbin[1]
        A_err  = np.sqrt(abin[1])/abinx
        B_err  = np.sqrt(bbin[1])/bbinx
        C_err  = np.sqrt(cbin[1])/cbinx
        D_err  = np.sqrt(dbin[1])/dbinx
        E_err  = np.sqrt(ebin[1])/ebinx
        F_err  = np.sqrt(fbin[1])/fbinx
        G_err  = np.sqrt(gbin[1])/gbinx
        H_err  = np.sqrt(hbin[1])/hbinx
        SR_err  = np.sqrt(SRbin[1])/SRbinx
        ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2))
        err = ratx*fbinx*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2)
        err1 = (2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2
        print("(%d,%f)"%(highx2,highy2/100),ratx*fbinx,SRbinx)
        expected.append(ratx*fbinx)
        expected_err.append(err)
        observed.append(SRbinx)
        observed_err.append(np.sqrt(SRbin_err))
        ratio.append(SRbinx/(ratx*fbinx))
        ratio_err.append((SRbinx/(ratx*fbinx))*np.sqrt(SR_err**2 + err1))
        points.append("(%d,%.2f)"%(highx2,highy2/100))
    if "QCD" in sample:
      ax.fill_between([x-0.5 for x in range(21)],np.append(expected,expected[-1]),color=sigcolors[sample],alpha=0.8,zorder=0,linestyle="-",step="post")
      col = "black"
    else:
      col = sigcolors[sample]
    hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
    ax.step(range(20),expected,color=col,label="%s: expected"%(sample),linestyle="--",where="mid")
    ax.errorbar(range(20),observed,yerr=observed_err,xerr=0.5,color=col,label="%s: observed"%(sample),ls='none',marker=".")
    ax1.errorbar(range(20),ratio,yerr=ratio_err,color=col,ls='none',marker="+")
    plt.xticks(range(20),points, rotation="-45")
  ax.legend()
  ax.set_yscale("log")
  y1, y2 = ax.get_ylim()
  ax.set_ylim(y1,y2*10)
  if zoom:
    ax1.set_ylim(0,10)
    ax.set_ylim(10,2000)
  #else:
  #  ax1.set_ylim(0,50)
  ax.set_ylabel("Events")
  ax1.axhline(y=1,color="gray",ls="--")
  ax1.axvline(x=4.5,color="grey",ls="--")
  ax1.axvline(x=9.5,color="grey",ls="--")
  ax1.axvline(x=14.5,color="grey",ls="--")
  ax.axvline(x=4.5,color="grey",ls="--")
  ax.axvline(x=9.5,color="grey",ls="--")
  ax.axvline(x=14.5,color="grey",ls="--")
  ax1.set_ylabel("Observed/Predicted")
  fig.suptitle("9 Bin Predicted vs Observed by Bin: %s"%labels[sample])
  fig.savefig("Plots/closureBinnedFull_%s_%s_%s_%s_%s.%s"%(sample,SR,gap,zoom,year,ext))
  plt.close()

def make_closure_correction_binned(sample="QCD",SR="SR1_suep",cut=0,point=0,gap=0):
  highx1 = inner_tracks#20
  highy1 = inner_sphere#38
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
  var = "nPFCand"
  SR = SR+"_%s"%cut
  if sample == "QCD":
     h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  elif sample == "RunA":
     h1 = datascaled[SR].integrate("axis",slice(0,1))
  elif sample == "Data":
     h1 = datafullscaled[SR].integrate("axis",slice(0,1))
  else:
    h1 = (sigscaled[sample][SR]+qcdscaled[SR]).integrate("axis",slice(0,1))

  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)

  expected = []
  expected_err = []
  observed = []
  observed_err = []
  ratio = []
  ratio_err = []
  points = []
  gapx = region_cuts_tracks[0]
  gapy = region_cuts_sphere[0]
  for highx2 in region_cuts_tracks:#[70,85,90,105]:
    for highy2 in region_cuts_sphere: #[50,65,80]:
      if gap > 0:
        gapx = highx2
        gapy = highy2
        if gap ==2:
          highy3 = highy2+10
          if highx2!=100:
            highx3 = highx2+10
      h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
      abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()]
      SRbin = h1.integrate("eventBoostedSphericity",slice(highy2/100,highy3/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]

      abinx = abin[0]
      bbinx = bbin[0]
      cbinx = cbin[0]
      dbinx = dbin[0]
      ebinx = ebin[0]
      fbinx = fbin[0]
      gbinx = gbin[0]
      hbinx = hbin[0]
      SRbinx = SRbin[0]
      abin_err = abin[1]
      bbin_err = bbin[1]
      cbin_err = cbin[1]
      dbin_err = dbin[1]
      ebin_err = ebin[1]
      fbin_err = fbin[1]
      gbin_err = gbin[1]
      hbin_err = hbin[1]
      SRbin_err = SRbin[1]
      A_err  = np.sqrt(abin[1])/abinx
      B_err  = np.sqrt(bbin[1])/bbinx
      C_err  = np.sqrt(cbin[1])/cbinx
      D_err  = np.sqrt(dbin[1])/dbinx
      E_err  = np.sqrt(ebin[1])/ebinx
      F_err  = np.sqrt(fbin[1])/fbinx
      G_err  = np.sqrt(gbin[1])/gbinx
      H_err  = np.sqrt(hbin[1])/hbinx
      SR_err  = np.sqrt(SRbin[1])/SRbinx
      ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2))
      err = ratx*fbinx*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2)
      err1 = (2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2
      print("(%d,%f)"%(highx2,highy2/100),ratx*fbinx,SRbinx)
      expected.append(ratx*fbinx)
      expected_err.append(err)
      observed.append(SRbinx)
      observed_err.append(np.sqrt(SRbin_err))
      ratio.append(SRbinx/(ratx*fbinx))
      ratio_err.append((SRbinx/(ratx*fbinx))*np.sqrt(SR_err**2 + err1))
      points.append("(%d,%.2f)"%(highx2,highy2/100))
  ax.errorbar(range(16),expected,yerr=expected_err,xerr=0.5,color="red",label="expected",ls='none')
  ax.errorbar(range(16),observed,yerr=observed_err,xerr=0.5,color="blue",label="observed",ls='none')
  ax1.errorbar(range(16),ratio,yerr=ratio_err,color="black",ls='none',marker="+")
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
  ax.legend()
  plt.xticks(range(16),points, rotation="-45")
  ax.set_yscale("log")
  ax.autoscale(axis='y', tight=True)
  ax1.set_yscale("log")
  ax1.autoscale(axis='y', tight=True)
  if(sample=="QCD"):
    ax1.set_ylim(0.0,2)
  ax.set_ylabel("Events")
  ax1.axhline(y=1,color="gray",ls="--")
  ax1.set_ylabel("Observed/Predicted")
  fig.suptitle("9 Bin Closure: %s"%(labels[sample]))
  fig.savefig("Plots/closureBinned_%s_%s_%s_%s.%s"%(sample,SR,gap,year,ext))
  plt.close()

def make_datacompare(sample,sr,cut,xlab=None,make_ratio=True):
  if cut == 2 or cut == 3:
    highx1 = inner_tracks#22
    highx2 = region_cuts_tracks[0]
    highy1 = inner_sphere#42
    highy2 = region_cuts_sphere[0]#70
  else:
    highx1 = 75
    highx2 = 100
    highy1 = 40
    highy2 = 50
  var = "nPFCand"
  sr = sr+"_%s"%cut
  h1 = qcddatafullscaled[sr].integrate("axis",slice(0,1))
  h2 = datafullscaled[sr].integrate("axis",slice(0,1))
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
  gapx = highx2
  gapy = highy2

  #h1 = h1.rebin(var,hist.bin(var,var,150,0,300))
  abin  = h1.integrate("eventBoostedSphericity",slice(  lowy/100.,  highy1/100.))
  dbin  = h1.integrate("eventBoostedSphericity",slice(highy1/100., highy2/100.))
  gbin  = h1.integrate("eventBoostedSphericity",slice(highy2/100., highy3/100.))
  abin2 = h2.integrate("eventBoostedSphericity",slice(  lowy/100.,  highy1/100.))
  dbin2 = h2.integrate("eventBoostedSphericity",slice(highy1/100., highy2/100.))
  gbin2 = h2.integrate("eventBoostedSphericity",slice(highy2/100., highy3/100.))
  abinx = h2.integrate("eventBoostedSphericity",slice( lowy/100.,  highy1/100.)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()][0]
  bbinx = h2.integrate("eventBoostedSphericity",slice( lowy/100.,  highy1/100.)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()][0]
  cbinx = h2.integrate("eventBoostedSphericity",slice( lowy/100.,  highy1/100.)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()][0]
  dbinx = h2.integrate("eventBoostedSphericity",slice(highy1/100., gapy/100.)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()][0]
  ebinx = h2.integrate("eventBoostedSphericity",slice(highy1/100., gapy/100.)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()][0]
  fbinx = h2.integrate("eventBoostedSphericity",slice(highy1/100., gapy/100.)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()][0]
  gbinx = h2.integrate("eventBoostedSphericity",slice(highy2/100., highy3/100.)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()][0]
  hbinx = h2.integrate("eventBoostedSphericity",slice(highy2/100., highy3/100.)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()][0]
  ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2))
  print(abin.to_hist().to_numpy())
  print(dbin.to_hist().to_numpy())
  print(gbin.to_hist().to_numpy())
  b1= abin.to_hist().to_numpy()
  b2= dbin.to_hist().to_numpy()
  b3= gbin.to_hist().to_numpy()
  d1= abin2.to_hist().to_numpy()
  d2= dbin2.to_hist().to_numpy()
  d3= gbin2.to_hist().to_numpy()
  for i,(b,d) in enumerate(zip([b1,b2,b3],[d1,d2,d3])):
    fig, (ax, ax1) = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(7,7),
        gridspec_kw={"height_ratios": (3, 1)},
        sharex=True
    )
    fig.subplots_adjust(hspace=.07)
    if i==2:
      ax.step(xbins(b[1]),b[0],color="blue",linestyle="--",where="mid",zorder=2,label=labels["QCD"])
      ax.step(xbins(d[1])[:highx2],d[0][:highx2],color="red",linestyle="--",where="mid",zorder=2,label=labels["Data"])
      ax1.scatter(xbins(b[1])[:highx2],d[0][:highx2]/b[0][:highx2],marker=".")
      ax.step(xbins(d2[1][highx2:]),d2[0][highx2:]*ratx,color="green",linestyle="--",where="mid",zorder=2,label="Predicted DATA")
      ax1.scatter(xbins(b[1][highx2:]),ratx*d2[0][highx2:]/b[0][highx2:],marker=".",color="green")
    else:
      ax.step(xbins(b[1]),b[0],color="blue",linestyle="--",where="mid",zorder=2,label=labels["QCD"])
      ax.step(xbins(d[1]),d[0],color="red",linestyle="--",where="mid",zorder=2,label=labels["Data"])
      ax1.scatter(xbins(b[1]),d[0]/b[0],marker=".")
    ax.axvline(x=highx1,color="green",ls="--")
    hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
    ax.axvline(x=highx2,color="magenta",ls="--")
    ax1.axvline(x=highx1,color="green",ls="--")
    ax1.axvline(x=highx2,color="magenta",ls="--")
    ax.autoscale(axis='y', tight=True)
    ax.set_yscale("log")
    ax.legend(loc="right")
    ax.set_xlim([0,125])
    ax1.set_ylim([0.5,1.5])
    ax1.axhline(y=1,color="grey",ls="--")
    ax1.set_ylabel("Data/MC")
    ax.set_ylabel("Events")
    ax1.set_xlabel(xlab)
    if i ==0:
      ax1.text(0,1,"A",fontsize = 18)
      ax1.text(30,1,"B",fontsize = 18)
      ax1.text(60,1,"C",fontsize = 18)
    elif i ==1:
      ax1.text(0,1,"D",fontsize = 18)
      ax1.text(30,1,"E",fontsize = 18)
      ax1.text(60,1,"F",fontsize = 18)
    else:
      ax1.text(0,1,"G",fontsize = 18)
      ax1.text(30,1,"H",fontsize = 18)
      ax1.text(60,1,"I(SR)",fontsize = 18)
    fig.savefig("Plots/controlbins_dist_%s_cut%s_%s_%s.%s"%(var,cut,i,year,ext))
    plt.close()

def make_datacompare2(sample,sr,cut,xlab=None,make_ratio=True):
  if cut == 2 or cut == 3:
    highx1 = inner_tracks#22
    highx2 = region_cuts_tracks[0]
    highy1 = inner_sphere#42
    highy2 = region_cuts_sphere[0]#70
  else:
    highx1 = 75
    highx2 = 100
    highy1 = 40
    highy2 = 50
  var = "nPFCand"
  sr = sr+"_%s"%cut
  h1 = qcddatafullscaled[sr].integrate("axis",slice(0,1))
  h2 = datafullscaled[sr].integrate("axis",slice(0,1))
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100
  gapx = highx2
  gapy = highy2

  abin  = h1.integrate("nPFCand",slice( lowx,  highx1))
  bbin  = h1.integrate("nPFCand",slice(highx1, highx2))
  cbin  = h1.integrate("nPFCand",slice(highx2, highx3))
  abin2 = h2.integrate("nPFCand",slice( lowx,  highx1))
  bbin2 = h2.integrate("nPFCand",slice(highx1, highx2))
  cbin2 = h2.integrate("nPFCand",slice(highx2, highx3))
  abinx = h2.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()][0]
  dbinx = h2.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()][0]
  gbinx = h2.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()][0]
  bbinx = h2.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()][0]
  ebinx = h2.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()][0]
  hbinx = h2.integrate("eventBoostedSphericity",slice(highy1/100, gapy/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()][0]
  cbinx = h2.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()][0]
  fbinx = h2.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,gapx)).sum().values(sumw2=True)[()][0]
  ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2))

  b1= abin.to_hist().to_numpy()
  b2= bbin.to_hist().to_numpy()
  b3= cbin.to_hist().to_numpy()
  d1= abin2.to_hist().to_numpy()
  d2= bbin2.to_hist().to_numpy()
  d3= cbin2.to_hist().to_numpy()
  for i,(b,d) in enumerate(zip([b1,b2,b3],[d1,d2,d3])):
    fig, (ax, ax1) = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(7,7),
        gridspec_kw={"height_ratios": (3, 1)},
        sharex=True
    )
    fig.subplots_adjust(hspace=.07)
    if i==2:
      ax.step(xbins(b[1]),b[0],color="blue",linestyle="--",where="mid",zorder=2,label=labels["QCD"])
      ax.step(xbins(d[1])[:highy2],d[0][:highy2],color="red",linestyle="--",where="mid",zorder=2,label=labels["Data"])
      ax1.scatter(xbins(b[1])[:highy2],d[0][:highy2]/b[0][:highy2],marker=".")
      ax.step(xbins(d2[1][highy2:]),d2[0][highy2:]*ratx,color="green",linestyle="--",where="mid",zorder=2,label="Predicted DATA")
      ax1.scatter(xbins(b[1][highy2:]),ratx*d2[0][highy2:]/b[0][highy2:],marker=".",color="green")
    else:
      ax.step(xbins(b[1]),b[0],color="blue",linestyle="--",where="mid",zorder=2,label=labels["QCD"])
      ax.step(xbins(d[1]),d[0],color="red",linestyle="--",where="mid",zorder=2,label=labels["Data"])
      ax1.scatter(xbins(b[1]),d[0]/b[0],marker=".")
    ax.axvline(x=lowy/100.,color="grey",ls="--")
    hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2,ax=ax)
    ax.axvline(x=highy1/100.,color="green",ls="--")
    ax.axvline(x=highy2/100.,color="magenta",ls="--")
    ax1.axvline(x=lowy/100.,color="grey",ls="--")
    ax1.axvline(x=highy1/100.,color="green",ls="--")
    ax1.axvline(x=highy2/100.,color="magenta",ls="--")
    ax.autoscale(axis='y', tight=True)
    ax.set_yscale("log")
    ax.legend(loc="right")
    ax.set_xlim([0,1])
    ax1.set_ylim([0.5,1.5])
    ax1.axhline(y=1,color="grey",ls="--")
    ax1.set_ylabel("Data/MC")
    ax.set_ylabel("Events")
    ax1.set_xlabel(xlab)
    if i ==0:
      ax1.text(0.0 ,1,"Excluded",fontsize = 18)
      ax1.text(0.3,1,"A",fontsize = 18)
      ax1.text(0.36,1,"D",fontsize = 18)
      ax1.text(0.62,1,"G",fontsize = 18)
    elif i ==1:
      ax1.text(0.0 ,1,"Excluded",fontsize = 18)
      ax1.text(0.3,1,"B",fontsize = 18)
      ax1.text(0.36,1,"E",fontsize = 18)
      ax1.text(0.62,1,"H",fontsize = 18)
    else:
      ax1.text(0.0 ,1,"Excluded",fontsize = 18)
      ax1.text(0.3,1,"C",fontsize = 18)
      ax1.text(0.36,1,"F",fontsize = 18)
      ax1.text(0.62,1,"I(SR)",fontsize = 18)
    fig.savefig("Plots/controlbins2_dist_%s_cut%s_%s_%s.%s"%(var,cut,i,year,ext))
    plt.close()
