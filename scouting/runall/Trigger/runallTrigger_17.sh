#1/bin/bash
for i in $(seq 0  42); do
python fillcoff3.py TriggerC ${i} 17
done
for i in $(seq 0  25); do
python fillcoff3.py TriggerD ${i} 17
done
for i in $(seq 0  36); do
python fillcoff3.py TriggerE ${i} 17
done
for i in $(seq 0  44); do
python fillcoff3.py TriggerF ${i} 17
done
