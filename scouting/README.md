
# 1) Make nTuples
```
- Follow instructions on github readme
https://github.com/tresreid/SUEPScouting/tree/mods

- make sure to use the mods branch
- make sure to load in the patutils package as well.
```
# 2) Run FillCoff.py to run over the ntuples with coffea and make intial histograms

github: https://github.com/tresreid/SUEPs/tree/master/scouting

-I run fillcoff on the MIT machines.
```
> ssh -X -Y -v <user>@submit07.mit.edu
or 
> ssh -X -Y -v <user>@submit04.mit.edu
```
I find only 07 and 04 work for me. 

-Run singularity shell
```
> ./shell
```
-Run fillcoff to produce histograms
--For signal
```
> python fillcoff3.py <sample> <decaymode> <era> <systematic> <temp> <phi>
``
where
<sample> = {125,200,300,400,500,600,700,800,900,1000}
<decaymode> = {0,1,2} corresponding to darkpho,darkphohad,generic
<systematic> = {0..18} corresponding to
0: "nominal"
1: "_track_up"
2: "_JES_up"
3: "_JES_down"
4: "_JER_up"
5: "_JER_down"
6: "_trigSF_up"
7: "_trigSF_down"
8: "_puweights_up"
9: "_puweights_down"
10: "_PSWeight_ISR_up"
11: "_PSWeight_FSR_up"
12: "_PSWeight_ISR_down"
13: "_PSWeight_FSR_down"
14: "_prefire_up"
15: "_prefire_down"
16: "_higgs_weights_up"
17: "_higgs_weights_down"

<phi> = "2.000" 
<temp> = "4p00" to 3 sigfigs
<era> = {18,17,16,16apv}

example
```
> python fillcoff3.py 125 2 16 16p0 4.000 
```
--For QCD or data
```
> python fillcoff3.py <sample> <batch> <era> 
```
where 
<qcdsample> = "HT2000"
<datasample> = "RunA"
<era> = {18,17,16,16apv}

directory "runall/" contains scripts to run across all files of different types in batches

-Other relavent directories
Systematics
Workflow

--workflow contains:
"getArrays.py" which loads all ntuple information into different awkward arrays for use in the cutflow.
"fillOutput.py" which fills the actual histograms with the distributions from each stage of the cutflow as defined in fillcoff.
"systematics.py" which contains functions to apply all scale factors and corrections and shift them for whichever uncertainty is being looked at.
"utils" contains supplimentary functions to calculate sphericity and make event displays

--Systematics conatins:
all files used for systematic corrections. Trigger scalefactors, jet corrections, goldenJSON files etc

-Files from fillcoff are typically saved in outhists. outhist also contains files to merge the batches into one distribution for QCD and data. 

# 3) Format Plots 

setup and run plotter
```
> source setup.sh
> cd plotter
> python plotcoff.py
```
output plots will be saved in plotter/Plots


