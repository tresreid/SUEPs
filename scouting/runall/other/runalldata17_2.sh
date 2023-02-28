#1/bin/bash
for i in $(seq 0 112); do
python fillcoff3.py RunD ${i} 17
done
for i in $(seq 0  312); do
python fillcoff3.py RunF ${i} 17
done
