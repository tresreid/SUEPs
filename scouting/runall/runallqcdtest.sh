#!/bin/bash

python fillcoff3.py HT200 -1
python fillcoff3.py HT300 -1
python fillcoff3.py HT500 -1
python fillcoff3.py HT700 -1
python fillcoff3.py HT1000 -1
python fillcoff3.py HT1500 -1
python fillcoff3.py HT2000 -1
python outhists/2018/mergeqcdtest.py
