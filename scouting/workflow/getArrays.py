import numpy as np
import awkward as ak

def load_vertex(arrays):
	print("Loading Vertex")
	vals_vertex = ak.zip({
                      'Vertex_valid': arrays["Vertex_isValidVtx"],
                      'Vertex_tracksSize': arrays["Vertex_tracksSize"],
                      'Vertex_chi2': arrays["Vertex_chi2"],
                      'Vertex_ndof': arrays["Vertex_ndof"],
                      'Vertex_z': arrays["Vertex_z"],
        })
	return vals_vertex

def load_jets(arrays,datatype):
	print("Loading Jets")
	vals_jet0 = ak.zip({
                       'pt' : arrays["Jet_pt"],
                       'eta': arrays["Jet_eta"],
                       'phi': arrays["Jet_phi"],
                       'mass': arrays["Jet_m"],
                       'area': arrays["Jet_area"],
                       'mass_raw': arrays["Jet_m"], # I think there should be another factor here?
                       'pt_raw': arrays["Jet_pt"],
                       'passId': arrays["Jet_passId"],
                       'ptGen': ak.values_astype(ak.without_parameters(ak.zeros_like(arrays["Jet_pt"])),np.float32)
        },with_name="Momentum4D")
	if datatype == "Trigger":
		vals_jet0['rho'] = vals_jet0["pt"]/vals_jet0["area"] #ak.broadcast_arrays(arrays["rho"], vals_jet0["pt"])[0]
	else:
		vals_jet0['rho'] = ak.broadcast_arrays(arrays["rho"], vals_jet0["pt"])[0]
	return vals_jet0
def load_gen(arrays):
	print("Loading Gen")
	vals_gen0 = ak.zip({
                         'pt' : arrays["gen_pt"],
                         'eta': arrays["gen_eta"],
                         'phi': arrays["gen_phi"],
                         'mass': arrays["gen_mass"],
                         'gen_dR':  np.sqrt(arrays["gen_dR"]),
                         'gen_fromSuep':  arrays["gen_fromSuep"],
                         'gen_PV':  arrays["gen_PV"],
                         'gen_PVdZ':  arrays["gen_PVdZ"],
          },with_name="Momentum4D")
	return vals_gen0
def load_scalar(arrays):
	print("Loading Scalar")
	scalar0  = ak.zip({
                         'pt' : arrays["scalar_pt"],
                         'eta': arrays["scalar_eta"],
                         'phi': arrays["scalar_phi"],
                         'mass': arrays["scalar_m"],
                         'beta': arrays["scalar_m"]/arrays["scalar_pt"],
          },with_name="Momentum4D")
	return scalar0
def load_tracks(arrays,signal):
	print("Loading Tracks")
	if(signal):
		vals_tracks0 = ak.zip({
                         'pt' : arrays["PFcand_pt"],
                         'eta': arrays["PFcand_eta"],
                         'phi': arrays["PFcand_phi"],
                         'mass': arrays["PFcand_m"],
                         'PFcand_dR':  np.sqrt(arrays["PFcand_dR"]),
                         'PFcand_fromsuep': arrays["PFcand_fromsuep"],
                         'PFcand_q': arrays["PFcand_q"],
                         'PFcand_vertex': arrays["PFcand_vertex"],
          },with_name="Momentum4D")
	else:
		vals_tracks0 = ak.zip({
                         'pt' : arrays["PFcand_pt"],
                         'eta': arrays["PFcand_eta"],
                         'phi': arrays["PFcand_phi"],
                         'mass': arrays["PFcand_m"],
                         'PFcand_q': arrays["PFcand_q"],
                         'PFcand_vertex': arrays["PFcand_vertex"],
          },with_name="Momentum4D")
	return vals_tracks0
def load_nsub(arrays):
	vals_nsub0 = ak.zip({
                "tau21": arrays["FatJet_tau21"],
                "tau32": arrays["FatJet_tau32"],
        })
	return vals_nsub0
def load_resolutions(scalar0,vals0,spherey2):
        print("calc res")
        scalar1  = scalar0[ vals0["FatJet_ncount30"] >= 2]
        suepvals = vals0[vals0.FatJet_ncount30 >=2]
        suepvalsx = suepvals[suepvals.triggerHt >=1]
        scalar2 = scalar1[suepvals.triggerHt >=1] # FJ > 2 cut is already applied from the suep array
        scalar = scalar2[suepvalsx.ht>=560] # FJ > 2 cut is already applied from the suep array
        res_beta = spherey2["SUEP_beta"]-scalar["beta"].to_numpy()
        res_pt = spherey2["SUEP_pt"]-scalar["pt"].to_numpy()
        res_mass = spherey2["SUEP_mass"]-scalar["mass"].to_numpy()
        phi1 = spherey2["SUEP_phi"].to_numpy()
        phi2 = scalar["phi"].to_numpy()
        res_dPhi0 = phi1-phi2 #SUEP_cand.phi.to_numpy()-scalar["phi"].to_numpy()
        res_dPhi00 = np.array([2*np.pi-x if x > np.pi else x for x in res_dPhi0])
        res_dPhi = np.array([2*np.pi+x if x < -np.pi else x for x in res_dPhi00])
        res_dEta = spherey2["SUEP_eta"].to_numpy()-scalar["eta"].to_numpy()
        res_dR = np.sqrt(np.square(res_dPhi) + np.square(res_dEta))
        resolutions = ak.zip({
          "res_pt" : res_pt,
          "res_mass" : res_mass,
          "res_dEta" : res_dEta,
          "res_dPhi" : res_dPhi,
          "res_dR" : res_dR,
          "res_beta" : res_beta

        })
        resolutions["wgt"] = spherey2["wgt"]
        return resolutions
def load_vals(arrays,dataset,era):
        if era == 18:
          tright = [item[7] for item in arrays["hltResult"]]
          trigcalo = [item[5] for item in arrays["hltResult"]] #calojet40 reference trigger
          trigmu = [item[2] for item in arrays["hltResult"]] #mu reference trigger
        else:
          tright = [item[5] for item in arrays["hltResult"]]
          trigcalo = [item[3] for item in arrays["hltResult"]] #calojet40 reference trigger
          trigmu = [item[1] for item in arrays["hltResult"]] #mu reference trigger
        #trigger order:
        #HLT Trigger DST_DoubleMu1_noVtx_CaloScouting_v2
        #HLT Trigger DST_DoubleMu3_noVtx_CaloScouting_Monitoring_v6
        #HLT Trigger DST_DoubleMu3_noVtx_CaloScouting_v6
        #HLT Trigger DST_DoubleMu3_noVtx_Mass10_PFScouting_v3
        #HLT Trigger DST_L1HTT_CaloScouting_PFScouting_v15
        #HLT Trigger DST_CaloJet40_CaloScouting_PFScouting_v15
        #HLT Trigger DST_HT250_CaloScouting_v10
        #HLT Trigger DST_HT410_PFScouting_v16
        if dataset == "Trigger":
          vals0 = ak.zip({
               'n_pfcand': arrays["n_pfcand"],
               'event_sphericity': arrays["event_sphericity"],
               'eventBoosted_sphericity': arrays["eventBoosted_sphericity"],
               'n_fatjet': arrays["n_fatjet"],
               'n_jetId': arrays["n_jetId"],
               'n_pfMu': arrays["n_pfMu"],
               'n_pfEl': arrays["n_pfEl"],
               'n_pvs': arrays["n_pvs"],
               #'PU': arrays["PU_num"],
               #'nPVs_good0': ak.count(arrays["Vertex_isValidVtx"],axis=-1),
               #'nPVs_good1': ak.count(arrays["Vertex_isValidVtx"][(arrays["Vertex_isValidVtx"] == 1)],axis=-1),
               #'nPVs_good2': ak.count(arrays["Vertex_isValidVtx"][(abs(arrays["Vertex_z"]) <24 ) & (arrays["Vertex_isValidVtx"] == 1)],axis=-1),
               #'nPVs_good3': ak.count(arrays["Vertex_isValidVtx"][(abs(arrays["Vertex_z"]) < 24) & (arrays["Vertex_ndof"]> 4 ) & (arrays["Vertex_isValidVtx"] == 1)],axis=-1),
               #'Vertex_tracksSize0': ak.max(arrays["Vertex_tracksSize"],axis=-1),
               #'nPVs_good4': ak.count(arrays["Vertex_tracksSize"][arrays["Vertex_tracksSize"] >3],axis=-1),
               #'nPVs_good5': ak.count(arrays["Vertex_tracksSize"][arrays["Vertex_tracksSize"] >5],axis=-1),
               #'nPVs_good6': ak.count(arrays["Vertex_tracksSize"][arrays["Vertex_tracksSize"] >7],axis=-1),
               #'nPVs_good7': ak.count(arrays["Vertex_tracksSize"][arrays["Vertex_tracksSize"] >10],axis=-1),
               #'nPVs_good8': ak.count(arrays["Vertex_tracksSize"][arrays["Vertex_tracksSize"] >15],axis=-1),
               #'nPVs_good9': ak.count(arrays["Vertex_tracksSize"][arrays["Vertex_tracksSize"] >25],axis=-1),
               #'Vertex_minZ' : ak.min(abs(np.subtract(ak.firsts(arrays["Vertex_z"]),arrays["Vertex_z"][:,1:])),axis=-1,mask_identity=False),
               'triggerHt': tright,
               'triggerMu': trigmu,
               'triggerCalo': trigcalo,
               #'PFcand_ncount0' :  ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.0 )],axis=-1),
               #'PFcand_ncount50' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.50)],axis=-1),
               #'PFcand_ncount60' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.60)],axis=-1),
               #'PFcand_ncount70' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.70)],axis=-1),
               #'PFcand_ncount75' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.75)],axis=-1),
               #'PFcand_ncount80' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.80)],axis=-1),
               #'PFcand_ncount90' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.90)],axis=-1),
               #'PFcand_ncount100': ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>1.0 )],axis=-1),
               #'PFcand_ncount150': ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>1.5 )],axis=-1),
               #'PFcand_ncount200': ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>2   )],axis=-1),
               #'PFcand_ncount300': ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>3   )],axis=-1),
               'FatJet_nconst' : ak.max(arrays["FatJet_nconst"],axis=-1,mask_identity=False),
        })
        else:
          vals0 = ak.zip({
               'n_pfcand': arrays["n_pfcand"],
               'event_sphericity': arrays["event_sphericity"],
               'eventBoosted_sphericity': arrays["eventBoosted_sphericity"],
               'n_fatjet': arrays["n_fatjet"],
               'n_jetId': arrays["n_jetId"],
               'n_pfMu': arrays["n_pfMu"],
               'n_pfEl': arrays["n_pfEl"],
               'n_pvs': arrays["n_pvs"],
               'PU': arrays["PU_num"],
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
               'triggerHt': tright,
               'triggerMu': trigmu,
               'triggerCalo': trigcalo,
               'PFcand_ncount0' :  ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.0 )],axis=-1),
               'PFcand_ncount50' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.50)],axis=-1),
               'PFcand_ncount60' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.60)],axis=-1),
               'PFcand_ncount70' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.70)],axis=-1),
               'PFcand_ncount75' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.75)],axis=-1),
               'PFcand_ncount80' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.80)],axis=-1),
               'PFcand_ncount90' : ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>0.90)],axis=-1),
               'PFcand_ncount100': ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>1.0 )],axis=-1),
               'PFcand_ncount150': ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>1.5 )],axis=-1),
               'PFcand_ncount200': ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>2   )],axis=-1),
               'PFcand_ncount300': ak.count(arrays["PFcand_pt"][(arrays["PFcand_q"] != 0) & (arrays["PFcand_vertex"] ==0) & (abs(arrays["PFcand_eta"]) < 2.4) & (arrays["PFcand_pt"]>3   )],axis=-1),
               'FatJet_nconst' : ak.max(arrays["FatJet_nconst"],axis=-1,mask_identity=False),
        })
        return vals0
