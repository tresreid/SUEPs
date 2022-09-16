#!/bin/bash
for file in *.txt; do 
    mv -- "$file" "${file%.txt}.jr.txt"
done
