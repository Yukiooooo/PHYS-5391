#!/usr/bin/env python

import urllib.request# url request module
import re            # regular expression module
import os            # global dirs module
import time          # time module
'''
This is the python code used for getting info
from our interested website and downloading 
'''
def IMF_Download(url,pattern,Directory):
    
    # Get info from our website 
    response = urllib.request.build_opener()
    
    # Get web content
    content = response.open(url).read().decode('utf8')
    
    # Select keyword 'pattern' from content
    filelist = re.findall(pattern, content, 0)
    
    # Eliminates duplicate elements
    hset = set(filelist)
         
    # Download link
    for href in hset:
        # 'if else' is used to distinguish the special case of only one link
        if(len(hset)>1):
            link = url + href[0] # get the downloading links for each data
            filename = os.path.join(Directory, href[0]) # creating filename & path
            print("==> Downloading",filename)
            urllib.request.urlretrieve(link, filename) # downloading data to local with filename
            print("==> Succeed！")
        else: # used for the case of only one link
            link = url + href # get the downloading links for all data
            filename = os.path.join(Directory, href) # creating filename & path
            print("==> Downloading",filename)
            urllib.request.urlretrieve(link, filename) # downloading data to local with filename
            print("==> Succeed！")
            
        # Setting sleep time, anti-reptile
        time.sleep(1)

# Now, we download IMF files from the 'links' in year of '2003' and 
# store them in the 'imf_data' folder inside the current directory
IMF_Download('http://www-personal.umich.edu/~dwelling/imf_2003/', # our link
              '(imf2003(\d*).dat)', # our downloading keywords
             './imf_data/') # our folder used for storing the data
