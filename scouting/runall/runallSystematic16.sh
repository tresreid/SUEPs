#!/bin/bash

#for i in $(seq 0  7); do
#for i in 10 11; do
for i in $(seq 0  15); do
python fillcoff3.py 125 2 16 ${i}
python fillcoff3.py 200 2 16 ${i}
python fillcoff3.py 300 2 16 ${i}
python fillcoff3.py 400 2 16 ${i}
python fillcoff3.py 500 2 16 ${i}
python fillcoff3.py 600 2 16 ${i}
python fillcoff3.py 700 2 16 ${i}
python fillcoff3.py 800 2 16 ${i}
python fillcoff3.py 900 2 16 ${i}
python fillcoff3.py 1000 2 16 ${i}
done
python fillcoff3.py 125 2 16 16
python fillcoff3.py 125 2 16 17
