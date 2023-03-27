#1/bin/bash
for i in $(seq 1114  1133); do
python fillcoff3.py RunD ${i} 18
done
