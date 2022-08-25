#!/bin/bash

files=(50 100 200 300 500 700 1000 1500 2000)

for i in ${files[@]}; do
  eosls /store/group/lpcsuep/Scouting/QCDv3/E03/2018/HT${i} > HT${i}v3.txt 
done
#eosls /store/group/lpcsuep/Scouting/Data/RunA > DataRunA.txt 
