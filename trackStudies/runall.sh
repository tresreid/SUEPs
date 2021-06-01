#!/bin/bash

./jetAlgoComp 0 0
./jetAlgoComp 1 0
./jetAlgoComp 2 0

./jetAlgoComp 3 0
./jetAlgoComp 4 0
./jetAlgoComp 5 0
./jetAlgoComp 6 0
./jetAlgoComp 7 0
./jetAlgoComp 8 0

./jetAlgoComp 3 1
./jetAlgoComp 4 1
./jetAlgoComp 5 1
./jetAlgoComp 6 1
./jetAlgoComp 7 1
./jetAlgoComp 8 1

cat data/qcd_300_v1.txt >> data/qcd_300_v0.txt
cat data/qcd_500_v1.txt >> data/qcd_500_v0.txt
cat data/qcd_700_v1.txt >> data/qcd_700_v0.txt
cat data/qcd_1000_v1.txt >> data/qcd_1000_v0.txt
cat data/qcd_1500_v1.txt >> data/qcd_1500_v0.txt
cat data/qcd_2000_v1.txt >> data/qcd_2000_v0.txt

./jetAlgoComp 9 0
./jetAlgoComp 10 0
./jetAlgoComp 11 0
