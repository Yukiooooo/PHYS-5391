#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sep 24 2020  This code is for two tasks:
(1) read the IMF/SW data files with the sciprog module
to use, put this file in a path where Python can find it.  

(2) read the Dst data files and convert into 1-D array, data format:
    http://wdc.kugi.kyoto-u.ac.jp/dstae/format/dstformat.html
    
@author: Yu Hong @ UT Alington
"""

#%% import modules used in this code; Do this first
import numpy as np # module for data analysis
import datetime as dt # module for datetime convert
import sciprog # module for read IMF files ==> from Dr. Daniel

# # =============================================================================
# # This part is used for the IMF & SW data file processing
# # =============================================================================
# #%% read files with the ImfData module
# print ("==> Reading the Dst data now ...",'\n')
# imf = sciprog.ImfData('./imf_aug2005.dat')

# # determine the variables in this data file
# Bx = imf['bx']; By = imf['by'];  Bz = imf['bz'];
# Vx = imf['vx']; Vy = imf['vy'];  Vz = imf['vz'];
# Rho = imf['rho']; Temp = imf['temp']; Time = imf['time']

# # calculate |B| & |V| with the class method from "sciprog"
# B = imf.calc_b()
# V = imf.calc_v()

# #%% print the temporal average of |B| & |V| with numpy.mean function
# print ("================= Basic Info ===================")
# print ('the temporal average of |B|: ', np.mean(B))
# print ('the temporal average of |V|: ',np.mean(V))
# print ("================================================")

# #%% write the data into a new file
# data_file = open('./my_imf_aug2005.txt','w') # open a new txt file with mode "write""

# # write the file header
# data_file.write('\n' + 'OMNI IMF & Solar Wind'+'\n'+'\n'+str(Time[0])+' to '+str(Time[-1])+'\n'+'\n'+\
#                     'year mo dy hr mn sc   bx    by    bz   |b|     vx       vy     vz     |v|' + '\n')

# # write the output data with for loop
# for ii, mf in enumerate(B): # ii is the lines of the data 
#     if ii < 0:
#         continue   
#     # write data with datatypes
#     data_file.write('%s' %Time[ii] + '%6.2f'*4 %(Bx[ii],By[ii],Bz[ii],mf) + \
#                     '%8.2f'*4 %(Vx[ii],Vy[ii],Vz[ii],V[ii]) + '\n') 
# data_file.close() # close the data file 

# print ('File writing completed ==> 100%')


# =============================================================================
# This part is used for the Dst data file processing
# =============================================================================
#%% read the full content into a "list", then we can use indices i.e.,list[i]
dst_list = open("./Dst_July2000.dat", "r").readlines()
print ("Reading the Dst data now ...")

#%% claim the parameters used in this code
day = len(dst_list); hour = 24

print ("==> Lines in this file:",len(dst_list),'\n')

points = day*hour # calculate the size of the 1-D array
# set-up a array structure to store the Dst data
dsts = np.zeros((points,1))

# get the time info from the Dst data format
epo_srt = dst_list[0][14:16]; epo_end = dst_list[day-1][14:16] # starting & ending centuries
year_srt = dst_list[0][3:5]; year_end = dst_list[day-1][3:5] # starting & ending years
mth_srt = dst_list[0][5:7]; mth_end = dst_list[day-1][5:7] # starting & ending months
day_srt = dst_list[0][8:10]; day_end = dst_list[day-1][8:10] # starting & ending days

# the complete starting & ending date info 
date_srt = str(epo_srt) + str(year_srt) + '-' + str(mth_srt) + '-' + str(day_srt)
date_end = str(epo_end) + str(year_end) + '-' + str(mth_end) + '-' + str(day_end)

#%% Method-1: read all the Dst data into a day*hour array structure
# set-up a days*hours dimensional array structure
dst_arr = np.zeros((day,hour))

# write the output data with for loop
for iday in range(day): # lines in the file
    for ihr in range(hour): # columns in the file
        
        # write the corresponing data into the days*hours array
        dst_arr[iday][ihr] = dst_list[iday][ihr*4+20:ihr*4+24]
        # get the finally 1-D Dst array with numpy.reshape 
        dsts0 = np.reshape(dst_arr,(points,1))

#%% Method-2: read all the Dst data directly into the 1-D array structure
for iday in range(day): # lines of original Dst data 
    for ihr in range(hour): # columns of the original Dst data
        # write the corresponing data into the 1-D array
        dsts[iday*24+ihr] = dst_list[iday][ihr*4+20:ihr*4+24]

#%% This part is used for exploring the data with numpy
print ('==> Basic info of the Dst data:','\n')

# set-up a new data structure of the calculated Dst values
dsts_info = np.zeros((day,5))

# calculate the basic values of Dst 
dst_min = np.around(np.min(dsts),decimals=0) # minimum
dst_max = np.around(np.max(dsts),decimals=0) # maximum
dst_ave = np.around(np.mean(dsts),decimals=0) # average
dst_med = np.around(np.median(dsts),decimals=0) # median
dst_std = np.around(np.std(dsts),decimals=0) # standard deviation
        
print ("The maximum of the total Dst is:", dst_max,' nT')
print ("The minimum of the total Dst is:", dst_min,' nT')
print ("The average of the total Dst is:", dst_ave,' nT')
print ("The median of the total Dst is:", dst_med,' nT')
print ("The standard deviation of the total Dst is:", dst_std,' nT')
print ("==================================================",'\n')

# Or may the daily min-, max-, etc are also helpful
dst_dayily_min = np.min(dst_arr,axis=1)
dst_dayily_max = np.max(dst_arr,axis=1)
dst_dayily_ave = np.mean(dst_arr,axis=1)
dst_dayily_med = np.median(dst_arr,axis=1)
dst_dayily_std = np.std(dst_arr,axis=1)



















