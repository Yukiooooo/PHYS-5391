#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:15:48 2020

@author: Yu Hong
"""
#%% import modules we need in this code
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import sciprog # pls put this module in the same path with this code
# =============================================================================
# #%% this is used for plotting Dst data
# =============================================================================
#%% read the full content into a "list", then we can use indices i.e.,list[i]
dst_list = open("./Dst_July2000.dat", "r").readlines()
print ("Reading the Dst data now ...")

#%% claim the parameters used in this code
day = len(dst_list); 
hour = 24 # the daily data resolution
date = 15 # this is the date we interested 

# set-up a array structure
event_dst = np.zeros((1,hour))

for ihr in range(hour): # columns in the file
    event_dst[:,ihr] = dst_list[date-1][ihr*4+20:ihr*4+24] # put the selected data into our array

# # =============================================================================
# # this is used for plotting IMF & solar wind data
# # =============================================================================
#%% read files with the ImfData module
print ("==> Reading the Dst data now ...",'\n')
imf = sciprog.ImfData('./imf_jul15_2000.dat')

# determine the variables in this data file
Bx = imf['bx']; By = imf['by'];  Bz = imf['bz'];
Vx = imf['vx']; Vy = imf['vy'];  Vz = imf['vz'];
Rho = imf['rho']; Temp = imf['temp']; Time = imf['time']

#%% define the time resolution of IMF & Dst data
time = np.arange(0,len(Bx),1); time2 = np.arange(0,hour,1)

#%% this part is used for plot setting
fig1, (ax0,ax1,ax2,ax3,ax4) = plt.subplots(5,1,figsize=(9,10),sharex=False) # set figure layout
plt.subplots_adjust(wspace=0, hspace=0.06) # set figure layout

n1 = 876; n2 = 1146 # find the position when Bz is negative ==> check the data

#%% setting unit size of the axises
y0_major_locator = MultipleLocator(20); y1_major_locator = MultipleLocator(150)
y2_major_locator = MultipleLocator(8); y3_major_locator = MultipleLocator(0.5)
y4_major_locator = MultipleLocator(100); x0_major_locator = MultipleLocator(4);
    
#%% settings for the figure
ax0.plot(time,By,'b-'); ax0.plot(time,Bz,'r-'); # plot 'By' & 'Bz'
ax0.set_ylim(-59,60,20) # set the y-axis region
ax0.set_ylabel('IMF (nT)',fontsize=12,color="k") # add label to the y-axis
ax0.yaxis.set_major_locator(y0_major_locator); # set the y-axis unit size

ax1.plot(time,Vx,color='purple',linestyle='-'); # plot 'Vx'
ax1.set_ylim(-1199,-600,100); # set the y-axis region
ax1.set_ylabel('Vx (km/s)',fontsize=12,color="k"); # add label to the y-axis
ax1.yaxis.set_major_locator(y1_major_locator) # set the y-axis unit size

ax2.plot(time,Rho,color='limegreen',linestyle='-'); # plot 'rho'
ax2.set_ylim(0,40,100) # set the y-axis region
ax2.set_ylabel(r'$\rho$ (n/cc)',fontsize=12,color="k"); # add label to the y-axis
ax2.yaxis.set_major_locator(y2_major_locator) # set the y-axis unit size

ax3.plot(time,Temp/10**6,color='orange',linestyle='-'); # plot 'temperature'
ax3.set_ylim(0,2.9,100) # set the y-axis region
ax3.set_ylabel(r'Temp (10 $^{6}$ K)',fontsize=12,color="k"); # add label to the y-axis
ax3.yaxis.set_major_locator(y3_major_locator) # set the y-axis unit size

ax4.plot(time2,event_dst.T,color='k',linestyle='-'); # plot 'Dst'
ax4.set_xlim(0,23,4); ax4.set_ylim(-350,50,100) # set the x and y-axis region
ax4.set_ylabel('Dst (nT)',fontsize=12,color="k") # add label to the y-axis
ax4.xaxis.set_major_locator(x0_major_locator); # set the x-axis unit size
ax4.yaxis.set_major_locator(y4_major_locator) # set the y-axis unit size

#%% add info about the axis
ax4.set_xlabel('UT of July 15 2000',fontsize=15,color="k") # add label to the x-axis
ax4.set_xticklabels((' ','00','04','08','12','16','                   20               00')) # add labels to the x-axis

# settings for the axis
for ax in [ax0,ax1,ax2,ax3]:
    ax.set_xlim(0,1440,180) # set the x-axis region
    ax.plot([n1,n1],[-10000,1000],'k--',linewidth=1.5); # plot vertical lines
    ax.plot([n2,n2],[-10000,1000],'k--',linewidth=1.5); # plot vertical lines
    ax.set_xticklabels((' ')) # remove the x-axis labels
ax4.plot([14,14],[-350,50],'k--',linewidth=1.5); # plot vertical lines
ax4.plot([18.3,18.3],[-350,50],'k--',linewidth=1.5); # plot vertical lines
ax4.plot([0,23],[0,0],color='b',linestyle='dashdot',linewidth=1) # plot horizontal lines

#%% add legend to the first panel
ax0.legend(loc='best');  # set the position of the legend
ax0.legend([r'B$_y$',r'B$_z$'],frameon=False) # remove the box of the legend

fig1.savefig('./imf_dst.png')




















