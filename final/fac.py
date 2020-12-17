#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:59:06 2020
THIS is used for processing FACs data from AMPERE
@author: Yu Hong
"""
from argparse import ArgumentParser # argparse module handles input arguments 
parser = ArgumentParser(description=__doc__) # docstring as our help message. 
parser.add_argument('-hemi', help='which hemisphere: N, S, g',
                    type=str) # select hemisphere you want: N, S, global mean
args = parser.parse_args() # get args from caller
#%% start by importing
import matplotlib.pyplot as plt # module for plotting
from fac_funct import read_ampfac, build_polar, fac_ave # module for processing FAC
from plot_funct import plot_fac, plot_colorbar, plot_info # module for plotting FAC
#%% imput data files ==> start with we already downloaded
file = './data/20130317.1000.3600.3600.north.grd.ncdf' # FAC at NH
sfile = './data/20130317.1000.3600.3600.south.grd.ncdf' # FAC at SH

#%% read FAC netCDF data with our module
ds = read_ampfac(file); sds = read_ampfac(sfile) # read FAC in NH & SH
print (ds) # print important data info
J = ds[0]; sJ = sds[0] # get the FAC data in NH & SH
mlt = ds[3]; colat = ds[2]; ds_time_st = ds[5]; ds_time_ed = ds[6] # other variables

#%% build the FAC data in polar coordinate
j_nh = build_polar(mlt,colat,J) # build for NH
j_sh = build_polar(mlt,colat,sJ) # build for SH
Jr = j_nh[0]; sJr = j_sh[0] # get the new FAC in NH & SH
theta = j_nh[1]; radiu = j_nh[2]; fac_add = j_nh[3] # other variables

#%% build the new FAC structure for GITM grids
fac = fac_ave(Jr,sJr,fac_add)
fac_nh = fac[0]; fac_sh = fac[1]; fac_tot = fac[2] # get new FAC in NH, SN and global

#%%  this part is used for plotting the FAC figures basically
figure = plot_fac(theta,radiu,Jr,sJr) # plot with our function
fig = figure[0]; ax0 = figure[1]; ax1 = figure[2] # get fig & axis info 
cnt0 = figure[3]; cnt1 = figure[4] # get subplot info

#%% this part is used for plotting colorbar
cbmin=-4; cbmax=4.1; step = 1; ylim = 50; start_ms = 0 # define needed parameters
xshift = -0.135; yshift = -0.135; width = 0.5 # define needed parameters
cb = plot_colorbar(fig,ax0,cnt0,xshift,yshift,width,cbmin,cbmax,step) # plot cb
cb.set_label(r'($\mu$A $\bullet$ m$^{-2}$)',fontsize=11.5) # add label to cb

#%% this part is used for add info to our subplots
for ax in [ax0,ax1]: # add for our subplots
    plot_info(ax) # add info to our plot
plt.savefig("FAC-2013031710.png") # save the output figure

#%% output data into txt files
data_file=open("./fac_2013031710.txt",'w') # name the output file and add header
data_file.write('AMPERE FAC AACGM'+'\n'+ds_time_st+' to '+ds_time_ed+'\n'+'\n'+\
                'yr mo dy hr mn sc ms mlt lat fac_n fac_s'+'\n'+'#START'+'\n')                  
for ii, data in enumerate(mlt.T): # write with loop
    if ii < 0:
        continue
    # write YYYY-MM-DD HH-MM-SS FAC in NH & SH info into the outputfile for further uses    
    data_file.write('%3d%2d%3d%3d%3d%3d%3d%3.0f%6.1f%6.2f%6.2f' %(ds[9],ds[10],ds[11],\
                    ds[12],ds[13],ds[14],start_ms,mlt.T[ii],ds[4].T[ii],J.T[ii],sJ.T[ii]) + '\n')    
data_file.close() # close the output file when finished

#%% output data into a txt file
data_file=open("./fac_2013031710_2d.txt",'w') # name the output file and add header
data_file.write('AMPERE FAC AACGM'+'\n'+ds_time_st+' to '+ds_time_ed+'\n'+'\n'+\
                'mlt = 25; mlat = 90'+'\n'+'#START'+'\n')           
for ii in range(len(fac_tot)): # select hemispheres 
    if args.hemi == 'N': # northern hemisphere
        fac_ut = fac_nh[ii] # write with loop
    elif args.hemi == 'S': # northern hemisphere
        fac_ut = fac_sh[ii]# assignment our array
    else: # global average
        fac_ut = fac_tot[ii] # assignment our array
    for jj, j_fac in enumerate(fac_ut): # write with loop
        if jj <0:
            continue
    # write the new struture into a txt file for GITM grids interface  
    data_file.write('%7.2f'*90 %(fac_ut[0],fac_ut[1],fac_ut[2],fac_ut[3],fac_ut[4]\
                    ,fac_ut[5],fac_ut[6],fac_ut[7],fac_ut[8],fac_ut[9],fac_ut[10] \
                    ,fac_ut[11],fac_ut[12],fac_ut[13],fac_ut[14],fac_ut[15],fac_ut[16] \
                    ,fac_ut[17],fac_ut[18],fac_ut[19],fac_ut[20],fac_ut[21],fac_ut[22] \
                    ,fac_ut[23],fac_ut[24],fac_ut[25],fac_ut[26],fac_ut[27],fac_ut[28] \
                    ,fac_ut[29],fac_ut[30],fac_ut[31],fac_ut[32],fac_ut[33],fac_ut[34] \
                    ,fac_ut[35],fac_ut[36],fac_ut[37],fac_ut[38],fac_ut[39],fac_ut[40] \
                    ,fac_ut[41],fac_ut[42],fac_ut[43],fac_ut[44],fac_ut[45],fac_ut[46] \
                    ,fac_ut[47],fac_ut[48],fac_ut[49],fac_ut[50],fac_ut[51],fac_ut[52] \
                    ,fac_ut[53],fac_ut[54],fac_ut[55],fac_ut[56],fac_ut[57],fac_ut[58] \
                    ,fac_ut[59],fac_ut[60],fac_ut[61],fac_ut[62],fac_ut[63],fac_ut[64] \
                    ,fac_ut[65],fac_ut[66],fac_ut[67],fac_ut[68],fac_ut[69],fac_ut[70] \
                    ,fac_ut[71],fac_ut[72],fac_ut[73],fac_ut[74],fac_ut[75],fac_ut[76] \
                    ,fac_ut[77],fac_ut[78],fac_ut[79],fac_ut[80],fac_ut[81],fac_ut[82] \
                    ,fac_ut[83],fac_ut[84],fac_ut[85],fac_ut[86],fac_ut[87],fac_ut[88] \
                    ,fac_ut[89]) + '\n') 
            
data_file.close() # close the output file when finished


