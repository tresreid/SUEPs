#1/bin/bash

for i in $(seq 0  50); do
python fillcoff3.py HT300 ${i} 17
done
for i in $(seq 0  62); do
python fillcoff3.py HT200 ${i} 17
done
