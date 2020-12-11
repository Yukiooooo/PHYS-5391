#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 03:44:28 2020

@author: Yu Hong
"""
# The argparse module handles input arguments from the unix shell
# command line interface.  We'll cover this more during our
# scripting section.
from argparse import ArgumentParser

# Handle all arguments first before performing the rest
# of the script.  Start by creating the parser object and using the
# docstring as our help message. 
parser = ArgumentParser(description=__doc__)

# Now, for our argument/option, add it to the parser and add help info.
# read the substorm output file created from the MSM 
parser.add_argument('substorm_filename', help='The name of the substorm output file to read.',
                    type=str)

# Get args from caller, collect arguments into a convenient object:
args = parser.parse_args()

# Now begin the rest of our script.
# Import shit.  I needed a lot of shit this time.  
import numpy as np # use the array module
import matplotlib.pyplot as plt # use the matplot module
from matplotlib.pyplot import MultipleLocator # Used to set graphic details

#%% read the full content into a "list", then we can use indices i.e.,list[i]
data = open(args.substorm_filename, "r").readlines()
print ("Reading the Substorm data now ...")
print ("==> Total Substorms find:",len(data),'\n')

# build a array structure for storing the substorm info
substorm = np.zeros((len(data),6))

# get the date-time info from the substorm list
for i in range(len(substorm)):
    substorm[i][0] = data[i][0:4] # year
    substorm[i][1] = data[i][5:7] # month 
    substorm[i][2] = data[i][8:10] # day
    substorm[i][3] = data[i][11:13] # hour
    substorm[i][4] = data[i][14:16] # minute
    substorm[i][5] = data[i][17:19] # second
    
    # separate substorms into different seasons
    eqn = [(substorm[:,1]==3)|(substorm[:,1]==4)|(substorm[:,1]==9)|(substorm[:,1]==10)]
    equinox = substorm[eqn] # substorms in Equinox
    
    smr = [(substorm[:,1]<=8) & (substorm[:,1]>=5)]
    summer = substorm[smr] # substorms in Summer
    
    wnt = [(substorm[:,1]<=2)|(substorm[:,1]>=11)]
    winter = substorm[wnt] # substorms in Winter
    
    
#%% this part is used for plotting our substorm results
# Draw a fan-shaped distribution chart
labes=['Equinox','Summer','Winter'] # set labes for our figure

pe = (100*len(equinox)/len(data)); # occurrence % in Equinox
ps = (100*len(summer)/len(data)); # occurrence % in Summer
pw = (100*len(winter)/len(data)); # occurrence % in Winter

fracs=[pe,ps,pw] # get fractions for plotting
explode=[0,0.1,0.05] # set the spacing between pie charts
plt.axes(aspect=1) # set total fraction for plotting

# plot a pie chart according to the parameters set above
plt.pie(x=fracs,labels=labes,autopct="%.0f%%",explode=explode,shadow=True)
# add title for the pie chart figure
plt.title('Seasonal Distribution of Substorms in 2003',fontsize=15,color='b')
# plt.show() 
# save the picture with a name
plt.savefig("seasonal_distribution.png")
    
#%% This is used for plotting the UT-distribution of Substorms
fig, ((ax0,ax1)) = plt.subplots(1,2,figsize=(10,5)) # set the picture layout
plt.subplots_adjust(wspace=0.25, hspace =0.15) # set image spaces

# get plotting parameters: x-axis & y-axis
x = np.arange(0,len(data),1); y = substorm[:,3]
   
ax0.scatter(x,y,alpha=0.6)  # Draw a scatter plot
ax0.set_xlabel('Substorm  in 2003',fontsize=13,color='b') # set x-label
ax0.set_ylabel('Universal  Time (hours)',fontsize=13,color='b') # set y-label
# plt.savefig("UT_distribution.png")

#%% This is used for plotting the time-interval between two substorms
dt = np.diff(substorm[:,3]) # calculate the time-interval between two substorms
x1 = np.arange(0,len(data)-1,1) # get the new x-axis parameter

for j in range(len(dt)): # if new day then dt plus 24 hours
    if dt[j] < 0: # if new day
        dt[j] = dt[j] + 24 # dt plus 24 hours
    
ax1.scatter(x1,dt,alpha=0.6,marker = '*',c='green') # Draw a scatter plot
ax1.set_xlabel('Substorm  in 2003',fontsize=13,color='b') # set x-label
ax1.set_ylabel('Time Interval (hours)',fontsize=13,color='b') # set y-label

x_major_locator = MultipleLocator(len(data)/6) # set the x-axis spacing
y_major_locator = MultipleLocator(4) # set the y-axis spacing

for ax in [ax0,ax1]: # set two axes at the same time
    ax.set_ylim(0,24) # set y-axes limit
    ax.yaxis.set_major_locator(y_major_locator) # set y-axes spacing
    ax.set_xlim(0,len(data)) # set y-axes limit
    ax.xaxis.set_major_locator(x_major_locator) # set x-axes spacing

#plt.show() 
# save the picture with a name
plt.savefig("Time Interval.png") 
    
    
   
    
    
    
    
