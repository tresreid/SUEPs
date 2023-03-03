import numpy as np
import awkward as ak

def packtrig(output,vals,var):
        output["trigdist_%s"%(var)].fill(cut="Cut 0: No cut", v1=vals[0][var],weight=vals[0]["PUwgt"])
        output["trigdist_%s"%(var)].fill(cut="Cut 1: HT Trig noRef", v1=vals[1][var],weight=vals[1]["PUwgt"])
        output["trigdist_%s"%(var)].fill(cut="Cut 2: CaloJet 40 Ref Trig", v1=vals[2][var],weight=vals[2]["PUwgt"])
        output["trigdist_%s"%(var)].fill(cut="Cut 3: CaloJet 40 Ref + HT Trig", v1=vals[3][var],weight=vals[3]["PUwgt"])
        output["trigdist_%s"%(var)].fill(cut="Cut 4: Mu Ref Trig", v1=vals[4][var],weight=vals[4]["PUwgt"])
        output["trigdist_%s"%(var)].fill(cut="Cut 5: Mu Ref + HT Trig", v1=vals[5][var],weight=vals[5]["PUwgt"])
        return output
def packsingledist(output,vals,var,wgt=True):
        if wgt:
          output["dist_%s"%(var)].fill(cut="cut 0:No cut", v1=vals[var],weight=vals["wgt"])
        else:
          output["dist_%s"%(var)].fill(cut="cut 0:No cut", v1=vals[var],weight=vals["PUwgt"])
        return output
def packdistnowgt(output,vals,var,prefix=""):
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 0:No cut", v1=vals[0][var],weight=vals[0]["PUwgt"])
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 1:HT Trig", v1=vals[1][var],weight=vals[1]["PUwgt"])
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 2:Ht>=560", v1=vals[2][var],weight=vals[2]["PUwgt"])
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 3:fj>=2", v1=vals[3][var],weight=vals[3]["PUwgt"])
        if("PFcand_n" in var):
          output["dist_%s%s"%(prefix,var)].fill(cut="cut 4:eventBoosted Sphericity >=0.6", v1=vals[4][var],weight=vals[4]["PUwgt"])
        else:
          output["dist_%s%s"%(prefix,var)].fill(cut="cut 4:nPFcand(SUEP)>=70", v1=vals[4][var],weight=vals[4]["PUwgt"])
        if(len(vals)>=6):
          output["dist_%s%s"%(prefix,var)].fill(cut="cut 5:eventBoosted Sphericity > 0.7", v1=vals[5][var],weight=vals[5]["PUwgt"])
        return output
def packdist(output,vals,var,prefix=""):
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 0:No cut", v1=vals[0][var],weight=vals[0]["wgt"])
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 1:HT Trig", v1=vals[1][var],weight=vals[1]["wgt"])
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 2:Ht>=560", v1=vals[2][var],weight=vals[2]["wgt"])
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 3:fj>=2", v1=vals[3][var],weight=vals[3]["wgt"])
        if("PFcand_n" in var):
          output["dist_%s%s"%(prefix,var)].fill(cut="cut 4:eventBoosted Sphericity >=0.6", v1=vals[4][var],weight=vals[4]["wgt"])
        else:
          output["dist_%s%s"%(prefix,var)].fill(cut="cut 4:nPFcand(SUEP)>=70", v1=vals[4][var],weight=vals[4]["wgt"])
        if(len(vals)>=6):
          output["dist_%s%s"%(prefix,var)].fill(cut="cut 5:eventBoosted Sphericity > 0.7", v1=vals[5][var],weight=vals[5]["wgt"])
          #output["dist_%s"%(var)].fill(cut="cut 3:Pre + nPVs < 30", v1=vals[5][var])
          #output["dist_%s"%(var)].fill(cut="cut 4:Pre + nPVs >=30", v1=vals[6][var])

        #output["dist_%s"%(var)].fill(cut="cut 4:FJ nPFCand>=80", v1=vals[4][var])
        return output
def packtrkFKID(output,vals,var,var2,prefix=""):
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 0:Preselection",          v1=ak.flatten(vals[0][var]), v2=ak.flatten(vals[0][var2]),weight=ak.flatten(vals[0]["wgt"]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 1: |eta| < 2.4",          v1=ak.flatten(vals[1][var]), v2=ak.flatten(vals[1][var2]),weight=ak.flatten(vals[1]["wgt"]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 2: q != 0",               v1=ak.flatten(vals[2][var]), v2=ak.flatten(vals[2][var2]),weight=ak.flatten(vals[2]["wgt"]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 3: PV = 0",               v1=ak.flatten(vals[3][var]), v2=ak.flatten(vals[3][var2]),weight=ak.flatten(vals[3]["wgt"]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 4: PFcand_pt > 0.5",      v1=ak.flatten(vals[4][var]), v2=ak.flatten(vals[4][var2]),weight=ak.flatten(vals[4]["wgt"]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 5: PFcand_pt > 0.6",      v1=ak.flatten(vals[5][var]), v2=ak.flatten(vals[5][var2]),weight=ak.flatten(vals[5]["wgt"]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 6: PFcand_pt > 0.7",      v1=ak.flatten(vals[6][var]), v2=ak.flatten(vals[6][var2]),weight=ak.flatten(vals[6]["wgt"]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 7: PFcand_pt > 0.75",     v1=ak.flatten(vals[7][var]), v2=ak.flatten(vals[7][var2]),weight=ak.flatten(vals[7]["wgt"]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 8: PFcand_pt > 0.8",      v1=ak.flatten(vals[8][var]), v2=ak.flatten(vals[8][var2]),weight=ak.flatten(vals[8]["wgt"]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 9: PFcand_pt > 0.9",      v1=ak.flatten(vals[9][var]), v2=ak.flatten(vals[9][var2]),weight=ak.flatten(vals[9]["wgt"]))
        output["dist_trkIDFK_%s%s"%(prefix,var)].fill(cut="cut 10: PFcand_pt > 1.0",     v1=ak.flatten(vals[10][var]), v2=ak.flatten(vals[10][var2]),weight=ak.flatten(vals[10]["wgt"]))
        return output
def packtrkID(output,vals,var,var2,var3,prefix=""):
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 0:Preselection",           v1=ak.flatten(vals[0][var]), v2=ak.flatten(vals[0][var2]), v3=ak.flatten(vals[0][var3]),weight=ak.flatten(vals[0]["wgt"]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 1: PFcand_pt > 0.5",       v1=ak.flatten(vals[1][var]), v2=ak.flatten(vals[1][var2]), v3=ak.flatten(vals[1][var3]),weight=ak.flatten(vals[1]["wgt"]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 2: PFcand_pt > 0.6",       v1=ak.flatten(vals[2][var]), v2=ak.flatten(vals[2][var2]), v3=ak.flatten(vals[2][var3]),weight=ak.flatten(vals[2]["wgt"]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 3: PFcand_pt > 0.7",       v1=ak.flatten(vals[3][var]), v2=ak.flatten(vals[3][var2]), v3=ak.flatten(vals[3][var3]),weight=ak.flatten(vals[3]["wgt"]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 4: PFcand_pt > 0.75",      v1=ak.flatten(vals[4][var]), v2=ak.flatten(vals[4][var2]), v3=ak.flatten(vals[4][var3]),weight=ak.flatten(vals[4]["wgt"]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 5: PFcand_pt > 0.8",       v1=ak.flatten(vals[5][var]), v2=ak.flatten(vals[5][var2]), v3=ak.flatten(vals[5][var3]),weight=ak.flatten(vals[5]["wgt"]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 6: PFcand_pt > 0.9",       v1=ak.flatten(vals[6][var]), v2=ak.flatten(vals[6][var2]), v3=ak.flatten(vals[6][var3]),weight=ak.flatten(vals[6]["wgt"]))
        output["dist_trkID_%s%s"%(prefix,var)].fill(cut="cut 7: PFcand_pt > 1.0",       v1=ak.flatten(vals[7][var]), v2=ak.flatten(vals[7][var2]), v3=ak.flatten(vals[7][var3]),weight=ak.flatten(vals[7]["wgt"]))
        return output
def packdistflat2D(output,vals,var1,var2,prefix=""):
        output["dist_%s%s_%s"%(prefix,var1,var2)].fill(cut="cut 0:No cut",       v1=ak.flatten(vals[0][var1]),v2 = ak.flatten(vals[0][var2]),weight=ak.flatten(vals[0]["wgt"]))
        output["dist_%s%s_%s"%(prefix,var1,var2)].fill(cut="cut 1:HT Trig",      v1=ak.flatten(vals[1][var1]),v2 = ak.flatten(vals[1][var2]),weight=ak.flatten(vals[1]["wgt"]))
        output["dist_%s%s_%s"%(prefix,var1,var2)].fill(cut="cut 2:Ht>=560",      v1=ak.flatten(vals[2][var1]),v2 = ak.flatten(vals[2][var2]),weight=ak.flatten(vals[2]["wgt"]))
        output["dist_%s%s_%s"%(prefix,var1,var2)].fill(cut="cut 3:fj>=2",        v1=ak.flatten(vals[3][var1]),v2 = ak.flatten(vals[3][var2]),weight=ak.flatten(vals[3]["wgt"]))
        output["dist_%s%s_%s"%(prefix,var1,var2)].fill(cut="cut 4:nPFCand(SUEP)>=70", v1=ak.flatten(vals[4][var1]),v2 = ak.flatten(vals[4][var2]),weight=ak.flatten(vals[4]["wgt"]))
        #if(len(vals)>=6):
        #  output["dist_%s%s"%(prefix,var)].fill(cut="cut 3:Pre + nPVs < 30", v1=ak.flatten(vals[5][var]))
        #  output["dist_%s%s"%(prefix,var)].fill(cut="cut 4:Pre + nPVs >=30", v1=ak.flatten(vals[6][var]))
        return output
def packdistflat(output,vals,var,prefix=""):
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 0:No cut",       v1=ak.flatten(vals[0][var]),weight=ak.flatten(vals[0]["wgt"]))
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 1:HT Trig",      v1=ak.flatten(vals[1][var]),weight=ak.flatten(vals[1]["wgt"]))
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 2:Ht>=560",      v1=ak.flatten(vals[2][var]),weight=ak.flatten(vals[2]["wgt"]))
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 3:fj>=2",        v1=ak.flatten(vals[3][var]),weight=ak.flatten(vals[3]["wgt"]))
        output["dist_%s%s"%(prefix,var)].fill(cut="cut 4:nPFCand(SUEP)>=70", v1=ak.flatten(vals[4][var]),weight=ak.flatten(vals[4]["wgt"]))
        #if(len(vals)>=6):
        #  output["dist_%s%s"%(prefix,var)].fill(cut="cut 3:Pre + nPVs < 30", v1=ak.flatten(vals[5][var]))
        #  output["dist_%s%s"%(prefix,var)].fill(cut="cut 4:Pre + nPVs >=30", v1=ak.flatten(vals[6][var]))
        return output
def packdist_fjn1(output,vals,var):
        output["dist_fjn1_%s"%(var)].fill(cut="cut 0:No cut",       v1=vals[0][var],weight=vals[0]["wgt"])
        output["dist_fjn1_%s"%(var)].fill(cut="cut 1:HT Trig",      v1=vals[1][var],weight=vals[1]["wgt"])
        output["dist_fjn1_%s"%(var)].fill(cut="cut 2:Ht>=560",      v1=vals[2][var],weight=vals[2]["wgt"])
        output["dist_fjn1_%s"%(var)].fill(cut="cut 3:nPFCand(SUEP)>=70", v1=vals[3][var],weight=vals[3]["wgt"])
        output["dist_fjn1_%s"%(var)].fill(cut="cut 4:BSphericity >=0.7",        v1=vals[4][var],weight=vals[4]["wgt"])
        return output
def packSR(output,vals,var):
        output["SR1_%s_0"%var].fill(axis="axis",       nPFCand=vals[3]["PFcand_ncount75"],eventBoostedSphericity=vals[3]["sphere_%s"%var],weight=vals[3]["wgt"])
        output["SR1_%s_1"%var].fill(axis="axis",       nPFCand=vals[3]["PFcand_ncount75"],eventBoostedSphericity=vals[3]["sphere1_%s"%var],weight=vals[3]["wgt"])
        output["SR1_%s_2"%var].fill(axis="axis",       nPFCand=vals[3]["FatJet_nconst"],eventBoostedSphericity=vals[3]["sphere_%s"%var],weight=vals[3]["wgt"])
        output["SR1_%s_3"%var].fill(axis="axis",       nPFCand=vals[3]["FatJet_nconst"],eventBoostedSphericity=vals[3]["sphere1_%s"%var],weight=vals[3]["wgt"])
        return output
def pack2D(output,vals,var1,var2):
        output["2d_%s_%s"%(var1,var2)].fill(cut="cut 0: No cut",       v1=vals[0][var1],v2=vals[0][var2],weight=vals[0]["wgt"])
        output["2d_%s_%s"%(var1,var2)].fill(cut="cut 1: No cut",       v1=vals[1][var1],v2=vals[1][var2],weight=vals[1]["wgt"])
        output["2d_%s_%s"%(var1,var2)].fill(cut="cut 2: No cut",       v1=vals[2][var1],v2=vals[2][var2],weight=vals[2]["wgt"])
        output["2d_%s_%s"%(var1,var2)].fill(cut="cut 3: No cut",       v1=vals[3][var1],v2=vals[3][var2],weight=vals[3]["wgt"])
        output["2d_%s_%s"%(var1,var2)].fill(cut="cut 4: No cut",       v1=vals[4][var1],v2=vals[4][var2],weight=vals[4]["wgt"])
        return output
def packtrig2D(output,vals,var1,var2):
        output["trig2d_%s_%s"%(var1,var2)].fill(cut="Cut 0: No cut",       v1=vals[0][var1],v2=vals[0][var2],weight=vals[0]["PUwgt"])
        output["trig2d_%s_%s"%(var1,var2)].fill(cut="Cut 1: HT Trig noRef",v1=vals[1][var1],v2=vals[1][var2],weight=vals[1]["PUwgt"])
        output["trig2d_%s_%s"%(var1,var2)].fill(cut="Cut 2: CaloJet 40 Ref Trig",     v1=vals[2][var1],v2=vals[2][var2],weight=vals[2]["PUwgt"])
        output["trig2d_%s_%s"%(var1,var2)].fill(cut="Cut 3: CaoloJet 40 Ref + HT Trig",  v1=vals[3][var1],v2=vals[3][var2],weight=vals[3]["PUwgt"])
        output["trig2d_%s_%s"%(var1,var2)].fill(cut="Cut 4: Mu Ref Trig",     v1=vals[4][var1],v2=vals[4][var2],weight=vals[4]["PUwgt"])
        output["trig2d_%s_%s"%(var1,var2)].fill(cut="Cut 5: Mu Ref + HT Trig",  v1=vals[5][var1],v2=vals[5][var2],weight=vals[5]["PUwgt"])
        return output

def fill_scalars(output,scalar0,vals,resolutions):
        vals_scalar1 = scalar0[vals[0].triggerHt >= 1]
        vals_scalar2 = vals_scalar1[vals[1].ht >= 560]
        vals_scalar3 = vals_scalar2[vals[2].FatJet_ncount50 >= 2]
        vals_scalar4 = vals_scalar3[vals[3].FatJet_nconst >= 70]
        vals_scalar = [scalar0,vals_scalar1,vals_scalar2,vals_scalar3,vals_scalar4]
        output = packdist(output,vals_scalar,"pt","scalar_")
        output = packdist(output,vals_scalar,"eta","scalar_")
        output = packdist(output,vals_scalar,"phi","scalar_")
        output = packdist(output,vals_scalar,"mass","scalar_")
        output = packdist(output,vals_scalar,"beta","scalar_")
        output = packsingledist(output,resolutions,"res_beta")
        output = packsingledist(output,resolutions,"res_pt")
        output = packsingledist(output,resolutions,"res_mass")
        output = packsingledist(output,resolutions,"res_dR")
        output = packsingledist(output,resolutions,"res_dPhi")
        output = packsingledist(output,resolutions,"res_dEta")
        return output

def fill_trkID(output,vals_tracks,vals,vals_gen0):
        print("filling cutflows trkID")
        trkID1 = vals_tracks[0][(vals[0].triggerHt >= 1) & (vals[0].ht >=560) ]
        #trkID1 = vals_tracks0[(vals0.triggerHt >= 1) & (vals0.ht >=560) &(vals0.FatJet_ncount50 >= 2)]

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

        vals_gen1 = vals_gen0[vals[0].triggerHt >= 1]
        vals_gen2 = vals_gen1[vals[1].ht >= 560]
        vals_gen3 = vals_gen2[vals[2].FatJet_ncount50 >= 2]
        vals_gen4 = vals_gen3[vals[3].FatJet_nconst >= 70]
        vals_gen = [vals_gen0,vals_gen1,vals_gen2,vals_gen3,vals_gen4]

        trkID5x = vals_gen2[vals_gen2.pt > 0.5]
        trkID6x = trkID5x[trkID5x.pt > 0.6]
        trkID7x = trkID6x[trkID6x.pt > 0.7]
        trkID8x = trkID7x[trkID7x.pt > 0.75]
        trkID9x = trkID8x[trkID8x.pt > 0.8]
        trkID10x = trkID9x[trkID9x.pt > 0.9]
        trkID11x = trkID10x[trkID10x.pt > 1.0]
        trkIDx = [vals_gen3,trkID5x,trkID6x,trkID7x,trkID8x,trkID9x,trkID10x,trkID11x]

        output = packtrkID(output,trkIDx,"pt" ,"gen_dR","gen_PV","gen_")
        output = packtrkID(output,trkIDx,"eta","gen_dR","gen_PV","gen_")
        output = packtrkID(output,trkIDx,"phi","gen_dR","gen_PV","gen_")
        output = packdistflat(output,vals_tracks,"PFcand_dR")
        output = packdistflat(output,vals_gen,"pt","gen_")
        output = packdistflat(output,vals_gen,"gen_dR")
        output = packdistflat(output,vals_gen,"eta","gen_")
        output = packdistflat(output,vals_gen,"phi","gen_")
        output = packdistflat(output,vals_gen,"gen_PV")
        output = packdistflat(output,vals_gen,"gen_PVdZ")
        #output = packsingledist(output,alldRtracks,"PFcand_alldR",wgt=False)
        return output
def fill_trigs(output,vals0):
        print("filling cutflows trigs")
        trig1 = vals0[vals0.triggerHt >=1] #HT no ref
        trig2 = vals0[vals0.triggerCalo >=1] # calojet ref
        trig3 = trig2[trig2.triggerHt >=1] # calojet +ht
        trig4 = vals0[vals0.triggerMu >=1] # mu ref
        trig5 = trig4[trig4.triggerHt >=1] # mu ref + ht
        trigs = [vals0,trig1,trig2,trig3,trig4,trig5]

        output = packtrig(output,trigs,"ht")
        output = packtrig(output,trigs,"ht20")
        output = packtrig(output,trigs,"ht30")
        output = packtrig(output,trigs,"ht40")
        output = packtrig(output,trigs,"ht50")

        output = packtrig(output,trigs,"n_pfMu")
        output = packtrig(output,trigs,"event_sphericity")
        output = packtrig(output,trigs,"FatJet_nconst")
        output = packtrig2D(output,trigs,"ht","event_sphericity")
        output = packtrig2D(output,trigs,"ht","FatJet_nconst")
        return output
def fill_vertex(output,vals_vertex0,vals):
        print("filling cutflows vertex")
        vals_vertex1 = vals_vertex0[vals[0].triggerHt >= 1]
        vals_vertex2 = vals_vertex1[vals[1].ht >= 560]
        vals_vertex3 = vals_vertex2[vals[2].FatJet_ncount50 >= 2]
        vals_vertex4 = vals_vertex3[vals[3].FatJet_nconst >=70]
        vals_vertex = [vals_vertex0,vals_vertex1,vals_vertex2,vals_vertex3,vals_vertex4]
        output = packdistflat(output,vals_vertex,"Vertex_valid","")
        output = packdistflat(output,vals_vertex,"Vertex_tracksSize","")
        output = packdistflat(output,vals_vertex,"Vertex_chi2","")
        output = packdistflat(output,vals_vertex,"Vertex_ndof","")
        output = packdistflat(output,vals_vertex,"Vertex_z","")
        return output
def fill_fatjet(output,vals,spherey2):
        print("filling cutflows FatJets")
        fj3 = spherey2[spherey2.FatJet_nconst >=70]
        fj4 = fj3[fj3.sphere1_suep >= 0.7]
        vals_fj = [vals[0],vals[1],vals[2],fj3,fj4]
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount30")
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount50")
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount100")
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount150")
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount200")
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount250")
        output = packdist_fjn1(output,vals_fj,"FatJet_ncount300")
        return output
def fill_PFncounts(output,valsx):
        output = packdist(output,valsx,"FatJet_nconst")
        output = packdist(output,valsx,"PFcand_ncount0")
        output = packdist(output,valsx,"PFcand_ncount50")
        output = packdist(output,valsx,"PFcand_ncount60")
        output = packdist(output,valsx,"PFcand_ncount70")
        output = packdist(output,valsx,"PFcand_ncount75")
        output = packdist(output,valsx,"PFcand_ncount80")
        output = packdist(output,valsx,"PFcand_ncount90")
        output = packdist(output,valsx,"PFcand_ncount100")
        output = packdist(output,valsx,"PFcand_ncount150")
        output = packdist(output,valsx,"PFcand_ncount200")
        output = packdist(output,valsx,"PFcand_ncount300")
        return output
def fill_jets(output,corrected_jets,vals,vals_fatjet0,vals_nsub0):
        print("filling cutflows jets, fatjets, and nsub")
        vals_jet1 = corrected_jets[vals[0].triggerHt >= 1]
        vals_jet2 = vals_jet1[vals[1].ht >= 560]
        vals_jet3 = vals_jet2[vals[2].FatJet_ncount50 >= 2]
        vals_jet4 = vals_jet3[vals[3].FatJet_nconst >= 70]

        vals_fatjet1 = vals_fatjet0[vals[0].triggerHt >= 1]
        vals_fatjet2 = vals_fatjet1[vals[1].ht >= 560]
        vals_fatjet3 = vals_fatjet2[vals[2].FatJet_ncount50 >= 2]
        vals_fatjet4 = vals_fatjet3[vals[3].FatJet_nconst >= 70]

        vals_nsub1 = vals_nsub0[vals[0].triggerHt >= 1]
        vals_nsub2 = vals_nsub1[vals[1].ht >= 560]
        vals_nsub3 = vals_nsub2[vals[2].FatJet_ncount50 >= 2]
        vals_nsub4 = vals_nsub3[vals[3].FatJet_nconst >= 70]
        vals_jet = [corrected_jets,vals_jet1,vals_jet2,vals_jet3,vals_jet4]
        vals_fatjet = [vals_fatjet0,vals_fatjet1,vals_fatjet2,vals_fatjet3,vals_fatjet4]
        vals_nsub = [vals_nsub0,vals_nsub1,vals_nsub2,vals_nsub3,vals_nsub4]

        output = packdistflat(output,vals_jet,"pt","Jet_")
        output = packdistflat(output,vals_jet,"eta","Jet_")
        output = packdistflat(output,vals_jet,"phi","Jet_")
        output = packdistflat(output,vals_nsub,"tau21","")
        output = packdistflat(output,vals_nsub,"tau32","")
        output = packdistflat(output,vals_fatjet,"pt","FatJet_")
        output = packdistflat(output,vals_fatjet,"eta","FatJet_")
        output = packdistflat(output,vals_fatjet,"phi","FatJet_")
        return output
def fill_vals(output, vals):
        print("filling cutflows vals")
        output = packdistnowgt(output,vals,"ht")
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
        #output = packdist(output,vals,"Vertex_minZ")
        #output = packdist(output,vals,"Vertex_tracksSize0")
        output = packdist(output,vals,"FatJet_ncount30")
        output = packdist(output,vals,"FatJet_ncount50")
        output = packdist(output,vals,"FatJet_ncount100")
        output = packdist(output,vals,"FatJet_ncount150")
        output = packdist(output,vals,"FatJet_ncount200")
        output = packdist(output,vals,"FatJet_ncount250")
        output = packdist(output,vals,"FatJet_ncount300")
        return output
def fill_offtracks(output,vals_offtracks):
        print("filling cutflows trk")

        output = packdistflat(output,vals_offtracks,"pt","offlinetrk_")
        output = packdistflat(output,vals_offtracks,"eta","offlinetrk_")
        output = packdistflat(output,vals_offtracks,"phi","offlinetrk_")
        output = packdistflat2D(output,vals_offtracks,"pt","eta","offlinetrk_")
        return output
def fill_tracks(output,vals_tracks):
        print("filling cutflows trk")

        output = packdistflat(output,vals_tracks,"pt","PFcand_")
        output = packdistflat(output,vals_tracks,"eta","PFcand_")
        output = packdistflat(output,vals_tracks,"phi","PFcand_")
        output = packdistflat2D(output,vals_tracks,"pt","eta","PFcand_")
        return output
