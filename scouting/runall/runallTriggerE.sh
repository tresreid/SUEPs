#1/bin/bash
for i in $(seq 0  36); do
python fillcoff3.py TriggerE ${i} 17
done
