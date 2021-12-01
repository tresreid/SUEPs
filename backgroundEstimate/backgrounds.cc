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
#include "TVectorD.h"
#include "TMatrixD.h"
#include "TMatrixDSym.h"

#include "/uscms/home/mreid/nobackup/sueps/CMSSW_10_6_13/src/SUEP_Analysis/SUEP_Analysis/PlotHelper.h"
using namespace fastjet;
using namespace std;

#include <vector>

tuple<double,double,double,
double,double,double,
double,double,double,
double,double,double,
double,double,double,
double,double,double,
double,double,double
> nsubjettiness(PseudoJet jet, float R)
{
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
  
  float rho0_05=0;
  float rho1_05=0;
  float rho2_05=0;
  float rho0_10=0;
  float rho1_10=0;
  float rho2_10=0;
  float rho0_20=0;
  float rho1_20=0;
  float rho2_20=0;
  float rho0_50=0;
  float rho1_50=0;
  float rho2_50=0;
  float rho0_15=0;
  float rho1_15=0;
  float rho2_15=0;
  float rho0_30=0;
  float rho1_30=0;
  float rho2_30=0;
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
    //Hungarian rpo
    if (dR_1 <= 0.5){
      rho0_50 += pt;
    }
    else if ((dR_1 > 0.5) && (dR_1 < 1.0)){
      rho1_50 += pt;
    }
    else if ((dR_1 > 1.0) && (dR_1 < 1.5)){
      rho2_50 += pt;
    }
    if (dR_1 <= 0.2){
      rho0_20 += pt;
    }
    else if ((dR_1 > 0.2) && (dR_1 <= 0.4)){
      rho1_20 += pt;
    }
    else if ((dR_1 > 0.4) && (dR_1 <= 0.6)){
      rho2_20 += pt;
    }
    if (dR_1 <= 0.1){
      rho0_10 += pt;
    }
    else if ((dR_1 > 0.1) && (dR_1 <= 0.2)){
      rho1_10 += pt;
    }
    else if ((dR_1 > 0.2) && (dR_1 <= 0.3)){
      rho2_10 += pt;
    }
    if (dR_1 <= 0.05){
      rho0_05 += pt;
    }
    else if ((dR_1 > 0.05) && (dR_1 <= 0.1)){
      rho1_05 += pt;
    }
    else if ((dR_1 > 0.1) && (dR_1 <= 0.15)){
      rho2_05 += pt;
    }
    if (dR_1 <= 0.3){
      rho0_30 += pt;
    }
    else if ((dR_1 > 0.3) && (dR_1 <= 0.6)){
      rho1_30 += pt;
    }
    else if ((dR_1 > 0.6) && (dR_1 <= 0.9)){
      rho2_30 += pt;
    }
    if (dR_1 <= 0.15){
      rho0_15 += pt;
    }
    else if ((dR_1 > 0.15) && (dR_1 <= 0.3)){
      rho1_15 += pt;
    }
    else if ((dR_1 > 0.3) && (dR_1 <= 0.45)){
      rho2_15 += pt;
    }

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
    //for(int j=0; j<i;j++){
    //  float phi_j = constituents[j].phi();
    //  float eta_j = constituents[j].eta();
    //  float pt_j = constituents[j].pt();
    //  float dEta_j = eta_j - eta;
    //  float dPhi_j = phi_j-phi > M_PI? (phi_j -phi) - 2*M_PI:phi_j -phi;
    //  float dR_ij = sqrt(dEta_j*dEta_j + dPhi_j*dPhi_j);
    //  e2 += pt*pt_j*dR_ij;
    //  for(int k=0; k<j;k++){
    //    float phi_k = constituents[k].phi();
    //    float eta_k = constituents[k].eta();
    //    float pt_k = constituents[k].pt();
    //    float dEta_ki = eta_k - eta;
    //    float dPhi_ki = phi_k-phi > M_PI? (phi_k -phi) - 2*M_PI:phi_k -phi;
    //    float dR_ki = sqrt(dEta_ki*dEta_ki + dPhi_ki*dPhi_ki);

    //    float dEta_kj = eta_j - eta_k;
    //    float dPhi_kj = phi_j-phi_k > M_PI? (phi_j -phi_k) - 2*M_PI:phi_j -phi_k;
    //    float dR_kj = sqrt(dEta_kj*dEta_kj + dPhi_kj*dPhi_kj);
    //    e3 += pt*pt_j*pt_k*dR_ij*dR_ki*dR_kj;

    //  }
    //}

  }

  //return{ t1/jet.pt(),t2/jet.pt(), t3/jet.pt(),e2/(jet.pt()*jet.pt()),e3/(jet.pt()*jet.pt()*jet.pt()),rho_1/(jet.pt()*0.5),rho_2/(jet.pt()*0.5),rho_3/(jet.pt()*0.5)   };
  return{ t1/jet.pt(),t2/jet.pt(), t3/jet.pt(),
          rho0_50/(jet.pt()*0.5),rho1_50/(jet.pt()*0.5),rho2_50/(jet.pt()*0.5),
          rho0_20/(jet.pt()*0.2),rho1_20/(jet.pt()*0.2),rho2_20/(jet.pt()*0.2),
          rho0_10/(jet.pt()*0.1),rho1_10/(jet.pt()*0.1),rho2_10/(jet.pt()*0.1),
          rho0_05/(jet.pt()*0.05),rho1_05/(jet.pt()*0.05),rho2_05/(jet.pt()*0.05),
          rho0_15/(jet.pt()*0.15),rho1_15/(jet.pt()*0.15),rho2_15/(jet.pt()*0.15),
          rho0_30/(jet.pt()*0.3),rho1_30/(jet.pt()*0.3),rho2_30/(jet.pt()*0.3)
          };
}



std::vector<double> compTensorsAndVectors(std::vector<TLorentzVector> tracks) {
  double r_=2.0;
  std::vector<double> eigenValues_ = std::vector<double>(3, 0);
  std::vector<double> eigenValuesNoNorm_ = std::vector<double>(3, 0);

  TMatrixD eigenVectors_;
  TVectorD eigenValuesTmp_, eigenValuesNoNormTmp_;

  TMatrixDSym momentumTensor(3);
  momentumTensor.Zero();

  if (tracks.size() == 0) return eigenValues_;
  double norm = 0.;
  TVector3 vec; 
  //TLorentzVector vec; 
  for (const auto& track : tracks) {

    vec = track.Vect();//.p4.Vect();
    double p2 = (vec).Dot(vec);
    double pR = (r_ == 2.) ? p2 : TMath::Power(p2, 0.5 * r_);
    norm += pR;
    double pRminus2 = (r_ == 2.) ? 1. : TMath::Power(p2, 0.5 * r_ - 1.);
    momentumTensor(0, 0) += pRminus2 * vec.X() * vec.X();
    momentumTensor(0, 1) += pRminus2 * vec.X() * vec.Y();
    momentumTensor(0, 2) += pRminus2 * vec.X() * vec.Z();
    momentumTensor(1, 0) += pRminus2 * vec.Y() * vec.X();
    momentumTensor(1, 1) += pRminus2 * vec.Y() * vec.Y();
    momentumTensor(1, 2) += pRminus2 * vec.Y() * vec.Z();
    momentumTensor(2, 0) += pRminus2 * vec.Z() * vec.X();
    momentumTensor(2, 1) += pRminus2 * vec.Z() * vec.Y();
    momentumTensor(2, 2) += pRminus2 * vec.Z() * vec.Z();
  }

  if (momentumTensor.IsSymmetric() && (momentumTensor.NonZeros() != 0)) {
    momentumTensor.EigenVectors(eigenValuesNoNormTmp_);
  }
  eigenValuesNoNorm_[0] = eigenValuesNoNormTmp_(0);
  eigenValuesNoNorm_[1] = eigenValuesNoNormTmp_(1);
  eigenValuesNoNorm_[2] = eigenValuesNoNormTmp_(2);
  momentumTensor *= (1. / norm);
    //std::cout << "norm " << norm << std::endl;
    //std::cout << " mt(0, 0)" <<  momentumTensor(0, 0) << std::endl;
    //std::cout << " mt(0, 1)" <<  momentumTensor(0, 1) << std::endl;
    //std::cout << " mt(0, 2)" <<  momentumTensor(0, 2) << std::endl;
    //std::cout << " mt(1, 0)" <<  momentumTensor(1, 0) << std::endl;
    //std::cout << " mt(1, 1)" <<  momentumTensor(1, 1) << std::endl;
    //std::cout << " mt(1, 2)" <<  momentumTensor(1, 2) << std::endl;
    //std::cout << " mt(2, 0)" <<  momentumTensor(2, 0) << std::endl;
    //std::cout << " mt(2, 1)" <<  momentumTensor(2, 1) << std::endl;
    //std::cout << " mt(2, 2)" <<  momentumTensor(2, 2) << std::endl;
  if (momentumTensor.IsSymmetric() && (momentumTensor.NonZeros() != 0)) {
    momentumTensor.EigenVectors(eigenValuesTmp_);
  }
  eigenValues_[0] = eigenValuesTmp_(0);
  eigenValues_[1] = eigenValuesTmp_(1);
  eigenValues_[2] = eigenValuesTmp_(2);
//  std::cout << eigenValues_[0] << " " << eigenValues_[1] << " " << eigenValues_[2] << std::endl;
    return eigenValues_;
}










//void getAllGen(vector<ROOT::Math::PtEtaPhiEVector> sueps, vector<ROOT::Math::PtEtaPhiEVector> isrs, vector<int> suep_id,vector<int> isr_id,FILE* OutFileGen,int entry){
//  for(int gen_i=0; gen_i < sueps.size(); gen_i++){
//          fprintf(OutFileGen,"%f %f %f %d 0 %d %d %d\n",
//          sueps[gen_i].pt(),sueps[gen_i].eta(),sueps[gen_i].phi(),suep_id[gen_i], sueps.size(), isrs.size(), entry);
//  }
//  for(int gen_i=0; gen_i < isrs.size(); gen_i++){
//          fprintf(OutFileGen,"%f %f %f %d 1 %d %d %d\n",
//          isrs[gen_i].pt(),isrs[gen_i].eta(),isrs[gen_i].phi(),isr_id[gen_i], sueps.size(), isrs.size(), entry);
//  }
//}
//void gen_match_remove(vector<PseudoJet> reco, vector<ROOT::Math::PtEtaPhiEVector> sueps, vector<ROOT::Math::PtEtaPhiEVector> isrs,FILE* OutFile,vector<vector<float>> reco_extra, vector<int> suep_id,vector<int> isr_id){
//  if(reco.size() ==0) {return;}
//  if( sueps.size() + isrs.size() ==0) {return;}
//  float min_dR = 9999;
//  int used_gen = -1;
//  int used_reco = -1;
//  int is_isr =-1;
//  for(int gen_i=0; gen_i < sueps.size()+isrs.size(); gen_i++){
//    for(int reco_i=0; reco_i < reco.size(); reco_i++){
//       float dEta;
//       float dPhi;
//       float dPt;
//       if(gen_i < sueps.size()){
//        dEta = reco[reco_i].eta() - sueps[gen_i].eta();
//        dPhi = abs(reco[reco_i].phi() - sueps[gen_i].phi());
//        dPt = abs(reco[reco_i].pt() - sueps[gen_i].pt())/(sueps[gen_i].pt());
//       }
//       else{
//        dEta = reco[reco_i].eta() - isrs[gen_i-sueps.size()].eta();
//        dPhi = abs(reco[reco_i].phi() - isrs[gen_i-sueps.size()].phi());
//        dPt = abs(reco[reco_i].pt() - isrs[gen_i-sueps.size()].pt())/(isrs[gen_i-sueps.size()].pt());
//       }
//       if(dPhi > M_PI){dPhi = dPhi - 2*M_PI;}
//       float dR = sqrt(dEta*dEta + dPhi*dPhi);
//       if( dR < min_dR && dPt < 0.3){
//          is_isr= (gen_i>=sueps.size());
//          min_dR = dR;
//          used_gen = gen_i-(is_isr*sueps.size());
//          used_reco = reco_i;
//       }
//    }
//  }
//  if(min_dR < 0.3){
//  if (is_isr == 0){ 
//    //fprintf(OutFile,"%d %d %d %f %d %d %f %f %f %f %f %f %d %f %f\n",reco.size(),sueps.size(),isrs.size(),min_dR,used_gen,used_reco,reco[used_reco].pt(),reco[used_reco].eta(),reco[used_reco].phi(),sueps[used_gen].pt(),sueps[used_gen].eta(),sueps[used_gen].phi(),is_isr,reco_extra.at(used_gen).at(0),reco_extra.at(used_gen).at(1));
//    fprintf(OutFile,"%d %d %d"
//           " %f %d %d %d"
//           " %f %f %f"
//           " %f %f %f"
//           " %d %d %d"
//           " %d %f %d"
//           " %d %d %d"
//           " %d %d %f %f"
//           " %d %f %f"
//           "\n",
//          reco.size(),sueps.size(),isrs.size(),
//          min_dR,used_gen,used_reco,is_isr,
//          reco[used_reco].pt(),reco[used_reco].eta(),reco[used_reco].phi(),
//          sueps[used_gen].pt(),sueps[used_gen].eta(),sueps[used_gen].phi(),
//          static_cast<int>(reco_extra.at(used_reco).at(0)),static_cast<int>(reco_extra.at(used_reco).at(1)), static_cast<int>(reco_extra.at(used_reco).at(2)),
//          static_cast<int>(reco_extra.at(used_reco).at(3)),reco_extra.at(used_reco).at(4), static_cast<int>(reco_extra.at(used_reco).at(5)),
//          static_cast<int>(reco_extra.at(used_reco).at(6)),static_cast<int>(reco_extra.at(used_reco).at(7)),suep_id[used_gen],
//          static_cast<int>(reco_extra.at(used_reco).at(8)),static_cast<int>(reco_extra.at(used_reco).at(9)),static_cast<float>(reco_extra.at(used_reco).at(10)),static_cast<float>(reco_extra.at(used_reco).at(11)),
//          static_cast<int>(reco_extra.at(used_reco).at(12)),static_cast<float>(reco_extra.at(used_reco).at(13)), static_cast<float>(reco_extra.at(used_reco).at(14))
//          );
//    sueps.erase(sueps.begin()+used_gen);
//    reco.erase(reco.begin()+used_reco);
//    reco_extra.erase(reco_extra.begin()+used_reco);
//    suep_id.erase(suep_id.begin()+used_gen);
//    gen_match_remove(reco,sueps,isrs,OutFile,reco_extra,suep_id,isr_id);
//  }
//  else if (is_isr==1){ 
//    //fprintf(OutFile,"%d %d %d %f %d %d %f %f %f %f %f %f %d %f %f\n",reco.size(),sueps.size(),isrs.size(),min_dR,used_gen,used_reco,reco[used_reco].pt(),reco[used_reco].eta(),reco[used_reco].phi(),isrs[used_gen].pt(),isrs[used_gen].eta(),isrs[used_gen].phi(),is_isr,reco_extra.at(used_gen).at(0),reco_extra.at(used_gen).at(1));
//    fprintf(OutFile,"%d %d %d"
//           " %f %d %d %d"
//           " %f %f %f"
//           " %f %f %f"
//           " %d %d %d"
//           " %d %f %d"
//           " %d %d %d"
//           " %d %d %f %f"
//           " %d %f %f"
//           "\n",
//          reco.size(),sueps.size(),isrs.size(),
//          min_dR,used_gen,used_reco,is_isr,
//          reco[used_reco].pt(),reco[used_reco].eta(),reco[used_reco].phi(),
//          isrs[used_gen].pt(),isrs[used_gen].eta(),isrs[used_gen].phi(),
//          static_cast<int>(reco_extra.at(used_reco).at(0)),static_cast<int>(reco_extra.at(used_reco).at(1)), static_cast<int>(reco_extra.at(used_reco).at(2)),
//          static_cast<int>(reco_extra.at(used_reco).at(3)),reco_extra.at(used_reco).at(4), static_cast<int>(reco_extra.at(used_reco).at(5)),
//          static_cast<int>(reco_extra.at(used_reco).at(6)),static_cast<int>(reco_extra.at(used_reco).at(7)),isr_id[used_gen],
//          static_cast<int>(reco_extra.at(used_reco).at(8)),static_cast<int>(reco_extra.at(used_reco).at(9)),static_cast<float>(reco_extra.at(used_reco).at(10)),static_cast<float>(reco_extra.at(used_reco).at(11)),
//          static_cast<int>(reco_extra.at(used_reco).at(12)),static_cast<float>(reco_extra.at(used_reco).at(13)), static_cast<float>(reco_extra.at(used_reco).at(14))
//          );
//    isrs.erase(isrs.begin()+used_gen);
//    reco.erase(reco.begin()+used_reco);
//    reco_extra.erase(reco_extra.begin()+used_reco);
//    isr_id.erase(isr_id.begin()+used_gen);
//    gen_match_remove(reco,sueps,isrs,OutFile,reco_extra,suep_id,isr_id);
//  }
//}
//else{
////      printf("No More Matches\n");
//    for(int used_recox=0; used_recox<reco.size();used_recox++){
//    fprintf(OutFile,"%d %d %d"
//           " %d %d %d %d"
//           " %f %f %f"
//           " %d %d %d"
//           " %d %d %d"
//           " %d %f %d"
//           " %d %d %d"
//           " %d %d %f %f"
//           " %d %f %f"
//           "\n",
//          0,0,0,
//          100,0,0,3,
//          reco[used_recox].pt(),reco[used_recox].eta(),reco[used_recox].phi(),
//          0,0,0,
//          static_cast<int>(reco_extra.at(used_recox).at(0)),static_cast<int>(reco_extra.at(used_recox).at(1)), static_cast<int>(reco_extra.at(used_recox).at(2)),
//          static_cast<int>(reco_extra.at(used_recox).at(3)),reco_extra.at(used_recox).at(4), static_cast<int>(reco_extra.at(used_recox).at(5)),
//          static_cast<int>(reco_extra.at(used_recox).at(6)),static_cast<int>(reco_extra.at(used_recox).at(7)), -1,
//          static_cast<int>(reco_extra.at(used_recox).at(8)),static_cast<int>(reco_extra.at(used_recox).at(9)),static_cast<float>(reco_extra.at(used_recox).at(10)),static_cast<float>(reco_extra.at(used_recox).at(11)),
//          static_cast<int>(reco_extra.at(used_recox).at(12)),static_cast<float>(reco_extra.at(used_recox).at(13)), static_cast<float>(reco_extra.at(used_recox).at(14))
//          );
//    }
//  }
//}
//
//
//void gen_match(vector<PseudoJet> reco, vector<ROOT::Math::PtEtaPhiEVector> sueps, vector<ROOT::Math::PtEtaPhiEVector> isrs,FILE* OutFile){
////  if(reco.size() ==0) {return;}
////  if( sueps.size() + isrs.size() ==0) {return;}
//  float min_dR = 9999;
//  int used_gen = -1;
//  int used_reco = -1;
//  int is_isr =-1;
//  for(int reco_i=0; reco_i < reco.size(); reco_i++){
//    for(int gen_i=0; gen_i < sueps.size(); gen_i++){
//       float dEta = reco[reco_i].eta() - sueps[gen_i].eta();
//       float dPhi = abs(reco[reco_i].phi() - sueps[gen_i].phi());
//       float dPt = abs(reco[reco_i].pt() - sueps[gen_i].pt())/(sueps[gen_i].pt());
//       if(dPhi > M_PI){dPhi = dPhi - 2*M_PI;}
//       float dR = sqrt(dEta*dEta + dPhi*dPhi);
//          is_isr= (gen_i>=sueps.size());
//          min_dR = dR;
//          used_gen = gen_i;
//          used_reco = reco_i;
//          fprintf(OutFile,"%d %d %d %f %d %d %f %f %f %f %f %f %d\n",reco.size(),sueps.size(),isrs.size(),min_dR,used_gen,used_reco,reco[used_reco].pt(),reco[used_reco].eta(),reco[used_reco].phi(),sueps[used_gen].pt(),sueps[used_gen].eta(),sueps[used_gen].phi(),is_isr);
//    }
//    for(int gen_i=0; gen_i < isrs.size(); gen_i++){
//       float dEta = reco[reco_i].eta() - isrs[gen_i].eta();
//       float dPhi = abs(reco[reco_i].phi() - isrs[gen_i].phi());
//       float dPt = abs(reco[reco_i].pt() - isrs[gen_i].pt())/(isrs[gen_i].pt());
//       if(dPhi > M_PI){dPhi = dPhi - 2*M_PI;}
//       float dR = sqrt(dEta*dEta + dPhi*dPhi);
//          is_isr= (gen_i>=sueps.size());
//          min_dR = dR;
//          used_gen = gen_i;
//          used_reco = reco_i;
//          fprintf(OutFile,"%d %d %d %f %d %d %f %f %f %f %f %f %d\n",reco.size(),sueps.size(),isrs.size(),min_dR,used_gen,used_reco,reco[used_reco].pt(),reco[used_reco].eta(),reco[used_reco].phi(),sueps[used_gen].pt(),sueps[used_gen].eta(),sueps[used_gen].phi(),is_isr);
//    }
//  }
//}

int main(int argc,char** argv){
  printf("Starting\n");
  ROOT::EnableThreadSafety();  
  ROOT::EnableImplicitMT();
  //TFile *infile = TFile::Open("root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v0.2/2018/NTUP/PrivateSamples.SUEP_2018_mMed-1000_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_0_RA2AnalysisTree.root");
  //string file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v0.2/2018/NTUP/";
  string file = "root://cmseos.fnal.gov//store/user/mreid/SUEPs/Production/";
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
//  case 3: file += "Autumn18.QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root";   sample="qcd_300";break;
//  case 4: file += "Autumn18.QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root";   sample="qcd_500";break;
//  case 5: file += "Autumn18.QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root";  sample="qcd_700";break;
//  case 6: file += "Autumn18.QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root"; sample="qcd_1000"; break;
//  case 7: file += "Autumn18.QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root"; sample="qcd_1500";break;
//  case 8: file += "Autumn18.QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root";  sample="qcd_2000"; break;
  case 9: file += "PrivateSamples.SUEP_2018_mMed-125_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_125";break;
  case 10: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.0/2018/NTUP/PrivateSamples.SUEP_2018_mMed-200_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_200";break;
  case 11: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.0/2018/NTUP/PrivateSamples.SUEP_2018_mMed-300_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_300";break;
//  case 0: file += "PrivateSamples.SUEP_2018_mMed-1000_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root";sample="sig_1000"; break;
//  case 1: file += "PrivateSamples.SUEP_2018_mMed-750_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_750";break;
//  case 2: file += "PrivateSamples.SUEP_2018_mMed-400_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_400";break;
//  case 3: file += "Autumn18.QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root";   sample="qcd_300";break;
//  case 4: file += "Autumn18.QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root";   sample="qcd_500";break;
//  case 5: file += "Autumn18.QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root";  sample="qcd_700";break;
//  case 6: file += "Autumn18.QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root"; sample="qcd_1000"; break;
//  case 7: file += "Autumn18.QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root"; sample="qcd_1500";break;
//  case 8: file += "Autumn18.QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RA2AnalysisTree.root";  sample="qcd_2000"; break;
//  case 9: file += "PrivateSamples.SUEP_2018_mMed-125_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_125";break;
//  case 10: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.0/2018/NTUP/PrivateSamples.SUEP_2018_mMed-200_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_200";break;
//  case 11: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.0/2018/NTUP/PrivateSamples.SUEP_2018_mMed-300_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_300";break;

//  case 20: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.1/2018/NTUP/PrivateSamples.SUEP_2018_mMed-400_mDark-1_temp-1_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="mDark1_temp1";break;
//  case 21: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.1/2018/NTUP/PrivateSamples.SUEP_2018_mMed-400_mDark-1_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="mDark1_temp2";break;
//  case 22: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.1/2018/NTUP/PrivateSamples.SUEP_2018_mMed-400_mDark-1_temp-5_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="mDark1_temp5";break;
//  case 23: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.1/2018/NTUP/PrivateSamples.SUEP_2018_mMed-400_mDark-2_temp-1_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="mDark2_temp1";break;
//  case 24: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.1/2018/NTUP/PrivateSamples.SUEP_2018_mMed-400_mDark-2_temp-5_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="mDark2_temp5";break;
//  case 25: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.1/2018/NTUP/PrivateSamples.SUEP_2018_mMed-400_mDark-5_temp-1_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="mDark5_temp1";break;
//  case 26: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.1/2018/NTUP/PrivateSamples.SUEP_2018_mMed-400_mDark-5_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="mDark5_temp2";break;
//  case 27: file = "root://cmseos.fnal.gov//store/user/kdipetri/SUEP/Production_v1.1/2018/NTUP/PrivateSamples.SUEP_2018_mMed-400_mDark-5_temp-5_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="mDark5_temp5";break; 

  default: file += "PrivateSamples.SUEP_2018_mMed-1000_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100_0_RA2AnalysisTree.root"; sample="sig_1000";break;
  }
  int batch = 0;
  if(argc>=3){batch = atoi(argv[2]);}
  //printf("opening file: %s\n",file.c_str());
  printf("sample: %s; batch:%d\n",sample.c_str(),batch);
  FILE* OutFile = fopen(("data/variables_"+sample+"_v"+to_string(batch)+".txt").c_str(),"w");
  //FILE* OutFileGen = fopen(("data/gentrack_"+sample+"_v"+to_string(batch)+".txt").c_str(),"w");
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
  vector<double>* trk_ptErr=0;
  vector<double>* trk_qoverpErr=0;
  vector<int>* trk_PVQuality=0;
  vector<double>* trk_dzPV0=0;
  vector<double>* trk_dzErrorPV0=0;
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
  t1->SetBranchAddress("Tracks_ptError",&trk_ptErr);
  t1->SetBranchAddress("Tracks_qoverpError",&trk_qoverpErr);
  t1->SetBranchAddress("Tracks_pvAssociationQuality",&trk_PVQuality);
  t1->SetBranchAddress("Tracks_dzPV0",&trk_dzPV0);
  t1->SetBranchAddress("Tracks_dzErrorPV0",&trk_dzErrorPV0);
//#pragma omp parallel for 

  int nentries=0;// = 10000;
  if(batch==0) {
    nentries=10000;
    //fprintf(OutFile,"event algo R jetid pt eta phi multiplicity girth mass trkpt medpt suep isr suep_tot isr_tot nvtx numInteractions scalar_dR scalar_pt scalar_eta scalar_phi suep_Ptwgt scalar_mass beta scalar_beta pt_dispersion lesHouches thrust t1 t2 t3 e2 e3\n");
  }
  else{nentries=t1->GetEntries();}
  //printf("b %d e %d\n",batch,nentries);
  int trig_pass =0;
  int jet_pass=0;
  for(int entry=10000*batch; entry<nentries; entry++){
  //for(int entry=0; entry<500; entry++){
    if(entry%1000==0) {printf("entry %d/%d\n",entry,nentries);}
    //if(find(skip.begin(),skip.end(),entry) != skip.end()){printf("skipping entry: %d\n",entry); continue;}
    t1->GetEntry(entry);
    if(ht <1200){ continue;}
    trig_pass++;
    vector<ROOT::Math::PtEtaPhiEVector> sueps;
    vector<ROOT::Math::PtEtaPhiEVector> isrs;
    ROOT::Math::PtEtaPhiEVector scalar;
    scalar.SetXYZT(0,0,0,0);
    vector<int> suep_id;
    vector<int> isr_id;
    // sort gen particles into isr and sueps
    //for(int igen=0;igen<genPart->size();igen++){
    //  //if(abs(gen_charge->at(igen)) != 1 || gen_status->at(igen) != 1 || abs(genPart->at(igen).eta()) >= 2.5 || genPart->at(igen).pt() <= 1){continue;}
    //  if(abs(gen_charge->at(igen)) != 1 || gen_status->at(igen) != 1 || abs(genPart->at(igen).eta()) >= 2.4){continue;}
    //  int pdgid = abs(gen_pdgId->at(igen));
    //  if((pdgid != 11) && (pdgid != 13) && (pdgid != 22) && (pdgid < 100 )){continue;}
    //  if(gen_parentId->at(igen) == 999998){ sueps.push_back(genPart->at(igen));scalar+=genPart->at(igen);suep_id.push_back(pdgid);} 
    //  else{ isrs.push_back(genPart->at(igen));isr_id.push_back(pdgid);} 

    //}
    vector<PseudoJet> particles;
    vector<PseudoJet> particles_id;
    vector<vector<float>> part_extra;
    vector<TLorentzVector> tracks_event;
    for(int itrk=0;itrk<trkPart->size();itrk++){
      //if ((trk_pv->at(itrk) <2) || (trk_matched->at(itrk) ==0)){continue;}

    double trkx = trkPart->at(itrk).x();
    double trky = trkPart->at(itrk).y();
    double trkz = trkPart->at(itrk).z();
    TLorentzVector trk;
    trk.SetXYZM(trkx,trky,trkz,0.13957);
    //if(trk.Pt() <= 1 || abs(trk.Eta()) >= 2.5){continue;}
    if( abs(trk.Eta()) >= 2.5){continue;} // extra leeway for gen matching
    if((trk_pv->at(itrk) < 2) || (trk_dzPV0->at(itrk) > 10) || (trk_dzErrorPV0->at(itrk) > 0.05 || trk.Pt() < 0.7)){continue;}
    if((trk_matched->at(itrk) ==0) && (abs(trk.Eta()) > 1.0)){continue;}
    particles.push_back(PseudoJet(trk.Px(),trk.Py(),trk.Pz(),trk.E()));
    tracks_event.push_back(trk);
    //vector<float> extra = {
    //  static_cast<float>(trk_pv->at(itrk)),
    //  static_cast<float>(trk_matched->at(itrk)),
    //  static_cast<float>(trk_foundHits->at(itrk)),
    //  static_cast<float>(trk_lostHits->at(itrk)),
    //  static_cast<float>(trk_chi2->at(itrk)),
    //  static_cast<float>(trk_nHits->at(itrk)),
    //  static_cast<float>(trk_nPixelHits->at(itrk)),
    //  static_cast<float>(trk_quality->at(itrk)),
    //  static_cast<float>(trkPart->size()),
    //  static_cast<float>(entry),
    //  static_cast<float>(trk_ptErr->at(itrk)),
    //  static_cast<float>(trk_qoverpErr->at(itrk)),
    //  static_cast<float>(trk_PVQuality->at(itrk)),
    //  static_cast<float>(trk_dzPV0->at(itrk)),
    //  static_cast<float>(trk_dzErrorPV0->at(itrk))
    //  };
    //part_extra.push_back(extra);

    }
    JetDefinition jet_def(antikt_algorithm,1.5);
    ClusterSequence cs(particles,jet_def);
    vector<PseudoJet> jets = sorted_by_pt(cs.inclusive_jets(30));
    unsigned int max_tracks = 0;
    unsigned int max_tracks_2 = 0;
    int highest_index = -1;
    int highest_index_2 = -1;
    for(int i = 0; i < jets.size(); i++) {
       PseudoJet jet = jets[i];
       if (jet.constituents().size() > max_tracks){ 
         highest_index_2 = highest_index;
         max_tracks_2 = max_tracks;
         highest_index = i;
         max_tracks = jet.constituents().size();
       }
       else if (jet.constituents().size() > max_tracks_2){ 
         highest_index_2 = i;
         max_tracks_2 = jet.constituents().size();
       }
    }
    if((highest_index == -1) || (highest_index_2 == -1)){continue;}
    PseudoJet jet = jets[highest_index];
    PseudoJet jet2 = jets[highest_index_2];
    TLorentzVector boostjet;
    boostjet.SetPtEtaPhiE(jet.pt(),jet.eta(),jet.phi(),jet.E());
    TVector3 boostvect = -boostjet.BoostVector();
    TLorentzVector boostisr;
    boostisr.SetPtEtaPhiE(jet2.pt(),jet2.eta(),jet2.phi(),jet2.E());
    boostisr.Boost(boostvect);
    float isr_phi = boostisr.Phi();
    float isr_eta = boostisr.Eta();
    //printf("%f %f %f\n",boostvect.x(),boostvect.y(),boostvect.z());
    
    //PseudoJet jet_boosted = jet.boost(jets[highest_index_2]);
    //float pf4 = (  jet.px()*jet2.px()+jet.py()*jet2.py()+jet.pz()*jet2.pz()+jet.E()*jet2.E())/jet2.m();
    //float fn = (pf4 + jet.E())/(jet2.E()+jet2.m());
    //printf("pt: %d %d %f %f\n",highest_index,highest_index_2,jet.pt(),jet_boosted.pt());

    //getAllGen(sueps, isrs, suep_id,isr_id,OutFileGen,entry);
    //gen_match_remove(particles,sueps,isrs,OutFile,part_extra,suep_id,isr_id);
    if(jet.constituents().size() <=2){continue;}
    jet_pass++;
    vector<TLorentzVector> tracks_boosted;
    //for (auto cont : jet_boosted.constituents()){
    //  TLorentzVector trk;
    //  trk.SetPtEtaPhiE(cont.pt(),cont.eta(),cont.phi(),cont.E());
    //  tracks_boosted.push_back(trk);
    //}
    vector<TLorentzVector> tracks;
    for (auto cont : jet.constituents()){
      TLorentzVector trk;
      trk.SetPtEtaPhiE(cont.pt(),cont.eta(),cont.phi(),cont.E());
      TLorentzVector trk_b;
      trk_b.SetPtEtaPhiE(cont.pt(),cont.eta(),cont.phi(),cont.E());
      trk_b.Boost(boostvect);
      tracks.push_back(trk);
      tracks_boosted.push_back(trk_b);
    }
    vector<TLorentzVector> tracks_event_boost;
    vector<TLorentzVector> tracks_event_boost2;
    vector<TLorentzVector> tracks_event_boost3;
    //PlotHelper plotter("");
    //TCanvas *c1 = new TCanvas("c1","c1",800,800);
    for (auto cont : tracks_event){
      TLorentzVector trk_b;
      trk_b.SetPtEtaPhiE(cont.Pt(),cont.Eta(),cont.Phi(),cont.E());
      trk_b.Boost(boostvect);
      //tracks_event_boost.push_back(trk_b);
  //plotter.Plot2D(Form("%s_evt%lli_event_display_tracks",sample_name.c_str(),ievent),";eta;phi;pt", track.p4.Eta(), track.p4.Phi(), 100, -3.5,3.5,100,-3.5,3.5 , track.p4.Pt());
  //plotter.Plot2D(Form("%s_evt%lli_event_display_tracks","test1",entry),";eta;phi;pt", trk_b.Eta(), trk_b.Phi(), 100, -3.5,3.5,100,-3.5,3.5 , trk_b.Pt());
  //plotter.Plot2D(Form("%s_evt%lli_event_display_tracks","test1",entry),";eta;phi;pt", cont.Eta(), cont.Phi(), 100, -3.5,3.5,100,-3.5,3.5 , cont.Pt());
      if(abs(cont.Phi()-jet2.phi()) > 1.6){
      //if(sqrt(((cont.Phi()-jet2.phi())*(cont.Phi()-jet2.phi()))+((cont.Eta()-jet2.eta())*(cont.Eta()-jet2.eta()))) > 2.0){
        tracks_event_boost2.push_back(trk_b); // remove isr preboost
  //plotter.Plot2D(Form("%s_evt%lli_event_display_tracks","test1",entry),";eta;phi;pt", trk_b.Eta(), trk_b.Phi(), 100, -3.5,3.5,100,-3.5,3.5 , trk_b.Pt());
      }
      if(abs(trk_b.Phi()-isr_phi) > 1.6){
      //if(sqrt(((trk_b.Phi()-isr_phi)*(trk_b.Phi()-isr_phi))+((trk_b.Eta()-isr_eta)*(trk_b.Eta()-isr_eta))) > 2.0){
        tracks_event_boost.push_back(trk_b); // remove isr post boost
      }
    }
// Save histograms here
//     TFile *output_file = TFile::Open(Form("event_%i.root",entry),"RECREATE");
//     c1->SetTickx(true);
//     c1->SetTicky(true);
//     plotter.DrawAll1D(c1);
//     plotter.DrawAll2D(c1, "colz");
//     c1->SaveAs(Form("neg_boostrm2_event_%i_sig300fix.pdf",entry));


    std::vector<double> eigentest = compTensorsAndVectors(tracks_event);
    std::vector<double> eigentest_boost = compTensorsAndVectors(tracks_event_boost); // remove isr post boost
    std::vector<double> eigentest_boost2 = compTensorsAndVectors(tracks_event_boost2);// remove isr pre boost
    //printf("eigen %f %f %f %f\n",eigentest[0],eigentest[1],eigentest[2],eigentest[3]);
    float sphericity = 1.5*(eigentest[1] + eigentest[2]);
    float sphericity_boosted = 1.5*(eigentest_boost[1] + eigentest_boost[2]);
    float sphericity_boosted2 = 1.5*(eigentest_boost2[1] + eigentest_boost2[2]);
    float C = 3*(eigentest[0]*eigentest[1] + eigentest[0]*eigentest[2]+ eigentest[1]*eigentest[2]);
    float C_boosted = 3*(eigentest_boost[0]*eigentest_boost[1]+eigentest_boost[0]*eigentest_boost[2]+eigentest_boost[1]*eigentest_boost[2]);
    float C_boosted2 = 3*(eigentest_boost2[0]*eigentest_boost2[1]+eigentest_boost2[0]*eigentest_boost2[2]+eigentest_boost2[1]*eigentest_boost2[2]);
    float D = 27*(eigentest[1]*eigentest[2]*eigentest[0]);
    float D_boosted = 27*(eigentest_boost[1]*eigentest_boost[2]*eigentest_boost[0]);
    float D_boosted2 = 27*(eigentest_boost2[1]*eigentest_boost2[2]*eigentest_boost2[0]);
    float aPlan = 1.5*(eigentest[1]);
    float aPlan_boosted = 1.5*(eigentest_boost[1]);
    float aPlan_boosted2 = 1.5*(eigentest_boost2[1]);
    //printf("sphericity %f %f\n",sphericity,sphericity_boosted);
    auto [t1,t2,t3,
          rho0_50,rho1_50,rho2_50,
          rho0_20,rho1_20,rho2_20,
          rho0_10,rho1_10,rho2_10,
          rho0_05,rho1_05,rho2_05,
          rho0_15,rho1_15,rho2_15,
          rho0_30,rho1_30,rho2_30
          ] = nsubjettiness(jet,1.5);
    //auto [t1,t2,t3,e2,e3] = nsubjettiness(jet,1.5);
    //printf("%f %f\n",t1/t2,t2/t3);
    fprintf(OutFile,"%d %f %f %f %d %d %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f\n",
            entry, jet.pt(), jet.eta(), jet.phi(), jet.constituents().size(),particles.size(),
            t1,t2,t3,t2/t1,t3/t2,
            rho0_50,rho1_50,rho2_50,
            rho0_20,rho1_20,rho2_20,
            rho0_10,rho1_10,rho2_10,
            rho0_05,rho1_05,rho2_05,
            rho0_15,rho1_15,rho2_15,
            rho0_30,rho1_30,rho2_30,
            sphericity, sphericity_boosted, sphericity_boosted2,
            C,C_boosted,C_boosted2,
            D,D_boosted,D_boosted2,
            aPlan,aPlan_boosted,aPlan_boosted2
    );

  }
fclose(OutFile);
printf("trigpass: %d; jetpass %d\n",trig_pass,jet_pass);
}
  
