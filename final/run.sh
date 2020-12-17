#!/bin/bash

chmod +x *.py

#****************************
# compile the python code
#**************************** 

./fac.py -hemi g
open *.png
sleep 2

#****************************
#  compile the Fortran code
#****************************

make help
make
#./j.exe

#****************************
#   compile the LaTex code
#****************************

make pdf
open final.pdf
make clean
sleep 2

#open *.htm
./j.exe
sleep 1

tkdiff fac_2013031710_2d.txt ./data/fac_2013031710_2d.txt