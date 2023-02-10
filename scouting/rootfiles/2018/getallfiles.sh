#!/bin/bash

files=(200 300 500 700 1000 1500 2000)

for i in ${files[@]}; do
  eosls /store/group/lpcsuep/Scouting/QCDv7/2018/HT${i} > HT${i}v7.txt 
done
#eosls /store/group/lpcsuep/Scouting/Data/RunA > DataRunA.txt 
