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
from lpcjobqueue import LPCCondorCluster
import sys
import vector
vector.register_awkward()
from math import pi

# register our candidate behaviors
from coffea.nanoevents.methods import candidate
ak.behavior.update(candidate.behavior)

signal=False
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
    #norm = ak.sum(particles.p ** r, axis=0, keepdims=True)
    norm = ak.sum(particles.p ** r, axis=1, keepdims=True)
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
                  ]])
    s = np.squeeze(np.moveaxis(s, 2, 0),axis=3)
    evals = np.sort(np.linalg.eigvalsh(s))
    return evals

def packtrig(output,vals,var):
        output["trigdist_%s"%(var)].fill(cut="Cut 0:No cut", v1=vals[0][var])
        output["trigdist_%s"%(var)].fill(cut="Mu Trig noRef", v1=vals[1][var]) 
        output["trigdist_%s"%(var)].fill(cut="HT Trig noRef", v1=vals[2][var]) 
        output["trigdist_%s"%(var)].fill(cut="HT Trig MuRef", v1=vals[3][var]) 
        return output
def packdist(output,vals,var):
        output["dist_%s"%(var)].fill(cut="cut 0:No cut", v1=vals[0][var])
        output["dist_%s"%(var)].fill(cut="cut 1:HT Trig", v1=vals[1][var]) 
        output["dist_%s"%(var)].fill(cut="cut 2:Ht>=600", v1=vals[2][var])
        output["dist_%s"%(var)].fill(cut="cut 3:fj>=2", v1=vals[3][var])
        if("PFcand_nconst" in var):
          output["dist_%s"%(var)].fill(cut="cut 4:eventBoosted Sphericity >=0.6", v1=vals[4][var])
        else:
          output["dist_%s"%(var)].fill(cut="cut 4:nPFCand>=140", v1=vals[4][var]) 
        #output["dist_%s"%(var)].fill(cut="cut 4:FJ nPFCand>=80", v1=vals[4][var]) 
        return output
def packtrkFKID(output,vals,var):
        output["dist_trkIDFK_%s"%(var)].fill(cut="cut 0:Preselection",           v1=ak.flatten(vals[0][var]))
        output["dist_trkIDFK_%s"%(var)].fill(cut="cut 1: |eta| < 2.4",           v1=ak.flatten(vals[1][var]))
        output["dist_trkIDFK_%s"%(var)].fill(cut="cut 2: q != 0",                v1=ak.flatten(vals[2][var]))
        output["dist_trkIDFK_%s"%(var)].fill(cut="cut 3: PV = 0",                v1=ak.flatten(vals[3][var]))
        output["dist_trkIDFK_%s"%(var)].fill(cut="cut 4: PFcand_pt > 0.5",       v1=ak.flatten(vals[4][var]))
        output["dist_trkIDFK_%s"%(var)].fill(cut="cut 5: PFcand_pt > 0.6",       v1=ak.flatten(vals[5][var]))
        output["dist_trkIDFK_%s"%(var)].fill(cut="cut 6: PFcand_pt > 0.7",       v1=ak.flatten(vals[6][var]))
        output["dist_trkIDFK_%s"%(var)].fill(cut="cut 7: PFcand_pt > 0.75",      v1=ak.flatten(vals[7][var]))
        output["dist_trkIDFK_%s"%(var)].fill(cut="cut 8: PFcand_pt > 0.8",       v1=ak.flatten(vals[8][var]))
        output["dist_trkIDFK_%s"%(var)].fill(cut="cut 9: PFcand_pt > 0.9",       v1=ak.flatten(vals[9][var]))
        output["dist_trkIDFK_%s"%(var)].fill(cut="cut 10: PFcand_pt > 1.0",      v1=ak.flatten(vals[10][var]))
        return output
def packtrkID(output,vals,var,var2):
#        output["dist_trkID_%s"%(var)].fill(cut="cut 1: dR <=0.05",       v1=ak.flatten(vals[1][var]))
        output["dist_trkID_%s"%(var)].fill(cut="cut 0:Preselection",           v1=ak.flatten(vals[0][var]), v2=ak.flatten(vals[0][var2]))
        output["dist_trkID_%s"%(var)].fill(cut="cut 1: PFcand_pt > 0.5",       v1=ak.flatten(vals[1][var]), v2=ak.flatten(vals[1][var2]))
        output["dist_trkID_%s"%(var)].fill(cut="cut 2: PFcand_pt > 0.6",       v1=ak.flatten(vals[2][var]), v2=ak.flatten(vals[2][var2]))
        output["dist_trkID_%s"%(var)].fill(cut="cut 3: PFcand_pt > 0.7",       v1=ak.flatten(vals[3][var]), v2=ak.flatten(vals[3][var2]))
        output["dist_trkID_%s"%(var)].fill(cut="cut 4: PFcand_pt > 0.75",      v1=ak.flatten(vals[4][var]), v2=ak.flatten(vals[4][var2]))
        output["dist_trkID_%s"%(var)].fill(cut="cut 5: PFcand_pt > 0.8",       v1=ak.flatten(vals[5][var]), v2=ak.flatten(vals[5][var2]))
        output["dist_trkID_%s"%(var)].fill(cut="cut 6: PFcand_pt > 0.9",       v1=ak.flatten(vals[6][var]), v2=ak.flatten(vals[6][var2]))
        output["dist_trkID_%s"%(var)].fill(cut="cut 7: PFcand_pt > 1.0",       v1=ak.flatten(vals[7][var]), v2=ak.flatten(vals[7][var2]))
        return output
def packdistflat(output,vals,var,prefix=""):
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 0:No cut",       v1=ak.flatten(vals[0][var]))
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 1:HT Trig",      v1=ak.flatten(vals[1][var])) 
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 2:Ht>=600",      v1=ak.flatten(vals[2][var]))
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 3:fj>=2",        v1=ak.flatten(vals[3][var]))
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 4:nPFCand>=140", v1=ak.flatten(vals[4][var])) 
        #output["dist_%s"%(var)].fill(cut="cut 4:FJ nPFCand>=80", v1=ak.flatten(vals[4][var])) 
        return output
def packdist_fjn1(output,vals,var):
        output["dist_fjn1_%s"%(var)].fill(cut="cut 0:No cut",       v1=vals[0][var])
        output["dist_fjn1_%s"%(var)].fill(cut="cut 1:HT Trig",      v1=vals[1][var]) 
        output["dist_fjn1_%s"%(var)].fill(cut="cut 2:Ht>=600",      v1=vals[2][var])
        output["dist_fjn1_%s"%(var)].fill(cut="cut 3:nPFCand>=140", v1=vals[3][var]) 
        #output["dist_fjn1_%s"%(var)].fill(cut="cut 3:FJ nPFCand>=80", v1=vals[3][var]) 
        output["dist_fjn1_%s"%(var)].fill(cut="cut 4:BSphericity >=0.4",        v1=vals[4][var])
        return output
def packSR(output,vals):
        output["SR1"].fill(axis="axis",       nPFCand=vals[3]["n_pfcand"],eventBoostedSphericity=vals[3]["eventBoosted_sphericity"])
        return output
def packSR2(output,vals):
        output["SR2"].fill(axis="axis",       FatJet_nconst=vals[3]["FatJet_nconst"],eventBoostedSphericity=vals[3]["eventBoosted_sphericity"])
        return output
pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50])
eta_bins = np.array(range(-250,250,25))/100.
phi_bins = np.array(range(-31,31,5))/10.
class MyProcessor(processor.ProcessorABC):
    def __init__(self):
        self._accumulator = processor.dict_accumulator({
            "sumw": processor.defaultdict_accumulator(float),
            "SR1" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR2" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("FatJet_nconst","FatJet_nconst",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
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
                      hist.Bin("v1","Ht",100,0,2500)
            ),
            "dist_sphere1": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphere1",50,0,1)
            ),
            "dist_sphere1b": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphere1b",50,0,1)
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
#             ###########TRACKS
#            "dist_trkFKID_PFcand_pt": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","PFcand_pt",pt_bins),
#                      hist.Bin("v2","PFcand_dR",100,0,0.3)
#            ),
#            "dist_trkFKID_PFcand_eta": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","PFcand_eta",eta_bins),
#                      hist.Bin("v2","PFcand_dR",100,0,0.3)
#            ),
#            "dist_trkFKID_PFcand_phi": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","PFcand_phi",phi_bins),
#                      hist.Bin("v2","PFcand_dR",100,0,0.3)
#            ),
#            "dist_PFcand_dR": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","PFcand_mindR",100,0,0.3)
#            ),
#            "dist_PFcand_alldR": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","PFcand_alldR",100,0,0.3)
#            ),
#            "dist_trkID_gen_pt": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","gen_pt",pt_bins),
#                      hist.Bin("v2","gen_dR",100,0,0.3)
#            ),
#            "dist_trkID_gen_eta": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","gen_eta",eta_bins),
#                      hist.Bin("v2","gen_dR",100,0,0.3)
#            ),
#            "dist_trkID_gen_phi": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","gen_phi",phi_bins),
#                      hist.Bin("v2","gen_dR",100,0,0.3)
#            ),
#            "dist_gen_dR": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","gen_dR",100,0,0.3)
#            ),
#            "dist_gen_pt": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","gen_pt",pt_bins)
#            ),
#            "dist_gen_eta": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","gen_eta",eta_bins)
#            ),
#            "dist_gen_phi": hist.Hist(
#                      "Events",
#                      hist.Cat("cut","Cutflow"),
#                      hist.Bin("v1","gen_phi",phi_bins)
#            ),
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
        output = self.accumulator.identity()
        #print(events)
        dataset = arrays.metadata['dataset']
        #arrays = {k: v for k,v in events.arrays(how=dict).items()}
        output["sumw"][dataset] += len(arrays) # get number of events
        tright = [item[7] for item in arrays["hltResult"]]
        trigmu = [item[2] for item in arrays["hltResult"]]
        vals0 = ak.zip({
               'ht': arrays["ht"],
               'n_pfcand': arrays["n_pfcand"],
               'event_sphericity': arrays["event_sphericity"],
               'eventBoosted_sphericity': arrays["eventBoosted_sphericity"],
               'n_fatjet': arrays["n_fatjet"],
               'n_jetId': arrays["n_jetId"],
               'n_pfMu': arrays["n_pfMu"],
               'n_pfEl': arrays["n_pfEl"],
               'bCandmask': [True if len(x) > 1 else False for x in arrays["bPFcand_pt"]],
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
                         'PFcand_alldR': arrays["PFcand_alldR"],
                         'PFcand_fromsuep': arrays["PFcand_fromsuep"],
                         'PFcand_q': arrays["PFcand_"],
                         'PFcand_vertex': arrays["PFcand_vertex"],
          },with_name="Momentum4D")
          vals_gen0 = ak.zip({
                         'pt' : arrays["gen_pt"],
                         'eta': arrays["gen_eta"],
                         'phi': arrays["gen_phi"],
                         'mass': arrays["gen_mass"],
                         'gen_dR':  arrays["gen_dR"],
                         'gen_fromSuep':  arrays["gen_fromSuep"],
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
                         'PFcand_q': arrays["PFcand_"],
                         'PFcand_vertex': arrays["PFcand_vertex"],
          }, with_name="Momentum4D")
        bCands = ak.zip({
            "pt":  [x for x in arrays["bPFcand_pt"]  if len(x) > 1],
            "eta": [x for x in arrays["bPFcand_eta"] if len(x) > 1],
            "phi": [x for x in arrays["bPFcand_phi"] if len(x) > 1],
            "mass":[x for x in arrays["bPFcand_m"]   if len(x) > 1] 
        }, with_name="Momentum4D") 



        track_cuts = ((arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>=0.50))
        tracks_cut0 = vals_tracks0[track_cuts]




        recluster_fatjet1  = vals_fatjet0[ vals0.bCandmask] # bCandmask implicitly has a cut on nFatJets >1 and nbPFCands >1
        SUEP_cand = ak.where(recluster_fatjet1.FatJet_nconst[:,1]<=recluster_fatjet1.FatJet_nconst[:,0],recluster_fatjet1[:,0],recluster_fatjet1[:,1])
        ISR_cand  = ak.where(recluster_fatjet1.FatJet_nconst[:,1]> recluster_fatjet1.FatJet_nconst[:,0],recluster_fatjet1[:,0],recluster_fatjet1[:,1])

        if (redoISRRM):
          boost_IRM = ak.zip({
              "px": SUEP_cand.px*-1,
              "py": SUEP_cand.py*-1,
              "pz": SUEP_cand.pz*-1,
              "mass": SUEP_cand.mass
          }, with_name="Momentum4D")
          ISR_cand_b = ISR_cand.boost_p4(boost_IRM)

          recotracks_IRM = tracks_cut0[vals0.bCandmask]
          tracks_IRM = recotracks_IRM.boost_p4(boost_IRM)
          IRM_cands = tracks_IRM[abs(tracks_IRM.deltaphi(ISR_cand_b)) >= 1.6]
          print(len(IRM_cands))
  

       ## resolution studies
       if(signal):
          scalar = scalar0[vals0.bCandmask]
          res_pt = SUEP_cand.pt/scalar["pt"]
          res_mass = SUEP_cand.mass/scalar["mass"]
          res_dPhi = SUEP_cand.phi-scalar["phi"]
          res_dEta = SUEP_cand.eta-scalar["eta"]
          res_dR = np.sqrt(res_dPhi*res_dPhi + res_dEta*res_dEta)
       ############################################################################## 




        print(len(bCands),len(vals0[vals0.bCandmask]))
        eigs = sphericity(self,bCands,2.0)
        eigs2 = sphericity(self,IRM_cands,2.0)
        spherex0 = vals0[vals0.bCandmask]
        spherex0["sphere1"] = 1.5 * (eigs[:,1]+eigs[:,0])
        spherex0["sphere1b"] = 1.5 * (eigs2[:,1]+eigs2[:,0])
        if(eventDisplay_knob):
          for evt in range(len(bCands)):
            print(evt)
            plot_display(evt,recotracks_IRM[evt],tracks_IRM[evt],SUEP_cand[evt],ISR_cand[evt],ISR_cand_b[evt],spherex0["sphere1b"][evt],len(IRM_cands[evt]))
        
        spherex1 = spherex0[spherex0.triggerHt >= 1]
        spherex2 = spherex1[spherex1.ht >= 600]
        spherex3 = spherex2[spherex2.FatJet_ncount30 >= 2]
        spherex4 = spherex3[spherex3.n_pfcand >= 140]
        
        sphere1 = [spherex0,spherex1,spherex2,spherex3,spherex4]
        
        #cutflow Ht
        vals1 = vals0[vals0.triggerHt >= 1]
        vals2 = vals1[vals1.ht >= 600]
        vals3 = vals2[vals2.FatJet_ncount50 >= 2]
        #vals3 = vals2[vals2.n_fatjet >= 2]
        #vals4 = vals3[vals3.FatJet_nconst >= 80]
        vals4 = vals3[vals3.n_pfcand >= 140]
        vals4x = vals3[vals3.eventBoosted_sphericity >= 0.6]

        vals_jet1 = vals_jet0[vals0.triggerHt >= 1]
        vals_jet2 = vals_jet1[vals1.ht >= 600]
        vals_jet3 = vals_jet2[vals2.FatJet_ncount50 >= 2]
        #vals_jet3 = vals_jet2[vals2.n_fatjet >= 2]
        #vals_jet4 = vals_jet3[vals3.FatJet_nconst >= 80]
        vals_jet4 = vals_jet3[vals3.n_pfcand >= 140]
        
        vals_fatjet1 = vals_fatjet0[vals0.triggerHt >= 1]
        vals_fatjet2 = vals_fatjet1[vals1.ht >= 600]
        vals_fatjet3 = vals_fatjet2[vals2.FatJet_ncount50 >= 2]
        #vals_fatjet3 = vals_fatjet2[vals2.n_fatjet >= 2]
        #vals_fatjet4 = vals_fatjet3[vals3.FatJet_nconst >= 80]
        vals_fatjet4 = vals_fatjet3[vals3.n_pfcand >= 140]
        
     
        vals_tracks1 = tracks_cut0[vals0.triggerHt >= 1]
        vals_tracks2 = vals_tracks1[vals1.ht >= 600]
        vals_tracks3 = vals_tracks2[vals2.FatJet_ncount50 >= 2]
        #vals_tracks3 = vals_tracks2[vals2.n_fatjet >= 2]
        #vals_tracks4 = vals_tracks3[vals3.FatJet_nconst >= 80]
        vals_tracks4 = vals_tracks3[vals3.n_pfcand >= 140]

        vals = [vals0,vals1,vals2,vals3,vals4]
        valsx = [vals0,vals1,vals2,vals3,vals4x]
        vals_jet = [vals_jet0,vals_jet1,vals_jet2,vals_jet3,vals_jet4]
        vals_fatjet = [vals_fatjet0,vals_fatjet1,vals_fatjet2,vals_fatjet3,vals_fatjet4]
        vals_tracks = [vals_tracks0,vals_tracks1,vals_tracks2,vals_tracks3,vals_tracks4]

        #fatjet n-1 cutflow
        #fj3 = vals2[vals2.FatJet_nconst >=80]
        fj3 = vals2[vals2.n_pfcand >=140]
        fj4 = fj3[fj3.eventBoosted_sphericity >= 0.6]
        vals_fj = [vals0,vals1,vals2,fj3,fj4]


        #trig cutflow
        trig1 = vals0[vals0.triggerMu >=1]
        trig2 = vals0[vals0.triggerHt >=1]
        trig3 = trig1[trig1.triggerHt >=1]
        trigs = [vals0,trig1,trig2,trig3]

        if(signal):
          trkID1 = vals_tracks0[(vals0.triggerHt >= 1) & (vals0.ht >=600) &(vals0.FatJet_ncount50 >= 2)]

          trkID2 = trkID1[abs(trkID1.eta) < 2.4]
          trkID3 = trkID2[trkID2.q != 0]
          trkID4 = trkID3[trkID3.vertex == 0]
          trkID5 = trkID4[trkID4.pt > 0.5]
          trkID6 = trkID5[trkID5.pt > 0.6]
          trkID7 = trkID6[trkID6.pt > 0.7]
          trkID8 = trkID7[trkID7.pt > 0.75]
          trkID9 = trkID8[trkID8.pt > 0.8]
          trkID10 = trkID9[trkID9.pt > 0.9]
          trkID11 = trkID10[trkID10.pt > 1.0]
          trkID = [trkID1,trkID2,trkID3,trkID4,trkID5,trkID6,trkID7,trkID8,trkID9,trkID10,trkID11]
          output = packtrkFKID(output,trkID,"pt" ,"PFcand_dR")
          output = packtrkFKID(output,trkID,"eta","PFcand_dR")
          output = packtrkFKID(output,trkID,"phi","PFcand_dR")

          vals_gen1 = vals_gen0[vals0.triggerHt >= 1]
          vals_gen2 = vals_gen1[vals1.ht >= 600]
          vals_gen3 = vals_gen2[vals2.FatJet_ncount50 >= 2]
          vals_gen4 = vals_gen3[vals3.n_pfcand >= 140]
          #vals_gen4 = vals_gen3[vals3.FatJet_nconst >= 80]
          vals_gen = [vals_gen0,vals_gen1,vals_gen2,vals_gen3,vals_gen4]
          trkID5x = vals_gen3[vals_gen3.gen_pt > 0.5]
          trkID6x = trkID5x[trkID5x.gen_pt > 0.6]
          trkID7x = trkID6x[trkID6x.gen_pt > 0.7]
          trkID8x = trkID7x[trkID7x.gen_pt > 0.75]
          trkID9x = trkID8x[trkID8x.gen_pt > 0.8]
          trkID10x = trkID9x[trkID9x.gen_pt > 0.9]
          trkID11x = trkID10x[trkID10x.gen_pt > 1.0]
          trkIDx = [vals_gen3,trkID5x,trkID6x,trkID7x,trkID8x,trkID9x,trkID10x,trkID11x]
          output = packtrkID(output,trkIDx,"gen_pt" ,"gen_dR")
          output = packtrkID(output,trkIDx,"gen_eta","gen_dR")
          output = packtrkID(output,trkIDx,"gen_phi","gen_dR")
          output = packdistflat(output,vals_tracks,"PFcand_dR")
          output = packdistflat(output,vals_tracks,"PFcand_alldR")
          output = packdistflat(output,vals_gen,"gen_pt")
          output = packdistflat(output,vals_gen,"gen_dR")
          output = packdistflat(output,vals_gen,"gen_eta")
          output = packdistflat(output,vals_gen,"gen_phi")

        output = packtrig(output,trigs,"ht")
        output = packtrig(output,trigs,"n_pfMu")
        #fill hists
        output = packSR(output,vals)
        output = packSR2(output,vals)
        output = packdist(output,vals,"ht")
        output = packdist(output,vals,"n_pfcand")
        output = packdist(output,vals,"event_sphericity")
        output = packdist(output,vals,"eventBoosted_sphericity")
        output = packdist(output,vals,"n_fatjet")
        output = packdist(output,vals,"n_jetId")
        output = packdist(output,vals,"n_pfMu")
        output = packdist(output,vals,"n_pfEl")
        
        output = packdistflat(output,vals_jet,"Jet_pt")
        output = packdistflat(output,vals_jet,"Jet_eta")
        output = packdistflat(output,vals_jet,"Jet_phi")
        output = packdistflat(output,vals_fatjet,"pt","FatJet_")
        output = packdistflat(output,vals_fatjet,"eta","FatJet_")
        output = packdistflat(output,vals_fatjet,"phi","FatJet_")
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
        
        #print(sphere1)
        #output = packdist(output,vals,"sphere1")
        output = packdist(output,sphere1,"sphere1")
        output = packdist(output,sphere1,"sphere1b")

        return output

    def postprocess(self, accumulator):
        return accumulator


# https://github.com/scikit-hep/uproot4/issues/122
uproot.open.defaults["xrootd_handler"] = uproot.source.xrootd.MultithreadedXRootDSource


fin = "HT2000"
batch = 0
if len(sys.argv) >= 2:
  fin = sys.argv[1]
#fin = "sig400"
if len(sys.argv) >= 3:
  batch = int(sys.argv[2])
if "HT" in fin:
  fs = np.loadtxt("rootfiles/%s.txt"%(fin),dtype=str)
  fs=fs[300*batch:10*(batch+1)]
  fileset = {
           fin : ["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCDv2/%s/%s"%(fin,f) for f in fs],
  }
elif "Run" in fin:
  #Runs = ["RunA","RunB","RunC"]
  fs = np.loadtxt("rootfiles/Data%s.txt"%(fin),dtype=str)
  fs=fs[30*batch:30*(batch+1)]
  fileset = {
            fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Data/%s/%s"%(fin,f) for f in fs]
  }  
else:
  decays = ["darkPho","darkPhoHad","generic"]
  fileset = {
            #fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Signal/%s_%s_dR.root"%(fin,decays[batch])]
            fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Signal/%s_%s_dR_num.root"%(fin,decays[batch])]
  }  


if __name__ == "__main__":
    tic = time.time()
    #print(sys.argv)
    cluster = LPCCondorCluster()
    # minimum > 0: https://github.com/CoffeaTeam/coffea/issues/465
    cluster.adapt(minimum=1, maximum=10)
    client = Client(cluster)

    exe_args = {
        "client": client,
        "savemetrics": True,
        "schema": BaseSchema, #nanoevents.NanoAODSchema,
        "align_clusters": True,
    }

    proc = MyProcessor()

    print("Waiting for at least one worker...")
    client.wait_for_workers(1)
    print("running %s %s"%(fin,batch))
#    out,metrics = processor.run_uproot_job(
#        fileset,
#        treename="mmtree/tree",
#        processor_instance=proc,
#        executor=processor.dask_executor,
#        executor_args=exe_args,
#        # remove this to run on the whole fileset:
#        #maxchunks=10,
#      #executor=processor.iterative_executor,
#      #executor_args={
#      #    "schema": BaseSchema,
#      #},
#    )
#
#    elapsed = time.time() - tic
#    print(f"Output: {out}")
#    print(f"Metrics: {metrics}")
#    print(f"Finished in {elapsed:.1f}s")
#    print(f"Events/s: {metrics['entries'] / elapsed:.0f}")
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

    with open("outhists/myhistos_%s_%s.p"%(fin,batch), "wb") as pkl_file:
        pickle.dump(out, pkl_file)
