import awkward as ak
from coffea import hist, processor, nanoevents
import uproot
from coffea.nanoevents import NanoEventsFactory, BaseSchema
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import uproot
import pickle
import time
from distributed import Client
#from lpcjobqueue import LPCCondorCluster
import sys
import vector
from math import pi
import dask
import fastjet

# register our candidate behaviors
from coffea.nanoevents.methods import candidate
ak.behavior.update(candidate.behavior)

eventDisplay_knob= False
redoISRRM = True
def get_dr_ring(dr, phi_c=0, eta_c=0, n_points=600):
    deta = np.linspace(-dr, +dr, n_points)
    dphi = np.sqrt(dr**2 - np.square(deta))
    deta = eta_c+np.concatenate((deta, deta[::-1]))
    dphi = phi_c+np.concatenate((dphi, -dphi[::-1]))
    return dphi, deta

def plot_display(ievt,particles,bparticles,suepjet,isrjet,bisrjet,sphericity,nbtracks):
    fig = plt.figure(figsize=(8,8))
    ax = plt.gca()

    ax.set_xlim(-pi,pi)
    ax.set_ylim(-2.5,2.5)
    ax.set_xlabel(r'$\phi$', fontsize=18)
    ax.set_ylabel(r'$\eta$', fontsize=18)
    ax.tick_params(axis='both', which='major', labelsize=12)
#    print(particles)

    ax.scatter(particles.phi, particles.eta, s=particles.pt, c='xkcd:blue', marker='o',label="ID tracks: %d"%len(particles))

    phi_s, eta_s = get_dr_ring(1.5,suepjet.phi, suepjet.eta)
    phi_s = phi_s[1:]
    eta_s = eta_s[1:]
    ax.plot(phi_s[phi_s> pi] - 2*pi, eta_s[phi_s>pi], color='xkcd:green',linestyle='--')
    ax.plot(phi_s[phi_s< -pi] + 2*pi, eta_s[phi_s<-pi], color='xkcd:green',linestyle='--')
    ax.plot(phi_s[phi_s< pi], eta_s[phi_s<pi], color='xkcd:green',linestyle='--',label="SUEP Jet")
    phi_i, eta_i = get_dr_ring(1.5,isrjet.phi, isrjet.eta)
    phi_i = phi_i[1:]
    eta_i = eta_i[1:]
    ax.plot(phi_i[phi_i> pi] - 2*pi, eta_i[phi_i>pi], color='xkcd:red',linestyle='--')
    ax.plot(phi_i[phi_i< -pi] + 2*pi, eta_i[phi_i<-pi], color='xkcd:red',linestyle='--')
    ax.plot(phi_i[phi_i< pi], eta_i[phi_i<pi], color='xkcd:red',linestyle='--',label="ISR Jet")

    plt.legend(title='Event (after selection): %d\n boosted Sphericity: %.2f'%(ievt,sphericity))
    hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)

    fig.savefig("Displays/nonboosted_%s"%ievt)
    plt.close()


    fig = plt.figure(figsize=(8,8))
    ax = plt.gca()

    ax.set_xlim(-pi,pi)
    ax.set_ylim(-2.5,2.5)
    ax.set_xlabel(r'$\phi$', fontsize=18)
    ax.set_ylabel(r'$\eta$', fontsize=18)
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.scatter(bparticles.phi, bparticles.eta, s=bparticles.pt, c='xkcd:magenta', marker='o',label="Boosted tracks:%s"%nbtracks)
    phi_ib, eta_ib = get_dr_ring(1.5,bisrjet.phi, bisrjet.eta)
    phi_ib = phi_ib[1:]
    eta_ib = eta_ib[1:]
    ax.plot(phi_ib[phi_ib> pi] - 2*pi, eta_ib[phi_ib>pi], color='xkcd:orange',linestyle='--')
    ax.plot(phi_ib[phi_ib< -pi] + 2*pi, eta_ib[phi_ib<-pi], color='xkcd:orange',linestyle='--')
    ax.plot(phi_ib[phi_ib< pi], eta_ib[phi_ib<pi], color='xkcd:orange',linestyle='--',label="Boosted ISR Jet")

    topline = bisrjet.phi+1.6
    botline = bisrjet.phi-1.6
    if topline > pi:
      topline = topline - 2*pi
    if botline < -pi:
      botline = botline + 2*pi
    ax.axvline(x=topline)
    ax.axvline(x=botline)

    plt.legend(title='Event (after selection): %d\n boosted Sphericity: %.2f'%(ievt,sphericity))
    hep.cms.label('',data=False,lumi=59.74,year=2018,loc=2)

    fig.savefig("Displays/boosted_%s"%ievt)
    plt.close()
    


def sphericity(self, particles, r):
    norm = ak.sum(particles.p ** r, axis=1, keepdims=True)
    #if norm ==0:
    #  return [-1,-1,-1]
    #s1 = [[
    s = np.array([[
                   ak.sum(particles.px * particles.px * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,
                   ak.sum(particles.px * particles.py * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,
                   ak.sum(particles.px * particles.pz * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm
                  ],
                  [
                   ak.sum(particles.py * particles.px * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,
                   ak.sum(particles.py * particles.py * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,
                   ak.sum(particles.py * particles.pz * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm
                  ],
                  [
                   ak.sum(particles.pz * particles.px * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,
                   ak.sum(particles.pz * particles.py * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,
                   ak.sum(particles.pz * particles.pz * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm
                   #ak.to_numpy(ak.sum(particles.px * particles.px * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,allow_missing=True),
                   #ak.to_numpy(ak.sum(particles.px * particles.py * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,allow_missing=True),
                   #ak.to_numpy(ak.sum(particles.px * particles.pz * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,allow_missing=True)
                  #]#,
                  #[#
                   #ak.to_numpy(ak.sum(particles.py * particles.px * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,allow_missing=True),
                   #ak.to_numpy(ak.sum(particles.py * particles.py * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,allow_missing=True),
                   #ak.to_numpy(ak.sum(particles.py * particles.pz * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,allow_missing=True)
                  #]#,
                  #[#
                   #ak.to_numpy(ak.sum(particles.pz * particles.px * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,allow_missing=True),
                   #ak.to_numpy(ak.sum(particles.pz * particles.py * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,allow_missing=True),
                   #ak.to_numpy(ak.sum(particles.pz * particles.pz * particles.p ** (r-2.0), axis=1 ,keepdims=True)/norm,allow_missing=True)
                  ]])
    #s = np.array(s1)
    #s = ak.to_numpy(s1,allow_missing=True)
    s = np.squeeze(np.moveaxis(s, 2, 0),axis=3)
    #np.nan_to_num(s)
    #for p1,n1,s1 in zip(particles,norm,s):
    #  print(n1)
    #  print(len(p1))
    #  print(p1[0])
    #  print(p1[1])
    #  print(p1[0].p)
    #  print(p1[1].p)
    #  print(p1[0].p**(-1))
    #  print(p1[1].p**(-1))
    #  print(s1)
    #  evals = np.sort(np.linalg.eigvalsh(s1))
    evals = np.sort(np.linalg.eigvalsh(s))
    return evals

def packtrig(output,vals,var):
        output["trigdist_%s"%(var)].fill(cut="Cut 0:No cut", v1=vals[0][var])
        output["trigdist_%s"%(var)].fill(cut="Mu Trig noRef", v1=vals[1][var]) 
        output["trigdist_%s"%(var)].fill(cut="HT Trig noRef", v1=vals[2][var]) 
        output["trigdist_%s"%(var)].fill(cut="HT Trig MuRef", v1=vals[3][var]) 
        return output
def packsingledist(output,vals,var):
        output["dist_%s"%(var)].fill(cut="cut 0:No cut", v1=vals[var])
        return output
def packdist(output,vals,var):
        output["dist_%s"%(var)].fill(cut="cut 0:No cut", v1=vals[0][var])
        output["dist_%s"%(var)].fill(cut="cut 1:HT Trig", v1=vals[1][var]) 
        output["dist_%s"%(var)].fill(cut="cut 2:Ht>=600", v1=vals[2][var])
        output["dist_%s"%(var)].fill(cut="cut 3:fj>=2", v1=vals[3][var])
        if("PFcand_n" in var):
          output["dist_%s"%(var)].fill(cut="cut 4:eventBoosted Sphericity >=0.6", v1=vals[4][var])
        else:
          output["dist_%s"%(var)].fill(cut="cut 4:nPFCand75>=140", v1=vals[4][var]) 
        if(len(vals)>=6):
          output["dist_%s"%(var)].fill(cut="cut 3:Pre + nPVs < 30", v1=vals[5][var]) 
          output["dist_%s"%(var)].fill(cut="cut 4:Pre + nPVs >=30", v1=vals[6][var]) 
      
        #output["dist_%s"%(var)].fill(cut="cut 4:FJ nPFCand>=80", v1=vals[4][var]) 
        return output
def packtrkFKID(output,vals,var,var2,prefix=""):
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 0:Preselection",          v1=ak.flatten(vals[0][var]), v2=ak.flatten(vals[0][var2]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 1: |eta| < 2.4",          v1=ak.flatten(vals[1][var]), v2=ak.flatten(vals[1][var2]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 2: q != 0",               v1=ak.flatten(vals[2][var]), v2=ak.flatten(vals[2][var2]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 3: PV = 0",               v1=ak.flatten(vals[3][var]), v2=ak.flatten(vals[3][var2]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 4: PFcand_pt > 0.5",      v1=ak.flatten(vals[4][var]), v2=ak.flatten(vals[4][var2]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 5: PFcand_pt > 0.6",      v1=ak.flatten(vals[5][var]), v2=ak.flatten(vals[5][var2]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 6: PFcand_pt > 0.7",      v1=ak.flatten(vals[6][var]), v2=ak.flatten(vals[6][var2]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 7: PFcand_pt > 0.75",     v1=ak.flatten(vals[7][var]), v2=ak.flatten(vals[7][var2]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 8: PFcand_pt > 0.8",      v1=ak.flatten(vals[8][var]), v2=ak.flatten(vals[8][var2]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 9: PFcand_pt > 0.9",      v1=ak.flatten(vals[9][var]), v2=ak.flatten(vals[9][var2]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 10: PFcand_pt > 1.0",     v1=ak.flatten(vals[10][var]), v2=ak.flatten(vals[10][var2]))
        return output
def packtrkID(output,vals,var,var2,prefix=""):
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 0:Preselection",           v1=ak.flatten(vals[0][var]), v2=ak.flatten(vals[0][var2]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 1: PFcand_pt > 0.5",       v1=ak.flatten(vals[1][var]), v2=ak.flatten(vals[1][var2]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 2: PFcand_pt > 0.6",       v1=ak.flatten(vals[2][var]), v2=ak.flatten(vals[2][var2]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 3: PFcand_pt > 0.7",       v1=ak.flatten(vals[3][var]), v2=ak.flatten(vals[3][var2]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 4: PFcand_pt > 0.75",      v1=ak.flatten(vals[4][var]), v2=ak.flatten(vals[4][var2]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 5: PFcand_pt > 0.8",       v1=ak.flatten(vals[5][var]), v2=ak.flatten(vals[5][var2]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 6: PFcand_pt > 0.9",       v1=ak.flatten(vals[6][var]), v2=ak.flatten(vals[6][var2]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 7: PFcand_pt > 1.0",       v1=ak.flatten(vals[7][var]), v2=ak.flatten(vals[7][var2]))
        return output
def packdistflat(output,vals,var,prefix=""):
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 0:No cut",       v1=ak.flatten(vals[0][var]))
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 1:HT Trig",      v1=ak.flatten(vals[1][var])) 
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 2:Ht>=600",      v1=ak.flatten(vals[2][var]))
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 3:fj>=2",        v1=ak.flatten(vals[3][var]))
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 4:nPFCand75>=140", v1=ak.flatten(vals[4][var])) 
        if(len(vals)>=6):
          output["dist_%s%s"%(prefix,var)].fill(cut="cut 3:Pre + nPVs < 30", v1=ak.flatten(vals[5][var])) 
          output["dist_%s%s"%(prefix,var)].fill(cut="cut 4:Pre + nPVs >=30", v1=ak.flatten(vals[6][var]))
        #output["dist_%s"%(var)].fill(cut="cut 4:FJ nPFCand>=80", v1=ak.flatten(vals[4][var])) 
        return output
def packdist_fjn1(output,vals,var):
        output["dist_fjn1_%s"%(var)].fill(cut="cut 0:No cut",       v1=vals[0][var])
        output["dist_fjn1_%s"%(var)].fill(cut="cut 1:HT Trig",      v1=vals[1][var]) 
        output["dist_fjn1_%s"%(var)].fill(cut="cut 2:Ht>=600",      v1=vals[2][var])
        output["dist_fjn1_%s"%(var)].fill(cut="cut 3:nPFCand75>=140", v1=vals[3][var]) 
        #output["dist_fjn1_%s"%(var)].fill(cut="cut 3:FJ nPFCand>=80", v1=vals[3][var]) 
        output["dist_fjn1_%s"%(var)].fill(cut="cut 4:BSphericity >=0.6",        v1=vals[4][var])
        return output
def packSR(output,vals,var):
        output["SR1_%s_0"%var].fill(axis="axis",       nPFCand=vals[3]["PFcand_ncount75"],eventBoostedSphericity=vals[3]["sphere_%s"%var])
        output["SR1_%s_1"%var].fill(axis="axis",       nPFCand=vals[3]["PFcand_ncount75"],eventBoostedSphericity=vals[3]["sphere1_%s"%var])
        output["SR1_%s_2"%var].fill(axis="axis",       nPFCand=vals[3]["FatJet_nconst0"],eventBoostedSphericity=vals[3]["sphere_%s"%var])
        output["SR1_%s_3"%var].fill(axis="axis",       nPFCand=vals[3]["FatJet_nconst0"],eventBoostedSphericity=vals[3]["sphere1_%s"%var])
        return output
def pack2D(output,vals,var1,var2):
        output["2d_%s_%s"%(var1,var2)].fill(cut="cut 0: No cut",       v1=vals[0][var1],v2=vals[0][var2])
        output["2d_%s_%s"%(var1,var2)].fill(cut="cut 1: No cut",       v1=vals[1][var1],v2=vals[1][var2])
        output["2d_%s_%s"%(var1,var2)].fill(cut="cut 2: No cut",       v1=vals[2][var1],v2=vals[2][var2])
        output["2d_%s_%s"%(var1,var2)].fill(cut="cut 3: No cut",       v1=vals[3][var1],v2=vals[3][var2])
        output["2d_%s_%s"%(var1,var2)].fill(cut="cut 4: No cut",       v1=vals[4][var1],v2=vals[4][var2])
        return output
pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50])
eta_bins = np.array(range(-250,250,25))/100.
phi_bins = np.array(range(-31,31,5))/10.
class MyProcessor(processor.ProcessorABC):
    def __init__(self):
        self._accumulator = processor.dict_accumulator({
            "sumw": processor.defaultdict_accumulator(float),
            "SR1_isr_0" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_suep_0" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_16_0" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_10_0" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_8_0" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_4_0" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_isr_1" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_suep_1" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_16_1" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_10_1" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_8_1" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_4_1" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_isr_2" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_suep_2" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_16_2" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_10_2" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_8_2" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_4_2" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_isr_3" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_suep_3" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_16_3" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_10_3" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_8_3" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_4_3" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            #"SR2" : hist.Hist(
            #          "Events",
            #          hist.Cat("axis","Axis"),
            #          hist.Bin("FatJet_nconst","FatJet_nconst",300,0,300),
            #          hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            #),
            #"SR3" : hist.Hist(
            #          "Events",
            #          hist.Cat("axis","Axis"),
            #          hist.Bin("nPFCand","nPFCand",300,0,300),
            #          hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            #),
            "trigdist_ht": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ht",100,0,1500)
            ),
            "trigdist_n_pfMu": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","n_pfMu",15,0,15)
            ),
            "dist_ht": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Ht",350,0,3500)
            ),
            #"dist_sphere1": hist.Hist(
            #          "Events",
            #          hist.Cat("cut","Cutflow"),
            #          hist.Bin("v1","Sphere1",50,0,1)
            #),
            "dist_sphere_16": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphereb_16",50,0,1)
            ),
            "dist_sphere1_16": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphere1b_16",50,0,1)
            ),
            "dist_sphere_10": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphereb_10",50,0,1)
            ),
            "dist_sphere1_10": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphere1b_10",50,0,1)
            ),
            "dist_sphere_8": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphereb_8",50,0,1)
            ),
            "dist_sphere1_8": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphere1b_8",50,0,1)
            ),
            "dist_sphere_4": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphereb_4",50,0,1)
            ),
            "dist_sphere1_4": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphere1b_4",50,0,1)
            ),
            "dist_sphere_suep": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphere_suep",50,0,1)
            ),
            "dist_sphere1_suep": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphere1_suep",50,0,1)
            ),
            "dist_sphere_isr": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphere_isr",50,0,1)
            ),
            "dist_sphere1_isr": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphere1_isr",50,0,1)
            ),
            "dist_event_sphericity": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphericity",50,0,1)
            ),
            "dist_eventBoosted_sphericity": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Boosted Sphericity",50,0,1)
            ),
            "dist_n_pvs": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPVs",100,0,100)
            ),
            "dist_nPVs_good0": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPVs",100,0,100)
            ),
            "dist_nPVs_good1": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPVs",100,0,100)
            ),
            "dist_nPVs_good2": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPVs",100,0,100)
            ),
            "dist_nPVs_good3": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPVs",100,0,100)
            ),
            "dist_nPVs_good4": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPVs",100,0,100)
            ),
            "dist_nPVs_good5": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPVs",40,0,40)
            ),
            "dist_nPVs_good6": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPVs",40,0,40)
            ),
            "dist_nPVs_good7": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPVs",40,0,40)
            ),
            "dist_nPVs_good8": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPVs",40,0,40)
            ),
            "dist_nPVs_good9": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPVs",40,0,40)
            ),
            #"2d_Vertex_tracksSize_n_pvs" : hist.Hist(
            #          "Events",
            #          hist.Cat("cut","Cutflow"),
            #          hist.Bin("v1","Vertex Tracks Size",200,0,200),
            #          hist.Bin("v2","nPVs",100,0,1)
            #),
            "dist_Vertex_minZ": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Vertex minZ",100,0,20)
            ),
            "dist_Vertex_valid": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Vertex Valid",5,0,5)
            ),
            "dist_Vertex_tracksSize0": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Vertex Track Size 0",200,0,200)
            ),
            "dist_Vertex_tracksSize": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Vertex Track Size",200,0,200)
            ),
            "dist_Vertex_ndof": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ndof",20,0,20)
            ),
            "dist_Vertex_chi2": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Vertex chi2",100,0,5)
            ),
            "dist_Vertex_z": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Vertex z",100,-50,50)
            ),
            "dist_n_pfcand": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand",50,0,300)
            ),
            "dist_PFcand_ncount0": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand0",50,0,300)
            ),
            "dist_PFcand_ncount50": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand50",50,0,300)
            ),
            "dist_PFcand_ncount75": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand75",50,0,300)
            ),
            "dist_PFcand_ncount100": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand100",50,0,300)
            ),
            "dist_PFcand_ncount150": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand150",50,0,300)
            ),
            "dist_PFcand_ncount200": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand200",50,0,300)
            ),
            "dist_PFcand_ncount300": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand300",50,0,300)
            ),
            "dist_n_jetId": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nJet",20,0,20)
            ),
            "dist_n_fatjet": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nFatJet",10,0,10)
            ),
            "dist_Jet_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Jet_pt",100,0,300)
            ),
            "dist_Jet_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Jet_eta",eta_bins)
            ),
            "dist_Jet_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Jet_phi",phi_bins)
            ),
            "dist_reFatJet_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","reFatJet_pt",100,0,300)
            ),
            "dist_reFatJet_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","reFatJet_eta",eta_bins)
            ),
            "dist_reFatJet_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","reFatJet_phi",phi_bins)
            ),
            "dist_FatJet_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_pt",100,0,300)
            ),
            "dist_FatJet_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_eta",eta_bins)
            ),
            "dist_FatJet_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_phi",phi_bins)
            ),
            "dist_fjn1_FatJet_ncount30": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount30",11,-0.5,10.5)
            ),
            "dist_fjn1_FatJet_ncount50": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount50",11,-0.5,10.5)
            ),
            "dist_fjn1_FatJet_ncount100": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount100",11,-0.5,10.5)
            ),
            "dist_fjn1_FatJet_ncount150": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount150",11,-0.5,10.5)
            ),
            "dist_fjn1_FatJet_ncount200": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount200",11,-0.5,10.5)
            ),
            "dist_fjn1_FatJet_ncount250": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount250",11,-0.5,10.5)
            ),
            "dist_fjn1_FatJet_ncount300": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount300",11,-0.5,10.5)
            ),
            "dist_FatJet_nconst": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_nconst",50,0,300)
            ),
            "dist_FatJet_ncount30": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount30",11,-0.5,10.5)
            ),
            "dist_FatJet_ncount50": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount50",11,-0.5,10.5)
            ),
            "dist_FatJet_ncount100": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount100",11,-0.5,10.5)
            ),
            "dist_FatJet_ncount150": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount150",11,-0.5,10.5)
            ),
            "dist_FatJet_ncount200": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount200",11,-0.5,10.5)
            ),
            "dist_FatJet_ncount250": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount250",11,-0.5,10.5)
            ),
            "dist_FatJet_ncount300": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","FatJet_ncount300",11,-0.5,10.5)
            ),
            "dist_PFcand_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_pt",pt_bins)
            ),
            "dist_PFcand_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_eta",eta_bins)
            ),
            "dist_PFcand_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_phi",phi_bins)
            ),
             ###########TRACKS
            "dist_trkIDFK_PFcand_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_pt",pt_bins),
                      hist.Bin("v2","PFcand_dR",100,0,0.3)
            ),
            "dist_trkIDFK_PFcand_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_eta",eta_bins),
                      hist.Bin("v2","PFcand_dR",100,0,0.3)
            ),
            "dist_trkIDFK_PFcand_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_phi",phi_bins),
                      hist.Bin("v2","PFcand_dR",100,0,0.3)
            ),
            "dist_PFcand_dR": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_mindR",100,0,0.3)
            ),
#            "dist_PFcand_alldR": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","PFcand_alldR",100,0,0.03)
#            ),
            "dist_res_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","res_pt",100,-2,2)
            ),
            "dist_res_mass": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","res_mass",100,-2,2)
            ),
            "dist_res_dR": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","res_dR",100,0,10)
            ),
            "dist_trkID_gen_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_pt",pt_bins),
                      hist.Bin("v2","gen_dR",100,0,0.3)
            ),
            "dist_trkID_gen_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_eta",eta_bins),
                      hist.Bin("v2","gen_dR",100,0,0.3)
            ),
            "dist_trkID_gen_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_phi",phi_bins),
                      hist.Bin("v2","gen_dR",100,0,0.3)
            ),
            "dist_gen_dR": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_dR",100,0,0.3)
            ),
            "dist_gen_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_pt",pt_bins)
            ),
            "dist_gen_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_eta",eta_bins)
            ),
            "dist_gen_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_phi",phi_bins)
            ),
            "dist_gen_PV": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_PV",4,0,4)
            ),
            "dist_gen_PVdZ": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_PVdZ",100,-5,5)
            ),
            "dist_n_pfMu": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","n_pfMuons",15,0,15)
            ),
            "dist_n_pfEl": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","n_pfElectrons",20,0,20)
            ),
        })

    @property
    def accumulator(self):
        return self._accumulator

    def process(self, arrays):
        vector.register_awkward()
        output = self.accumulator.identity()
        #print(events)
        dataset = arrays.metadata['dataset']
        #arrays = {k: v for k,v in events.arrays(how=dict).items()}
        output["sumw"][dataset] += len(arrays) # get number of events
        tright = [item[7] for item in arrays["hltResult"]]
        trigmu = [item[5] for item in arrays["hltResult"]] #actually calojet40 reference trigger
        #trigger order:
        #HLT Trigger DST_DoubleMu1_noVtx_CaloScouting_v2
        #HLT Trigger DST_DoubleMu3_noVtx_CaloScouting_Monitoring_v6
        #HLT Trigger DST_DoubleMu3_noVtx_CaloScouting_v6
        #HLT Trigger DST_DoubleMu3_noVtx_Mass10_PFScouting_v3
        #HLT Trigger DST_L1HTT_CaloScouting_PFScouting_v15
        #HLT Trigger DST_CaloJet40_CaloScouting_PFScouting_v15
        #HLT Trigger DST_HT250_CaloScouting_v10
	#HLT Trigger DST_HT410_PFScouting_v16


        vals0 = ak.zip({
               'ht': arrays["ht"],
               'n_pfcand': arrays["n_pfcand"],
               'event_sphericity': arrays["event_sphericity"],
               'eventBoosted_sphericity': arrays["eventBoosted_sphericity"],
               'n_fatjet': arrays["n_fatjet"],
               'n_jetId': arrays["n_jetId"],
               'n_pfMu': arrays["n_pfMu"],
               'n_pfEl': arrays["n_pfEl"],
               'n_pvs': arrays["n_pvs"],
               'nPVs_good0': ak.count(arrays["Vertex_isValidVtx"],axis=-1),
               'nPVs_good1': ak.count(arrays["Vertex_isValidVtx"][(arrays["Vertex_isValidVtx"] == 1)],axis=-1),
               'nPVs_good2': ak.count(arrays["Vertex_isValidVtx"][(abs(arrays["Vertex_z"]) <24 ) & (arrays["Vertex_isValidVtx"] == 1)],axis=-1),
               'nPVs_good3': ak.count(arrays["Vertex_isValidVtx"][(abs(arrays["Vertex_z"]) < 24) & (arrays["Vertex_ndof"]> 4 ) & (arrays["Vertex_isValidVtx"] == 1)],axis=-1),
               'Vertex_tracksSize0': ak.max(arrays["Vertex_tracksSize"],axis=-1),
               'nPVs_good4': ak.count(arrays["Vertex_tracksSize"][arrays["Vertex_tracksSize"] >3],axis=-1),
               'nPVs_good5': ak.count(arrays["Vertex_tracksSize"][arrays["Vertex_tracksSize"] >5],axis=-1),
               'nPVs_good6': ak.count(arrays["Vertex_tracksSize"][arrays["Vertex_tracksSize"] >7],axis=-1),
               'nPVs_good7': ak.count(arrays["Vertex_tracksSize"][arrays["Vertex_tracksSize"] >10],axis=-1),
               'nPVs_good8': ak.count(arrays["Vertex_tracksSize"][arrays["Vertex_tracksSize"] >15],axis=-1),
               'nPVs_good9': ak.count(arrays["Vertex_tracksSize"][arrays["Vertex_tracksSize"] >25],axis=-1),
               'Vertex_minZ' : ak.min(abs(np.subtract(ak.firsts(arrays["Vertex_z"]),arrays["Vertex_z"][:,1:])),axis=-1,mask_identity=False),
               #'bCandmask': [True if len(x) > 1 else False for x in arrays["bPFcand_pt"]],
               'triggerHt': tright,
               'triggerMu': trigmu,
               'PFcand_ncount0' :  ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.0 )],axis=-1),
               'PFcand_ncount50' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.50)],axis=-1),
               'PFcand_ncount75' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.75)],axis=-1),
               'PFcand_ncount100': ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>1.0 )],axis=-1),
               'PFcand_ncount150': ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>1.5 )],axis=-1),
               'PFcand_ncount200': ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>2   )],axis=-1),
               'PFcand_ncount300': ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>3   )],axis=-1),
               'FatJet_ncount30': ak.count(arrays["FatJet_pt"],axis=-1),
               'FatJet_ncount50': ak.count(arrays["FatJet_pt"][arrays["FatJet_pt"]>50],axis=-1),
               'FatJet_ncount100': ak.count(arrays["FatJet_pt"][arrays["FatJet_pt"]>100],axis=-1),
               'FatJet_ncount150': ak.count(arrays["FatJet_pt"][arrays["FatJet_pt"]>150],axis=-1),
               'FatJet_ncount200': ak.count(arrays["FatJet_pt"][arrays["FatJet_pt"]>200],axis=-1),
               'FatJet_ncount250': ak.count(arrays["FatJet_pt"][arrays["FatJet_pt"]>250],axis=-1),
               'FatJet_ncount300': ak.count(arrays["FatJet_pt"][arrays["FatJet_pt"]>300],axis=-1),
               'FatJet_nconst' : ak.max(arrays["FatJet_nconst"],axis=-1,mask_identity=False),
        })

        vals_vertex0 = ak.zip({
                      'Vertex_valid': arrays["Vertex_isValidVtx"],
                      'Vertex_tracksSize': arrays["Vertex_tracksSize"],
                      'Vertex_chi2': arrays["Vertex_chi2"],
                      'Vertex_ndof': arrays["Vertex_ndof"],
                      'Vertex_z': arrays["Vertex_z"],
        })
        vals_jet0 = ak.zip({
                       'Jet_pt' : arrays["Jet_pt"],
                       'Jet_eta': arrays["Jet_eta"],
                       'Jet_phi': arrays["Jet_phi"],
        })
        print("loaded jet")
        vals_fatjet0 = ak.zip({
                       'pt' : arrays["FatJet_pt"],
                       'eta': arrays["FatJet_eta"],
                       'phi': arrays["FatJet_phi"],
                       'mass': arrays["FatJet_mass"],
                       'FatJet_nconst': arrays["FatJet_nconst"],
        }, with_name="Momentum4D")
        print("loaded fatjet")
        if(signal):
          vals_tracks0 = ak.zip({
                         'pt' : arrays["PFcand_pt"],
                         'eta': arrays["PFcand_eta"],
                         'phi': arrays["PFcand_phi"],
                         'mass': arrays["PFcand_m"],
                         'PFcand_dR': arrays["PFcand_dR"],
                         'PFcand_fromsuep': arrays["PFcand_fromsuep"],
                         'PFcand_q': arrays["PFcand_q"],
                         'PFcand_vertex': arrays["PFcand_vertex"],
          },with_name="Momentum4D")
          vals_gen0 = ak.zip({
                         'pt' : arrays["gen_pt"],
                         'eta': arrays["gen_eta"],
                         'phi': arrays["gen_phi"],
                         'mass': arrays["gen_mass"],
                         'gen_dR':  arrays["gen_dR"],
                         'gen_fromSuep':  arrays["gen_fromSuep"],
                         'gen_PV':  arrays["gen_PV"],
                         'gen_PVdZ':  arrays["gen_PVdZ"],
          },with_name="Momentum4D")
          scalar0  = ak.zip({
                         'pt' : arrays["scalar_pt"],
                         'eta': arrays["scalar_eta"],
                         'phi': arrays["scalar_phi"],
                         'mass': arrays["scalar_m"],
          },with_name="Momentum4D")
        else:
          vals_tracks0 = ak.zip({
                         'pt' : arrays["PFcand_pt"],
                         'eta': arrays["PFcand_eta"],
                         'phi': arrays["PFcand_phi"],
                         'mass': arrays["PFcand_m"],
                         'PFcand_q': arrays["PFcand_q"],
                         'PFcand_vertex': arrays["PFcand_vertex"],
          }, with_name="Momentum4D")
        print("loaded tracks")
        bCands = ak.zip({
            "pt":  [x for x in arrays["bPFcand_pt"]  if len(x) > 1],
            "eta": [x for x in arrays["bPFcand_eta"] if len(x) > 1],
            "phi": [x for x in arrays["bPFcand_phi"] if len(x) > 1],
            "mass":[x for x in arrays["bPFcand_m"]   if len(x) > 1] 
        }, with_name="Momentum4D") 



#        alldRtracks = ak.zip({'PFcand_alldR': arrays["PFcand_alldR"]})
#        alldRtracks = ak.flatten(alldRtracks)
#        print(alldRtracks)
#        print(len(alldRtracks))

        track_cuts = ((arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>=0.75))
        tracks_cut0 = vals_tracks0[track_cuts]
        tracks_cuts1 = ((tracks_cut0.x !=0)&(tracks_cut0.y !=0 )&(tracks_cut0.z !=0) &(tracks_cut0.p !=0))
        tracks_cut0 = tracks_cut0[tracks_cuts1]

        #tracks_cut1x = tracks_cut0[(vals0.triggerHt==1) & (vals0.ht >=600)]
        minPt = 30
        jetdef = fastjet.JetDefinition(fastjet.antikt_algorithm,1.5)
        cluster = fastjet.ClusterSequence(tracks_cut0,jetdef)
        ak_inclusive_jets = ak.with_name(cluster.inclusive_jets(),"Momentum4D")
        ak_inclusive_cluster = ak.with_name(cluster.constituents(),"Momentum4D")
        minPtCut = ak_inclusive_jets.pt > minPt
        ak_inclusive_jets = ak_inclusive_jets[minPtCut]
        ak_inclusive_cluster = ak_inclusive_cluster[minPtCut]
        highpt_jet = ak.argsort(ak_inclusive_jets.pt, axis=1, ascending=False, stable=True)
        ak_inclusive_jets = ak_inclusive_jets[highpt_jet]
        ak_inclusive_cluster = ak_inclusive_cluster[highpt_jet]
        
        ak_pt = ak_inclusive_jets.pt
        vals_refatjet0 =ak.zip({
            "pt": ak_inclusive_jets.pt,
            "eta": ak_inclusive_jets.eta,
            "phi": ak_inclusive_jets.phi,
            "mass": ak_inclusive_jets.m,
            "FatJet_nconst": ak.num(ak_inclusive_cluster,axis=-1),
        }, with_name="Momentum4D")


        #recluster_fatjet1  = vals_fatjet0[ vals0.FatJet_ncount30 >= 2] 
        #print(len(recluster_fatjet1))
        #SUEP_cand = ak.where(recluster_fatjet1.FatJet_nconst[:,1]<=recluster_fatjet1.FatJet_nconst[:,0],recluster_fatjet1[:,0],recluster_fatjet1[:,1])
        #ISR_cand  = ak.where(recluster_fatjet1.FatJet_nconst[:,1]> recluster_fatjet1.FatJet_nconst[:,0],recluster_fatjet1[:,0],recluster_fatjet1[:,1])

        rerecluster_fatjet1  = vals_refatjet0[ ak.count(vals_refatjet0["pt"][vals_refatjet0["pt"]>30],axis=-1) >= 2] 
        rerecluster_fatjet1x  = ak_inclusive_cluster[ ak.count(vals_refatjet0["pt"][vals_refatjet0["pt"]>30],axis=-1) >= 2] 
        print(len(rerecluster_fatjet1))
        reSUEP_cand = ak.where(rerecluster_fatjet1.FatJet_nconst[:,1]<=rerecluster_fatjet1.FatJet_nconst[:,0],rerecluster_fatjet1x[:,0],rerecluster_fatjet1x[:,1])
        reISR_cand  = ak.where(rerecluster_fatjet1.FatJet_nconst[:,1]> rerecluster_fatjet1.FatJet_nconst[:,0],rerecluster_fatjet1x[:,0],rerecluster_fatjet1x[:,1])
        SUEP_cand = ak.where(rerecluster_fatjet1.FatJet_nconst[:,1]<=rerecluster_fatjet1.FatJet_nconst[:,0],rerecluster_fatjet1[:,0],rerecluster_fatjet1[:,1])
        ISR_cand  = ak.where(rerecluster_fatjet1.FatJet_nconst[:,1]> rerecluster_fatjet1.FatJet_nconst[:,0],rerecluster_fatjet1[:,0],rerecluster_fatjet1[:,1])

        if (redoISRRM):
          print("calc sphericity")
          boost_IRM = ak.zip({
              "px": SUEP_cand.px*-1,
              "py": SUEP_cand.py*-1,
              "pz": SUEP_cand.pz*-1,
              "mass": SUEP_cand.mass
          }, with_name="Momentum4D")
          ISR_cand_b = ISR_cand.boost_p4(boost_IRM) # boosted ISR jet

          recotracks_IRM = tracks_cut0[ak.count(vals_refatjet0["pt"][vals_refatjet0["pt"]>30],axis=-1) >= 2] # tracks
          tracks_IRM = recotracks_IRM.boost_p4(boost_IRM) # boosted tracks
          tracks_cuts1x = (tracks_IRM.p !=0)
          tracks_IRM = tracks_IRM[tracks_cuts1x]
          spherex0 = vals0[ak.count(vals_refatjet0["pt"][vals_refatjet0["pt"]>30],axis=-1) >= 2]
          spherex0["FatJet_nconst0"] = SUEP_cand["FatJet_nconst"]
        
          reSUEP_cand = reSUEP_cand.boost_p4(boost_IRM)
          tracks_cuts2x = (reSUEP_cand.p !=0)
          reSUEP_cand = reSUEP_cand[tracks_cuts2x]
          reonetrackcut = (ak.num(reSUEP_cand) >=2) 
          #reSUEP_cand = ak.mask(reSUEP_cand,reonetrackcut)
          reSUEP_cand = reSUEP_cand[reonetrackcut]
          spherey0 = spherex0[reonetrackcut]
          if(len(reSUEP_cand)!=0):
            #print(ak.min(ak.count(reSUEP_cand,axis=-1)))
            #print(reSUEP_cand)
            reeigs2 = sphericity(self,reSUEP_cand,2.0) # normal sphericity
            reeigs1 = sphericity(self,reSUEP_cand,1.0) # sphere 1
            spherey0["sphere1_suep"] = 1.5 * (reeigs1[:,1]+reeigs1[:,0])
            spherey0["sphere_suep"] = 1.5 * (reeigs2[:,1]+reeigs2[:,0])
          else:
            spherey0["sphere1_suep"] = -1 
            spherey0["sphere_suep"] = -1
          
          spherey1 = spherey0[spherey0.triggerHt >= 1]
          spherey2 = spherey1[spherey1.ht >= 600]
          spherey3 = spherey2[spherey2.FatJet_ncount50 >= 2]
          spherey4 = spherey3[spherey3.PFcand_ncount75 >= 140]
          #spherey5 = spherey2[spherey2.n_pvs < 30]
          #spherey6 = spherey2[spherey2.n_pvs <= 30]
          sphere1y = [spherey0,spherey1,spherey2,spherey3,spherey4]#,spherey5,spherey6]
          output = packdist(output,sphere1y,"sphere1_suep")
          output = packdist(output,sphere1y,"sphere_suep")
          output = packSR(output,sphere1y,"suep")
          IRM_candsvx2 = tracks_IRM[abs(recotracks_IRM[tracks_cuts1x].deltaR(ISR_cand)) >= 1.5] # remove all tracks that would be in the ISR jet unboosted
          #IRM_candsvx2 = recotracks_IRM[abs(recotracks_IRM.deltaR(ISR_cand)) >= 1.5] # remove all tracks that would be in the ISR jet unboosted
          #IRM_candvx2 = IRM_candsvx2.boost_p4(boost_IRM)
          reonetrackcutx = (ak.num(IRM_candsvx2) >=2)
          #IRM_candvx2 = ak.mask(IRM_candvx2,reonetrackcutx)
          IRM_candsvx2 = IRM_candsvx2[reonetrackcutx]
          spherez0 = spherex0[reonetrackcutx]
          if(len(IRM_candsvx2)!=0):
            rexeigs2 = sphericity(self,IRM_candsvx2,2.0) # normal sphericity
            rexeigs1 = sphericity(self,IRM_candsvx2,1.0) # sphere 1
            spherez0["sphere1_isr"] = 1.5 * (rexeigs1[:,1]+rexeigs1[:,0])
            spherez0["sphere_isr"] = 1.5 * (rexeigs2[:,1]+rexeigs2[:,0])
          else:
            spherez0["sphere1_isr"] = -1 
            spherez0["sphere_isr"] = -1
          spherez1 = spherez0[spherez0.triggerHt >= 1]
          spherez2 = spherez1[spherez1.ht >= 600]
          spherez3 = spherez2[spherez2.FatJet_ncount50 >= 2]
          spherez4 = spherez3[spherez3.PFcand_ncount75 >= 140]
          #spherez5 = spherez2[spherez2.n_pvs < 30]
          #spherez6 = spherez2[spherez2.n_pvs <= 30]
          
          sphere1z = [spherez0,spherez1,spherez2,spherez3,spherez4]#,spherez5,spherez6]
          output = packdist(output,sphere1z,"sphere1_isr")
          output = packdist(output,sphere1z,"sphere_isr")
          output = packSR(output,sphere1z,"isr")

          def sphericityCalc(output,cut):
            IRM_cands = tracks_IRM[abs(tracks_IRM.deltaphi(ISR_cand_b)) >= cut/10.]
            onetrackcut = (ak.num(IRM_cands) >=2) # cut to pick out events that survive the isr removal
            IRM_cands = IRM_cands[onetrackcut]
            spherexx = spherex0[onetrackcut]
            #IRM_cands = ak.mask(IRM_cands,onetrackcut)
  

            print(len(IRM_cands),len(spherex0))
            if(len(IRM_cands)!=0):
              eigs2 = sphericity(self,IRM_cands,2.0) # normal sphericity
              eigs1 = sphericity(self,IRM_cands,1.0) # sphere 1
              spherexx["sphere1_%s"%cut] = 1.5 * (eigs1[:,1]+eigs1[:,0])
              spherexx["sphere_%s"%cut] = 1.5 * (eigs2[:,1]+eigs2[:,0])
            else:
              spherexx["sphere1_%s"%cut] = -1 
              spherexx["sphere_%s"%cut] = -1
            spherex1 = spherexx[spherexx.triggerHt >= 1]
            spherex2 = spherex1[spherex1.ht >= 600]
            spherex3 = spherex2[spherex2.FatJet_ncount50 >= 2]
            spherex4 = spherex3[spherex3.PFcand_ncount75 >= 140]
            #spherex5 = spherex2[spherex2.n_pvs < 30]
            #spherex6 = spherex2[spherex2.n_pvs <= 30]
            sphere1 = [spherexx,spherex1,spherex2,spherex3,spherex4]#,spherex5,spherex6]
            output = packdist(output,sphere1,"sphere1_%s"%cut)
            output = packdist(output,sphere1,"sphere_%s"%cut)
            output = packSR(output,sphere1,cut)
            del sphere1
            del spherexx
            del spherex1
            del spherex2
            del spherex3
            del spherex4
            #del spherex5
            #del spherex6
            return output
          output = sphericityCalc(output,16)
          output = sphericityCalc(output,10)
          output = sphericityCalc(output,8)
          output = sphericityCalc(output,4)

          if(eventDisplay_knob):
            for evt in range(len(bCands)):
              print(evt)
              plot_display(evt,recotracks_IRM[evt],tracks_IRM[evt],SUEP_cand[evt],ISR_cand[evt],ISR_cand_b[evt],spherex0["sphere1b"][evt],len(IRM_cands[evt]))
          print("filling cutflows") 
        
       ## resolution studies
        if(signal):
          print("calc res")
          scalar = scalar0[(vals0.FatJet_ncount50 >=2) & (vals0.triggerHt >=1) & (vals0.ht>=600)]
          suepvals = vals0[vals0.FatJet_ncount50 >=2]
          SUEP_cand = SUEP_cand[(suepvals.triggerHt >=1) & (suepvals.ht>=600)] # FJ > 2 cut is already applied from the suep array
          res_pt = (SUEP_cand.pt.to_numpy()-scalar["pt"].to_numpy())/scalar["pt"].to_numpy()
          res_mass = (SUEP_cand.mass.to_numpy()-scalar["mass"].to_numpy())/scalar["mass"].to_numpy()
          res_dPhi = SUEP_cand.phi.to_numpy()-scalar["phi"].to_numpy()
          res_dEta = SUEP_cand.eta.to_numpy()-scalar["eta"].to_numpy()
          res_dR = np.sqrt(res_dPhi*res_dPhi + res_dEta*res_dEta)
          resolutions = ak.zip({
            "res_pt" : res_pt,
            "res_mass" : res_mass,
            "res_dR" : res_dR
        
          })
       ############################################################################## 
        #cutflow Ht
        vals1 = vals0[vals0.triggerHt >= 1]
        vals2 = vals1[vals1.ht >= 600]
        vals3 = vals2[vals2.FatJet_ncount50 >= 2]
        #vals3 = vals2[vals2.n_fatjet >= 2]
        #vals4 = vals3[vals3.FatJet_nconst >= 80]
        vals4 = vals3[vals3.PFcand_ncount75 >= 140]
        vals4x = vals3[vals3.eventBoosted_sphericity >= 0.6]
        #vals5 = vals2[vals2.n_pvs < 30]
        #vals6 = vals2[vals2.n_pvs >= 30]

        vals_jet1 = vals_jet0[vals0.triggerHt >= 1]
        vals_jet2 = vals_jet1[vals1.ht >= 600]
        vals_jet3 = vals_jet2[vals2.FatJet_ncount50 >= 2]
        #vals_jet3 = vals_jet2[vals2.n_fatjet >= 2]
        #vals_jet4 = vals_jet3[vals3.FatJet_nconst >= 80]
        vals_jet4 = vals_jet3[vals3.PFcand_ncount75 >= 140]
        #vals_jet5 = vals_jet2[vals2.n_pvs < 30]
        #vals_jet6 = vals_jet2[vals2.n_pvs >= 30]
        
        print("filling cutflows fj") 
        vals_fatjet1 = vals_fatjet0[vals0.triggerHt >= 1]
        vals_fatjet2 = vals_fatjet1[vals1.ht >= 600]
        vals_fatjet3 = vals_fatjet2[vals2.FatJet_ncount50 >= 2]
        #vals_fatjet3 = vals_fatjet2[vals2.n_fatjet >= 2]
        #vals_fatjet4 = vals_fatjet3[vals3.FatJet_nconst >= 80]
        vals_fatjet4 = vals_fatjet3[vals3.PFcand_ncount75 >= 140]
        #vals_fatjet5 = vals_fatjet2[vals2.n_pvs < 30]
        #vals_fatjet6 = vals_fatjet2[vals2.n_pvs >= 30]
        
        vals_refatjet1 = vals_refatjet0[vals0.triggerHt >=1]
        vals_refatjet2 = vals_refatjet1[vals1.ht >= 600]
        vals_refatjet3 = vals_refatjet2[vals2.FatJet_ncount50 >= 2]
        vals_refatjet4 = vals_refatjet3[vals3.PFcand_ncount75 >= 140]
        #vals_refatjet5 = vals_refatjet2[vals2.n_pvs < 30]
        #vals_refatjet6 = vals_refatjet2[vals2.n_pvs >= 30]
        
     
        print("filling cutflows trk") 
        vals_tracks1 = tracks_cut0[vals0.triggerHt >= 1]
        vals_tracks2 = vals_tracks1[vals1.ht >= 600]
        vals_tracks3 = vals_tracks2[vals2.FatJet_ncount50 >= 2]
        #vals_tracks3 = vals_tracks2[vals2.n_fatjet >= 2]
        #vals_tracks4 = vals_tracks3[vals3.FatJet_nconst >= 80]
        vals_tracks4 = vals_tracks3[vals3.PFcand_ncount75 >= 140]
        print("filling cutflows vertex") 
        vals_vertex1 = vals_vertex0[vals0.triggerHt >= 1]
        vals_vertex2 = vals_vertex1[vals1.ht >= 600]
        vals_vertex3 = vals_vertex2[vals2.FatJet_ncount50 >= 2]
        vals_vertex4 = vals_vertex3[vals3.PFcand_ncount75 >=140]
        #vals_vertex5 = vals_vertex3[vals3.n_pvs < 30]
        #vals_vertex6 = vals_vertex3[vals3.n_pvs >= 30]
        #vals_vertex4 = vals_vertex3[vals3.PFcand_ncount75 >= 140]

        vals = [vals0,vals1,vals2,vals3,vals4]#,vals5,vals6]
        valsx = [vals0,vals1,vals2,vals3,vals4x]#,vals5,vals6]
        vals_jet = [vals_jet0,vals_jet1,vals_jet2,vals_jet3,vals_jet4]#,vals_jet5,vals_jet6]
        vals_fatjet = [vals_fatjet0,vals_fatjet1,vals_fatjet2,vals_fatjet3,vals_fatjet4]#,vals_fatjet5,vals_fatjet6]
        vals_refatjet = [vals_refatjet0,vals_refatjet1,vals_refatjet2,vals_refatjet3,vals_refatjet4]#,vals_refatjet5,vals_refatjet6]
        vals_tracks = [vals_tracks0,vals_tracks1,vals_tracks2,vals_tracks3,vals_tracks4]
        vals_vertex = [vals_vertex0,vals_vertex1,vals_vertex2,vals_vertex3,vals_vertex4]#,vals_vertex5,vals_vertex6]

        #fatjet n-1 cutflow
        #fj3 = vals2[vals2.FatJet_nconst >=80]
        fj3 = vals2[vals2.PFcand_ncount75 >=140]
        fj4 = fj3[fj3.eventBoosted_sphericity >= 0.6]
        vals_fj = [vals0,vals1,vals2,fj3,fj4]


        #trig cutflow
        trig1 = vals0[vals0.triggerMu >=1]
        trig2 = vals0[vals0.triggerHt >=1]
        trig3 = trig1[trig1.triggerHt >=1]
        trigs = [vals0,trig1,trig2,trig3]

        if(signal):
          print("filling cutflows trkID") 
          trkID1 = vals_tracks0[(vals0.triggerHt >= 1) & (vals0.ht >=600) &(vals0.FatJet_ncount50 >= 2)]

          trkID2 = trkID1[abs(trkID1.eta) < 2.4]
          trkID3 = trkID2[trkID2.PFcand_q != 0]
          trkID4 = trkID3[trkID3.PFcand_vertex == 0]
          trkID5 = trkID4[trkID4.pt > 0.5]
          trkID6 = trkID5[trkID5.pt > 0.6]
          trkID7 = trkID6[trkID6.pt > 0.7]
          trkID8 = trkID7[trkID7.pt > 0.75]
          trkID9 = trkID8[trkID8.pt > 0.8]
          trkID10 = trkID9[trkID9.pt > 0.9]
          trkID11 = trkID10[trkID10.pt > 1.0]
          trkID = [trkID1,trkID2,trkID3,trkID4,trkID5,trkID6,trkID7,trkID8,trkID9,trkID10,trkID11]
          output = packtrkFKID(output,trkID,"pt" ,"PFcand_dR","PFcand_")
          output = packtrkFKID(output,trkID,"eta","PFcand_dR","PFcand_")
          output = packtrkFKID(output,trkID,"phi","PFcand_dR","PFcand_")

          vals_gen1 = vals_gen0[vals0.triggerHt >= 1]
          vals_gen2 = vals_gen1[vals1.ht >= 600]
          vals_gen3 = vals_gen2[vals2.FatJet_ncount50 >= 2]
          vals_gen4 = vals_gen3[vals3.n_pfcand >= 140]
          #vals_gen4 = vals_gen3[vals3.FatJet_nconst >= 80]
          vals_gen = [vals_gen0,vals_gen1,vals_gen2,vals_gen3,vals_gen4]
          trkID5x = vals_gen3[vals_gen3.pt > 0.5]
          trkID6x = trkID5x[trkID5x.pt > 0.6]
          trkID7x = trkID6x[trkID6x.pt > 0.7]
          trkID8x = trkID7x[trkID7x.pt > 0.75]
          trkID9x = trkID8x[trkID8x.pt > 0.8]
          trkID10x = trkID9x[trkID9x.pt > 0.9]
          trkID11x = trkID10x[trkID10x.pt > 1.0]
          trkIDx = [vals_gen3,trkID5x,trkID6x,trkID7x,trkID8x,trkID9x,trkID10x,trkID11x]
          output = packtrkID(output,trkIDx,"pt" ,"gen_dR","gen_")
          output = packtrkID(output,trkIDx,"eta","gen_dR","gen_")
          output = packtrkID(output,trkIDx,"phi","gen_dR","gen_")
          output = packdistflat(output,vals_tracks,"PFcand_dR")
          output = packdistflat(output,vals_gen,"pt","gen_")
          output = packdistflat(output,vals_gen,"gen_dR")
          output = packdistflat(output,vals_gen,"eta","gen_")
          output = packdistflat(output,vals_gen,"phi","gen_")
          output = packdistflat(output,vals_gen,"gen_PV")
          output = packdistflat(output,vals_gen,"gen_PVdZ")
#          output = packsingledist(output,alldRtracks,"PFcand_alldR")
          output = packsingledist(output,resolutions,"res_pt")
          output = packsingledist(output,resolutions,"res_mass")
          output = packsingledist(output,resolutions,"res_dR")
          #print(sphere1)
          #output = packdist(output,sphere1,"sphere1")
        #output = packdist(output,sphere1,"sphere1b_16")
        #output = packdist(output,sphere1,"sphereb_16")
        #output = packdist(output,sphere1,"sphere1b_10")
        #output = packdist(output,sphere1,"sphereb_10")
        #output = packdist(output,sphere1,"sphere1b_8")
        #output = packdist(output,sphere1,"sphereb_8")
        #output = packdist(output,sphere1,"sphere1b_4")
        #output = packdist(output,sphere1,"sphereb_4")

        output = packtrig(output,trigs,"ht")
        output = packtrig(output,trigs,"n_pfMu")
        #fill hists
        print("filling hists") 
        #output = packSR(output,sphere1y)
        #output = packSR2(output,sphere1y)
        #output = packSR3(output,sphere1y)
        output = packdist(output,vals,"ht")
        output = packdist(output,vals,"n_pfcand")
        output = packdist(output,vals,"event_sphericity")
        output = packdist(output,vals,"eventBoosted_sphericity")
        output = packdist(output,vals,"n_fatjet")
        output = packdist(output,vals,"n_jetId")
        output = packdist(output,vals,"n_pfMu")
        output = packdist(output,vals,"n_pfEl")
        output = packdist(output,vals,"n_pvs")
        output = packdist(output,vals,"nPVs_good0")
        output = packdist(output,vals,"nPVs_good1")
        output = packdist(output,vals,"nPVs_good2")
        output = packdist(output,vals,"nPVs_good3")
        output = packdist(output,vals,"nPVs_good4")
        output = packdist(output,vals,"nPVs_good5")
        output = packdist(output,vals,"nPVs_good6")
        output = packdist(output,vals,"nPVs_good7")
        output = packdist(output,vals,"nPVs_good8")
        output = packdist(output,vals,"nPVs_good9")
        output = packdist(output,vals,"Vertex_minZ")
        output = packdist(output,vals,"Vertex_tracksSize0")
        output = packdistflat(output,vals_vertex,"Vertex_valid","")
        output = packdistflat(output,vals_vertex,"Vertex_tracksSize","")
        output = packdistflat(output,vals_vertex,"Vertex_chi2","")
        output = packdistflat(output,vals_vertex,"Vertex_ndof","")
        output = packdistflat(output,vals_vertex,"Vertex_z","")
#        output = pack2D(output,vals_vertex,"Vertex_tracksSize","n_pvs")
        
        output = packdistflat(output,vals_jet,"Jet_pt")
        output = packdistflat(output,vals_jet,"Jet_eta")
        output = packdistflat(output,vals_jet,"Jet_phi")
        output = packdistflat(output,vals_fatjet,"pt","FatJet_")
        output = packdistflat(output,vals_fatjet,"eta","FatJet_")
        output = packdistflat(output,vals_fatjet,"phi","FatJet_")
        output = packdistflat(output,vals_refatjet,"pt","reFatJet_")
        output = packdistflat(output,vals_refatjet,"eta","reFatJet_")
        output = packdistflat(output,vals_refatjet,"phi","reFatJet_")
        output = packdistflat(output,vals_tracks,"pt","PFcand_")
        output = packdistflat(output,vals_tracks,"eta","PFcand_")
        output = packdistflat(output,vals_tracks,"phi","PFcand_")
        output = packdist(output,vals,"FatJet_ncount30")
        output = packdist(output,vals,"FatJet_ncount50")
        output = packdist(output,vals,"FatJet_ncount100")
        output = packdist(output,vals,"FatJet_ncount150")
        output = packdist(output,vals,"FatJet_ncount200")
        output = packdist(output,vals,"FatJet_ncount250")
        output = packdist(output,vals,"FatJet_ncount300")
        output = packdist(output,valsx,"FatJet_nconst")
        output = packdist(output,valsx,"PFcand_ncount0")
        output = packdist(output,valsx,"PFcand_ncount50")
        output = packdist(output,valsx,"PFcand_ncount75")
        output = packdist(output,valsx,"PFcand_ncount100")
        output = packdist(output,valsx,"PFcand_ncount150")
        output = packdist(output,valsx,"PFcand_ncount200")
        output = packdist(output,valsx,"PFcand_ncount300")

        output = packdist_fjn1(output,vals_fj,"FatJet_ncount30")
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount50")
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount100")
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount150")
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount200")
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount250")
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount300")
        

        return output

    def postprocess(self, accumulator):
        return accumulator


# https://github.com/scikit-hep/uproot4/issues/122
uproot.open.defaults["xrootd_handler"] = uproot.source.xrootd.MultithreadedXRootDSource


fin = "HT2000"
batch = 0
signal=False
runInteractive=False
if len(sys.argv) >= 2:
  fin = sys.argv[1]
#fin = "sig400"
if len(sys.argv) >= 3:
  batch = int(sys.argv[2])
if "HT" in fin:
  fs = np.loadtxt("rootfiles/%s.txt"%(fin),dtype=str)
  start = 100*batch
  end = 100*(batch+1)
  if (end > len(fs)):
    fs = fs[start:]
  else:
    fs=fs[start:end]
  fileset = {
           fin : ["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCDv2/%s/%s"%(fin,f) for f in fs],
           #fin: ['root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCDv2/HT2000/4C832A72-AF24-D045-ACE7-67DFC5D01F90.root']
  }
elif "Run" in fin:
  #Runs = ["RunA","RunB","RunC"]
  fs = np.loadtxt("rootfiles/Data%s.txt"%(fin),dtype=str)
  fs=fs[10*batch:10*(batch+1)]
  fileset = {
            fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Data/%s/%s"%(fin,f) for f in fs]
  }  
elif "Trigger" in fin:
  #Runs = ["RunA","RunB","RunC"]
  #runInteractive=True
  fs = np.loadtxt("rootfiles/%s.txt"%(fin),dtype=str)
  fs=fs[10*batch:10*(batch+1)]
  fileset = {
            fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Data/ScoutingPFCommissioning+Run2018A-v1+RAW/%s"%(f) for f in fs]
  }  
else:
  signal=True
  runInteractive=True
  decays = ["darkPho","darkPhoHad","generic"]
  fileset = {
            fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Signal/%s_%s_PV.root"%(fin,decays[batch])]
            #fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Signal/%s_%s_dR.root"%(fin,decays[batch])]
  }  


if __name__ == "__main__":
    tic = time.time()
    #print(sys.argv)
    #dask.config.set({"distributed.scheduler.worker-ttl": "10min"})

    #cluster = LPCCondorCluster(
    #      memory="8GB",
    #)
    # minimum > 0: https://github.com/CoffeaTeam/coffea/issues/465
    #cluster.adapt(minimum=1, maximum=10)
    #client = Client(cluster)

    exe_args = {
        #"client": client,
        "savemetrics": True,
        "schema": BaseSchema, #nanoevents.NanoAODSchema,
        #"align_clusters": True,
    }

    proc = MyProcessor()

    print("Waiting for at least one worker...")
    #client.wait_for_workers(1)
    print("running %s %s"%(fin,batch))
    if(runInteractive):
      out = processor.run_uproot_job(
        fileset,
        treename="mmtree/tree",
        processor_instance=proc,
        executor=processor.iterative_executor,
        executor_args={
            "schema": BaseSchema,
        },
       # maxchunks=4,
      )
      print(out)
    else:
      out,metrics = processor.run_uproot_job(
          fileset,
          treename="mmtree/tree",
          processor_instance=proc,
          executor=processor.dask_executor,
          executor_args=exe_args,
          #dynamic_chunksize= {"memory":2048},
          chunksize= 10000,
          # remove this to run on the whole fileset:
          #maxchunks=10,
        #executor=processor.iterative_executor,
        #executor_args={
        #    "schema": BaseSchema,
        #},
      )

      elapsed = time.time() - tic
      print(f"Output: {out}")
      print(f"Metrics: {metrics}")
      print(f"Finished in {elapsed:.1f}s")
      print(f"Events/s: {metrics['entries'] / elapsed:.0f}")

    with open("outhists/myhistos_%s_%s.p"%(fin,batch), "wb") as pkl_file:
        pickle.dump(out, pkl_file)
