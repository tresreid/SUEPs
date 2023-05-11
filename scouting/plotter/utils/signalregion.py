from utils.utils import *

def makeSR(sample,var,cut,lines=0,SR=0):
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

      name = var+"_%s"%cut
      print(name)
      xvar = "nPFCand"
      scaled = sigscaled[sample]
      s = scaled[name].to_hist().to_numpy()
      b = qcdscaled[name].to_hist().to_numpy()
      print(s)
      fig, ax1 = plt.subplots()

      hx = hist.plot2d(
          scaled[name].integrate("axis",slice(0,1)),
          xvar,
          ax=ax1,
      )
      hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2)
      fig.suptitle("SR: %s"%sample)
      fig.savefig("Plots/%s_sig_%s_%s_%s.%s"%(var,sample,cut,year,ext))
      plt.close()

      fig, ax1 = plt.subplots()

      hx = hist.plot2d(
          qcdscaled[name].integrate("axis",slice(0,1)),
          xvar,
          ax=ax1,
      )
      fig.suptitle("SR: %s"%labels["QCD"])
      hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2)
      fig.savefig("Plots/%s_bkg_%s_%s.%s"%(var,cut,year,ext))
      plt.close()

      fig, ax1 = plt.subplots()

      h0 = hist.plot2d(
          scaled[name].integrate("axis",slice(0,1)),
          xvar,
          ax=ax1,
          patch_opts={'cmap': 'blues_alpha',"vmin":0,"vmax":10}
          #patch_opts={'cmap': 'blues_alpha',"vmin":0,"vmax":150}
      )
      h1 = hist.plot2d(
          qcdscaled[name].integrate("axis",slice(0,1)),
          xvar,
          ax=ax1,
          patch_opts={'cmap': 'reds_alpha',"vmin":0,"vmax":2000}
          #patch_opts={'cmap': 'reds_alpha',"vmin":0,"vmax":80000}
      )
      h2 = hist.plot2d(
          scaled[name].integrate("axis",slice(0,1)),
          xvar,
          ax=ax1,
          clear=False,
          patch_opts={'cmap': "blues_alpha","vmin":0,"vmax":10}
          #patch_opts={'cmap': "blues_alpha","vmin":0,"vmax":150}
      )
      xline = region_cuts_tracks[SR]
      yline = region_cuts_sphere[SR]/100. #0.5
      if lines==4:
        ax1.axhline(y=0.3,color="grey",ls="--")
        ax1.axhspan(0,0.3, hatch="/", color="grey",alpha=0.3)
        ax1.axvline(x=xline,color="red",ls="--")
        ax1.axhline(y=yline,color="red",ls="--")
        ax1.text(20,0.3,"A",fontsize = 22)
        ax1.text(20,0.8,"B",fontsize = 22)
        ax1.text(100,0.3,"C",fontsize = 22)
        ax1.text(100,0.8,"SR",fontsize = 22)
        ax1.text(20,0.15,"EXCLUDED",fontsize = 22)
      if lines==6:
        ax1.axhline(y=0.3,color="grey",ls="--")
        ax1.axhspan(0,0.3, hatch="/", color="grey",alpha=0.3)
        ax1.axvline(x=xline,color="red",ls="--")
        ax1.axhline(y=yline,color="red",ls="--")
        ax1.axvline(x=inner_tracks,color="blue",ls="--")
        ax1.text(0,0.3,"A",fontsize = 18)
        ax1.text(0,0.8,"D",fontsize = 18)
        ax1.text(30,0.3,"B",fontsize = 18)
        ax1.text(30,0.8,"E",fontsize = 18)
        ax1.text(100,0.3,"C",fontsize = 18)
        ax1.text(100,0.8,"SR",fontsize = 18)
        ax1.text(20,0.15,"EXCLUDED",fontsize = 22)
      if lines==9:
        ax1.axhline(y=0.3,color="grey",ls="--")
        ax1.axhspan(0,0.3, hatch="/", color="grey",alpha=0.3)
        ax1.axvline(x=inner_tracks,color="blue",ls="--")
        ax1.axhline(y=inner_sphere/100.,color="blue",ls="--")
        ax1.axvline(x=xline,color="red",ls="--")
        ax1.axhline(y=yline,color="red",ls="--")
        ax1.text(0,0.3,"A",fontsize = 14)
        ax1.text(0,0.34,"D",fontsize = 14)
        ax1.text(0,0.8,"G",fontsize = 14)
        ax1.text(30,0.3,"B",fontsize = 14)
        ax1.text(30,0.34,"E",fontsize = 14)
        ax1.text(30,0.8,"H",fontsize = 14)
        ax1.text(100,0.3,"C",fontsize = 14)
        ax1.text(100,0.34,"F",fontsize = 14)
        ax1.text(100,0.8,"SR",fontsize = 14)
        ax1.text(20,0.15,"EXCLUDED",fontsize = 22)
      #fig.suptitle("SR: TTBar + %s"%sample)
      fig.suptitle("SR: QCD + %s"%sample)
      ax1.set_xlabel("SUEP Jet Track Multiplicity")
      ax1.set_ylabel("Boosted Sphericity")
      hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2)
      fig.savefig("Plots/SR_%s_%s_bkg_%s_%s_%s.%s"%(sample,var,cut,lines,year,ext))
      plt.close()

def makeSRSignif(sample,var,cut,xline=None,yline=None):
      name = var+"_%s"%cut
      print(name)
      xvar = "SUEP Jet Track Multiplicity"
      scaled = sigscaled[sample]
      s = scaled[name].to_hist().to_numpy()
      b = qcdscaled[name].to_hist().to_numpy()
      sb = b[0][0]
      sig, sigbkg = get_sig2d(s[0][0],sb,xbins(s[2]),xbins(s[3]))
      signif = sig/ np.sqrt(np.add(np.add(sig,sigbkg),np.square(sigbkg)))
      signif = np.nan_to_num(signif)
      maxi = np.max(signif)
      maxindex = unravel_index(np.argmax(signif),signif.shape)
      maxes = heapq.nlargest(5,range(len(signif.flatten())),signif.flatten().take)
      for m in maxes:
        u = unravel_index(m,signif.shape)

      fig, ax = plt.subplots()
      shw = ax.imshow(np.transpose(signif), interpolation='none',origin="lower",cmap="gist_ncar")
      ax.set_xticks([0,50,100,150,200,250,300])
      ax.set_xticklabels([0,50,100,150,200,250,300])
      ax.set_yticks([0,20,40,60,80,100])
      ax.set_yticklabels([0,.20,.40,.60,.80,1])
      bar = plt.colorbar(shw)
      bar.set_label("Significance")
      ax.set_xlabel(xvar)
      if( xline is not None):
        ax.axvline(x=xline,color="grey")
      if( yline is not None):
        ax.axhline(y=yline,color="grey")
      ax.set_ylabel("Boosted Sphericity")
      ax.text(maxindex[0],maxindex[1],"X=%.2f(%d,%.2f)"%(maxi,maxindex[0],maxindex[1]/100))
      ax.set_aspect("auto")
      fig.suptitle("Significance: %s"%sample)
      hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2)
      fig.savefig("Plots/signif2d_%s_%s_%s_%s.%s"%(sample,var,cut,year,ext))
      plt.close()

def makeSRSignig9(sample="QCD",SR="SR1_suep",cut=3):
  if cut == 2 or cut == 3:
    highx2 = region_cuts_tracks[0]
    highy2 = region_cuts_sphere[0]
  else:
    highx2 = 100
    highy2 = 70
  var = "nPFCand"
  SR = SR+"_%s"%cut
  if sample == "QCD":
     h1 = qcdscaled[SR].integrate("axis",slice(0,1))
  else:
    h1 = (scaled[SR]+qcdscaled[SR]).integrate("axis",slice(0,1))
  lowx =0
  lowy = 30
  highx3 = 300
  highy3 = 100

  fig, (ax, ax1) = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7,7),
      gridspec_kw={"height_ratios": (3, 1)},
      sharex=True
  )
  fig.subplots_adjust(hspace=.07)
  h1 = h1.rebin(var,hist.Bin(var,var,150,0,300))
  signif=[]
  for highx1 in range(0,highx2,2):
    signif1=[]
    for highy1 in range(30,highy2,4):
      abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
      cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
      fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
      gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
      hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
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
      A_err  = np.sqrt(abin[1])/abinx
      B_err  = np.sqrt(bbin[1])/bbinx
      C_err  = np.sqrt(cbin[1])/cbinx
      D_err  = np.sqrt(dbin[1])/dbinx
      E_err  = np.sqrt(ebin[1])/ebinx
      F_err  = np.sqrt(fbin[1])/fbinx
      G_err  = np.sqrt(gbin[1])/gbinx
      H_err  = np.sqrt(hbin[1])/hbinx
      SRbin_err = np.sqrt(SRbin[1])
      ratx = (gbinx*cbinx/abinx)*((hbinx/ebinx)**4)*(fbinx**3)/(((gbinx*fbinx/dbinx)**2)*((hbinx*cbinx/bbinx)**2))

      error = 100*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2)
      signif1.append(error)
    signif.append(signif1)
  signif = np.array(signif)
  mini = np.nanmin(signif)
  minindex = unravel_index(np.nanargmin(signif),signif.shape)
  fig, ax = plt.subplots()
  shw = ax.imshow(np.transpose(signif), interpolation='none',origin="lower",cmap="gist_ncar")
  ax.set_xticks(range(0,35,5))
  ax.set_xticklabels([x*2 for x in range(0,35,5)])
  ax.set_yticks(range(0,10,2))
  ax.set_yticklabels([x*4+30 for x in range(0,10,2)])
  bar = plt.colorbar(shw)
  bar.set_label("Statistical Uncertainty (%)")
  ax.set_xlabel("SUEP Jet Track Multiplicity")
  ax.set_ylabel("Boosted Sphericity")
  ax.text(minindex[0],minindex[1],"X=%.2f(%d,%.2f)"%(mini,minindex[0]*2,(minindex[1]*4+30)/100))

  highx1 = minindex[0]*2
  highy1 = (minindex[1]*4+30)
  abin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  bbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  cbin = h1.integrate("eventBoostedSphericity",slice( lowy/100,  highy1/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  dbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  ebin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
  fbin = h1.integrate("eventBoostedSphericity",slice(highy1/100, highy2/100)).integrate(  var,slice(highx2,highx3)).sum().values(sumw2=True)[()]
  gbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(lowx,highx1  )).sum().values(sumw2=True)[()]
  hbin = h1.integrate("eventBoostedSphericity",slice(highy2/100, highy3/100)).integrate(  var,slice(highx1,highx2)).sum().values(sumw2=True)[()]
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
  A_err  = np.sqrt(abin[1])/abinx
  B_err  = np.sqrt(bbin[1])/bbinx
  C_err  = np.sqrt(cbin[1])/cbinx
  D_err  = np.sqrt(dbin[1])/dbinx
  E_err  = np.sqrt(ebin[1])/ebinx
  F_err  = np.sqrt(fbin[1])/fbinx
  G_err  = np.sqrt(gbin[1])/gbinx
  H_err  = np.sqrt(hbin[1])/hbinx
  print("A: ",(1*A_err)**2)
  print("B: ",(2*B_err)**2)
  print("C: ",(1*C_err)**2)
  print("D: ",(2*D_err)**2)
  print("E: ",(4*E_err)**2)
  print("F: ",(2*F_err)**2)
  print("G: ",(1*G_err)**2)
  print("H: ",(2*H_err)**2)
  print("total: ",100*np.sqrt((2*H_err)**2 +(2*D_err)**2 +(2*B_err)**2 +(2*F_err)**2 +(G_err)**2 +(C_err)**2 +(A_err)**2 + (4*E_err)**2))

  ax.set_aspect("auto")
  fig.suptitle("Significance: %s"%sample)
  hep.cms.label('',data=False,lumi=lumi/1000,year=year,loc=2)
  fig.savefig("Plots/closureerr9_%s_%s_%s_%s.%s"%(sample,var,cut,year,ext))
  plt.close()
