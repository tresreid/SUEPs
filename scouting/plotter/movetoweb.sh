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
#outdir=/publicweb/m/mreid/SUEPs/trackdropeff #_withoutdrop
#outdir=/publicweb/m/mreid/SUEPs/chi_test #_withoutdrop
#outdir=/publicweb/m/mreid/SUEPs/fullplotstest_offline_scouting_compare_17 #_withoutdrop
#outdir=/publicweb/m/mreid/SUEPs/fullplotstest_16compare18 #qcd_scouting_full_offline_scouting_compare #_withoutdrop
#outdir=/publicweb/m/mreid/SUEPs/fullplots_161718 #qcd_scouting_full_offline_scouting_compare #_withoutdrop
outdir=/publicweb/m/mreid/SUEPs/fullplots_18test
#outdir=/publicweb/m/mreid/SUEPs/newlimittest
rm -r $outdir
mkdir $outdir
cp -r $dir/* $outdir

