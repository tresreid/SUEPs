#!/bin/bash 
outdir=sueps/trackStudies
rm -r /cdat/tem/mgr85/www/${outdir}
mkdir -p /cdat/tem/mgr85/www/${outdir}
#rm -r ~/public_html/www/${outdir}
cp -r Plots/ /cdat/tem/mgr85/www/${outdir}
#ln -sv /cdat/tem/mgr85/www/${outdir} ~/public_html/${outdir}
