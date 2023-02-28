#1/bin/bash
for i in $(seq 0  10); do
#python nPVplots.py RunA ${i}
python fillcoff3.py RunB ${i} 16
done
