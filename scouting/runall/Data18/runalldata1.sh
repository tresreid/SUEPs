#1/bin/bash
for i in $(seq 0  100); do
python fillcoff3.py RunA ${i} 18
done
