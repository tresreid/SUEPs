#!/bin/bash

#for i in $(seq 0  7); do
#for i in 10 11; do
for i in $(seq 0  15); do
#python fillcoff3.py sig125 2 16 ${i}
#python fillcoff3.py sig200 2 16 ${i}
#python fillcoff3.py sig300 2 16 ${i}
#python fillcoff3.py sig400 2 16 ${i}
python fillcoff3.py sig700 2 16 ${i}
python fillcoff3.py sig1000 2 16 ${i}
done
#python fillcoff3.py sig125 2 16 16
#python fillcoff3.py sig125 2 16 17
