#1/bin/bash
for i in $(seq 0  48); do
python fillcoff3.py TriggerC ${i} 17
done
