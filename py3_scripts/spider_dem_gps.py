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
data_path = "../Processed/"
# This file was previously prepared
dem_gps = pd.read_csv(data_path+"blight_demolition.csv")

# set up the service url and key
serviceurl = 'https://data.detroitmi.gov/resource/snut-x2sy.json?'
servicekey =  "" # put your own key here

def grap_gps(line):
    """
    This method cleans up the address
    """
    add_detroit = line["address"]
    add_detroit = re.sub(" E\.? ","",add_detroit)
    add_detroit = re.sub(" W\.? ","",add_detroit)
    add_detroit = re.sub(" N\.? ","",add_detroit)
    add_detroit = re.sub(" S\.? ","",add_detroit)
    add_detroit = re.sub(" BLVD\.?","",add_detroit)
    add_detroit = re.sub(" AVE\.?","",add_detroit)
    add_detroit = re.sub(" ST\.?","",add_detroit)
    add_detroit = re.sub("-"," ",add_detroit)
    add_detroit = re.sub(" {2,}"," ",add_detroit)

    url = serviceurl + urllib.parse.urlencode({'address': add_detroit,'$$app_token':token.apptoken})
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or len(js)<1:
        print("Failure To Retrieve",url)
        return pd.Series({"long":pd.np.nan,"lat":pd.np.nan})
    else:
        print("Retrieve",url)
    lat = js[0]["latitude"]
    lng = js[0]["longitude"]
    return pd.Series({"long":lng,"lat":lat})

missing_gps = dem_gps[["long","lat"]].apply(lambda line: any(line.isnull()),axis=1)
spider_gps = dem_gps.loc[missing_gps].indexs
print("Extracting gps")
dem_gps.loc[spider_gps,["long","lat"]] = dem_gps.loc[spider_gps].apply(grap_gps,axis=1)
missing_gps = dem_gps[["long","lat"]].apply(lambda line: any(line.isnull()),axis=1)
print(sum(missing_gps))
print(dem_gps.loc[spider_gps].head(100))
dem_gps[["address","date","type","lat","long"]].to_csv(data_path+"blight_demolition.csv",index=False)
