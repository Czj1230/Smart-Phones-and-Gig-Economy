import json
import requests

# most visited ten countries : https://www.worldatlas.com/articles/10-most-visited-countries-in-the-world.html


# list vehicles request

from datetime import datetime
from datetime import timedelta
import zlib


listVehicleUrl = "https://api.turo.com/api/vehicle/detail?startDate=08%2F05%2F2022&endDate=08%2F08%2F2022&startTime=10%3A00&endTime=10%3A00&vehicleId=1626157"
dateFormat = "%Y-%m-%d %H:%M:%S"


app = 'Turo'


payload={}
headers = {
  'newrelic': 'eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IjMwNjk1NTEiLCJkLmFwIjoiODU3NDg5OTQ3IiwiZC50ciI6IjE3MzkzZjk1NWRlNzQ4MDhiNjhiM2RmNTM0OWE0ZjFlIiwiZC5pZCI6IjJlNGU0ZjcwM2ZiMDQ2ODkiLCJkLnRpIjoxNjYwMDU2MDU1NDU1fX0=',
  'traceparent': '00-17393f955de74808b68b3df5349a4f1e-2e4e4f703fb04689-00',
  'tracestate': '@nr=0-2-3069551-857489947-2e4e4f703fb04689----1660056055455',
  'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N976N Build/QP1A.190711.020)Turo/22.25.0',
  'x-mobile_carrier_country': 'US',
  'accept-language': 'en-US',
  'referer': 'android-app://com.turo.feature.vehicledetail.vehicledetailfragment',
  'client-capabilities': 'ANDROID_PAY',
  'x-require-non-null-response': 'true',
  'authorization': 'Bearer 6acc0dae-4e3b-4032-b576-722b1a0654b7',
  'accept-encoding': 'gzip',
  'cookie': 'td_dv_mf=samsung; td_dv_mo=SM-N976N; td_dv_uid=ffe19848-4a76-4fd5-bc41-62c4b8aff13f; preferredLocale=en_US; sid=7TZ6QlgpRIWo-G0Kcznqkw; rr_u_cid=ffe19848-4a76-4fd5-bc41-62c4b8aff13f; __cf_bm=y40yrCJtoX7M2FibLLJtgfE.Xg3YLxp2pd5Neihl7qQ-1660054901-0-AZccH6byDwPm/GbZzat56ev+z8+vT9RRbrYAuJZnIxsSUYS06kMyxel5/kgfcNnigwJ8Jv8I6ey8C4udB5F5Il1w/jZnfONhP6vxuUv2YlZt; preferredLocale=en_US; sid=7TZ6QlgpRIWo-G0Kcznqkw',
  'x-newrelic-id': 'VwYBWFNWCRAIUVZWDwgOUlM='
}

carIdList = []
fx = open('carIdListFileofOttawa','r')
content = fx.read()
fx.close()
print(len(content))
content = content[1:len(content)-1]
print(content)
content = content.split(', ')
for carId in content:
  print(carId)
  carIdList.append(carId)
# print(len(carIdList)) 
# print(type(carIdList))           


for carID in carIdList:

    listVehicleUrl = "https://api.turo.com/api/vehicle/detail?startDate=08%2F20%2F2022&endDate=08%2F25%2F2022&startTime=10%3A00&endTime=10%3A00&vehicleId=TB1"  

    # replace car ID
    listVehicleUrl = listVehicleUrl.replace('TB1',str(carID))


    response = requests.request("GET", listVehicleUrl, headers=headers, data=payload, verify=False)
    content = zlib.compress(response.text.encode())



    print(len(content))

    fx = open('DetailsOfVehicles/'+"carID~"+str(carID)+'~'+app,'wb')
    fx.write(content)
    fx.close()

    print("done!")

            
            
        
    



