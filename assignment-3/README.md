# This is the introduction for my assignment 3. 

## Introduction to each file
**hw-3.tex** % this is the source code of LaTex

**imf_dst.png** % the figure will be found in the same path of the python code and then to be inserted into the LaTex

**sciprog.py** % this is the python module used for reading IMF data files

**my_plot.py** % this is the python code used for plotting IMF & solar wind and Dst index 

**Dst_July2000.dat** % this is the Dst data to be used 

**imf_jul15_2000.dat.dat** % this is the IMF & solar wind data to be used 

## How to compile these files
Please download all the stuffs in this folder or clone with your command 
$ git clone "links"

If you use the command line, compile the Latex code with 

$ pdflatex hw-3.tex

In order to compile the python code, please use Spyder. If you use the command line, please choose python (not ipython), 
remember to put the sciprog.py file in the same path with my_plot.py

$ python my_plot.py
