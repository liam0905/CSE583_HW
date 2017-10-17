"""This Program Analyzes Weather Data."""

import pandas as pd
import sys 
import argparse

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

   try:
    df = pd.read_csv(sys.argv[1])
    print(analyze(df))
  except: FileNotFoundError
   print("Enter the .py name followed by the .csv name")
    
    
    if (sys.argv[1] == "--help") or (sys.argv[1] == "-h"):
        print("Enter the name of the .csv file after the name of the .py file")   
        
    else: 
        df = pd.read_csv(sys.argv[1])
        print(analyze(df))

        #or (len(sys.argv[1]) == 0):
    
   