#1/bin/bash
for i in $(seq 0  250); do
python fillcoff3.py RunD ${i}
done
