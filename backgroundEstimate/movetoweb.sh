#!/bin/bash

dir=/uscms/home/mreid/nobackup/sueps/analysis/SUEPs/backgroundEstimate/Plots
for d in $(find ${dir} -type d)
do
  #Do something, the directory is accessible with $d:
  echo $d
  python3 $dir/../make_html_listing.py $d
done
#outdir=/publicweb/m/mreid/SUEPs/trackStudy_ptErr
outdir=/publicweb/m/mreid/SUEPs/Closurev5fin
rm -r $outdir
mkdir $outdir
cp -r $dir/* $outdir

