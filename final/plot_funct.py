#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:18:28 2020
These are functions for plotting figure and colorbar
@author: Yu Hong
"""
#%% import modules
import numpy as np
import matplotlib.pyplot as plt

#%% 
def plot_fac(theta,radiu,Jr,sJr):
    """
    Plot the AMPERE FAC result in the polar coordinate
    """
    # create a figure object and set spacing
    fig, ((ax0,ax1)) = plt.subplots(1,2,figsize=(9,6)) 
    plt.subplots_adjust(wspace=0.55, hspace =0.1)    
    # define the axis limitation parameter
    ylim = 50
    # set the region of the color contour 
    level0 = np.linspace(-4.0,4.0)    
    # add subplots to the figure object
    ax0 = plt.subplot(121,polar=True)
    ax1 = plt.subplot(122,polar=True)   
    # plot the NH and SH FAC
    cnt0 = ax0.contourf(theta+0.5*np.pi-12*(np.pi/12),radiu,Jr,61,levels=level0,cmap="bwr") 
    cnt1 = ax1.contourf(theta+0.5*np.pi-12*(np.pi/12),radiu,sJr[::-1,:],61,levels=level0,cmap="bwr")     
    # plot the y-axis labels
    ax0.set_ylabel(r'Northern Hemisphere',fontsize=13.5,color='black',labelpad=28.5)
    ax1.set_ylabel(r'Southern Hemisphere',fontsize=13.5,color='black',labelpad=28.5)    
    # add text for subplots
    ax0.text(-73,82,"(a)",size=12,color="red")
    ax1.text(-73,82,"(b)",size=12,color="red")   
    # add text for the figure as the title
    ax0.text(np.pi/2,ylim+26,r'             AMPERE derived FACs, Sun, 17 Mar 2013,',fontsize=14,va='center',ha='center') 
    ax1.text(np.pi/2,ylim+26,'10:00:00 GMT to 10:10:00 GMT        ',fontsize=14,va='center',ha='center') 
    
    return fig, ax0, ax1, cnt0, cnt1
    
#%%
def plot_colorbar(fig,ax,cnt,xshift,yshift,width,cbmin,cbmax,step):
    """
    This is used for plotting colorbar for our FAC figure
    """    
    # get the position info of our plot
    pos=ax.get_position()
    cbx = pos.x1+xshift # adjust with x position
    cby = pos.y0+yshift # adjust with y position
    # set the colorbar position with related to the figure
    cbar_ax = fig.add_axes([cbx,cby,width,pos.height/18])
    # plot the colorbar
    cb = fig.colorbar(cnt,cax=cbar_ax,orientation="horizontal")
    # set colorbar region with min & max & step
    cbticks=np.arange(cbmin,cbmax,step); cb.set_ticks(cbticks)
    
    return cb # return the colorbar

#%%
def plot_info(ax):
    """
    This funct is used for adding info for our plot
    """    
    ax.set_yticklabels(('80','70','60','50','40'),fontsize=11.2)  # add y-axis labels
    ax.set_xticklabels(('06',' ','12',' ','18', ' ','00'),fontsize=12)  # add x-axis labels    
    # define the axis limitation parameter
    ylim = 50; ax.set_ylim(0,50) # set y-axis limit
    # add text for the y-axis label
    ax.text(np.pi/5,ylim+13,'LAT',fontsize=13.5,va='center',ha='center')
    # add grids for the plot
    ax.grid(True, linestyle="-",color="k",linewidth="0.5")
    # set axis tick color
    ax.tick_params(axis='y', colors='k')
    # set x-axis label
    ax.set_xlabel('MLT',fontsize=13.5)
    
    
    
    
    