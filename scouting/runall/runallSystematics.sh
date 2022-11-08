#!/bin/bash

#for i in $(seq 0  7); do
for i in $(seq 0  9); do
python fillcoff3.py sig125 2 17 ${i}
python fillcoff3.py sig200 2 17 ${i}
python fillcoff3.py sig300 2 17 ${i}
python fillcoff3.py sig400 2 17 ${i}
python fillcoff3.py sig700 2 17 ${i}
python fillcoff3.py sig1000 2 17 ${i}
done
