#1/bin/bash
for i in $(seq 400  538); do
python fillcoff3.py RunA ${i} 18
done
