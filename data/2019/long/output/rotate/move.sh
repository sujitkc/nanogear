#!/bin/bash

files=( `ls *.xyz` );
newfiles=()
for name in ${files[@]}; do
  newfiles+=(${name/.xyz/})
done

for name in ${newfiles[@]}; do
  mkdir ${name}
  mv  ${name}.xyz ${name}/input.xyz
done
