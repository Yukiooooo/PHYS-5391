# This is the work space for homework-5: Substorms Substorms Everywhere

## Introduction to each file
**spider.py** % the python code for downloading imf files

**assignment1.bib** % this is the source code of BibTex

**Makefile** % this is the Makefile for compiling the above two codes

**rick-morty.png** % this is the figure to be inserted into the LaTex code and final .pdf

**arrow.py** % this is the python code to be inserted into the final .pdf

## How to compile these files
Please download all the stuffs in this folder or clone with your command 
$ git clone "links"

$ python spider.py or 
$ chmod +x spider.py
$ ./spider.py

If you use the command line, there are two basic ways to complete my codes.

__Method 1: # using Makefile #__

$ make % very straightforward to compile all the steps and get the final .pdf

$ make clean % use this if you want to clear all the files created by $ make

__Method 2: # Compile by steps #__

$ pdflatex assignment1.tex

$ pdflatex assignment1.tex

$ bibtex assignment1 

$ pdflatex assignment1.tex
