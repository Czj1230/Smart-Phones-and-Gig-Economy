import os
import json
import zlib 

path = r"ListOfVehicles"
city = "Ottawa"
carIdList = []

directories = os.listdir( path )
for file in directories:
    if city in file:
        print(file)
        fx = open('ListOfVehicles/'+file,'rb')
        vehiclesList = json.loads(zlib.decompress(fx.read()).decode())
        fx.close()
        # print(file, vehiclesList.keys())
        # print(type(vehiclesList))
        # print(vehiclesList['list'][0]['vehicle']['id'])
        for vehicle in vehiclesList['list']:
            print(vehicle['vehicle']['id'])
            carIdList.append(vehicle['vehicle']['id'])


carIdList = list(set(carIdList))
print("Total number of vehilces in "+city)
print(len(carIdList))
