#1/bin/bash

for i in $(seq 0  43); do
python fillcoff3.py HT200 ${i} 16apv
done
#for i in $(seq 0  43); do
#python fillcoff3.py HT300 ${i} 16apv
#done
#for i in $(seq 0  51); do
#python fillcoff3.py HT500 ${i} 16apv
#done
#for i in $(seq 0  38); do
#python fillcoff3.py HT700 ${i} 16apv
#done
#for i in $(seq 0  14); do
#python fillcoff3.py HT1000 ${i} 16apv
#done
for i in $(seq 0  18); do
python fillcoff3.py HT1500 ${i} 16apv
done
#for i in $(seq 0  5); do
#python fillcoff3.py HT2000 ${i} 16apv
#done
