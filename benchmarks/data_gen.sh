#!/bin/bash

# arg1: number of files to generate
# arg2: number of Bytes to generate per file 
# arg3: name of folder to place generated data 

mkdir $3

begin_index=0
n=$(($2/100)) 
for i in $(seq 0 $(($1-1)))
do
    ./gensort -a -b$begin_index $n $3/input$i
    begin_index=$(($begin_index+$n))
done

cd $3
cat input* > input
cd ..
mv -v $3 input_files
