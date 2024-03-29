#!/bin/bash

files=(
  33_0
  33_2
  33_7
  44_11
  44_4
  44_9
  55_1
  55_6
  66_10
  66_3
  66_8
  77_12
  77_5
  33_10
  33_3
  33_8
  44_12
  44_5
  55_0
   55_2
  55_7
  66_11
  66_4
  66_9
  77_1
  77_6
  33_11
  33_4
  33_9
  44_1
  44_6
  55_10
  55_3
  55_8
  66_12
  66_5
  77_0
  77_2
  77_7
  33_12
  33_5
  44_0
  44_2
  44_7
  55_11
  55_4
  55_9
  66_1
  66_6
  77_10
  77_3
  77_8
  33_1
  33_6
  44_10
  44_3
  44_8
  55_12
  55_5
  66_0
  66_2
  66_7
  77_11
  77_4
  77_9
)

for name in ${files[@]}; do
  mkdir ${name}
  mv  ${name}.xyz ${name}/input.xyz
done
