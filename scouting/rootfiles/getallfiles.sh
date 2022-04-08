#!/bin/bash

files=(50 100 200 300 500 700 1000 1500 2000)

for i in ${files[@]}; do
  eosls /store/group/lpcsuep/Scouting/QCDv2/HT${i} > HT${i}.txt 
done
