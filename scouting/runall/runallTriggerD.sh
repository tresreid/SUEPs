#1/bin/bash
for i in $(seq 0  25); do
python fillcoff3.py TriggerD ${i} 17
done
