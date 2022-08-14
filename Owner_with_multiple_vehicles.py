import requests
import json

# most visited ten countries : https://www.worldatlas.com/articles/10-most-visited-countries-in-the-world.html


# list vehicles request

from datetime import datetime
from datetime import timedelta
import zlib

url = "https://api.turo.com/api/drivers/25729598/vehicles"
app = 'Turo'

payload={}
headers = {
  'tracestate': '@nr=0-2-3069551-857489947-f9ef2056e5fd4ec1----1660061974633',
  'traceparent': '00-0a00c8b214384b08adbeb6cde1fdd34e-f9ef2056e5fd4ec1-00',
  'newrelic': 'eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IjMwNjk1NTEiLCJkLmFwIjoiODU3NDg5OTQ3IiwiZC50ciI6IjBhMDBjOGIyMTQzODRiMDhhZGJlYjZjZGUxZmRkMzRlIiwiZC5pZCI6ImY5ZWYyMDU2ZTVmZDRlYzEiLCJkLnRpIjoxNjYwMDYxOTc0NjMzfX0=',
  'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N976N Build/QP1A.190711.020)Turo/22.25.0',
  'x-mobile_carrier_country': 'US',
  'accept-language': 'en-US',
  'referer': 'android-app://com.turo.legacy.ui.activity.viewprofileactivity',
  'client-capabilities': 'ANDROID_PAY',
  'x-require-non-null-response': 'true',
  'authorization': 'Bearer 6acc0dae-4e3b-4032-b576-722b1a0654b7',
  'accept-encoding': 'gzip',
  'cookie': 'td_dv_mf=samsung; td_dv_mo=SM-N976N; td_dv_uid=ffe19848-4a76-4fd5-bc41-62c4b8aff13f; preferredLocale=en_US; sid=Ng09R00CROWA60GPc3IniA; rr_u_cid=ffe19848-4a76-4fd5-bc41-62c4b8aff13f; __cf_bm=Wa5QGmfEiEju5Wlw3rrZDRq2s6qILL_hw.1BNMIqksA-1660062225-0-ATvgNQ0DV5Yev7ssqlT6uuiC5rJPd7VyxqowAM9X0WVtyu1BHVUY2ZfRbhNpaxGgt7W8egJlEdI7Ge/XH3Vwwg07v6ZNRXduCQP03yPibuNm; preferredLocale=en_US; sid=Ng09R00CROWA60GPc3IniA',
  'x-newrelic-id': 'VwYBWFNWCRAIUVZWDwgOUlM='
}
ownerIdList = []
fx = open('ownerIdListFile','r')
content = fx.read()
fx.close()
print(len(content))
content = content[1:len(content)-1]

content = content.split(', ')
for ownerId in content:
  ownerIdList.append(ownerId)

fx = open('ownerCarNumber','w')
for driverID in ownerIdList:
    OwnerCarListUrl = "https://api.turo.com/api/drivers/TB1/vehicles"
    
    # replace driver ID
    OwnerCarListUrl = OwnerCarListUrl.replace('TB1',str(driverID))


    response = requests.request("GET", OwnerCarListUrl, headers=headers, data=payload, verify=False)
    content = json.loads(response.text)


    print(len(content["list"]))
    
    fx.write(str(driverID)+" "+str(len(content["list"]))+"\n")
    

fx.close()
    
            
        
    



