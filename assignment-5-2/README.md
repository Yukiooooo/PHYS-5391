Definitely this assignment should be my lowest graded assignment. LOL

# This is a what-to-do for folders: mod_heq & cn_heq 

## Introduction to mod_heq

**ModHeatEq.f90** % the Fortran module for calculating Heat Equation

**write2d.f90** % the Fortran code for writing output file of the results

**HeatEq.f90** % the 'Main Program' for calculating the Heat Equation (calling modules and subroutines)

**Makefile** % this is the Makefile for compiling the above three codes

**results_correct.txt** % the correct result used for comparing with the output file

**viz_results.py** % the python code used for visualization the output file

## How to compile these files
Please download all the SIX files in this folder or clone my repository via:

$ git clone https://github.com/Yukiooooo/PHYS-5391.git

to compile these Fortran codes, please use command line via:

$ make heat.exe 

you'll get a executable heat.exe, in your command line, with:

$ ./heat.exe 

then a 'results.txt' output file is created, you can compare this data with the reference data via:

$ diff results.txt results_correct.txt or use tkdiff
  
to get the plot, in your command line via:

$ make viz

then you'll get the finally plot of the results of Heat Equation



If you use the command line, there are two basic ways to complete my codes.

__Method 1: # using Makefile #__

$ make % very straightforward to compile all the steps and get the final .pdf

$ make clean % use this if you want to clear all the files created by $ make

__Method 2: # Compile by steps #__

$ pdflatex assignment1.tex

$ pdflatex assignment1.tex

$ bibtex assignment1 

$ pdflatex assignment1.tex
