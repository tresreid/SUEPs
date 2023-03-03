#1/bin/bash
for i in $(seq 300  400); do
python fillcoff3.py RunA ${i} 18
done
