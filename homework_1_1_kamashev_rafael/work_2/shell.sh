#!/bin/bash

while read line
do
    eval $line
done < "${1:-/dev/stdin}"
