# This is the work space for Substorms Substorms Everywhere

## Introduction to each file
**spider.py** % the python code for downloading IMF files

**sciprog.py** % the source code for reading IMF files

**msm.py** % the python script for MSM model: find substorms

**msm_eva.py** % the python code for analyzing the substorm results


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
