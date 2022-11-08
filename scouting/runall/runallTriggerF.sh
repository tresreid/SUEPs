#1/bin/bash
for i in $(seq 0  44); do
python fillcoff3.py TriggerF ${i} 17
done
