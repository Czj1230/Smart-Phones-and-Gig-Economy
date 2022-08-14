import os
import json
import zlib 

from datetime import datetime
from datetime import timedelta
path = r"ListOfVehicles"
city = "Ottawa"

now = datetime(2022,8,20)

maxDays = 60

for DayDelta in range(0,maxDays):
    startDate = now+timedelta(days=DayDelta)
    # print(str(startDate))
    t = str(startDate).split()[0]
    # print(t)
    carIdList = []
    directories = os.listdir( path )
    for file in directories:
        if city in file and t in file:
            print(file)
            fx = open('ListOfVehicles/'+file,'rb')
            vehiclesList = json.loads(zlib.decompress(fx.read()).decode())
            fx.close()
            # print(file, vehiclesList.keys())
            # print(type(vehiclesList))
            # print(vehiclesList['list'][0]['vehicle']['id'])
            for vehicle in vehiclesList['list']:
                # print(vehicle['vehicle']['id'])
                carIdList.append(vehicle['vehicle']['id'])


    carIdList = list(set(carIdList))
    if(len(carIdList)>0):
        print(t+" Total number of vehilces in "+city)
        print(len(carIdList))
