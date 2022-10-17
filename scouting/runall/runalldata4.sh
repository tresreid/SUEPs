#1/bin/bash
for i in $(seq 301  400); do
python fillcoff3.py RunA ${i}
done
