import requests

# most visited ten countries : https://www.worldatlas.com/articles/10-most-visited-countries-in-the-world.html
countriesList = {}
countriesList['United States'] = {}


# 5 most populous cities of each country
countriesList['United States']['New York City'] = [40.691156, -73.942609]




# list vehicles request

from datetime import datetime
from datetime import timedelta
import zlib


listVehicleUrl = "https://index.getaround.com/v1.0/search?sort=distance&start_time=2022-07-22T04%3A00%3A00Z&end_time=2022-07-22T12%3A00%3A00Z&lat=40.7127753&lng=-74.0059728&distance=100.0&properties=car_id%2Ccar_name%2Clatitude%2Clongitude%2Cmake%2Cmodel%2Cyear%2Ccar_photo_v2%2Cowner_id%2Cowner_name%2Cowner_photo_v2%2Cprice_hourly%2Cdistance%2Csubtotal_price%2Ctotal_price%2Ctimezone%2Ccountry%2Cpostcode%2Caddress_state%2Caddress_city%2Cstars_rating%2Crating_count%2Cis_new%2Cmarket_tags%2Cfeatures&page_size=5000&page_sort=distance"
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
        'user-agent': 'Dalvik/2.1.0',
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
                print(str(tempStart),str(tempEnd), str(uptoDate))

                while tempEnd < upperLimitDate:
                    listVehicleUrl = "https://index.getaround.com/v1.0/search?start_time=TB1&end_time=TB2&lat=TB3&lng=TB4&distance=100.0&properties=car_id%2Clatitude%2Clongitude%2Cmake%2Cmodel%2Cyear%2Ccar_photo_v2%2Cowner_id%2Cowner_name%2Cowner_photo_v2%2Cprice_hourly%2Cdistance%2Csubtotal_price%2Ctotal_price%2Ctimezone%2Ccountry%2Cpostcode%2Caddress_state%2Caddress_city%2Cstars_rating%2Crating_count%2Cis_new%2Cmarket_tags%2Cfeatures&page_size=5000&uid=5965553788649472"

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

                    

                    tempEnd = tempStart + timedelta(hours=1)
                    break

                # for endDayDelta in range(statDayDelta, maxDays):
                #     for endtHourDelta in range(0,24):
                # # print(str(tempStart),hoursToBeAdded,str(startDate), str(now))
                break
            break
        break
    # break
    
# read and decompress 
import os
import json 

path = r"ListOfVehicles"

directories = os.listdir( path )
for file in directories:
    if ('GetAround' in file or 'Turo' in file) and '.' not in file:
        print(file)
        fx = open('ListOfVehicles/'+file,'rb')
        vehiclesList = json.loads(zlib.decompress(fx.read()).decode())
        fx.close()


        print(file, vehiclesList.keys(), len(vehiclesList['cars']))



# content = 
# 
# # print(decomp)