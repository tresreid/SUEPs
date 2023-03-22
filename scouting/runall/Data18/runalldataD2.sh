#1/bin/bash
for i in $(seq 328  500); do
python fillcoff3.py RunD ${i} 18
done
