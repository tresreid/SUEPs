#1/bin/bash
for i in $(seq 71  268); do
python fillcoff3.py RunC ${i} 18
done
