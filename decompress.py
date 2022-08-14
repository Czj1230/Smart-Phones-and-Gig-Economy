# read and decompress 
import os
import json
import zlib 

path = r"ListOfVehicles"
path_carDetail = r"DetailsofVehicles"

directories = os.listdir( path_carDetail )
for file in directories:
    if ('GetAround' in file or 'Turo' in file) and '.' not in file and 'Ottawa' in file:
        print(file)
        fx = open('ListOfVehicles/'+file,'rb')
        vehiclesList = json.loads(zlib.decompress(fx.read()).decode())
        fx2 = open('response','w')
        fx2.write(str(zlib.decompress(fx.read()).decode()))
        fx.close()

        print(file, vehiclesList.keys())

    break