#include "TROOT.h"
#include "omp.h"
#include "TTree.h"
#include "TFile.h"
#include "TBranch.h"
#include "Math/PtEtaPhiE4D.h"
#include "Math/PtEtaPhiM4D.h"
#include "Math/LorentzVector.h"
#include "Math/Vector4Dfwd.h"
#include "fastjet/ClusterSequence.hh"
#include "fastjet/PseudoJet.hh"
#include <cmath>
#include <tuple>
#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include "TLorentzVector.h"
using namespace fastjet;
using namespace std;

#include <vector>


float scalarDR(PseudoJet jet,ROOT::Math::PtEtaPhiEVector scalar){
    float dPhi = abs(jet.phi() - scalar.Phi());
    if(dPhi > M_PI){dPhi = dPhi - 2*M_PI;}
    float dEta = jet.eta() - scalar.Eta();
    float dR = sqrt(dEta*dEta + dPhi*dPhi);
  return dR;
}
tuple<double,double,double,double,double,double> jet_angularities(PseudoJet jet,float R){
  float girth = 0;
  float pt_dispersion = 0;
  float lesHouches = 0;
  float thrust = 0;
  float pt_avg =0;
  int count =0;
  vector<PseudoJet> constituents = jet.constituents();
  vector<float> pt_sorted;
  for(int i=0; i< constituents.size(); i++){
    float phi = constituents[i].phi();
    float eta = constituents[i].eta();
    float pt = constituents[i].pt();
    auto it = upper_bound(pt_sorted.cbegin(),pt_sorted.cend(),pt);
    pt_sorted.insert(it,pt);
    float dPhi = abs(jet.phi() - phi);
    if(dPhi > M_PI){dPhi = dPhi - 2*M_PI;}
    float dEta = jet.eta() - eta;
    float dR = sqrt(dEta*dEta + dPhi*dPhi);
    girth += pt * dR/R; // divide by R is new
    pt_dispersion = pt*pt;
    lesHouches = pt *sqrt(dR/R);
    thrust = pt * (dR/R)*(dR/R);
    pt_avg += pt;
    count += 1;
  }
  int size = pt_sorted.size();
  float median_pt;
  if(size == 0){median_pt =0;}
  else{
    median_pt = pt_sorted.size() %2 == 1? pt_sorted.at(((pt_sorted.size()+1)/2)-1): pt_sorted.at((pt_sorted.size()/2)-1);
  }
  return {(girth / jet.pt()),((pt_avg/count)/jet.pt()),median_pt/jet.pt(),pt_dispersion/(jet.pt()*jet.pt()),lesHouches/jet.pt(),thrust/jet.pt()};
}

tuple<double,double,double,double,double> nsubjettiness(PseudoJet jet, float R){

  vector<PseudoJet> constituents = jet.constituents();
  JetDefinition jet_def(kt_algorithm,R);
  ClusterSequence cs(constituents,jet_def);
  vector<PseudoJet> jets_2 = sorted_by_pt(cs.exclusive_jets(2));
  vector<PseudoJet> jets_3 = sorted_by_pt(cs.exclusive_jets(3));
  float eta_1_0 = jet.eta();
  float phi_1_0 = jet.phi();
  float eta_2_0 = jets_2[0].eta();
  float eta_2_1 = jets_2[1].eta();
  float phi_2_0 = jets_2[0].phi();
  float phi_2_1 = jets_2[1].phi();
  float eta_3_0 = jets_3[0].eta();
  float eta_3_1 = jets_3[1].eta();
  float eta_3_2 = jets_3[2].eta();
  float phi_3_0 = jets_3[0].phi();
  float phi_3_1 = jets_3[1].phi();
  float phi_3_2 = jets_3[2].phi();


  float t1 =0;
  float t2 =0;
  float t3 =0;
  float e2 =0;
  float e3 =0;
  for(int i=0; i<constituents.size(); i++){
    float phi = constituents[i].phi();
    float eta = constituents[i].eta();
    float pt = constituents[i].pt();

    float dEta_1_0 = eta_1_0-eta;
    float dPhi_1_0 = phi_1_0-phi > M_PI? (phi_1_0 -phi) - 2*M_PI:phi_1_0 -phi;

    float dEta_2_0 = eta_2_0-eta;
    float dEta_2_1 = eta_2_1-eta;
    float dPhi_2_0 = phi_2_0-phi > M_PI? (phi_2_0 -phi) - 2*M_PI:phi_2_0 -phi;
    float dPhi_2_1 = phi_2_1-phi > M_PI? (phi_2_1 -phi) - 2*M_PI:phi_2_1 -phi;

    float dEta_3_0 = eta_3_0-eta;
    float dEta_3_1 = eta_3_1-eta;
    float dEta_3_2 = eta_3_2-eta;
    float dPhi_3_0 = phi_3_0-phi > M_PI? (phi_3_0 -phi) - 2*M_PI:phi_3_0 -phi;
    float dPhi_3_1 = phi_3_1-phi > M_PI? (phi_3_1 -phi) - 2*M_PI:phi_3_1 -phi;
    float dPhi_3_2 = phi_3_2-phi > M_PI? (phi_3_2 -phi) - 2*M_PI:phi_3_2 -phi;

    float dR_1 = sqrt(dEta_1_0*dEta_1_0 + dPhi_1_0*dPhi_1_0);

    float dR_2_0 = sqrt(dEta_2_0*dEta_2_0 + dPhi_2_0*dPhi_2_0);
    float dR_2_1 = sqrt(dEta_2_1*dEta_2_1 + dPhi_2_1*dPhi_2_1);
    float dR_2 = dR_2_0 < dR_2_1? dR_2_0: dR_2_1; // take minimum

    float dR_3_0 = sqrt(dEta_3_0*dEta_3_0 + dPhi_3_0*dPhi_3_0);
    float dR_3_1 = sqrt(dEta_3_1*dEta_3_1 + dPhi_3_1*dPhi_3_1);
    float dR_3_2 = sqrt(dEta_3_2*dEta_3_2 + dPhi_3_2*dPhi_3_2);
    float dR_3x = dR_3_0 < dR_3_1? dR_3_0: dR_3_1; // take min{0,1}
    float dR_3 = dR_3x < dR_3_2? dR_3x: dR_3_2; // take min{3, min{0,1}}
    t1 += pt* dR_1; //n subjettiness 1
    t2 += pt* dR_2; //n subjettiness 2
    t3 += pt* dR_3; //n subjettiness 3
    for(int j=0; j<i;j++){
      float phi_j = constituents[j].phi();
      float eta_j = constituents[j].eta();
      float pt_j = constituents[j].pt();
      float dEta_j = eta_j - eta;
      float dPhi_j = phi_j-phi > M_PI? (phi_j -phi) - 2*M_PI:phi_j -phi;
      float dR_ij = sqrt(dEta_j*dEta_j + dPhi_j*dPhi_j);
      e2 += pt*pt_j*dR_ij;
      for(int k=0; k<j;k++){
        float phi_k = constituents[k].phi();
        float eta_k = constituents[k].eta();
        float pt_k = constituents[k].pt();
        float dEta_ki = eta_k - eta;
        float dPhi_ki = phi_k-phi > M_PI? (phi_k -phi) - 2*M_PI:phi_k -phi;
        float dR_ki = sqrt(dEta_ki*dEta_ki + dPhi_ki*dPhi_ki);

        float dEta_kj = eta_j - eta_k;
        float dPhi_kj = phi_j-phi_k > M_PI? (phi_j -phi_k) - 2*M_PI:phi_j -phi_k;
        float dR_kj = sqrt(dEta_kj*dEta_kj + dPhi_kj*dPhi_kj);
        e3 += pt*pt_j*pt_k*dR_ij*dR_ki*dR_kj;
        //printf("e3: %e %f %f %f %f %f %f %f %f\n",e3,pt,pt_j,pt_k,dR_ij,dR_ki,dR_kj,dEta_kj,dPhi_kj);
    
      }
    }
  
  }

  return{ t1/jet.pt(),t2/jet.pt(), t3/jet.pt(),e2/(jet.pt()*jet.pt()),e3/(jet.pt()*jet.pt()*jet.pt())};
}



tuple<int,int,float/*,float, float,float,float,float*/> jet_constituents(PseudoJet jet, vector<ROOT::Math::PtEtaPhiEVector> sueps, vector<ROOT::Math::PtEtaPhiEVector> isrs){
    int scalar_part = 0;
    int isr_part = 0;
    float suep_pt =0;
    float total_pt =0;
//    ROOT::Math::PtEtaPhiEVector gen_4vec;
//    ROOT::Math::PtEtaPhiMVector reco_4vec;
//    ROOT::Math::PtEtaPhiMVector fin_4vec;
//    PseudoJet reco_pseudo;
//    PseudoJet gen_pseudo;
//    gen_4vec.SetXYZT(0,0,0,0); 
//    reco_4vec.SetXYZT(0,0,0,0); 
//    fin_4vec.SetXYZT(0,0,0,0); 
    vector<PseudoJet> constituents = jet.constituents();
    for(int i=0; i< constituents.size(); i++){
    float min_dR = 9999;
    bool is_scalar = false;
    int gen_thissuep=-1;
    float phi = constituents[i].phi();
    float eta = constituents[i].eta();
    float pt = constituents[i].pt();
    for(int j=0; j<sueps.size();j++){
      if(abs(sueps[j].pt() - pt)/sueps[j].pt() > 0.3) {continue;}
      float dPhi = abs(sueps[j].phi() - phi);
      if(dPhi > M_PI){dPhi = dPhi - 2*M_PI;}
      float dEta = sueps[j].eta() - eta;
      float dR = sqrt(dEta*dEta + dPhi*dPhi);
      //printf("%f\n",dR);
      if(dR < min_dR){
        is_scalar = true;
//        gen_thissuep=j;
        min_dR = dR;
      }
    }
    for(int j=0; j<isrs.size();j++){
      if(abs(isrs[j].pt() - pt)/isrs[j].pt() > 0.3) {continue;}
      float dPhi = abs(isrs[j].phi() - phi);
      if(dPhi > M_PI){dPhi = dPhi - 2*M_PI;}
      float dEta = isrs[j].eta() - eta;
      float dR = sqrt(dEta*dEta + dPhi*dPhi);
      if(dR < min_dR){
        is_scalar = false;
        min_dR = dR;
      }
    }
    if(is_scalar){ 
      scalar_part++;
      suep_pt+=pt;
//      gen_4vec += sueps[gen_thissuep];
//      reco_pseudo += constituents[i];
//      ROOT::Math::PtEtaPhiMVector reco_thissuep(pt,eta,phi,constituents[i].m());
//      reco_4vec += reco_thissuep;
//      ROOT::Math::PtEtaPhiMVector fin_thissuep(pt,eta,phi,sueps[gen_thissuep].M());
//      fin_4vec += fin_thissuep;
//      PseudoJet gen_thissuepv2(sueps[gen_thissuep].Px(),sueps[gen_thissuep].Py(),sueps[gen_thissuep].Pz(),sueps[gen_thissuep].E());
//      gen_pseudo += gen_thissuepv2;
      //printf("%d %f %f %f %f %f %f %f %f\n",i,pt,sueps[gen_thissuep].pt(),eta,sueps[gen_thissuep].eta(),phi,sueps[gen_thissuep].phi(),constituents[i].m(),sueps[gen_thissuep].M());
    }
    else {isr_part++;}
    total_pt+=pt;
    //if(min_dR < 1000){printf("%f\n",min_dR);} 
  }
  return {scalar_part, isr_part, suep_pt/total_pt};//, gen_pseudo.m(),gen_4vec.M(), reco_pseudo.m(),reco_4vec.M(),fin_4vec.M()};
}

    //run different clustering algorithms
inline JetDefinition getJetDef(int algo, float Ri){
    if(algo == 0){JetDefinition jet_def(cambridge_algorithm,Ri);
      return jet_def;
    }
    if(algo == 1){JetDefinition jet_def(kt_algorithm,Ri);
      return jet_def;
    }
    else{JetDefinition jet_def(antikt_algorithm,Ri);
      return jet_def;
    }
}

int main(int argc,char** argv){
  printf("Starting\n");
  ROOT::EnableThreadSafety();  
  ROOT::EnableImplicitMT();
  //TFile *infile = TFile::Open("root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v0.2/2018/NTUP/PrivateSamples.SUEP_2018_mMed-1000_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_0_RA2AnalysisTree.root");
  string file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v0.2/2018/NTUP/";
  int data=-1;
  vector<int> skip;
  string sample;
  if(argc!=1){data = atoi(argv[1]);}
  switch(data){
  case -1: file += "PrivateSamples.SUEP_2018_mMed-1000_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root";sample="test"; break;
  //case -1: file += "PrivateSamples.SUEP_2018_mMed-1000_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-100_0_RA2AnalysisTree.root";sample="test"; break;
  case 0: file += "PrivateSamples.SUEP_2018_mMed-1000_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root";sample="sig_1000"; break;
  case 1: file += "PrivateSamples.SUEP_2018_mMed-750_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_750";break;
  case 2: file += "PrivateSamples.SUEP_2018_mMed-400_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_400";break;
  case 3: file += "Autumn18.QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root";   sample="qcd_300";break;
  case 4: file += "Autumn18.QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root";   sample="qcd_500";break;
  case 5: file += "Autumn18.QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root";  sample="qcd_700";break;
  case 6: file += "Autumn18.QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root"; sample="qcd_1000"; break;
  case 7: file += "Autumn18.QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root"; sample="qcd_1500";break;
  case 8: file += "Autumn18.QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root";  sample="qcd_2000"; break;
  case 9: file += "PrivateSamples.SUEP_2018_mMed-125_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_125";break;
  case 10: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.0/2018/NTUP/PrivateSamples.SUEP_2018_mMed-200_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_200";break;
  case 11: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.0/2018/NTUP/PrivateSamples.SUEP_2018_mMed-300_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_300";break;
  default: file += "PrivateSamples.SUEP_2018_mMed-1000_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_1000";break;
  }
  int batch = 0;
  if(argc>=3){batch = atoi(argv[2]);}
  //printf("opening file: %s\n",file.c_str());
  printf("sample: %s; batch:%d\n",sample.c_str(),batch);
  FILE* OutFile = fopen(("data/"+sample+"_v"+to_string(batch)+".txt").c_str(),"w");
  TFile *infile = TFile::Open(file.c_str());

  TTree *t1= (TTree*)infile->Get("TreeMaker2/PreSelection");
  vector<ROOT::Math::PtEtaPhiEVector>* genPart = 0;
  vector<ROOT::Math::DisplacementVector3D<ROOT::Math::Cartesian3D<double>>>* trkPart =0;
  double ht;
  vector<int>* gen_parentId=0;
  vector<int>* gen_charge =0;
  vector<int>* gen_pdgId =0;
  vector<int>* gen_status=0;
  vector<int>* trk_pv =0;
  vector<bool>* trk_matched =0;
  int nvtx =0;
  int numInteractions =0;
  t1->SetBranchAddress("GenParticles",&genPart);
  t1->SetBranchAddress("Tracks",&trkPart);
  t1->SetBranchAddress("HT",&ht);
  t1->SetBranchAddress("GenParticles_ParentId",&gen_parentId);
  t1->SetBranchAddress("GenParticles_Charge",&gen_charge);
  t1->SetBranchAddress("GenParticles_PdgId",&gen_pdgId);
  t1->SetBranchAddress("GenParticles_Status",&gen_status);
  t1->SetBranchAddress("Tracks_fromPV0",&trk_pv);
  t1->SetBranchAddress("Tracks_matchedToPFCandidate",&trk_matched);
  t1->SetBranchAddress("NVtx",&nvtx);
  t1->SetBranchAddress("NumInteractions",&numInteractions);
//#pragma omp parallel for 

  int nentries=0;// = 10000;
  if(batch==0) {
    nentries=10000;
    fprintf(OutFile,"event algo R jetid pt eta phi multiplicity girth mass trkpt medpt suep isr suep_tot isr_tot nvtx numInteractions scalar_dR scalar_pt scalar_eta scalar_phi suep_Ptwgt scalar_mass beta scalar_beta pt_dispersion lesHouches thrust t1 t2 t3 e2 e3\n");
  }
  else{nentries=t1->GetEntries();}
  //printf("b %d e %d\n",batch,nentries);
  for(int entry=10000*batch; entry<nentries; entry++){
  //for(int entry=24; entry<25; entry++){
    if(entry%1000==0) {printf("entry %d/%d\n",entry,nentries);}
    //if(find(skip.begin(),skip.end(),entry) != skip.end()){printf("skipping entry: %d\n",entry); continue;}
    t1->GetEntry(entry);
    if(ht <1200){ continue;}
    vector<ROOT::Math::PtEtaPhiEVector> sueps;
    vector<ROOT::Math::PtEtaPhiEVector> isrs;
    ROOT::Math::PtEtaPhiEVector scalar;
    scalar.SetXYZT(0,0,0,0);

    // sort gen particles into isr and sueps
    for(int igen=0;igen<genPart->size();igen++){
      if(abs(gen_charge->at(igen)) != 1 || gen_status->at(igen) != 1 || abs(genPart->at(igen).eta()) >= 2.5 || genPart->at(igen).pt() <= 1){continue;}
      int pdgid = abs(gen_pdgId->at(igen));
      if((pdgid != 11) && (pdgid != 13) && (pdgid != 22) && (pdgid < 100 )){continue;}
      if(gen_parentId->at(igen) == 999998){ sueps.push_back(genPart->at(igen));scalar+=genPart->at(igen);} 
      else{ isrs.push_back(genPart->at(igen));} 

    }
    //printf("scalar: %f %f %f\n",scalar.Pt(),scalar.Eta(),scalar.Phi());
    vector<PseudoJet> particles;
    for(int itrk=0;itrk<trkPart->size();itrk++){
      if ((trk_pv->at(itrk) <2) || (trk_matched->at(itrk) ==0)){continue;}

    double trkx = trkPart->at(itrk).x();
    double trky = trkPart->at(itrk).y();
    double trkz = trkPart->at(itrk).z();
    //ROOT::Math::PxPyPzEVector trk;
    TLorentzVector trk;
    //trk.SetPxPyPzE(trkx,trky,trkz,trkx*trkx+trky*trky+trkz*trkz+0.13957*0.13957);
    trk.SetXYZM(trkx,trky,trkz,0.13957);
    //trk.SetPtEtaPhiM(trkPart->at(itrk).Pt(),trkPart->at(itrk).Eta(),trkPart->at(itrk).Phi(),0.13957);
    if(trk.Pt() <= 1 || abs(trk.Eta()) >= 2.5){continue;}
    //particles.push_back(PseudoJet(trkx,trky,trkz,trkPart->at(itrk).e()));
    //particles.push_back(PseudoJet(trkx,trky,trkz,trkx*trkx+trky*trky+trkz*trkz+0.13957*0.13957));
    particles.push_back(PseudoJet(trk.Px(),trk.Py(),trk.Pz(),trk.E()));
    //particles.push_back(PseudoJet(trk.Px(),trk.Py(),trk.Pz(),sqrt(trk.Px()*trk.Px()+trk.Py()*trk.Py()+trk.Pz()*trk.Pz()+0.13957*0.13957)));
    //printf("x: %f, y: %f, z: %f, E: %f, pt: %f, eta: %f, phi: %f\n",trk.X(),trk.Y(),trk.Z(),trk.E(),trk.Pt(),trk.Eta(),trk.Phi());
    //printf("x: %f, y: %f, z: %f, E: %f, pt: %f, eta: %f, phi: %f\n",trk.x(),trk.y(),trk.z(),trk.E(),trk.Pt(),trk.Eta(),trk.Phi());
    }

    ////run different clustering algorithms
    int algos[] = {-1,0,1};
    float Rs[] = {0.8,1.0,1.5,2.0};
//#pragma omp parallel for
    for(int algo : algos){
//#pragma omp parallel for
      for(float Ri : Rs){
    
        JetDefinition jet_def = getJetDef(algo,Ri);
        ClusterSequence cs(particles,jet_def);
        vector<PseudoJet> jets = sorted_by_pt(cs.inclusive_jets(30));
        //vector<PseudoJet> jets = sorted_by_pt(cs.exclusive_jets(5));
        unsigned int max_tracks = 0;
        int highest_index = -1;
        for(int i = 0; i < jets.size(); i++) {
          PseudoJet jet = jets[i];
          //printf("%d \n",jet.constituents().size());
          if (jet.constituents().size() > max_tracks){ // save only highest multiplicity jet (less data)
          //printf("%d %d %d %d\n",entry,algo,Ri,highest_index);
            highest_index = i;
            max_tracks = jet.constituents().size();
          }
        }
          if(highest_index == -1){continue;}
          //if(highest_index !=0){printf("%d %d %d %d\n",entry,algo,Ri,highest_index);}
          PseudoJet jet = jets[highest_index];
          auto [suep_part, isr_part,suep_ptwgt/*,genpseudo,gen4vecmass,recopseudo,reco4vecmass,fin4vecmass*/] = jet_constituents(jet,sueps,isrs);
          auto [girth, trackpt,medpt,pt_dispersion,lesHouches,thrust] = jet_angularities(jet,Ri);
          auto scalar_dr = scalarDR(jet,scalar);
          float beta = sqrt(jet.modp2())/jet.E();
          float scalar_beta = scalar.Beta();
          auto [t1,t2,t3,e2,e3] = nsubjettiness(jet,Ri);

          //printf("%d %d %.1f %d %f %f %f %d %f %f %f %d %d %d %d %d %d\n",entry,algo, Ri,i,jet.pt(),jet.eta(),jet.phi(),jet.constituents().size(),girth,sqrt(jet.m()),trackpt, suep_part, isr_part,sueps.size(), isrs.size(), nvtx, numInteractions);   
          fprintf(OutFile,"%d %d %.1f %d %f %f %f %d %f %f %f %f %d %d %d %d %d %d %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f\n",
                 entry,algo, Ri,highest_index,//0-3
                 jet.pt(),jet.eta(),jet.phi(),jet.constituents().size(),//4-7
                 girth,/*sqrt(*/jet.m()/*)*/,trackpt,medpt,//8-11
                 suep_part, isr_part,sueps.size(), isrs.size(), //12-15
                 nvtx, numInteractions,//16-17
                 scalar_dr,scalar.Pt(),scalar.Eta(),scalar.Phi(),suep_ptwgt,scalar.M(),//18-23
                 beta,scalar_beta,//24-25
                 pt_dispersion,lesHouches,thrust,//26-28,genpseudo,gen4vecmass,recopseudo,reco4vecmass,fin4vecmass); 
                 t1,t2,t3,e2,e3 //29-33
                 );
        //}
      }
    }

  }
fclose(OutFile);
}
  
