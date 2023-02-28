#1/bin/bash

for i in $(seq 0  40); do
python fillcoff3.py HT200 ${i} 16
done
#for i in $(seq 0  39); do
#python fillcoff3.py HT300 ${i} 16
#done
#for i in $(seq 0  56); do
#python fillcoff3.py HT500 ${i} 16
#done
#for i in $(seq 0  47); do
#python fillcoff3.py HT700 ${i} 16
#done
#for i in $(seq 0  13); do
#python fillcoff3.py HT1000 ${i} 16
#done
for i in $(seq 0  11); do
python fillcoff3.py HT1500 ${i} 16
done
#for i in $(seq 0  6); do
#python fillcoff3.py HT2000 ${i} 16
#done
