#1/bin/bash
for i in $(seq 101  200); do
python fillcoff3.py RunA ${i}
done
