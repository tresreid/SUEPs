#1/bin/bash
for i in $(seq 251  500); do
python fillcoff3.py RunD ${i} 18
done
