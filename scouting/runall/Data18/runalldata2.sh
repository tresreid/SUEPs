#1/bin/bash
for i in $(seq 100  200); do
python fillcoff3.py RunA ${i} 18
done
