#1/bin/bash
for i in $(seq 501  725); do
python fillcoff3.py RunD ${i}
done
