#!/bin/bash

for i in $(seq 825 25 1600); do
#for i in $(seq 0 25 1600); do
j=$((25+${i}))
python tracks2.py ${i} ${j}
done
python tracks2.py 1600 1631
