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


void getAllGen(vector<ROOT::Math::PtEtaPhiEVector> sueps, vector<ROOT::Math::PtEtaPhiEVector> isrs, vector<int> suep_id,vector<int> isr_id,FILE* OutFileGen,int entry){
  for(int gen_i=0; gen_i < sueps.size(); gen_i++){
          fprintf(OutFileGen,"%f %f %f %d 0 %d %d %d\n",
          sueps[gen_i].pt(),sueps[gen_i].eta(),sueps[gen_i].phi(),suep_id[gen_i], sueps.size(), isrs.size(), entry);
  }
  for(int gen_i=0; gen_i < isrs.size(); gen_i++){
          fprintf(OutFileGen,"%f %f %f %d 1 %d %d %d\n",
          isrs[gen_i].pt(),isrs[gen_i].eta(),isrs[gen_i].phi(),isr_id[gen_i], sueps.size(), isrs.size(), entry);
  }
}
void gen_match_remove(vector<PseudoJet> reco, vector<ROOT::Math::PtEtaPhiEVector> sueps, vector<ROOT::Math::PtEtaPhiEVector> isrs,FILE* OutFile,vector<vector<float>> reco_extra, vector<int> suep_id,vector<int> isr_id){
  if(reco.size() ==0) {return;}
  if( sueps.size() + isrs.size() ==0) {return;}
  float min_dR = 9999;
  int used_gen = -1;
  int used_reco = -1;
  int is_isr =-1;
  for(int gen_i=0; gen_i < sueps.size()+isrs.size(); gen_i++){
    for(int reco_i=0; reco_i < reco.size(); reco_i++){
       float dEta;
       float dPhi;
       float dPt;
       if(gen_i < sueps.size()){
        dEta = reco[reco_i].eta() - sueps[gen_i].eta();
        dPhi = abs(reco[reco_i].phi() - sueps[gen_i].phi());
        dPt = abs(reco[reco_i].pt() - sueps[gen_i].pt())/(sueps[gen_i].pt());
       }
       else{
        dEta = reco[reco_i].eta() - isrs[gen_i-sueps.size()].eta();
        dPhi = abs(reco[reco_i].phi() - isrs[gen_i-sueps.size()].phi());
        dPt = abs(reco[reco_i].pt() - isrs[gen_i-sueps.size()].pt())/(isrs[gen_i-sueps.size()].pt());
       }
       if(dPhi > M_PI){dPhi = dPhi - 2*M_PI;}
       float dR = sqrt(dEta*dEta + dPhi*dPhi);
       if( dR < min_dR && dPt < 0.3){
          is_isr= (gen_i>=sueps.size());
          min_dR = dR;
          used_gen = gen_i-(is_isr*sueps.size());
          used_reco = reco_i;
       }
    }
  }
  if(min_dR < 0.3){
  if (is_isr == 0){ 
    //fprintf(OutFile,"%d %d %d %f %d %d %f %f %f %f %f %f %d %f %f\n",reco.size(),sueps.size(),isrs.size(),min_dR,used_gen,used_reco,reco[used_reco].pt(),reco[used_reco].eta(),reco[used_reco].phi(),sueps[used_gen].pt(),sueps[used_gen].eta(),sueps[used_gen].phi(),is_isr,reco_extra.at(used_gen).at(0),reco_extra.at(used_gen).at(1));
    fprintf(OutFile,"%d %d %d"
           " %f %d %d %d"
           " %f %f %f"
           " %f %f %f"
           " %d %d %d"
           " %d %f %d"
           " %d %d %d"
           " %d %d"
           "\n",
          reco.size(),sueps.size(),isrs.size(),
          min_dR,used_gen,used_reco,is_isr,
          reco[used_reco].pt(),reco[used_reco].eta(),reco[used_reco].phi(),
          sueps[used_gen].pt(),sueps[used_gen].eta(),sueps[used_gen].phi(),
          static_cast<int>(reco_extra.at(used_reco).at(0)),static_cast<int>(reco_extra.at(used_reco).at(1)), static_cast<int>(reco_extra.at(used_reco).at(2)),
          static_cast<int>(reco_extra.at(used_reco).at(3)),reco_extra.at(used_reco).at(4), static_cast<int>(reco_extra.at(used_reco).at(5)),
          static_cast<int>(reco_extra.at(used_reco).at(6)),static_cast<int>(reco_extra.at(used_reco).at(7)),suep_id[used_gen],
          static_cast<int>(reco_extra.at(used_reco).at(8)),static_cast<int>(reco_extra.at(used_reco).at(9))
          );
    sueps.erase(sueps.begin()+used_gen);
    reco.erase(reco.begin()+used_reco);
    reco_extra.erase(reco_extra.begin()+used_reco);
    suep_id.erase(suep_id.begin()+used_gen);
    gen_match_remove(reco,sueps,isrs,OutFile,reco_extra,suep_id,isr_id);
  }
  else if (is_isr==1){ 
    //fprintf(OutFile,"%d %d %d %f %d %d %f %f %f %f %f %f %d %f %f\n",reco.size(),sueps.size(),isrs.size(),min_dR,used_gen,used_reco,reco[used_reco].pt(),reco[used_reco].eta(),reco[used_reco].phi(),isrs[used_gen].pt(),isrs[used_gen].eta(),isrs[used_gen].phi(),is_isr,reco_extra.at(used_gen).at(0),reco_extra.at(used_gen).at(1));
    fprintf(OutFile,"%d %d %d"
           " %f %d %d %d"
           " %f %f %f"
           " %f %f %f"
           " %d %d %d"
           " %d %f %d"
           " %d %d %d"
           " %d %d"
           "\n",
          reco.size(),sueps.size(),isrs.size(),
          min_dR,used_gen,used_reco,is_isr,
          reco[used_reco].pt(),reco[used_reco].eta(),reco[used_reco].phi(),
          isrs[used_gen].pt(),isrs[used_gen].eta(),isrs[used_gen].phi(),
          static_cast<int>(reco_extra.at(used_reco).at(0)),static_cast<int>(reco_extra.at(used_reco).at(1)), static_cast<int>(reco_extra.at(used_reco).at(2)),
          static_cast<int>(reco_extra.at(used_reco).at(3)),reco_extra.at(used_reco).at(4), static_cast<int>(reco_extra.at(used_reco).at(5)),
          static_cast<int>(reco_extra.at(used_reco).at(6)),static_cast<int>(reco_extra.at(used_reco).at(7)),isr_id[used_gen],
          static_cast<int>(reco_extra.at(used_reco).at(8)),static_cast<int>(reco_extra.at(used_reco).at(9))
          );
    isrs.erase(isrs.begin()+used_gen);
    reco.erase(reco.begin()+used_reco);
    reco_extra.erase(reco_extra.begin()+used_reco);
    isr_id.erase(isr_id.begin()+used_gen);
    gen_match_remove(reco,sueps,isrs,OutFile,reco_extra,suep_id,isr_id);
  }
}
else{
//      printf("No More Matches\n");
    for(int used_recox=0; used_recox<reco.size();used_recox++){
    fprintf(OutFile,"%d %d %d"
           " %d %d %d %d"
           " %f %f %f"
           " %d %d %d"
           " %d %d %d"
           " %d %f %d"
           " %d %d %d"
           " %d %d"
           "\n",
          0,0,0,
          100,0,0,3,
          reco[used_recox].pt(),reco[used_recox].eta(),reco[used_recox].phi(),
          0,0,0,
          static_cast<int>(reco_extra.at(used_recox).at(0)),static_cast<int>(reco_extra.at(used_recox).at(1)), static_cast<int>(reco_extra.at(used_recox).at(2)),
          static_cast<int>(reco_extra.at(used_recox).at(3)),reco_extra.at(used_recox).at(4), static_cast<int>(reco_extra.at(used_recox).at(5)),
          static_cast<int>(reco_extra.at(used_recox).at(6)),static_cast<int>(reco_extra.at(used_recox).at(7)), -1,
          static_cast<int>(reco_extra.at(used_recox).at(8)),static_cast<int>(reco_extra.at(used_recox).at(9))
          );
    }
  }
}


void gen_match(vector<PseudoJet> reco, vector<ROOT::Math::PtEtaPhiEVector> sueps, vector<ROOT::Math::PtEtaPhiEVector> isrs,FILE* OutFile){
//  if(reco.size() ==0) {return;}
//  if( sueps.size() + isrs.size() ==0) {return;}
  float min_dR = 9999;
  int used_gen = -1;
  int used_reco = -1;
  int is_isr =-1;
  for(int reco_i=0; reco_i < reco.size(); reco_i++){
    for(int gen_i=0; gen_i < sueps.size(); gen_i++){
       float dEta = reco[reco_i].eta() - sueps[gen_i].eta();
       float dPhi = abs(reco[reco_i].phi() - sueps[gen_i].phi());
       float dPt = abs(reco[reco_i].pt() - sueps[gen_i].pt())/(sueps[gen_i].pt());
       if(dPhi > M_PI){dPhi = dPhi - 2*M_PI;}
       float dR = sqrt(dEta*dEta + dPhi*dPhi);
          is_isr= (gen_i>=sueps.size());
          min_dR = dR;
          used_gen = gen_i;
          used_reco = reco_i;
          fprintf(OutFile,"%d %d %d %f %d %d %f %f %f %f %f %f %d\n",reco.size(),sueps.size(),isrs.size(),min_dR,used_gen,used_reco,reco[used_reco].pt(),reco[used_reco].eta(),reco[used_reco].phi(),sueps[used_gen].pt(),sueps[used_gen].eta(),sueps[used_gen].phi(),is_isr);
    }
    for(int gen_i=0; gen_i < isrs.size(); gen_i++){
       float dEta = reco[reco_i].eta() - isrs[gen_i].eta();
       float dPhi = abs(reco[reco_i].phi() - isrs[gen_i].phi());
       float dPt = abs(reco[reco_i].pt() - isrs[gen_i].pt())/(isrs[gen_i].pt());
       if(dPhi > M_PI){dPhi = dPhi - 2*M_PI;}
       float dR = sqrt(dEta*dEta + dPhi*dPhi);
          is_isr= (gen_i>=sueps.size());
          min_dR = dR;
          used_gen = gen_i;
          used_reco = reco_i;
          fprintf(OutFile,"%d %d %d %f %d %d %f %f %f %f %f %f %d\n",reco.size(),sueps.size(),isrs.size(),min_dR,used_gen,used_reco,reco[used_reco].pt(),reco[used_reco].eta(),reco[used_reco].phi(),sueps[used_gen].pt(),sueps[used_gen].eta(),sueps[used_gen].phi(),is_isr);
    }
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
  FILE* OutFile = fopen(("data/track_"+sample+"_v"+to_string(batch)+".txt").c_str(),"w");
  FILE* OutFileGen = fopen(("data/gentrack_"+sample+"_v"+to_string(batch)+".txt").c_str(),"w");
  //FILE* OutFile = fopen(("data/"+sample+"_v"+to_string(batch)+".txt").c_str(),"w");
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
  vector<int>* trk_foundHits =0;
  vector<int>* trk_lostHits =0;
  vector<double>* trk_chi2 =0;
  vector<int>* trk_nHits =0;
  vector<int>* trk_nPixelHits=0;
  vector<int>* trk_quality=0;
  //vector<int>* trk_PVQuality=0;
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
  t1->SetBranchAddress("Tracks_foundHits",&trk_foundHits);
  t1->SetBranchAddress("Tracks_lostHits",&trk_lostHits);
  t1->SetBranchAddress("Tracks_normalizedChi2",&trk_chi2);
  t1->SetBranchAddress("Tracks_numberOfHits",&trk_nHits);
  t1->SetBranchAddress("Tracks_numberOfPixelHits",&trk_nPixelHits);
  t1->SetBranchAddress("Tracks_quality",&trk_quality);
  //t1->SetBranchAddress("Tracks_PVAssociationQuality",&trk_PVQuality);
//#pragma omp parallel for 

  int nentries=0;// = 10000;
  if(batch==0) {
    nentries=10000;
    //fprintf(OutFile,"event algo R jetid pt eta phi multiplicity girth mass trkpt medpt suep isr suep_tot isr_tot nvtx numInteractions scalar_dR scalar_pt scalar_eta scalar_phi suep_Ptwgt scalar_mass beta scalar_beta pt_dispersion lesHouches thrust t1 t2 t3 e2 e3\n");
  }
  else{nentries=t1->GetEntries();}
  //printf("b %d e %d\n",batch,nentries);
  for(int entry=10000*batch; entry<nentries; entry++){
  //for(int entry=67; entry<70; entry++){
    if(entry%1000==0) {printf("entry %d/%d\n",entry,nentries);}
    //if(find(skip.begin(),skip.end(),entry) != skip.end()){printf("skipping entry: %d\n",entry); continue;}
    t1->GetEntry(entry);
    if(ht <1200){ continue;}
    vector<ROOT::Math::PtEtaPhiEVector> sueps;
    vector<ROOT::Math::PtEtaPhiEVector> isrs;
    ROOT::Math::PtEtaPhiEVector scalar;
    scalar.SetXYZT(0,0,0,0);
    vector<int> suep_id;
    vector<int> isr_id;
    // sort gen particles into isr and sueps
    for(int igen=0;igen<genPart->size();igen++){
      //if(abs(gen_charge->at(igen)) != 1 || gen_status->at(igen) != 1 || abs(genPart->at(igen).eta()) >= 2.5 || genPart->at(igen).pt() <= 1){continue;}
      if(abs(gen_charge->at(igen)) != 1 || gen_status->at(igen) != 1 || abs(genPart->at(igen).eta()) >= 2.4){continue;}
      int pdgid = abs(gen_pdgId->at(igen));
      if((pdgid != 11) && (pdgid != 13) && (pdgid != 22) && (pdgid < 100 )){continue;}
      if(gen_parentId->at(igen) == 999998){ sueps.push_back(genPart->at(igen));scalar+=genPart->at(igen);suep_id.push_back(pdgid);} 
      else{ isrs.push_back(genPart->at(igen));isr_id.push_back(pdgid);} 

    }
    vector<PseudoJet> particles;
    vector<PseudoJet> particles_id;
    vector<vector<float>> part_extra;
    for(int itrk=0;itrk<trkPart->size();itrk++){
      //if ((trk_pv->at(itrk) <2) || (trk_matched->at(itrk) ==0)){continue;}

    double trkx = trkPart->at(itrk).x();
    double trky = trkPart->at(itrk).y();
    double trkz = trkPart->at(itrk).z();
    TLorentzVector trk;
    trk.SetXYZM(trkx,trky,trkz,0.13957);
    //if(trk.Pt() <= 1 || abs(trk.Eta()) >= 2.5){continue;}
    if( abs(trk.Eta()) >= 2.5){continue;} // extra leeway for gen matching
    particles.push_back(PseudoJet(trk.Px(),trk.Py(),trk.Pz(),trk.E()));
    vector<float> extra = {
      static_cast<float>(trk_pv->at(itrk)),
      static_cast<float>(trk_matched->at(itrk)),
      static_cast<float>(trk_foundHits->at(itrk)),
      static_cast<float>(trk_lostHits->at(itrk)),
      static_cast<float>(trk_chi2->at(itrk)),
      static_cast<float>(trk_nHits->at(itrk)),
      static_cast<float>(trk_nPixelHits->at(itrk)),
      static_cast<float>(trk_quality->at(itrk)),
      static_cast<float>(trkPart->size()),
      static_cast<float>(entry)
      };
    part_extra.push_back(extra);

    }
    getAllGen(sueps, isrs, suep_id,isr_id,OutFileGen,entry);
    gen_match_remove(particles,sueps,isrs,OutFile,part_extra,suep_id,isr_id);

  }
fclose(OutFile);
}
  
