
# This is an implementation of the Weasel Program written in python. #

## Introduction to each file
**assignment1.tex** % this is the source code of LaTex

**assignment1.bib** % this is the source code of BibTex

**Makefile** % this is the Makefile for compiling the above two codes

**rick-morty.png** % this is the figure to be inserted into the LaTex code and final .pdf

**arrow.py** % this is the python code to be inserted into the final .pdf

## How to compile these files
Please download all the stuffs in this folder or clone with your command 
$ git clone "links"

If you use the command line, there are two basic ways to complete my codes.

__Method 1: # using Makefile #__

$ make % very straightforward to compile all the steps and get the final .pdf

$ make clean % use this if you want to clear all the files created by $ make

__Method 2: # Compile by steps #__

$ pdflatex assignment1.tex

$ pdflatex assignment1.tex

$ bibtex assignment1 

$ pdflatex assignment1.tex

License.
GNU GPL; see LICENSE.txt for more information

Installation.
None needed

About.
An implementation of the Weasel Program written in python.
Demonstrates that the process of evolutionary systems, random variation combined with non-random cumulative selection, is different from pure chance.
Usage.
python weasel.py <mutation probability>
<mutation probability> is optional; no argument => default of 1/2000
then enter y or n to use locking
System Requirements.
python 3.x.
