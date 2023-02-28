#1/bin/bash
for i in $(seq 0  234); do
python fillcoff3.py RunC ${i} 17
done
for i in $(seq 0  222); do
python fillcoff3.py RunE ${i} 17
done
