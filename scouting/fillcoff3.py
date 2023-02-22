import awkward as ak
from coffea import hist, processor, nanoevents, lumi_tools
import uproot
from coffea.nanoevents import NanoEventsFactory, BaseSchema
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import pickle
import time
from distributed import Client
#from lpcjobqueue import LPCCondorCluster
import sys
import vector
from math import pi
import dask
import fastjet

from coffea.jetmet_tools import FactorizedJetCorrector, JetCorrectionUncertainty
from coffea.jetmet_tools import JECStack, CorrectedJetsFactory
from coffea.lookup_tools import extractor

#from coffea.analysis_tools import Weights


# register our candidate behaviors
from coffea.nanoevents.methods import candidate
ak.behavior.update(candidate.behavior)

from workflow.getArrays import *
from workflow.fillOutput import *
from workflow.systematics import *
from workflow.utils import *

########SYSTEMATICS
trigSystematics = 0 #0: nominal, 1: up err, 2: down err
AK4sys = 0 #o: nominal, 1: err up, 2 err dowm
AK15sys = 0 #o: nominal, 1: err up, 2 err dowm
PUSystematics = 0 #0: nominal, 1: up err, 2: down err
PSSystematics = 0 #0: nominal, 1: up err, 2: down err
PrefireSystematics = 0 #0: nominal, 1: up err, 2: down err
higgsSystematics = 0
killTrks = False
era=18
datatype= "MC"
runoffline=True
HEM_veto = True
lepton_veto = True

########################
eventDisplay_knob= False#True
redoISRRM = True


pt_bins = np.array([0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50])
eta_bins = np.array(range(-250,250,25))/100.
pt_bins2 = np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.75,1,1.25,1.5,2.0,3,10,20,50])
eta_bins2 = np.array(range(-250,275,25))/100.
phi_bins = np.array(range(-31,31,5))/10.
class MyProcessor(processor.ProcessorABC):
    def __init__(self):
        self._accumulator = processor.dict_accumulator({
            "sumw": processor.defaultdict_accumulator(float),
            "SR1_isrsuep_0" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_isrsuep_1" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_isrsuep_2" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
            "SR1_isrsuep_3" : hist.Hist(
                      "Events",
                      hist.Cat("axis","Axis"),
                      hist.Bin("nPFCand","nPFCand",300,0,300),
                      hist.Bin("eventBoostedSphericity","eventBoostedSphericity",100,0,1)
            ),
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
            "trigdist_FatJet_nconst": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","SUEP Jet multiplicity",100,0,300)
            ),
            "trigdist_event_sphericity": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","eventSphericity (not boosted)",100,0,1)
            ),
            "trigdist_ht": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ht",1500,0,1500)
            ),
            "trigdist_ht20": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ht",1500,0,1500)
            ),
            "trigdist_ht30": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ht",1500,0,1500)
            ),
            "trigdist_ht40": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ht",1500,0,1500)
            ),
            "trigdist_ht50": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ht",1500,0,1500)
            ),
            "trigdist_n_pfMu": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","n_pfMu",15,0,15)
            ),
            "dist_ht": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Ht",3500,0,3500)
            ),
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
            "dist_sphere_isrsuep": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphere_isr",50,0,1)
            ),
            "dist_sphere1_isrsuep": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Sphere1_isr",50,0,1)
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
            "dist_cparam_suep": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","cParam_suep",50,0,1)
            ),
            "dist_cparam1_suep": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","cParam1_suep",50,0,1)
            ),
            "dist_dparam_suep": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","dParam_suep",50,0,1)
            ),
            "dist_dparam1_suep": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","dParam1_suep",50,0,1)
            ),
            "dist_aplanarity_suep": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Aplanarity_suep",50,0,1)
            ),
            "dist_aplanarity1_suep": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","Aplanarity1_suep",50,0,1)
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
            "trig2d_ht_FatJet_nconst" : hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ht",150,0,1500),
                      hist.Bin("v2","Suep jet Track Multiplicity",50,0,300)
            ),
            "trig2d_ht_event_sphericity" : hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ht",150,0,1500),
                      hist.Bin("v2","Sphericity (unboosted)",50,0,1)
            ),
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
            "dist_PFcand_ncount60": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand60",50,0,300)
            ),
            "dist_PFcand_ncount70": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand70",50,0,300)
            ),
            "dist_PFcand_ncount75": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand75",50,0,300)
            ),
            "dist_PFcand_ncount80": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand80",50,0,300)
            ),
            "dist_PFcand_ncount90": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","nPFCand90",50,0,300)
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
                      hist.Bin("v1","Jet_pt",100,0,1000)
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
                      hist.Bin("v1","FatJet_pt",100,0,1000)
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
            "dist_offlinetrk_pt_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","offlinetrk_pt",pt_bins2),
                      hist.Bin("v2","offlinetrk_eta",eta_bins2)
            ),
            "dist_offlinetrk_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","offlinetrk_pt",pt_bins2)
            ),
            "dist_offlinetrk_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","offlinetrk_eta",eta_bins2)
            ),
            "dist_offlinetrk_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","offlinetrk_phi",phi_bins)
            ),
            "dist_PFcand_pt_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_pt",pt_bins2),
                      hist.Bin("v2","PFcand_eta",eta_bins2)
            ),
            "dist_PFcand_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_pt",pt_bins2)
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
                      hist.Bin("v1","PFcand_mindR",50,0,0.3)
            ),
            "dist_PFcand_alldR": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","PFcand_alldR",50,0,0.3)
            ),
            "dist_tau21": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","tau21",100,0,1)
            ),
            "dist_tau32": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","tau32",100,0,1)
            ),
            "dist_SUEP_girth": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","SUEP_girth",100,0,2)
            ),
            "dist_SUEP_ptDispersion": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","SUEP_ptDispersion",100,0,1)
            ),
            "dist_SUEP_lesHouches": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","SUEP_lesHouches",100,0,2)
            ),
            "dist_SUEP_thrust": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","SUEP_thrust",100,0,2)
            ),
            "dist_SUEP_beta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","SUEP_beta",100,0,5)
            ),
            "dist_SUEP_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","SUEP_pt",50,0,500)
            ),
            "dist_SUEP_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","SUEP_eta",eta_bins)
            ),
            "dist_SUEP_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","SUEP_phi",phi_bins)
            ),
            "dist_SUEP_mass": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","SUEP_mass",100,0,1000)
            ),
            "dist_ISR_beta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ISR_beta",100,0,5)
            ),
            "dist_ISR_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ISR_pt",50,0,500)
            ),
            "dist_ISR_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ISR_eta",eta_bins)
            ),
            "dist_ISR_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ISR_phi",phi_bins)
            ),
            "dist_ISR_mass": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","ISR_mass",100,0,1000)
            ),
            "dist_scalar_beta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","scalar_beta",100,0,5)
            ),
            "dist_scalar_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","scalar_pt",100,0,500)
            ),
            "dist_scalar_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","scalar_eta",eta_bins)
            ),
            "dist_scalar_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","scalar_phi",phi_bins)
            ),
            "dist_scalar_mass": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","scalar_mass",100,0,1000)
            ),
            "dist_res_beta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","res_pt",50,-5,5)
            ),
            "dist_res_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","res_pt",50,-1000,300)
            ),
            "dist_res_mass": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","res_mass",50,-1000,300)
            ),
            "dist_res_dR": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","res_dR",50,0,6)
            ),
            "dist_res_dEta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","res_dEta",100,-3,3)
            ),
            "dist_res_dPhi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","res_dPhi",100,-7,7)
            ),
            "dist_trkID_gen_pt": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_pt",pt_bins),
                      hist.Bin("v2","gen_dR",100,0,0.3),
                      hist.Bin("v3","gen_PV",4,0,4)
            ),
            "dist_trkID_gen_eta": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_eta",eta_bins),
                      hist.Bin("v2","gen_dR",100,0,0.3),
                      hist.Bin("v3","gen_PV",4,0,4)
            ),
            "dist_trkID_gen_phi": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_phi",phi_bins),
                      hist.Bin("v2","gen_dR",100,0,0.3),
                      hist.Bin("v3","gen_PV",4,0,4)
            ),
            "dist_gen_dR": hist.Hist(
                      "Events",
                      hist.Cat("cut","Cutflow"),
                      hist.Bin("v1","gen_dR",50,0,0.3)
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
        dataset = arrays.metadata['dataset']
        output["sumw"][dataset] += len(arrays) # get number of events
        if "DATA" in datatype:
          arrays = applyGoldenJSON(era,arrays)

        vals0 = load_vals(arrays,datatype,era) 
        vals_vertex0 = load_vertex(arrays) 
        vals_jet0 = load_jets(arrays,datatype) 
        corrected_jets = correctJets(vals_jet0,arrays.caches[0],era,datatype,Run)
        if HEM_veto:
          corrected_jets = corrected_jets[ (corrected_jets["eta"] < -3.0) | (corrected_jets["eta"] > -1.3) | (corrected_jets["phi"] < -1.57) | (corrected_jets["phi"] > -0.87)]


        vals_nsub0 = load_nsub(arrays) 
        vals_tracks0 = load_tracks(arrays,signal) 
        calculateHT(vals0,corrected_jets,AK4sys)
        vals_offline0 = load_offline(arrays) 

        vals_electron0 = load_electrons(arrays)
        vals_muon0 = load_muons(arrays)
        vals0["selected_electrons"] = ak.count(vals_electron0["pt"][(vals_electron0["electron_ID"] == 1 )
        & (vals_electron0["pt"] >= 15 )
        & (abs(vals_electron0["dxy"]) < 0.05 + 0.05*(abs(vals_electron0["eta"])> 1.479))
        & (abs(vals_electron0["dz"]) < 0.10 + 0.1*(abs(vals_electron0["eta"])> 1.479) )
        & ((abs(vals_electron0["eta"]) < 1.444 ) | (abs(vals_electron0["eta"]) > 1.566 ))
        & (abs(vals_electron0["eta"]) < 2.5)
        ],axis=-1)

        vals0["selected_muons"] = ak.count(vals_muon0["pt"][(vals_muon0["pt"] >=10) 
	& (abs(vals_muon0["dxy"]) <= 0.02)
	& (abs(vals_muon0["dz"]) <= 0.1)
	& (abs(vals_muon0["muon_trkiso"]) < 0.10 )
	& (abs(vals_muon0["eta"]) < 2.4 )
	& ((vals_muon0["muon_global"] ==1) | (vals_muon0["muon_tracker"]==1))
	],axis =-1)

        vals0["lepton_veto"] = (vals0["selected_electrons"] == 0) & (vals0["selected_muons"] ==0)
        ####Weights#######

        if "DATA" not in datatype and "Trigger" not in datatype:
        	if era==16:
        		vals0["trigwgt"] =1
        	else: 
        		vals0["trigwgt"] = gettrigweights(vals0["ht"],trigSystematics,era)
        	vals0["PUwgt"] = pileup_weight(vals0["PU"],PUSystematics,era)*vals0["lepton_veto"]
       		vals0["PSwgt"] = PS_weight(arrays,PSSystematics)
       		vals0["Prefirewgt"] = prefire_weight(arrays,PrefireSystematics)
        	vals0["wgt"] = vals0["trigwgt"]*vals0["PUwgt"]*vals0["PSwgt"]*vals0["Prefirewgt"]
        else:
                vals0["wgt"] = 1*vals0["lepton_veto"]
                vals0["PUwgt"] = 1*vals0["lepton_veto"]
        if(signal):
          vals_gen0 = load_gen(arrays) 
          scalar0  = load_scalar(arrays)
          if "125" in fin:
            vals0["higgswgt"] = higgs_reweight(scalar0["pt"],higgsSystematics)
            vals0["wgt"] = vals0["wgt"]*vals0["higgswgt"]
          vals_gen0["wgt"] = vals0["wgt"]
          scalar0["wgt"] = vals0["wgt"]
          alldRtracks = ak.zip({'PFcand_alldR': np.sqrt(arrays["PFcand_alldR"])})
          alldRtracks["PUwgt"] = vals0["PUwgt"] 
          alldRtracks = ak.flatten(alldRtracks)
          output = packsingledist(output,alldRtracks,"PFcand_alldR",wgt=False)
        vals_nsub0["wgt"] = vals0["wgt"]
        vals_nsub0["PUwgt"] = vals0["PUwgt"]
        vals_tracks0["wgt"] = vals0["wgt"]
        vals_tracks0["PUwgt"] = vals0["PUwgt"]
        corrected_jets["wgt"] = vals0["wgt"]
        corrected_jets["PUwgt"] = vals0["PUwgt"]
        vals_vertex0["wgt"] = vals0["wgt"]
        vals_vertex0["PUwgt"] = vals0["PUwgt"]
        print("weights set")


        if ("Trigger" in datatype):
          output = fill_trigs(output,vals0)
        else:

          track_cuts = ((arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>=0.75))
          if(runoffline):
            vals_offline0 = load_offline(arrays) 
            track_cutsoffline = ((arrays["offlineTrack_quality"] ==1) & (abs(arrays["offlineTrack_eta"]) < 2.4) & (arrays["offlineTrack_pt"]>=0.75))
            #track_cutsoffline = ((arrays["offlineTrack_dzError"] < 0.02) & (arrays["offlineTrack_quality"] ==1) & (abs(arrays["offlineTrack_eta"]) < 2.4) & (arrays["offlineTrack_pt"]>=0.75))
            #track_cutsoffline = ((arrays["offlineTrack_PFcandq"] != 0) & (arrays["offlineTrack_PFcandpv"] ==0) & (abs(arrays["offlineTrack_PFcandeta"]) < 2.4) & (arrays["offlineTrack_PFcandpt"]>=0.75))
            vals_offline0["wgt"] = vals0["wgt"]
            vals_offline0["PUwgt"] = vals0["PUwgt"]
            offline_cut0 = vals_offline0[track_cutsoffline]
            #tracks_cut0 = killTracksOffline(offline_cut0)
          #else:
          tracks_cut0 = vals_tracks0[track_cuts]
          if (killTrks):
            tracks_cut0 = killTracks(tracks_cut0)

          minPt = 30
          jetdef = fastjet.JetDefinition(fastjet.antikt_algorithm,1.5)
          cluster = fastjet.ClusterSequence(tracks_cut0,jetdef)
          ak_inclusive_jets = ak.with_name(cluster.inclusive_jets(),"Momentum4D")
          ak_inclusive_cluster = ak.with_name(cluster.constituents(),"Momentum4D")

          minPtCut = ak_inclusive_jets.pt > minPt
          ak_inclusive_jets = ak_inclusive_jets[minPtCut]
          ak_inclusive_cluster = ak_inclusive_cluster[minPtCut]
          highpt_jet = ak.argsort(ak_inclusive_jets.pt, axis=1, ascending=False, stable=True)
          jets_sorted = ak_inclusive_jets[highpt_jet]
          cluster_sorted = ak_inclusive_cluster[highpt_jet]
          
          print("Clustered")
          
          vals_fatjet0 =ak.zip({
              "pt": jets_sorted.pt,
              "eta": jets_sorted.eta,
              "phi": jets_sorted.phi,
              "mass": jets_sorted.m,
              "FatJet_nconst": ak.num(cluster_sorted,axis=-1),
          }, with_name="Momentum4D")
          vals_fatjet0["wgt"] = vals0["wgt"]
          vals_fatjet0["PUwgt"] = vals0["PUwgt"]
          vals0["FatJet_ncount30"] = ak.count(vals_fatjet0["pt"][vals_fatjet0["pt"]>30],axis=-1)
          vals0["FatJet_ncount50"] = ak.count(vals_fatjet0["pt"][vals_fatjet0["pt"]>50],axis=-1)
          vals0["FatJet_ncount100"] = ak.count(vals_fatjet0["pt"][vals_fatjet0["pt"]>100],axis=-1)
          vals0["FatJet_ncount150"] = ak.count(vals_fatjet0["pt"][vals_fatjet0["pt"]>150],axis=-1)
          vals0["FatJet_ncount200"] = ak.count(vals_fatjet0["pt"][vals_fatjet0["pt"]>200],axis=-1)
          vals0["FatJet_ncount250"] = ak.count(vals_fatjet0["pt"][vals_fatjet0["pt"]>250],axis=-1)
          vals0["FatJet_ncount300"] = ak.count(vals_fatjet0["pt"][vals_fatjet0["pt"]>300],axis=-1)


          jets_pTsorted  = vals_fatjet0[ vals0["FatJet_ncount30"] >=2]
          clusters_pTsorted  = cluster_sorted[ vals0["FatJet_ncount30"] >= 2] 
          reSUEP_cand = ak.where(jets_pTsorted.FatJet_nconst[:,1] <=jets_pTsorted.FatJet_nconst[:,0],clusters_pTsorted[:,0],clusters_pTsorted[:,1])
          reISR_cand  = ak.where(jets_pTsorted.FatJet_nconst[:,1] > jets_pTsorted.FatJet_nconst[:,0],clusters_pTsorted[:,0],clusters_pTsorted[:,1])
          SUEP_cand   = ak.where(jets_pTsorted.FatJet_nconst[:,1] <=jets_pTsorted.FatJet_nconst[:,0],jets_pTsorted[:,0],jets_pTsorted[:,1])
          ISR_cand    = ak.where(jets_pTsorted.FatJet_nconst[:,1] > jets_pTsorted.FatJet_nconst[:,0],jets_pTsorted[:,0],jets_pTsorted[:,1])

          if (redoISRRM):
            print("calc sphericity")
            boost_IRM = ak.zip({
                "px": SUEP_cand.px*-1,
                "py": SUEP_cand.py*-1,
                "pz": SUEP_cand.pz*-1,
                "mass": SUEP_cand.mass
            }, with_name="Momentum4D")
            ISR_cand_b = ISR_cand.boost_p4(boost_IRM) # boosted ISR jet

            recotracks_IRM = tracks_cut0[vals0["FatJet_ncount30"] >= 2] # tracks
            tracks_IRM = recotracks_IRM.boost_p4(boost_IRM) # boosted tracks
            tracks_cuts1x = (tracks_IRM.p !=0)
            tracks_IRM = tracks_IRM[tracks_cuts1x]

            spherex0 = vals0[vals0["FatJet_ncount30"] >= 2]
            spherex0["FatJet_nconst"] = SUEP_cand["FatJet_nconst"]
            spherex0["SUEP_pt"] = SUEP_cand["pt"]
            spherex0["SUEP_eta"] = SUEP_cand["eta"]
            spherex0["SUEP_phi"] = SUEP_cand["phi"]
            spherex0["SUEP_mass"] = SUEP_cand["mass"]
            spherex0["SUEP_beta"] = SUEP_cand["mass"]/SUEP_cand["pt"]
            spherex0["ISR_pt"]   = ISR_cand["pt"]
            spherex0["ISR_eta"]  = ISR_cand["eta"]
            spherex0["ISR_phi"]  = ISR_cand["phi"]
            spherex0["ISR_mass"] = ISR_cand["mass"]
            spherex0["ISR_beta"] = ISR_cand["mass"]/ISR_cand["pt"]

            spherex0["SUEP_girth"],spherex0["SUEP_ptDispersion"],spherex0["SUEP_lesHouches"],spherex0["SUEP_thrust"] = jetAngularities(SUEP_cand,reSUEP_cand)
          
            reSUEP_cand = reSUEP_cand.boost_p4(boost_IRM)
            tracks_cuts2x = (reSUEP_cand.p !=0)
            reSUEP_cand = reSUEP_cand[tracks_cuts2x]
            reonetrackcut = (ak.num(reSUEP_cand) >=2) 
            reSUEP_cand = reSUEP_cand[reonetrackcut]
            spherey0 = spherex0[reonetrackcut]
            if(len(reSUEP_cand)!=0):
              reeigs2 = sphericity(self,reSUEP_cand,2.0) # normal sphericity
              reeigs1 = sphericity(self,reSUEP_cand,1.0) # sphere 1
              spherey0["sphere1_suep"] = 1.5 * (reeigs1[:,1]+reeigs1[:,0])
              spherey0["sphere_suep"] = 1.5 * (reeigs2[:,1]+reeigs2[:,0])

              spherey0["cparam1_suep"] = 3 * (reeigs1[:,0]*reeigs1[:,1]+reeigs1[:,0]*reeigs1[:,2]+reeigs1[:,1]*reeigs1[:,2])
              spherey0["cparam_suep"] = 3 * (reeigs2[:,0]*reeigs2[:,1]+reeigs2[:,0]*reeigs2[:,2]+reeigs2[:,1]*reeigs2[:,2])
              spherey0["dparam1_suep"] = 27 * (reeigs1[:,2]*reeigs1[:,1]*reeigs1[:,0])
              spherey0["dparam_suep"] = 27 * (reeigs2[:,2]*reeigs2[:,1]*reeigs2[:,0])
              spherey0["aplanarity1_suep"] = 1.5 * (reeigs1[:,0])
              spherey0["aplanarity_suep"] = 1.5 * (reeigs2[:,0])
            else:
              spherey0["sphere1_suep"] = -1 
              spherey0["sphere_suep"] = -1
              spherey0["cparam1_suep"] = -1 
              spherey0["cparam_suep"] = -1
              spherey0["dparam1_suep"] = -1 
              spherey0["dparam_suep"] = -1
              spherey0["aplanarity1_suep"] = -1 
              spherey0["aplanarity_suep"] = -1
            
            spherey1 = spherey0[spherey0.triggerHt >= 1]
            spherey2 = spherey1[spherey1.ht >= 560]
            spherey3 = spherey2[spherey2.FatJet_ncount50 >= 2]
            spherey4 = spherey3[spherey3.FatJet_nconst >= 70]
            sphere1y = [spherey0,spherey1,spherey2,spherey3,spherey4]#,spherey5,spherey6]

            #wgts = trigwgts
            output = packdist(output,sphere1y,"cparam1_suep")
            output = packdist(output,sphere1y,"cparam_suep")
            output = packdist(output,sphere1y,"dparam1_suep")
            output = packdist(output,sphere1y,"dparam_suep")
            output = packdist(output,sphere1y,"aplanarity1_suep")
            output = packdist(output,sphere1y,"aplanarity_suep")

            output = packdist(output,sphere1y,"sphere1_suep")
            output = packdist(output,sphere1y,"sphere_suep")
            output = packSR(output,sphere1y,"suep")
            output = packdist(output,sphere1y,"SUEP_beta")
            output = packdist(output,sphere1y,"SUEP_pt")
            output = packdist(output,sphere1y,"SUEP_eta")
            output = packdist(output,sphere1y,"SUEP_phi")
            output = packdist(output,sphere1y,"SUEP_mass")
            output = packdist(output,sphere1y,"ISR_beta")
            output = packdist(output,sphere1y,"ISR_pt")
            output = packdist(output,sphere1y,"ISR_eta")
            output = packdist(output,sphere1y,"ISR_phi")
            output = packdist(output,sphere1y,"ISR_mass")
            output = packdist(output,sphere1y,"SUEP_girth")
            output = packdist(output,sphere1y,"SUEP_ptDispersion")
            output = packdist(output,sphere1y,"SUEP_lesHouches")
            output = packdist(output,sphere1y,"SUEP_thrust")
            #################################ISR################################
            boost_IRMxx = ak.zip({
                "px": ISR_cand.px*-1,
                "py": ISR_cand.py*-1,
                "pz": ISR_cand.pz*-1,
                "mass": ISR_cand.mass
            }, with_name="Momentum4D")

            recotracks_IRMxx = tracks_cut0[vals0["FatJet_ncount30"] >= 2] # tracks
            tracks_IRMxx = recotracks_IRMxx.boost_p4(boost_IRMxx) # boosted tracks
            tracks_cuts1xxx = (tracks_IRMxx.p !=0)
            tracks_IRMxx = tracks_IRMxx[tracks_cuts1xxx]

            reISR_cand = reISR_cand.boost_p4(boost_IRMxx)
            tracks_cuts2xxx = (reISR_cand.p !=0)
            reISR_cand = reISR_cand[tracks_cuts2xxx]
            reonetrackcutxx = (ak.num(reISR_cand) >=2) 
            reISR_cand = reISR_cand[reonetrackcutxx]
            spherey0xx = spherex0[reonetrackcutxx]
            if(len(reSUEP_cand)!=0):
              reeigs2xx = sphericity(self,reISR_cand,2.0) # normal sphericity
              reeigs1xx = sphericity(self,reISR_cand,1.0) # sphere 1
              spherey0xx["sphere1_isrsuep"] = 1.5 * (reeigs1xx[:,1]+reeigs1xx[:,0])
              spherey0xx["sphere_isrsuep"] = 1.5 * (reeigs2xx[:,1]+reeigs2xx[:,0])
            else:
              spherey0xx["sphere1_isrsuep"] = -1 
              spherey0xx["sphere_isrsuep"] = -1
            
            spherey1xx = spherey0xx[spherey0xx.triggerHt >= 1]
            spherey2xx = spherey1xx[spherey1xx.ht >= 560]
            spherey3xx = spherey2xx[spherey2xx.FatJet_ncount50 >= 2]
            spherey4xx = spherey3xx[spherey3xx.FatJet_nconst >= 70]
            sphere1yxx = [spherey0xx,spherey1xx,spherey2xx,spherey3xx,spherey4xx]#,spherey5,spherey6]
            output = packdist(output,sphere1yxx,"sphere1_isrsuep")
            output = packdist(output,sphere1yxx,"sphere_isrsuep")
            output = packSR(output,sphere1yxx,"isrsuep")
            #################################ISR################################
            if(eventDisplay_knob):
              for evt in range(20):
                print(evt)
                plot_display(fin,evt,spherey0["ht"][evt],recotracks_IRM[evt],tracks_IRM[evt],SUEP_cand[evt],ISR_cand[evt],ISR_cand_b[evt],spherey0["sphere1_suep"][evt],reSUEP_cand[evt],reISR_cand[evt])
            IRM_candsvx2 = tracks_IRM[abs(recotracks_IRM[tracks_cuts1x].deltaR(ISR_cand)) >= 1.5] # remove all tracks that would be in the ISR jet unboosted
            reonetrackcutx = (ak.num(IRM_candsvx2) >=2)
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
            spherez2 = spherez1[spherez1.ht >= 560]
            spherez3 = spherez2[spherez2.FatJet_ncount50 >= 2]
            spherez4 = spherez3[spherez3.FatJet_nconst >= 70]
            sphere1z = [spherez0,spherez1,spherez2,spherez3,spherez4]#,spherez5,spherez6]
            output = packdist(output,sphere1z,"sphere1_isr")
            output = packdist(output,sphere1z,"sphere_isr")
            output = packSR(output,sphere1z,"isr")

            def sphericityCalc(output,cut):
              IRM_cands = tracks_IRM[abs(tracks_IRM.deltaphi(ISR_cand_b)) >= cut/10.]
              onetrackcut = (ak.num(IRM_cands) >=2) # cut to pick out events that survive the isr removal
              IRM_cands = IRM_cands[onetrackcut]
              spherexx = spherex0[onetrackcut]
  

              if(len(IRM_cands)!=0):
                eigs2 = sphericity(self,IRM_cands,2.0) # normal sphericity
                eigs1 = sphericity(self,IRM_cands,1.0) # sphere 1
                spherexx["sphere1_%s"%cut] = 1.5 * (eigs1[:,1]+eigs1[:,0])
                spherexx["sphere_%s"%cut] = 1.5 * (eigs2[:,1]+eigs2[:,0])
              else:
                spherexx["sphere1_%s"%cut] = -1 
                spherexx["sphere_%s"%cut] = -1
              spherex1 = spherexx[spherexx.triggerHt >= 1]
              spherex2 = spherex1[spherex1.ht >= 560]
              spherex3 = spherex2[spherex2.FatJet_ncount50 >= 2]
              spherex4 = spherex3[spherex3.FatJet_nconst >= 70]
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
              return output
            output = sphericityCalc(output,16)
            output = sphericityCalc(output,10)
            output = sphericityCalc(output,8)
            output = sphericityCalc(output,4)

            print("filling cutflows") 
          
       #  # resolution studies
          if(signal):
            resolutions = load_resolutions(scalar0,vals0,spherey2)
          #cutflow Ht
          vals1 = vals0[vals0.triggerHt >= 1]
          vals2 = vals1[vals1.ht >= 560]
          vals3 = spherey3 #vals2[vals2.FatJet_ncount50 >= 2]
          vals4 = vals3[vals3.FatJet_nconst >= 70]
          vals5 = vals4[vals4.sphere1_suep >= 0.7]
          vals4x = vals3[vals3.sphere1_suep >= 0.7]


          
          #print("filling cutflows trk") 
          vals_tracks1 = tracks_cut0[vals0.triggerHt >= 1]
          vals_tracks2 = vals_tracks1[vals1.ht >= 560]
          vals_tracks3 = vals_tracks2[vals2.FatJet_ncount50 >= 2]
          vals_tracks4 = vals_tracks3[vals3.FatJet_nconst >= 70]

          vals = [vals0,vals1,vals2,vals3,vals4,vals5]
          valsx = [vals0,vals1,vals2,vals3,vals4x]
          vals_tracks = [vals_tracks0,vals_tracks1,vals_tracks2,vals_tracks3,vals_tracks4]

          if(runoffline):
            vals_offtracks1 = offline_cut0[vals0.triggerHt >= 1]
            vals_offtracks2 = vals_offtracks1[vals1.ht >= 560]
            vals_offtracks3 = vals_offtracks2[vals2.FatJet_ncount50 >= 2]
            vals_offtracks4 = vals_offtracks3[vals3.FatJet_nconst >= 70]

            vals_offtracks = [offline_cut0,vals_offtracks1,vals_offtracks2,vals_offtracks3,vals_offtracks4]
            output = fill_offtracks(output,vals_offtracks)


          #fill hists
          print("filling hists") 
          output = fill_vals(output,vals)
          output = fill_trigs(output,vals0)
          output = fill_tracks(output,vals_tracks)
          output = fill_vertex(output,vals_vertex0,vals)
          output = fill_jets(output,corrected_jets,vals,vals_fatjet0,vals_nsub0)
          output = fill_PFncounts(output,valsx)
          output = fill_fatjet(output,vals,spherey2)
          if(signal):
            output = fill_trkID(output,vals_tracks,vals,vals_gen0)
            output = fill_scalars(output,scalar0,vals,resolutions)
        

        return output

    def postprocess(self, accumulator):
        return accumulator


# https://github.com/scikit-hep/uproot4/issues/122
uproot.open.defaults["xrootd_handler"] = uproot.source.xrootd.MultithreadedXRootDSource


fin = "HT2000"
batch = 0
signal=False
runInteractive=True # False
systematicType =0
Run=""
if len(sys.argv) >= 2:
  fin = sys.argv[1]
#fin = "sig400"
if len(sys.argv) >= 3:
  batch = sys.argv[2]
if len(sys.argv) >= 4:
  era = int(sys.argv[3])
if len(sys.argv) >= 5:
  systematicType = int(sys.argv[4])
if "HT" in fin:
  datatype="MC"
  #datatype="Trigger"
  fs = np.loadtxt("rootfiles/20%s/new_files/%sv7.txt"%(era,fin),dtype=str)
  batch = int(batch)
  if(batch == -1): #test
  	fileset = {
  	         fin: ['root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCDv4/20%s/%s/test.root'%(era,fin)]
  	}
  else:
  	start = 100*batch
  	end = 100*(batch+1)
  	if (end > len(fs)):
  	  fs = fs[start:]
  	else:
  	  fs=fs[start:end]
  	htslices = {"HT200":"200to300","HT300":"300to500","HT500":"500to700","HT700":"700to1000","HT1000":"1000to1500","HT1500":"1500to2000","HT2000":"2000toInf"}
  	htslice = htslices[fin]
  	fileset = {
  	         fin : ["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCDv7/20%s/%s/QCD_HT%s_TuneCP5_13TeV-madgraphMLM-pythia8+RunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2+AODSIM/%s"%(era,fin,htslice,f) for f in fs],
  	         #fin: ['root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/QCDv4/2018/HT1000/test.root']
  	}
elif "Run" in fin:
  datatype="DATA"
  Run = fin[3:]
  print("Run",Run)
  #Runs = ["RunA","RunB","RunC"]
  fs = np.loadtxt("rootfiles/20%s/Data_%s.txt"%(era,fin),dtype=str)
  batch = int(batch)
  fs=fs[5*batch:5*(batch+1)]
  if(era==18):
    fileset = {
     #       fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Datav4/20%s/%s/%s"%(era,fin,f) for f in fs]
            fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Datav4/20%s/%s/ScoutingPFHT+Run20%s%s-v1+RAW/%s"%(era,fin,era,Run,f) for f in fs]
    }
  elif(era==16):
    fileset = {
     #       fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Datav4/20%s/%s/%s"%(era,fin,f) for f in fs]
            fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Datav4/20%s/ScoutingPFHT+Run20%s%s-v2+RAW/%s"%(era,era,Run,f) for f in fs]
    }
  else:  
    fileset = {
            fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Datav4/20%s/%s/%s"%(era,fin,f) for f in fs]
            #fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Datav4/20%s/%s/ScoutingPFHT+Run20%s%s-v1+RAW/%s"%(era,fin,era,Run,f) for f in fs]
    }  
elif "Trigger" in fin:
  datatype="Trigger"
  Run = fin[7:]
  print("Run",Run)
  #Runs = ["RunA","RunB","RunC"]
  #runInteractive=True
  fs = np.loadtxt("rootfiles/20%s/Trigger_%s.txt"%(era,Run),dtype=str)
  batch = int(batch)
  fs=fs[10*batch:10*(batch+1)]
  fileset = {
            fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Datav4/20%s/Trigger/ScoutingPFCommissioning+Run20%s%s-v1+RAW/%s"%(era,era,Run,f) for f in fs]
  }  
else:
  datatype="MC"
  signal=True
  runInteractive=True
  decays = {"0":"darkPho","1":"darkPhoHad","2":"generic","m2t0p5":"m2t0p5","m2t1":"m2t1","m2t2":"m2t2","m2t3":"m2t3","m2t4":"m2t4","m3t1p5":"m3t1p5","m3t3":"m3t3","m3t6":"m3t6","m5t1":"m5t1","m5t5":"m5t5","m5t10":"m5t10"}
  fileset = {
            fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Signal/20%s/%s_%s.root"%(era,fin,decays[batch])]
            #fin:["root://cmseos.fnal.gov//store/group/lpcsuep/Scouting/Signal/%s_%s_PU.root"%(fin,decays[batch])]
  }  
appendname=""
if systematicType ==1:
	killTrks = True
	appendname = "killtrk"
if systematicType ==2:
	AK4sys = 1 #o: nominal, 1: err up, 2 err dowm
	appendname = "AK4up"
if systematicType ==3:
	AK4sys = 2 #o: nominal, 1: err up, 2 err dowm
	appendname = "AK4down"
if systematicType ==4:
	trigSystematics = 1 #0: nominal, 1: up err, 2: down err
	appendname = "trigup"
if systematicType ==5:
	trigSystematics = 2 #0: nominal, 1: up err, 2: down err
	appendname = "trigdown"
if systematicType ==6:
	PUSystematics = 1 #0: nominal, 1: up err, 2: down err
	appendname = "PUup"
if systematicType ==7:
	PUSystematics = 2 #0: nominal, 1: up err, 2: down err
	appendname = "PUdown"
if systematicType ==8:
	PSSystematics = 1 #0: nominal, 1: up err, 2: down err
	appendname = "PSup"
if systematicType ==9:
	PSSystematics = 2 #0: nominal, 1: up err, 2: down err
	appendname = "PSdown"
if systematicType ==10:
	PrefireSystematics = 1 #0: nominal, 1: up err, 2: down err
	appendname = "Prefireup"
if systematicType ==11:
	PrefireSystematics = 2 #0: nominal, 1: up err, 2: down err
	appendname = "Prefiredown"
if systematicType ==12:
	higgsSystematics = 1 #0: nominal, 1: up err, 2: down err
	appendname = "higgsup"
if systematicType ==13:
	higgsSystematics = 2 #0: nominal, 1: up err, 2: down err
	appendname = "higgsdown"
	

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
    print("running %s %s %s 20%s"%(fin,batch,appendname,era))
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

    if signal:
      datatype = "SIG"
    if batch == -1:
      batch = "test"
    with open("outhists/20%s/%s/myhistos_%s_%s%s_20%s.p"%(era,datatype,fin,batch,appendname,era), "wb") as pkl_file:
    #with open("outhists/myhistos_%s_%skilltrk.p"%(fin,batch), "wb") as pkl_file:
        pickle.dump(out, pkl_file)
