#!/bin/bash

#for i in $(seq 0  7); do
#for i in 10 11; do
for i in $(seq 6  15); do
python fillcoff3.py 125 2 17 ${i}
python fillcoff3.py 200 2 17 ${i}
python fillcoff3.py 300 2 17 ${i}
python fillcoff3.py 400 2 17 ${i}
python fillcoff3.py 700 2 17 ${i}
python fillcoff3.py 1000 2 17 ${i}
done
python fillcoff3.py 125 2 17 16
python fillcoff3.py 125 2 17 17
##for i in 10 11; do
#for i in $(seq 1  9); do
#python fillcoff3.py sig125 2 17 ${i}
#python fillcoff3.py sig200 2 17 ${i}
#python fillcoff3.py sig300 2 17 ${i}
#python fillcoff3.py sig400 2 17 ${i}
#python fillcoff3.py sig700 2 17 ${i}
#python fillcoff3.py sig1000 2 17 ${i}
#done
##for i in $(seq 1  9); do
#for i in 10 11; do
#python fillcoff3.py sig125 2 16 ${i}
#python fillcoff3.py sig200 2 16 ${i}
#python fillcoff3.py sig300 2 16 ${i}
#python fillcoff3.py sig400 2 16 ${i}
#python fillcoff3.py sig700 2 16 ${i}
#python fillcoff3.py sig1000 2 16 ${i}
#done
#python fillcoff3.py sig125 2 18 12
#python fillcoff3.py sig125 2 18 13
#python fillcoff3.py sig125 2 17 12
#python fillcoff3.py sig125 2 17 13
#python fillcoff3.py sig125 2 16 12
#python fillcoff3.py sig125 2 16 13
