#!/bin/bash
# Jordan Matuszewski 08/07/19

for source in ../Working/corpus/*
do
    dest=$(basename $source)
    echo $dest
    ./VictoriaAutoEdits.py < $source > corpus/$dest
done
