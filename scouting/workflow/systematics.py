import awkward as ak
import numpy as np
import uproot
from coffea.jetmet_tools import FactorizedJetCorrector, JetCorrectionUncertainty
from coffea.jetmet_tools import JECStack, CorrectedJetsFactory
from coffea.lookup_tools import extractor

#from coffea.analysis_tools import Weights


# register our candidate behaviors
from coffea.nanoevents.methods import candidate
ak.behavior.update(candidate.behavior)





def correctJets(vals_jet0,cache,era=18,datatype="MC",Run=""):
        if datatype == "Trigger":
          #datatype = "DATA"
          return vals_jet0
        ext_ak4 = extractor()
        if era==18:
          if Run != "":
            Run = "_Run%s"%Run
          jecdir = "Autumn18%s_V19_%s"%(Run,datatype)
          jerdir = "Autumn18_V7b_%s"%(datatype)
        elif era==17:
          if Run =="D" or Run =="E":
            Run = "DE"
          jecdir = "Fall17_17Nov2017%s_V32_%s"%(Run,datatype)
          jerdir = "Summer19UL17_JRV3_%s"%(datatype)
        elif era==16:
          jecdir = "Summer16_07Aug2017%s_V11_%s"%(Run,datatype)
          jerdir = "Summer20UL16_JRV3_%s"%(datatype)
        else:
          jerdir = "Summer19UL%s_JRV3_%s"%(era,datatype)
        jecpath = "jetscale_corrections/20%s/"%(era)+jecdir
        jerpath = "jetresolution_corrections/20%s/"%(era)+jerdir
        ext_ak4.add_weight_sets([
            "* * systematics/" + jecpath+"_L1FastJet_AK4PF.jec.txt", #looks to be 0,
            "* * systematics/" + jecpath+"_L1RC_AK4PF.jec.txt", #needs area
            "* * systematics/" + jecpath+"_L2L3Residual_AK4PF.jec.txt",
            "* * systematics/" + jecpath+"_L2Relative_AK4PF.jec.txt",
            "* * systematics/" + jecpath+"_L3Absolute_AK4PF.jec.txt", #looks to be 1, no change
            "* * systematics/" + jecpath+"_Uncertainty_AK4PF.junc.txt",
       #     "* * systematics/" + jerpath+"_PtResolution_AK4PF.jr.txt",
       #     "* * systematics/" + jerpath+"_SF_AK4PF.jersf.txt",
        ])
        if "DATA" not in datatype:
        	ext_ak4.add_weight_sets([
            	"* * systematics/" + jerpath+"_PtResolution_AK4PF.jr.txt",
            	"* * systematics/" + jerpath+"_SF_AK4PF.jersf.txt",
        	])
        ext_ak4.finalize()

        jec_stack_names_ak4 = [
            jecdir + "_L1FastJet_AK4PF",
            jecdir + "_L2Relative_AK4PF",
            jecdir + "_L3Absolute_AK4PF",
            jecdir + "_Uncertainty_AK4PF",
        ]
        if(datatype=="DATA"):
          jec_stack_names_ak4 = [
            jecdir + "_L1RC_AK4PF",
            jecdir + "_L2L3Residual_AK4PF"
        ]+ jec_stack_names_ak4
        else:
          jec_stack_names_ak4 = [
            jerdir + "_PtResolution_AK4PF",
            jerdir + "_SF_AK4PF",
        ]+ jec_stack_names_ak4

        evaluator_ak4 = ext_ak4.make_evaluator()

        jec_inputs_ak4 = {name: evaluator_ak4[name] for name in jec_stack_names_ak4}
        jec_stack_ak4 = JECStack(jec_inputs_ak4)
        name_map = jec_stack_ak4.blank_name_map
        name_map['JetPt'] = 'pt'
        name_map['JetMass'] = 'mass'
        name_map['JetEta'] = 'eta'
        name_map['JetA'] = 'area'
        name_map['massRaw'] = 'mass_raw'
        name_map['ptRaw'] = 'pt_raw'
        name_map['ptGenJet'] = 'ptGen'
        name_map['Rho'] = 'rho'
        jet_factory = CorrectedJetsFactory(name_map, jec_stack_ak4)
        return jet_factory.build(vals_jet0, lazy_cache=cache)
def pileup_weight(puarray,systematics=0,era=18):
    if era == 18:
        f_MC = uproot.open("systematics/pileup/mcPileupUL2018.root")
        f_data = uproot.open("systematics/pileup/PileupHistogram-UL2018-100bins_withVar.root")
    elif era == 17:
        f_MC = uproot.open("systematics/pileup/mcPileupUL2017.root")
        f_data = uproot.open("systematics/pileup/PileupHistogram-UL2017-100bins_withVar.root")
    elif era == 16:
        f_MC = uproot.open("systematics/pileup/mcPileupUL2016.root")
        f_data = uproot.open("systematics/pileup/PileupHistogram-UL2016-100bins_withVar.root")
    else:
        print('no pileup weights because no year was selected for function pileup_weight')

    hist_MC = f_MC['pu_mc'].to_numpy()
    #Normalize the data distribution
    hist_data = f_data['pileup'].to_numpy()
    hist_data[0].sum()
    norm_data = hist_data[0]/hist_data[0].sum()
    weights = np.divide(norm_data, hist_MC[0], out=np.ones_like(norm_data), where=hist_MC[0]!=0)

    #The plus version of the pileup
    hist_data_plus = f_data['pileup_plus'].to_numpy()
    hist_data_plus[0].sum()
    norm_data_plus = hist_data_plus[0]/hist_data_plus[0].sum()
    weights_plus = np.divide(norm_data_plus, hist_MC[0], out=np.ones_like(norm_data_plus), where=hist_MC[0]!=0)

    #The minus version of the pileup
    hist_data_minus = f_data['pileup_minus'].to_numpy()
    hist_data_minus[0].sum()
    norm_data_minus = hist_data_minus[0]/hist_data_minus[0].sum()
    weights_minus = np.divide(norm_data_minus, hist_MC[0], out=np.ones_like(norm_data_minus), where=hist_MC[0]!=0)
    #print("PU: ",weights)
    if systematics==0:
      return np.take(weights,puarray)
    elif systematics==1:
      return np.take(weights_plus,puarray)
    elif systematics==2:
      return np.take(weights_minus,puarray)
    else:
      return np.take(weights,puarray)
def gettrigweights(htarray,systematics=0,era=18):
    bins, trigwgts, wgterr = np.loadtxt("systematics/triggers/trigger_systematics_%s.txt"%(era), delimiter=",")
    htbin = np.digitize(htarray,bins)
    trigwgts =np.insert(trigwgts,0,0)
    wgterr =np.insert(wgterr,0,0)
    scaleFactorNom = np.take(trigwgts,htbin)
    scaleFactorErr = np.take(wgterr,htbin)
    if systematics==1:
       scaleFactor = scaleFactorNom + scaleFactorErr
    elif systematics==2:
       scaleFactor = scaleFactorNom - scaleFactorErr
    else:
       scaleFactor = scaleFactorNom
    return scaleFactor
def killTracks(tracks_cut0):
        np.random.seed(2022) #random seed to get repeatable results
        probs = ak.where(ak.flatten(tracks_cut0["pt"]) < 20,0.05,0.02) #5% if pt < 1, otherwise 2%.
        rands = np.random.rand(len(probs)) > probs
        trk_killer = ak.Array(ak.layout.ListOffsetArray64(tracks_cut0.layout.offsets, ak.layout.NumpyArray(rands)))
        tracks_cut0 = tracks_cut0[trk_killer]
        return tracks_cut0
def calculateHT(vals0,corrected_jets,AK4sys):
        print("calculating HT with systematic %s"%AK4sys)
        if AK4sys ==1 :
                vals0['ht20'] = ak.sum(corrected_jets.JES_jes.up["pt"][(corrected_jets["passId"] ==1) & (corrected_jets.JES_jes.up["pt"] > 20)],axis=-1)
                vals0['ht30'] = ak.sum(corrected_jets.JES_jes.up["pt"][(corrected_jets["passId"] ==1) & (corrected_jets.JES_jes.up["pt"] > 30)],axis=-1)
                vals0['ht40'] = ak.sum(corrected_jets.JES_jes.up["pt"][(corrected_jets["passId"] ==1) & (corrected_jets.JES_jes.up["pt"] > 40)],axis=-1)
                vals0['ht50'] = ak.sum(corrected_jets.JES_jes.up["pt"][(corrected_jets["passId"] ==1) & (corrected_jets.JES_jes.up["pt"] > 50)],axis=-1)
        elif AK4sys ==2 :
                vals0['ht20'] = ak.sum(corrected_jets.JES_jes.down["pt"][(corrected_jets["passId"] ==1) & (corrected_jets.JES_jes.down["pt"] > 20)],axis=-1)
                vals0['ht30'] = ak.sum(corrected_jets.JES_jes.down["pt"][(corrected_jets["passId"] ==1) & (corrected_jets.JES_jes.down["pt"] > 30)],axis=-1)
                vals0['ht40'] = ak.sum(corrected_jets.JES_jes.down["pt"][(corrected_jets["passId"] ==1) & (corrected_jets.JES_jes.down["pt"] > 40)],axis=-1)
                vals0['ht50'] = ak.sum(corrected_jets.JES_jes.down["pt"][(corrected_jets["passId"] ==1) & (corrected_jets.JES_jes.down["pt"] > 50)],axis=-1)
        else:
                vals0['ht20'] = ak.sum(corrected_jets["pt"][(corrected_jets["passId"] ==1) & (corrected_jets["pt"] > 20)],axis=-1)
                vals0['ht30'] = ak.sum(corrected_jets["pt"][(corrected_jets["passId"] ==1) & (corrected_jets["pt"] > 30)],axis=-1)
                vals0['ht40'] = ak.sum(corrected_jets["pt"][(corrected_jets["passId"] ==1) & (corrected_jets["pt"] > 40)],axis=-1)
                vals0['ht50'] = ak.sum(corrected_jets["pt"][(corrected_jets["passId"] ==1) & (corrected_jets["pt"] > 50)],axis=-1)
        vals0['ht'] = vals0['ht30']
        return vals0
