#1/bin/bash
#python fillcoff3.py RunA 0
#python fillcoff3.py RunA 1
#python fillcoff3.py RunA 2
#python fillcoff3.py RunA 3
#python fillcoff3.py RunA 4
#python fillcoff3.py RunA 5
#python fillcoff3.py RunA 6
#python fillcoff3.py RunA 7
#python fillcoff3.py RunA 8
for i in $(seq 135  268); do
#python nPVplots.py RunA ${i}
python fillcoff3.py RunC ${i}
done
#for i in $(seq 26  50); do
#python fillcoff3.py RunA ${i}
#done
#for i in $(seq 51  75); do
#python fillcoff3.py RunA ${i}
#done
#for i in $(seq 76  100); do
#python fillcoff3.py RunA ${i}
#done
#for i in $(seq 101  125); do
#python fillcoff3.py RunA ${i}
#done
#for i in $(seq 126  150); do
#python fillcoff3.py RunA ${i}
#done
#for i in $(seq 151  175); do
#python fillcoff3.py RunA ${i}
#done
#for i in $(seq 176  200); do
#python fillcoff3.py RunA ${i}
#done
#for i in $(seq 201  225); do
#python fillcoff3.py RunA ${i}
#done
#for i in $(seq 226  250); do
#python fillcoff3.py RunA ${i}
#done

#
