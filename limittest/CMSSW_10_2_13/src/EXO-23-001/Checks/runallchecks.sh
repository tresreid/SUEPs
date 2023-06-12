#!/bin/bash

datacard="cards-GluGluToSUEP_HT400_T2p00_mS1000.000_mPhi2.00_T2.000_modegeneric"

#rm -r ../cards-GluGluToSUEP_HT400*
#cp -r ../../../../SUEPLimits/${datacard}/ ../
datacard="../${datacard}/combined.root"

combine -M FitDiagnostics -d ${datacard} -t -1 --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t0.root -g plots_t0.root >> ./fitResults_t0 

combine -M FitDiagnostics -d ${datacard} -t -1 --expectSignal 1  --forceRecreateNLL -n _t1
# Increase the rMin value if (rMin * Nsig + Nbackground) < 0 for any channel
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> ./fitResults_t1 

combineTool.py -M Impacts -d ${datacard} -t -1 --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0
combineTool.py -M Impacts -d ${datacard} -t -1 --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1

combineTool.py -M Impacts -d ${datacard} -o impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 --job-mode interactive --task-name t0 --sub-opts '+JobFlavour = "espresso"'
combineTool.py -M Impacts -d ${datacard} -o impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1 --job-mode interactive --task-name t1 --sub-opts '+JobFlavour = "espresso"'

combineTool.py -M Impacts -d ${datacard} -m 1 -n t0 -o impacts_t0.json
combineTool.py -M Impacts -d ${datacard} -m 1 -n t1 -o impacts_t1.json

plotImpacts.py -i  impacts_t0.json -o  impacts_t0
plotImpacts.py -i  impacts_t1.json -o  impacts_t1


