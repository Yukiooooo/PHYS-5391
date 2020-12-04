#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 03:44:28 2020

@author: jonas
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
parser.add_argument('substorm_filename', help='The name of the substorm output file to read.',
                    type=str)

# Get args from caller, collect arguments into a convenient object:
args = parser.parse_args()

# Now begin the rest of our script.
# Import shit.  I needed a lot of shit this time.  
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
from matplotlib import ticker
from matplotlib import rcParams
from matplotlib.pyplot import MultipleLocator

#%% read the full content into a "list", then we can use indices i.e.,list[i]
data = open(args.substorm_filename, "r").readlines()
print ("Reading the Substorm data now ...")
print ("==> Total Substorms find:",len(data),'\n')

# build a array structure for stroing the substorm info
substorm = np.zeros((len(data),6))

# get the date-time info from the substorm list
for i in range(len(substorm)):
    substorm[i][0] = data[i][0:4] # year
    substorm[i][1] = data[i][5:7] # month 
    substorm[i][2] = data[i][8:10] # day
    substorm[i][3] = data[i][11:13] # hour
    substorm[i][4] = data[i][14:16] # minute
    substorm[i][5] = data[i][17:19] # second
    
#    eqn = (substorm[:,1] ==3 or substorm[:,1] == 4 or substorm[:,1] == 9 or substorm[:,1] == 10)

    eqn = [(substorm[:,1]==3)|(substorm[:,1]==4)|(substorm[:,1]==9)|(substorm[:,1]==10)]
    equinox = substorm[eqn]
    
    smr = [(substorm[:,1]<=8) & (substorm[:,1]>=5)]
    summer = substorm[smr]
    
    wnt = [(substorm[:,1]<=2)|(substorm[:,1]>=11)]
    winter = substorm[wnt]
    
    
#%% this used for plotting our substorm results
labes=['Equinox','Summer','Winter']

pe = (100*len(equinox)/len(data));
ps = (100*len(summer)/len(data));
pw = (100*len(winter)/len(data));

fracs=[pe,ps,pw]
explode=[0,0.1,0.05]
#设置x,y轴比例为1：1，从而达到一个正的圆
plt.axes(aspect=1)
#labels标签参数,x是对应的数据列表,autopct显示每一个区域占的比例,explode突出显示某一块,shadow阴影
plt.pie(x=fracs,labels=labes,autopct="%.0f%%",explode=explode,shadow=True)
plt.title('Seasonal Distribution of Substorms in 2003',fontsize=15,color='b')
#plt.show()
plt.savefig("seasonal_distribution.png")
    
# This is used for plotting the UT-distribution of Substorms
fig, ((ax0,ax1)) = plt.subplots(1,2,figsize=(10,5)) 
plt.subplots_adjust(wspace=0.25, hspace =0.15)

x = np.arange(0,len(data),1); y = substorm[:,3]   
ax0.scatter(x,y,alpha=0.6)  
ax0.set_xlabel('Substorm  in 2003',fontsize=13,color='b')
ax0.set_ylabel('Universal  Time',fontsize=13,color='b')
# plt.savefig("UT_distribution.png")


# This is used for plotting the time-interval between two substorms
dt = np.diff(substorm[:,3]); x1 = np.arange(0,len(data)-1,1); 

for j in range(len(dt)):
    if dt[j] < 0:
        dt[j] = dt[j] + 24
    
ax1.scatter(x1,dt,alpha=0.6,marker = '*',c='green')  
ax1.set_xlabel('Substorm  in 2003',fontsize=13,color='b')
ax1.set_ylabel('Time Interval',fontsize=13,color='b')

x_major_locator = MultipleLocator(len(data)/6); 
y_major_locator = MultipleLocator(4); 

for ax in [ax0,ax1]:
    ax.set_ylim(0,24)
    ax.yaxis.set_major_locator(y_major_locator)
    ax.set_xlim(0,len(data))
    ax.xaxis.set_major_locator(x_major_locator)

#plt.show() 
plt.savefig("Time Interval.png") 
    
    
   
    
    
    
    
