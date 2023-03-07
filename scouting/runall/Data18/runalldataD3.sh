#1/bin/bash
for i in $(seq 525  725); do
python fillcoff3.py RunD ${i} 18
done
