#1/bin/bash
for i in $(seq 0  26); do
python fillcoff3.py RunF ${i} 16
done
