#!/bin/bash

files=(200 300 500 700 1000 1500 2000)

#for i in ${files[@]}; do
#  eosls /store/group/lpcsuep/Scouting/QCDv4/2017/HT${i} > HT${i}v4.txt 
#done
eosls /store/group/lpcsuep/Scouting/Datav4/2017/RunC > Data_RunC.txt 
eosls /store/group/lpcsuep/Scouting/Datav4/2017/RunD > Data_RunD.txt 
eosls /store/group/lpcsuep/Scouting/Datav4/2017/RunE > Data_RunE.txt 
eosls /store/group/lpcsuep/Scouting/Datav4/2017/RunF > Data_RunF.txt 
