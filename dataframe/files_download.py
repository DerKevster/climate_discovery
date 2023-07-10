#Import the list of all weather stations

import pandas as pd

data = pd.read_csv('Weather_Stations.csv', delimiter=';')
station_list = data['Column1'].tolist()

#Download data from all weather stations

import urllib.request

n=52500

for station in station_list[52500:]:
    url = f"https://www.ncei.noaa.gov/data/global-summary-of-the-month/access/{station}"
    destination = f"/home/kev/code/DerKevster/climate_discovery/raw_data/{station}"
    urllib.request.urlretrieve(url, destination)

    n+=1

    print(f'{station} added. {n}/{len(station_list)}')
