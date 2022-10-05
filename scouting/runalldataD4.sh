#1/bin/bash
for i in $(seq 751  1133); do
python fillcoff3.py RunD ${i}
done
