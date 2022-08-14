import requests

# most visited ten countries : https://www.worldatlas.com/articles/10-most-visited-countries-in-the-world.html


# list vehicles request

from datetime import datetime
from datetime import timedelta
import zlib

app = 'Turo'

payload={}
headers = {
  'newrelic': 'eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IjMwNjk1NTEiLCJkLmFwIjoiODU3NDg5OTQ3IiwiZC50ciI6IjRlNWU5OGM2ZjA1ODQxNzZhMTYxMjFmMGVkODI2ZWIwIiwiZC5pZCI6ImRiZGI0NzM4YTFmMjQxNzciLCJkLnRpIjoxNjYwMDYxOTc0NjI4fX0=',
  'tracestate': '@nr=0-2-3069551-857489947-dbdb4738a1f24177----1660061974627',
  'traceparent': '00-4e5e98c6f0584176a16121f0ed826eb0-dbdb4738a1f24177-00',
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
print(content)
content = content.split(', ')
for ownerId in content:
  ownerIdList.append(ownerId)

for driverID in ownerIdList:
    listVehicleUrl = "https://api.turo.com/api/driver/detail?driverId=TB1"
    
    # replace driver ID
    listVehicleUrl = listVehicleUrl.replace('TB1',str(driverID))
    print(listVehicleUrl)

    response = requests.request("GET", listVehicleUrl, headers=headers, data=payload, verify=False)
    content = zlib.compress(response.text.encode())

    


    print(len(content))

    fx = open('CarOwnerProfile/'+"driverID~"+str(driverID)+"~"+app,'wb')
    fx.write(content)
    fx.close()

    print("done!")

    
            
        
    



