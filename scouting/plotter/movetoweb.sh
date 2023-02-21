#!/bin/bash

dir=${PWD}/Plots
#dir=${PWD}/Displays
for d in $(find ${dir} -type d)
do
  #Do something, the directory is accessible with $d:
  echo $d
  python3 $dir/../make_html_listing.py $d
done
#outdir=/publicweb/m/mreid/SUEPs/tests_data16compare #_withoffselection
#outdir=/publicweb/m/mreid/SUEPs/tests_2dcompare #_withoffselection
#outdir=/publicweb/m/mreid/SUEPs/tests_dataonlineofflinecompare_offlinetest #_withoffselection
outdir=/publicweb/m/mreid/SUEPs/qcd_scouting_full_ratiotest2 #_withoutdrop
rm -r $outdir
mkdir $outdir
cp -r $dir/* $outdir

