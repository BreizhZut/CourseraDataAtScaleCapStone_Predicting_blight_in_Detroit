import pandas as pd
import os
import re

import urllib.request, urllib.parse, urllib.error
import json
import ssl
import secret_token as token
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Read the data run projection and rename columns
data_path = "/Users/dtweed/Coursera/DataAtScale/Capstone/Data/"
spider_file = data_path+"blight_incident_count.csv"
blight_gps = pd.read_csv(spider_file)

serviceurl = 'https://data.detroitmi.gov/resource/snut-x2sy.json?'
servicekey = "" # Put your won key here

def grap_gps(line):
    url = serviceurl + urllib.parse.urlencode({'address': line['address'],'$$app_token':token.apptoken})#,"key":servicekey})
    #    url = serviceurl + urllib.parse.urlencode({'address': add_detroit,"key":servicekey})
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    try:
        js = json.loads(data)
    except:
        js = None

#    if not js or 'status' not in js or js['status'] != 'OK' :
    if not js or len(js)<1:
        #print("Failure To Retrieve",url)
        return pd.Series({"long":0.0,"lat":0.0})
#    else:
#        print("Retrieve",url)
#    lat = js["results"][0]["geometry"]["location"]["lat"]
#    lng = js["results"][0]["geometry"]["location"]["lng"]
    lat = js[0]["latitude"]
    lng = js[0]["longitude"]
    return pd.Series({"long":lng,"lat":lat})

missing_gps = blight_gps[["long","lat"]].apply(lambda line: any(line.isnull()),axis=1)
print("Still left", sum(missing_gps))
print(sum(missing_gps),len(missing_gps))
print("Extracting gps")
while(sum(missing_gps)>0):
    spider_gps = blight_gps.loc[missing_gps].head(1000).index
    blight_gps.loc[spider_gps,["long","lat"]] = blight_gps.loc[spider_gps].apply(grap_gps,axis=1)
    blight_gps.to_csv(spider_file,index=False)
    missing_gps = blight_gps[["long","lat"]].apply(lambda line: any(line.isnull()),axis=1)
    print("Still left", sum(missing_gps))
