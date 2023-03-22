#1/bin/bash
for i in $(seq 500  750); do
python fillcoff3.py RunD ${i} 18
done
