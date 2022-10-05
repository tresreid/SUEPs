#!/bin/bash

for i in $(seq 6  7); do
#for i in $(seq 1  7); do
#python fillcoff3.py sig200 2 ${i}
#python fillcoff3.py sig300 2 ${i}
#python fillcoff3.py sig400 2 ${i}
python fillcoff3.py sig700 2 ${i}
#python fillcoff3.py sig1000 2 ${i}
done
