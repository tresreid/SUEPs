#!/bin/bash

for phi in "4.000"; do 
#for temp in "8p00"; do
for temp in "16p0" "1p00" "2p00" "4p00" "8p00"; do
for i in $(seq 0  15); do
python fillcoff3.py 125 2 16apv ${i} ${temp} ${phi} 
python fillcoff3.py 200 2 16apv ${i} ${temp} ${phi}
python fillcoff3.py 300 2 16apv ${i} ${temp} ${phi}
python fillcoff3.py 400 2 16apv ${i} ${temp} ${phi}
python fillcoff3.py 500 2 16apv ${i} ${temp} ${phi}
python fillcoff3.py 600 2 16apv ${i} ${temp} ${phi}
python fillcoff3.py 700 2 16apv ${i} ${temp} ${phi}
python fillcoff3.py 800 2 16apv ${i} ${temp} ${phi}
python fillcoff3.py 900 2 16apv ${i} ${temp} ${phi}
python fillcoff3.py 1000 2 16apv ${i} ${temp} ${phi} 
done
python fillcoff3.py 125 2 16apv 16 ${temp} ${phi} 
python fillcoff3.py 125 2 16apv 17 ${temp} ${phi} 
done
done
