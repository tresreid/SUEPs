#!/bin/bash

for i in $(seq 1  7); do
python fillcoff3.py sig200 2 ${i}
python fillcoff3.py sig300 2 ${i}
python fillcoff3.py sig400 2 ${i}
python fillcoff3.py sig750 2 ${i}
python fillcoff3.py sig1000 2 ${i}
done
