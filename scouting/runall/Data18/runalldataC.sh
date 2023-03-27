#1/bin/bash
for i in $(seq 83  268); do
python fillcoff3.py RunC ${i} 18
done
