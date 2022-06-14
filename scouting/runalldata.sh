#1/bin/bash
#python fillcoff2.py RunA 0
#python fillcoff2.py RunA 1
#python fillcoff2.py RunA 2
#python fillcoff2.py RunA 3
#python fillcoff2.py RunA 4
#python fillcoff2.py RunA 5
#python fillcoff2.py RunA 6
#python fillcoff2.py RunA 7
#python fillcoff2.py RunA 8
for i in $(seq 95  100); do
#python nPVplots.py RunA ${i}
python fillcoff2.py RunA ${i}
done
#for i in $(seq 26  50); do
#python fillcoff2.py RunA ${i}
#done
#for i in $(seq 51  75); do
#python fillcoff2.py RunA ${i}
#done
#for i in $(seq 76  100); do
#python fillcoff2.py RunA ${i}
#done
#for i in $(seq 101  125); do
#python fillcoff2.py RunA ${i}
#done
#for i in $(seq 126  150); do
#python fillcoff2.py RunA ${i}
#done
#for i in $(seq 151  175); do
#python fillcoff2.py RunA ${i}
#done
#for i in $(seq 176  200); do
#python fillcoff2.py RunA ${i}
#done
#for i in $(seq 201  225); do
#python fillcoff2.py RunA ${i}
#done
#for i in $(seq 226  250); do
#python fillcoff2.py RunA ${i}
#done

#
