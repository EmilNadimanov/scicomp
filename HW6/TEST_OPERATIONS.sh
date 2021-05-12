#!/bin/bash

for file in stats-mean.py stats-median.py stats-mad.py stats-stddev.py stats-variance.py
do
result=`seq 1 5 | ./$file`;
operation=`echo $file | sed "s@stats-\(.*\)\.py@\1@g"`;
echo "$operation(1, 2, 3, 4, 5) = $result"
done
