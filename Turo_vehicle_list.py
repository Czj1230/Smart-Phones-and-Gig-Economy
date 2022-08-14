import requests

# most visited ten countries : https://www.worldatlas.com/articles/10-most-visited-countries-in-the-world.html
countriesList = {}
countriesList['Canada'] = {}
countriesList['UK'] = {}
countriesList['United States'] = {}

# 5 most populous cities of each country
countriesList['Canada']['Ottawa'] = [45.406162, -75.698775]
# countriesList['Canada']['Toronto'] = [43.668432, -79.384777]
# countriesList['UK']['London'] = [51.500905, -0.124443]
# countriesList['UK']['Birmingham'] = [52.479111, -1.904099]
# countriesList['United States']['Phoenix'] = [33.456941, -112.077480]
# countriesList['United States']['Los Angeles'] = [34.043724, -118.244801]
# countriesList['United States']['Denver'] = [39.735400, -104.989505]
# countriesList['United States']['Bridgeport'] = [41.190174, -73.180567]
# countriesList['United States']['Jacksonville'] = [30.395341, -81.637948]
# countriesList['United States']['Atlanta'] = [33.779472, -84.385445]
# countriesList['United States']['Honolulu'] = [21.340395, -157.836534]
# countriesList['United States']['Chicago'] = [41.821113, -87.708655]
# countriesList['United States']['Indianapolis'] = [39.761504, -86.156134]
# countriesList['United States']['New Orleans'] = [29.924748, -90.072254]
# countriesList['United States']['Baltimore'] = [39.318097, -76.650032]
# countriesList['United States']['Columbus'] = [39.959460, -82.952415]
# countriesList['United States']['Portland'] = [45.512322, -122.705310]
# countriesList['United States']['Philadelphia'] = [40.000057, -75.157892]
# countriesList['United States']['Providence'] = [41.821470, -71.424959]
# countriesList['United States']['Charleston'] = [32.791877, -79.955414]
# countriesList['United States']['Nashville'] = [36.145422, -86.766181]
# countriesList['United States']['Houston'] = [29.644818, -95.405172]
# countriesList['United States']['Salt Lake City'] = [40.809539, -111.923269]
# countriesList['United States']['Virginia Beach'] = [36.823423, -76.042899]
# countriesList['United States']['Seattle'] = [47.617054, -122.330032]
# countriesList['United States']['Milwaukee'] = [43.015146, -87.928987]


# list vehicles request

from datetime import datetime
from datetime import timedelta
import zlib


listVehicleUrl = "https://api.turo.com/api/search?startDate=08%2F20%2F2022&startTime=10%3A00&endDate=08%2F25%2F2022&endTime=10%3A00&latitude=45.4215296&longitude=-75.69719309999999"
dateFormat = "%Y-%m-%d %H:%M:%S"


app = 'Turo'
for country in countriesList.keys():
    for city in countriesList[country].keys():
        print(country, city)

        now = datetime(2022,8,20,10,00,00,00)

        startDate = now + timedelta(hours=1)
        # print(country, city, startDate)

        
        maxDays = 60

        payload={}
        headers = {
            'tracestate': '@nr=0-2-3069551-857489947-60e5f128e2fe4abc----1660053816148',
            'newrelic': 'eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IjMwNjk1NTEiLCJkLmFwIjoiODU3NDg5OTQ3IiwiZC50ciI6ImI0OWY5NzUyY2M1YzQ0OWQ5NWUzOTVhZjc5MmFjNjMwIiwiZC5pZCI6IjYwZTVmMTI4ZTJmZTRhYmMiLCJkLnRpIjoxNjYwMDUzODE2MTQ4fX0=',
            'traceparent': '00-b49f9752cc5c449d95e395af792ac630-60e5f128e2fe4abc-00',
            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N976N Build/QP1A.190711.020)Turo/22.25.0',
            'x-mobile_carrier_country': 'US',
            'accept-language': 'en-US',
            'referer': 'android-app://com.turo.search.presentation.ui.activity.searchactivity',
            'client-capabilities': 'ANDROID_PAY',
            'x-require-non-null-response': 'true',
            'authorization': 'Bearer 6acc0dae-4e3b-4032-b576-722b1a0654b7',
            'accept-encoding': 'gzip',
            'cookie': 'td_dv_mf=samsung; td_dv_mo=SM-N976N; __cf_bm=dYxFIWi2XW_dQGDsV8Ib1DQwPMSIuO1Bj2AeJf.slUE-1660053796-0-AVmzSk8+QfdLPsa9FNO8yWE+fOHZrzP53PUYIEWNcYPKwL/KPC1hxIesmMPIqzZq611weZzzxcWceZ3JbS4M41P5PFYK0STM052mkrmRjPG2; td_dv_uid=ffe19848-4a76-4fd5-bc41-62c4b8aff13f; preferredLocale=en_US; sid=7TZ6QlgpRIWo-G0Kcznqkw; rr_u_cid=ffe19848-4a76-4fd5-bc41-62c4b8aff13f; __cf_bm=9iZw5bR1GzcZaODOxo9VWTy7LAMcIxt7grlry8yWk_A-1660054327-0-AU5GNz7tTOu6OBFlSxW37bdlh/d3uDkEzlD1+0vVvWGBzGZJ3DWIsr1Q/5bLa8oOtHsXocmjGQBbh4ONVgYaaG0Jpd0z0hwMepravHKlA/mG; preferredLocale=en_US; sid=7TZ6QlgpRIWo-G0Kcznqkw',
            'x-newrelic-id': 'VwYBWFNWCRAIUVZWDwgOUlM='
        }
        count = 0
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
                    listVehicleUrl = "https://api.turo.com/api/search?startDate=TB1&startTime=TB2&endDate=TB3&endTime=TB4&latitude=TB5&longitude=TB6"
                    #listVehicleUrl = "https://api.turo.com/api/search?startDate=08%2F05%2F2022&startTime=10%3A00&endDate=08%2F08%2F2022&endTime=10%3A00&latitude=45.4215296&longitude=-75.69719309999999"

                    date = str(tempStart).split(' ')[0]
                    date = date.split('-')
                    t1 = date[1]+"%2F"+date[2]+"%2F"+date[0]

                    # replace start date
                    listVehicleUrl = listVehicleUrl.replace('TB1',t1)

                    #2022-07-28T04%3A00%3A00
                    t2 = str(tempStart).split(' ')[1].split('.')[0]
                    t2 = t2.replace(':','%3A')
                    t2 = t2.split('%3A')[0]
                    t2 = t2 +'%3A00'

                    # replace start time
                    listVehicleUrl = listVehicleUrl.replace('TB2',t2)


                    date = str(tempEnd).split(' ')[0]
                    date = date.split('-')
                    t3 = date[1]+"%2F"+date[2]+"%2F"+date[0]

                    # replace start date
                    listVehicleUrl = listVehicleUrl.replace('TB3',t3)

                    #2022-07-28T04%3A00%3A00
                    t4 = str(tempEnd).split(' ')[1].split('.')[0]
                    t4 = t4.replace(':','%3A')
                    t4 = t4.split('%3A')[0]
                    t4 = t4 +'%3A00'

                    # replace start time
                    listVehicleUrl = listVehicleUrl.replace('TB4',t4)

                    #replace lat 
                    listVehicleUrl = listVehicleUrl.replace('TB5',str(countriesList[country][city][0]))

                    #replace long
                    listVehicleUrl = listVehicleUrl.replace('TB6',str(countriesList[country][city][1]))

                    # print(listVehicleUrl)

                    response = requests.request("GET", listVehicleUrl, headers=headers, data=payload, verify=False)
                    content = zlib.compress(response.text.encode())

                    
                    print(len(content))

                    t1 = t1.split('%2F')
                    t1 = t1[2]+"-"+t1[0]+"-"+t1[1]
                    t2 = t2.replace('%3A00','')
                    t3 = t3.split('%2F')
                    t3 = t3[2]+"-"+t3[0]+"-"+t3[1]
                    t4 = t4.replace('%3A00','')
                    fx = open('ListOfVehicles/'+country+'~'+city+'~'+app+'~'+t1+"T"+t2+'~'+t3+"T"+t4,'wb')
                    fx.write(content)
                    fx.close()

                    print(country+" "+city+" "+str(count)+" done! ")
                    
                    tempEnd = tempEnd + timedelta(hours=1)
                    count += 1
                    
