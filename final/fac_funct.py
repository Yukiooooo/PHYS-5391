#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:18:28 2020
These are functions for compiling j.exe
@author: Yu Hong
"""
#%% import modules
import numpy as np
import netCDF4 as nc
import datetime
#%% 
def read_ampfac(filename):
    """
    This is used for reading AMPERE FAC netCDF files
    """
    ds = nc.Dataset(filename) # read the netCDF data file
    print (ds); print(ds.dimensions) # print important file info
    # read variables inside the netCDF data file
    for var in ds.variables.values(): # define the variables with their 'name'
        nlat = ds['nlat'][:]; nlon = ds['nlon'][:] # nlat & nlon
        start_yr = ds['start_yr'][:]; end_yr = ds['end_yr'][:] # start/end year
        start_mo = ds['start_mo'][:]; end_mo = ds['end_mo'][:] # start/end month
        start_dy = ds['start_dy'][:]; end_dy = ds['end_dy'][:] # start/end day
        start_mt = ds['start_mt'][:]; end_mt = ds['end_mt'][:] # start/end hour
        start_hr = ds['start_hr'][:]; end_hr = ds['end_hr'][:] # start/end minute
        start_sc = ds['start_sc'][:]; end_sc = ds['end_sc'][:] # start/end second
        # calculate string for start time and end time with datetime module
        ds_time_st = str(datetime.datetime(start_yr,start_mo,start_dy,start_hr,start_mt,start_sc))
        ds_time_ed = str(datetime.datetime(end_yr,end_mo,end_dy,end_hr,end_mt,end_sc))
        # get the position info of the netCDF FAC data
        colat = np.array(ds['colat'][:]); mlt = np.array(ds['mlt'][:]); lat = 90-colat
        J = np.array(ds['Jr'][:]); dJ = ds['dJr'][:] # get FAC and dFAC seems always zero
    
    return J, dJ, colat, mlt, lat, ds_time_st, ds_time_ed, nlat, nlon, start_yr, \
    start_mo, start_dy, start_hr, start_mt, start_sc # return variables needed
    
#%%
def build_polar(mlt,colat,J):
    """
    This is used to rebuild the FAC data into a polar structure
    """
    # define the parameters: num of lats & lts
    nlat = 50; nlt = 24
    fac_add = np.zeros((nlt+1,40)) # create a zeros arry for |lat|<40 deg
    theta = (mlt.reshape(nlt,nlat))*(np.pi/12) # get the polar coordinate theta
    radiu = colat.reshape(nlt,nlat) # get the polar coordinate radiu
    # reshape the FAC into mlt*mlat coordinate
    Jr = J.reshape(nlt,nlat)
    # get new shape of theta within degree 360=0 
    theta_add = theta[0]+2*np.pi 
    theta = np.vstack((theta,theta_add)) # get the theta in polar coordinate     
    radiu = np.vstack((radiu,radiu[0])) # get the radiu in polar coordinate
    # get new shape of FAC within degree 360=0
    Jr_add = (Jr[0]+Jr[23])/2 # use the average value
    Jr = np.vstack((Jr,Jr_add)) # get the FAC in polar coordinate
    
    return Jr, theta, radiu, fac_add # return variables needed


#%% 
def fac_ave(Jr,sJr,fac_add):
    """
    This is used for calculating the average J between NH and SH
    """
    fac_ave = (Jr + sJr)/2 # calculate NH-SH average
    fac_nh = np.hstack((Jr,fac_add)) # create new FAC at NH
    fac_sh = np.hstack((sJr,fac_add)) # create new FAC at SH
    fac_tot = np.hstack((fac_ave,fac_add)) # create new global FAC 
    
    return fac_nh, fac_sh, fac_tot # return FAC at NH, SH and global
    
    
    
    