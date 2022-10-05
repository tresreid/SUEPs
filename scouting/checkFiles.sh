#!/bin/bash

checkem (){
if  [ ! -f "outhists/myhistos_${1}_${2}.p" ]; then
    echo "python fillcoff3.py $1 $2"
fi
}

for i in $(seq 0  9); do
checkem "HT2000" ${i}
done
for i in $(seq 0  18); do
checkem "HT1500" ${i}
done
for i in $(seq 0  60); do
checkem "HT700" ${i}
done
for i in $(seq 0  22); do
checkem "HT1000" ${i}
done
for i in $(seq 0  62); do
checkem "HT500" ${i}
done
for i in $(seq 0  64); do
checkem "HT300" ${i}
done
for i in $(seq 0  68); do
checkem "HT200" ${i}
done
#for i in $(seq 0  538); do
#checkem "RunA" ${i}
#done
#for i in $(seq 0  310); do
#checkem "RunB" ${i}
#done
#for i in $(seq 0  268); do
#checkem "RunC" ${i}
#done
#for i in $(seq 0  1138); do
#checkem "RunD" ${i}
#done
