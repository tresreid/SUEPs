#!/bin/bash

for i in $(seq 0  15); do
python fillcoff3.py 700 2 18 ${i} "8p00" "4.000"
done
