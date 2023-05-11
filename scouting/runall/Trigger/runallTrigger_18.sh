#1/bin/bash
for i in $(seq 0  37); do
python fillcoff3.py TriggerA ${i} 18
done
for i in $(seq 0  23); do
python fillcoff3.py TriggerB ${i} 18
done
for i in $(seq 0  19); do
python fillcoff3.py TriggerC ${i} 18
done
for i in $(seq 0  76); do
python fillcoff3.py TriggerD ${i} 18
done
