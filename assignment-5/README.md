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

$ python *.py

Also, you can run them as scripts by adding permission via:

$ chmod +x xxx.py

$ ./*.py

__Step 1: # downloading IMF files #__

First, create a folder in your current directory to store the downloaded IMF files, here we name the folder as 'imf_data'

$ mkdir imf_data

$ ./spider.py

In line-76 of spider.py, you can edit your target links; In line-77 you can change the target data with keywords; In line-78 
you can change the folder name where you want to store the data. 


__Step 2: # finding substorms with MSM #__

$ ./msm.py -h

First, use the above command to check what arguments/options are needed: imffolder ==> ./imf_data; output_file ==> you can
give any name you want; -D ==> here we use 2.69 hr; -N here we use 366, which is the days in a year (you can set -D as 1 for testing)

$ ./msm.py ./imf_data/ output_file.txt -D 2.69 -N 366

__Step 3: # evoluate substorms #__

$./msm_eva.py -h

Similarly, use this command to check what arguments/options are needed. Here, the output_file created in last step needed to be added via:

$ ./msm_eva.py output_file.txt 









$ make clean % use this if you want to clear all the files created by $ make

__Method 2: # Compile by steps #__

$ pdflatex assignment1.tex

$ pdflatex assignment1.tex

$ bibtex assignment1 

$ pdflatex assignment1.tex
