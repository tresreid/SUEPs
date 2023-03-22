#1/bin/bash
for i in $(seq 0  638); do
python fillcoff3.py RunH ${i} 16
done
