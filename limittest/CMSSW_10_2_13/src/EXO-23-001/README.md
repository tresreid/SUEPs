
**(a) a brief description of the signal and control regions (if any)**
Regions are defined in the plane of two discriminators, constituents and sphericity of the SUEP jet; the signal region is defined with > 50 and > 0.6 respectively, and we use 8 control regions for an extended ABCD method. We have 3 bins in the signal region defined by [50, 70), [70, 85), [85, inf) in constituents. 

**(b) special instructions or tags to set up combine (if necessary)**
N/A.

**(c) example combine command (with special options if any)**
We first combine all the different cards (other years can also be included in the same way):
```
combineCards.py -S catcrA2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-cat_crA2018.dat catcrB2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-cat_crB2018.dat catcrC2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-cat_crC2018.dat catcrD2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-cat_crD2018.dat catcrE2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-cat_crE2018.dat Bin1crF2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-Bin1crF2018.dat Bin2crF2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-Bin2crF2018.dat Bin3crF2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-Bin3crF2018.dat catcrG2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-cat_crG2018.dat catcrH2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-cat_crH2018.dat Bin1Sig2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-Bin1Sig2018.dat Bin2Sig2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-Bin2Sig2018.dat Bin3Sig2018=cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/shapes-Bin3Sig2018.dat > cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/combined.dat
```

Then the text2workspace:
```
text2workspace.py -m 125 cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/combined.dat -o cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/combined.root
```

And the combine:
```
combine  -M AsymptoticLimits --datacard cards-GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric/combined.root -m 125 --cl 0.95 --name GluGluToSUEP_HT400_T2p00_mS125.000_mPhi2.00_T2.000_modegeneric  --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --run blind

**(d) expected output**
Sample output: for all years.

```
 <<< Combine >>>
Will use a-priori expected background instead of a-posteriori one.
>>> method used is AsymptoticLimits
>>> random number generator seed is 123456

 -- AsymptoticLimits ( CLs ) --
Expected  2.5%: r < 0.1222
Expected 16.0%: r < 0.1607
Expected 50.0%: r < 0.2188
Expected 84.0%: r < 0.2964
Expected 97.5%: r < 0.3842

Done in 0.01 min (cpu), 0.01 min (real)
```
