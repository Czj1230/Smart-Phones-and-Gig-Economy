# read and decompress 
import os
import json
import zlib 
import numpy as np

path = r"DetailsofVehicles"
carBrand = {} # calculate the average price of each car brand ???

directories = os.listdir( path )
for file in directories:
    print(file)
    fx = open('DetailsofVehicles/'+file,'rb')
    attributeList = json.loads(zlib.decompress(fx.read()).decode())
    fx.close()

    # print(file, attibuteList.keys())
    brand = attributeList["vehicle"]["make"]
    price = attributeList["dateRangeRate"]["defaultAverageDailyPrice"]

    if(not carBrand.get(brand)):
        carBrand[brand]=[]
        carBrand[brand].append(int(price))
    else:
        carBrand[brand].append(int(price))


AveragePrice = {}
fx = open('carAveragePrice','w')
for brand in carBrand:
    print(brand)
    mean = np.mean(carBrand[brand])
    AveragePrice[brand] = mean
    print(mean)
    fx.write(brand+" "+str(mean)+"\n")

fx.close()