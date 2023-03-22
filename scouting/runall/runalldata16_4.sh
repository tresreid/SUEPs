#1/bin/bash
for i in $(seq 157  200); do
python fillcoff3.py RunB ${i} 16
python fillcoff3.py RunC ${i} 16
python fillcoff3.py RunD ${i} 16
python fillcoff3.py RunE ${i} 16
done
