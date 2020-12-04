#!/usr/bin/env python

import urllib.request# url request module
import re            # regular expression
import os            # global dirs
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
            link = url + href[0]
            filename = os.path.join(Directory, href[0])
            print("==> Downloading",filename)
            urllib.request.urlretrieve(link, filename)
            print("==> Succeed！")
        else:
            link = url +href
            filename = os.path.join(Directory, href)
            print("==> Downloading",filename)
            urllib.request.urlretrieve(link, filename)
            print("==> Succeed！")
            
        # Setting sleep time, anti-reptile
        time.sleep(1)

# Now, we download IMF files from the 'links' in year of '2003' and 
# store them in the 'imf_data' folder inside the current directory
IMF_Download('http://www-personal.umich.edu/~dwelling/imf_2003/',
              '(imf2003(\d*).dat)',
             './imf_data/')
