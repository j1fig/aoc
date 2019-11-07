#!/bin/bash

YEAR=$1
DAY=$2
DIR=$1-$2

mkdir $DIR
aocd $DAY $YEAR >> $DIR/data.txt
cp template.py $DIR/solve.py
cp test_template.py $DIR/test_solve.py
chmod +x $DIR/solve.py
