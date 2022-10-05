#1/bin/bash
for i in $(seq 401  500); do
python fillcoff3.py RunA ${i}
done
