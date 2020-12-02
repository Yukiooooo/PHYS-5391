#!/usr/bin/env python

import urllib.request# url request
import re            # regular expression
import os            # dirs
import time
'''
url äèçå
pattern æååçåéåéè
Directory äèçå
'''
def BatchDownload(url,pattern,Directory):
    
    # Pull the request and simulate it as a browser -> Skip the anti-crawler mechanism
#    headers = {'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    opener = urllib.request.build_opener()
#    opener.addheaders = [headers]
    
    # èåçéåå
    content = opener.open(url).read().decode('utf8')
    
    # æéæåèèå，äcontentäåéåéèpattern
    raw_hrefs = re.findall(pattern, content, 0)
    
    # setåææééååç
    hset = set(raw_hrefs)
         
    # äèéæ
    for href in hset:
        # äæäif else æääåååæääéæççåæå
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

#BatchDownload('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/',
#              '(Storm-Data-Export-Format.docx)',
#              '/Users/jonas/Desktop/hw-5_script/data_download')
        
#BatchDownload('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/',
#              '(Storm-Data-Export-Format.pdf)',
#              'E:\stormevents\csvfiles')
        
#BatchDownload('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/',
#              '(StormEvents_details-ftp_v1.0_d(\d*)_c(\d*).csv.gz)',
#              'E:\stormevents\csvfiles')
        
#BatchDownload('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/',
#              '(StormEvents_fatalities-ftp_v1.0_d(\d*)_c(\d*).csv.gz)',
#              'E:\stormevents\csvfiles')

#BatchDownload('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/',
#              '(StormEvents_locations-ftp_v1.0_d(\d*)_c(\d*).csv.gz)',
#              '/Users/jonas/Desktop/hw-5_script/data_download')

#BatchDownload('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/legacy/',
#              '(ugc_areas.csv)',
#              'E:\stormevents\csvfiles\legacy')

#BatchDownload('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/',
#              '(ugc_areas.csv)',
#              'E:\stormevents\csvfiles')

BatchDownload('http://www-personal.umich.edu/~dwelling/imf_2003/',
              '(imf2003(\d*).dat)',
              '/Users/jonas/Desktop/hw-5_script/data_download')
