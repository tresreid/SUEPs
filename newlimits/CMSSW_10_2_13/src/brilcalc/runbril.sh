#!/bin/bash

#brilcalc lumi -b "STABLE BEAMS" --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -u /fb -i /uscms/home/mreid/nobackup/sueps/analysis/SUEPs/scouting/systematics/GoldenJSON/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt  --hltpath "DST_HT410_PFScouting_v*"

#brilcalc lumi -b "STABLE BEAMS" --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -u /fb -i /uscms/home/mreid/nobackup/sueps/analysis/SUEPs/scouting/systematics/GoldenJSON/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt   --hltpath "DST_HT410_PFScouting_v*"
#brilcalc lumi -b "STABLE BEAMS" --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -u /fb -i /uscms/home/mreid/nobackup/sueps/analysis/SUEPs/scouting/systematics/GoldenJSON/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt --hltpath "DST_HT410_PFScouting_v*"

#brilcalc lumi -c web -i newoutput/lumiSummaryGolden_H_16.json --hltpath "DST_HT410_PFScouting_v*"
#brilcalc lumi -c web -i newoutput/lumiSummaryGolden_C_17.json --hltpath "DST_HT410_PFScouting_v*"
#brilcalc lumi -c web -i newoutput/lumiSummaryGolden_C_18.json --hltpath "DST_HT410_PFScouting_v*"
brilcalc lumi -c web -i newoutput/lumiSummaryGolden_trigF_17.json --hltpath "DST_HT410_PFScouting_v*"
