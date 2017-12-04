#!/bin/bash

# arg1: number of files to generate
# arg2: number of records to generate per file 
# arg3: name of folder to place generated data 

cd gensort-linux-1.5/64
mkdir $3

begin_index=0
for i in $(seq 0 $(($1-1)))
do
    ./gensort -a -b$begin_index $2 $3/input$i
    begin_index=$(($begin_index+$2))
done

cd $3
cat input* > input
cd ..
mv -v $3 ../../

