import os
import json
import zlib 

path = r"DetailsofVehicles"
carBrand = {}
carBrand["da"]=[20,30]

if(not carBrand.get("Japan")):
    carBrand["Japan"]=[]
    carBrand["Japan"].append(30)
print(carBrand["Japan"])

if(not carBrand.get("Japan")):
    carBrand["Japan"]=[]
    carBrand["Japan"].append(20)
else:
    carBrand["Japan"].append(20)
print(carBrand["Japan"])