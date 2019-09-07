#!/bin/bash

    (sed 's/     /,/' $1) \
  | (sed 's/    /,/') \
  | (sed 's/   /,/') \
  | (sed 's/  /,/') > ${1}-formatted
