#1/bin/bash
for i in $(seq 23  100); do
#python nPVplots.py RunA ${i}
python fillcoff3.py RunA ${i}
done
