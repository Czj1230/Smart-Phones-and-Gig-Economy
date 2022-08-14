import os
import json
import zlib 

path = r"ListOfVehicles"

carIdList = []

directories = os.listdir( path )
for file in directories:
    if 'Turo' in file and  'Ottawa' in file:
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

print(len(carIdList))
carIdList = list(set(carIdList))
print(len(carIdList))
fx = open('carIdListFileofOttawa','w')
fx.write(str(carIdList))
fx.close()

#===============================================================================
#To load carIdList from string
#===============================================================================
# path = r"ListOfVehicles"

# carIdList = []

# directories = os.listdir( path )
# for file in directories:
#     if 'Turo' in file:
#         print(file)
#         content = open(path+"\\"+file,'r').read()
#         carListDict = content                      #string
#         carListDict = json.loads(carListDict)      #still string
#         carListDict = json.loads(carListDict)      #json

#         print(carListDict.keys())
#         fx = open('carIdListTemp','w')       # write to another file
#         fx.write(json.dumps(carListDict))
#         fx.close

