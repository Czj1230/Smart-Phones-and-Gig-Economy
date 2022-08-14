import requests

# most visited ten countries : https://www.worldatlas.com/articles/10-most-visited-countries-in-the-world.html
countriesList = {}
countriesList['United States'] = {}


# 5 most populous cities of each country
#Colorado state
countriesList['United States']['Denver'] = [39.730394, -104.990234]
countriesList['United States']['Bridgeport'] = [41.175370, -73.190236]



# list vehicles request

from datetime import datetime
from datetime import timedelta
import zlib


listVehicleUrl = "https://index.getaround.com/v1.0/search?start_time=2022-08-03T08%3A15%3A00Z&end_time=2022-08-03T16%3A15%3A00Z&lat=39.732133499999996&lng=-104.96012569999999&distance=20.0&properties=car_id%2Ccar_name%2Clatitude%2Clongitude%2Cmake%2Cmodel%2Cyear%2Ccar_photo_v2%2Cowner_id%2Cowner_name%2Cowner_photo_v2%2Cprice_hourly%2Cdistance%2Csubtotal_price%2Ctotal_price%2Ctimezone%2Ccountry%2Cpostcode%2Caddress_state%2Caddress_city%2Cstars_rating%2Crating_count%2Cis_new%2Cmarket_tags%2Cfeatures"
dateFormat = "%Y-%m-%d %H:%M:%S"


app = 'GetAround'
for country in countriesList.keys():
    for city in countriesList[country].keys():
        print(country, city)

        now = datetime.now()

        startDate = now + timedelta(hours=1)
        # print(country, city, startDate)

        
        maxDays = 60

        payload={}
        headers = {
            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N976N Build/QP1A.190711.020) Getaround-Android/433 gzip',
            'x-analytics-data': '{"context":{"app":{"build":433.0,"name":"Getaround","namespace":"com.getaround.android","version":"3.2.3"},"traits":{"anonymousId":"8bc39a52-f983-4ed9-8a84-99073178ef3a","userId":"6723152062578688","id":"6723152062578688"},"library":{"name":"analytics-android","version":"4.3.0"},"os":{"name":"Android","version":"7.1.2"},"timezone":"Asia/Shanghai","screen":{"density":1.5,"width":720.0,"height":1280.0},"userAgent":"Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N976N Build/QP1A.190711.020)","locale":"en-US","device":{"id":"044089a8cc401c76","manufacturer":"samsung","model":"SM-N976N","name":"d2q","advertisingId":"c89d1298-7c8f-42a8-a094-2f8cdd835c1a","adTrackingEnabled":true},"network":{"wifi":true,"carrier":"T-Mobile","bluetooth":false,"cellular":false}}}',
            'accept-encoding': 'gzip'
        }


        for statDayDelta in range(0,maxDays):
            for startHourDelta in range(0,24):
                hoursToBeAdded = startHourDelta+(24*statDayDelta)

                #new start and end date for the ietration
                tempStart = startDate + timedelta(hours=hoursToBeAdded)
                tempEnd = tempStart + timedelta(hours=1)

                #upper limit of while loop 
                upperLimitDate = startDate + timedelta(hours=(maxDays*24)+24)
                print(str(tempStart),str(tempEnd))

                while tempEnd < upperLimitDate:
                    listVehicleUrl = "https://index.getaround.com/v1.0/search?start_time=TB1&end_time=TB2&lat=TB3&lng=TB4&distance=20.0&properties=car_id%2Ccar_name%2Clatitude%2Clongitude%2Cmake%2Cmodel%2Cyear%2Ccar_photo_v2%2Cowner_id%2Cowner_name%2Cowner_photo_v2%2Cprice_hourly%2Cdistance%2Csubtotal_price%2Ctotal_price%2Ctimezone%2Ccountry%2Cpostcode%2Caddress_state%2Caddress_city%2Cstars_rating%2Crating_count%2Cis_new%2Cmarket_tags%2Cfeatures"

                    #2022-07-28T04%3A00%3A00
                    t1 = str(tempStart).split(' ')[0]+'T'+str(tempStart).split(' ')[1].split('.')[0]
                    t1 = t1.replace(':','%3A')
                    t1 = t1.split('%3A')[0]
                    t1 = t1 +'%3A00%3A00Z'

                    # replace start time
                    listVehicleUrl = listVehicleUrl.replace('TB1',t1)

                    t2 = str(tempEnd).split(' ')[0]+'T'+str(tempEnd).split(' ')[1].split('.')[0]
                    t2 = t2.replace(':','%3A')
                    t2 = t2.split('%3A')[0]
                    t2 = t2 +'%3A00%3A00Z'

                    #replace end time
                    listVehicleUrl = listVehicleUrl.replace('TB2',t2)

                    #replace lat 
                    listVehicleUrl = listVehicleUrl.replace('TB3',str(countriesList[country][city][0]))

                    #replace long
                    listVehicleUrl = listVehicleUrl.replace('TB4',str(countriesList[country][city][1]))

                    # print(listVehicleUrl)

                    response = requests.request("GET", listVehicleUrl, headers=headers, data=payload)
                    content = zlib.compress(response.text.encode())

                    


                    print(len(content))

                    t1 = t1.replace('%3A00%3A00Z','')
                    t2 = t2.replace('%3A00%3A00Z','')
                    fx = open('ListOfVehicles/'+country+'~'+city+'~'+app+'~'+t1+'~'+t2,'wb')
                    fx.write(content)
                    fx.close()

                    print("done!")
                    

                    tempEnd = tempEnd + timedelta(hours=1)


                # for endDayDelta in range(statDayDelta, maxDays):
                #     for endtHourDelta in range(0,24):
                # # print(str(tempStart),hoursToBeAdded,str(startDate), str(now))

    
# read and decompress 
# import os
# import json 

# path = r"ListOfVehicles"

# directories = os.listdir( path )
# for file in directories:
#     if ('GetAround' in file or 'Turo' in file) and '.' not in file:
#         print(file)
#         fx = open('ListOfVehicles/'+file,'rb')
#         vehiclesList = json.loads(zlib.decompress(fx.read()).decode())
#         fx.close()


#         print(file, vehiclesList.keys(), len(vehiclesList['cars']))



# content = 
# 
# # print(decomp)