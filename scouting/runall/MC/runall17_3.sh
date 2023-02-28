#1/bin/bash

#for i in $(seq 0  66); do
#python fillcoff3.py HT200 ${i} 17
#done
#for i in $(seq 0  65); do
#python fillcoff3.py HT300 ${i} 17
#done
#for i in $(seq 0  72); do
#python fillcoff3.py HT500 ${i} 17
#done
for i in $(seq 0  57); do
python fillcoff3.py HT700 ${i} 17
done
for i in $(seq 0  18); do
python fillcoff3.py HT1000 ${i} 17
done
#for i in $(seq 0  10); do
#python fillcoff3.py HT1500 ${i} 17
#done
#for i in $(seq 0  9); do
#python fillcoff3.py HT2000 ${i} 17
#done
