#1/bin/bash
for i in $(seq 0  37); do
python fillcoff3.py Trigger ${i}
done
