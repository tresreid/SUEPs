#1/bin/bash
for i in $(seq 0  350); do
python fillcoff3.py RunG ${i} 16
done
