#!/bin/bash

files=( 500 700 1000 1500 2000)

for i in ${files[@]}; do
  eosls /store/group/lpcsuep/Scouting/QCD/HT${i} > HT${i}.txt 
done
