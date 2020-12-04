# This is the work space for Substorms Substorms Everywhere

## Introduction to each file
**spider.py** % the python code for downloading IMF files

**sciprog.py** % the source code for reading IMF files

**msm.py** % the python script for MSM model: find substorms

**msm_eva.py** % the python code for analyzing the substorm results


## How to compile these files
Please download all the stuffs in this folder or clone my repository in command line via: 

$ git clone https://github.com/Yukiooooo/PHYS-5391.git

All the following steps can be achieved in command line:

__Step 0: # adding execute permission #__

You can compile all the python codes through: 

$ python xxx.py

Also, you can add permission and run them as scripts via:

$ chmod +x xxx.py

$ ./xxx.py

__Step 1: # downloading IMF files #__

$ ./spider.py



$ make clean % use this if you want to clear all the files created by $ make

__Method 2: # Compile by steps #__

$ pdflatex assignment1.tex

$ pdflatex assignment1.tex

$ bibtex assignment1 

$ pdflatex assignment1.tex
