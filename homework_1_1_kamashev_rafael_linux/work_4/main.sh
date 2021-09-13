#!/bin/bash

rm -rf abc/ xyz/
clear
mkdir abc xyz
touch abc/file.txt
link abc/file.txt xyz/file.txt
ls -lia abc
ls -lia xyz
find . -inum `ls -i abc | grep file.txt | cut -d' ' -f1`
find . -inum `ls -i abc | grep file.txt | cut -d' ' -f1` -exec rm -f {} \;
ls -a abc
ls -a xyz
