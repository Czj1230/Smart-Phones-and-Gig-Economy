
import requests

# most visited ten countries : https://www.worldatlas.com/articles/10-most-visited-countries-in-the-world.html


# list vehicles request

from datetime import datetime
from datetime import timedelta
import zlib

url = "https://api.turo.com/api/listings/977522/additional_features"
app = 'Turo'

payload={}
headers = {
  'tracestate': '@nr=0-2-3069551-857489947-cc0fb95cd2ce416c----1659536708581',
  'newrelic': 'eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IjMwNjk1NTEiLCJkLmFwIjoiODU3NDg5OTQ3IiwiZC50ciI6Ijg1MjMzMGJjY2UzYjRlNzY4M2ZlZmVhZDZiZjcwNzA2IiwiZC5pZCI6ImNjMGZiOTVjZDJjZTQxNmMiLCJkLnRpIjoxNjU5NTM2NzA4NTgxfX0=',
  'traceparent': '00-852330bcce3b4e7683fefead6bf70706-cc0fb95cd2ce416c-00',
  'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N976N Build/QP1A.190711.020)Turo/22.25.0',
  'x-mobile_carrier_country': 'US',
  'accept-language': 'en-US',
  'referer': 'android-app://com.turo.feature.featuresandbadges.presentation.featuresandbadgesfragment',
  'client-capabilities': 'ANDROID_PAY',
  'x-require-non-null-response': 'true',
  'authorization': 'Bearer 3027a370-1b5e-46f2-97e0-33b106ba0a05',
  'accept-encoding': 'gzip',
  'cookie': 'td_dv_mf=samsung; td_dv_mo=SM-N976N; __cf_bm=BUcND5UPzIYUK.i1iMczoAOfRLtUIUVBBRlYQSKuB.I-1659536168-0-AbMpJ5fp3bZgur0WtsCVWV3vKWEwniAyiHAUSbFKEllQufYWnIaOKACbEMedbfIhHhlLJvW4Tre3OAYeMUxEvbPSO1Cmr3gkBqDF1UsgTWC2; td_dv_uid=ffe19848-4a76-4fd5-bc41-62c4b8aff13f; preferredLocale=en_US; sid=fKf6g9jQTpyU855V0SBihw; rr_u_cid=ffe19848-4a76-4fd5-bc41-62c4b8aff13f; preferredLocale=en_US; sid=fKf6g9jQTpyU855V0SBihw',
  'x-newrelic-id': 'VwYBWFNWCRAIUVZWDwgOUlM='
}

carIdList = []
fx = open('carIdListFile','r')
content = fx.read()
fx.close()
print(len(content))
content = content[1:len(content)-1]
print(content)
content = content.split(',')
for carId in content:
  carIdList.append(carId)

for carID in carIdList:
    url = "https://api.turo.com/api/listings/TB1/additional_features"
    
    # replace driver ID
    url = url.replace('TB1',str(carID))
    print(url)

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    content = zlib.compress(response.text.encode())

    


    print(len(content))

    fx = open('VehicleFeatures/'+"carID~"+str(carID)+"~"+app,'wb')
    fx.write(content)
    fx.close()

    print("done!")

    
            
        
    



