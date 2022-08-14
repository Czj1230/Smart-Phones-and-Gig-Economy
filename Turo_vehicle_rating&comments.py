import requests

# most visited ten countries : https://www.worldatlas.com/articles/10-most-visited-countries-in-the-world.html


# list vehicles request

from datetime import datetime
from datetime import timedelta
import zlib


listVehicleUrl = "https://api.turo.com/api/vehicle/reviews?vehicleId=977522&page=1"
dateFormat = "%Y-%m-%d %H:%M:%S"


app = 'Turo'


payload={}
headers = {
  'newrelic': 'eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IjMwNjk1NTEiLCJkLmFwIjoiODU3NDg5OTQ3IiwiZC50ciI6IjViZTBiNDhjOTMyNzRlNzE5NTljMjcxOTFhMGM5YTBmIiwiZC5pZCI6IjY1OGQzNzA0MzE2YjRiZDMiLCJkLnRpIjoxNjU5NTM2MjEyMTg3fX0=',
  'traceparent': '00-5be0b48c93274e71959c27191a0c9a0f-658d3704316b4bd3-00',
  'tracestate': '@nr=0-2-3069551-857489947-658d3704316b4bd3----1659536212187',
  'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N976N Build/QP1A.190711.020)Turo/22.25.0',
  'x-mobile_carrier_country': 'US',
  'accept-language': 'en-US',
  'referer': 'android-app://com.turo.feature.vehiclereviews.presentation.vehiclereviewsfragment',
  'client-capabilities': 'ANDROID_PAY',
  'x-require-non-null-response': 'true',
  'authorization': 'Bearer 3027a370-1b5e-46f2-97e0-33b106ba0a05',
  'accept-encoding': 'gzip',
  'cookie': 'td_dv_mf=samsung; td_dv_mo=SM-N976N; __cf_bm=BUcND5UPzIYUK.i1iMczoAOfRLtUIUVBBRlYQSKuB.I-1659536168-0-AbMpJ5fp3bZgur0WtsCVWV3vKWEwniAyiHAUSbFKEllQufYWnIaOKACbEMedbfIhHhlLJvW4Tre3OAYeMUxEvbPSO1Cmr3gkBqDF1UsgTWC2; td_dv_uid=ffe19848-4a76-4fd5-bc41-62c4b8aff13f; preferredLocale=en_US; sid=fKf6g9jQTpyU855V0SBihw; rr_u_cid=ffe19848-4a76-4fd5-bc41-62c4b8aff13f; __cf_bm=i2p.NUistCuEM9RG.j92FCIhUqQFUdpDP9GpdvdhEAo-1659534738-0-AbedA8OzdOzLyx/W3fLxf+nSWz1Vk972nEzSDXXBVYGc/1yIpvCYRrdVZO9vO1iva+aKB5X7YhwRrXLmJmC3u/6bqimW2GpppLc8sCbUtu2k; preferredLocale=en_US; sid=fKf6g9jQTpyU855V0SBihw',
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

    listVehicleUrl = "https://api.turo.com/api/vehicle/reviews?vehicleId=TB1&page=1"  

    # replace car ID
    listVehicleUrl = listVehicleUrl.replace('TB1',str(carID))


    print(listVehicleUrl)

    response = requests.request("GET", listVehicleUrl, headers=headers, data=payload, verify=False)
    content = zlib.compress(response.text.encode())

    


    print(len(content))

    fx = open('VehicleComments/'+"carID~"+str(carID)+'~'+app,'wb')
    fx.write(content)
    fx.close()

    print("done!")

            
            
        
    



