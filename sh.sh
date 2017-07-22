#!/bin/bash

# Script for performance testing
rm log.log
./server.py > /dev/null &

for i in `seq 1 100`;
do
	./client.py $i > /dev/null &
done

python3
a=$(ps ax |grep python3 |awk 'BEGIN {ORS=" "}; {print $1}')
kill $a
echo "$counter"