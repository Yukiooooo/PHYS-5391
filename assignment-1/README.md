# This is a Latex template for my future write-ups. 

## Introduction to each file
**assignment1.tex** % this is the source code of LaTex

**assignment1.bib** % this is the source code of BibTex

**Makefile** % this is the Makefile for compiling the above two codes

**rick-morty.png** % this is the figure to be inserted into the LaTex code and final .pdf

**arrow.py** % this is the python code to be inserted into the final .pdf

## How to compile these files
Please download all the stuffs in this folder or use your command and type:
$ git clone 

If you use the command line, there are two basic ways to complete the .tex code.

_Method 1: # using Makefile #_
$ make % 

_Method 2: # Compile by steps #

$ pdflatex assignment1.tex

$ pdflatex assignment1.tex

$ bibtex assignment1 

$ pdflatex assignment1.tex
