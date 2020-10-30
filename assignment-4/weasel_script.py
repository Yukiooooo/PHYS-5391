#!/usr/bin/env python

"""
This is python script for using "Weasel Program", please put this code with
weasel_pro.py together in the same path, in your command line first do:
    $ python weasel_pro.py
then compile this script in following way:
    $ python weasel_script.py
then enter the desired number of offspring and mutation rate, then "Enter"
==> you'll get the generations required to reach the target string :D     
"""
#%% from our module import the founction
from  weasel_pro import offspring_select

#%% input the number of offspring and mutation rate you want, end with 'enter'
num_child = int(input("please give the offspring numbers: ")) 
mute_rate = float(input("please give the mutation rate [0,1]: "))

# call the founction we defined in weasel_pro.py, and return the generations:
gen = offspring_select("METHINKS IT IS LIKE A WEASEL",num_child,mute_rate) 
print ("generations needed = ", gen) # print the finally generations needed