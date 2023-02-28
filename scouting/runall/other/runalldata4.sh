#1/bin/bash
for i in $(seq 313  400); do
python fillcoff3.py RunA ${i}
done
