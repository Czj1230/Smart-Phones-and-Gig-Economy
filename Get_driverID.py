import os
import json
import zlib 

path = r"ListOfVehicles"

ownerIdList = []

directories = os.listdir( path )
for file in directories:
    if ('GetAround' in file or 'Turo' in file) and '.' not in file and 'Ottawa' in file:
        print(file)
        fx = open('ListOfVehicles/'+file,'rb')
        vehiclesList = json.loads(zlib.decompress(fx.read()).decode())
        fx.close()
        # print(file, vehiclesList.keys())
        # print(type(vehiclesList))
        # print(vehiclesList['list'][0]['vehicle']['id'])
        for vehicle in vehiclesList['list']:
            print(vehicle['owner']['id'])
            ownerIdList.append(vehicle['owner']['id'])

print(len(ownerIdList))
ownerIdList = list(set(ownerIdList))
print(len(ownerIdList))
fx = open('ownerIdListFile','w')
fx.write(str(ownerIdList))
fx.close()