#1/bin/bash
for i in $(seq 149  310); do
python fillcoff3.py RunB ${i} 18
done
