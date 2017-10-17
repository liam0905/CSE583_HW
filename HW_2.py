"""This Program Analyzes Weather Data."""

import pandas as pd
import sys 

def analyze(df):

    rainy_cities = []
    rain_max = df.RainInches.max()
    for index, row in df.iterrows():
        if row['RainInches'] == rain_max:
            rainy_cities.append(row['City'])
    if len(rainy_cities) == 5:
        return "%s, %s, %s, %s,and %s have %d inches of rain per year!" % (rainy_cities[0],rainy_cities[1], rainy_cities[2],rainy_cities[3],rainy_cities[4],rain_max)
    if len(rainy_cities) == 4:
        return "%s, %s, %s, and %s have %d inches of rain per year!" % (rainy_cities[0],rainy_cities[1], rainy_cities[2],rainy_cities[3],rain_max)
    if len(rainy_cities) == 3:
        return "%s, %s, and %s have %d inches of rain per year!" % (rainy_cities[0],rainy_cities[1], rainy_cities[2] ,rain_max)
    elif len(rainy_cities) == 2:
        return "%s and %s have %d inches of rain per year!" % (rainy_cities[0],rainy_cities[1] ,rain_max)
    elif len(rainy_cities) ==1:
        return "%s has %d inches of rain per year!" % (rainy_cities[0], rain_max)      
            

if __name__ == "__main__":

   # try::
   # df = pd.read_csv(sys.argv[1])
   # print(analyze(df))
   # except 