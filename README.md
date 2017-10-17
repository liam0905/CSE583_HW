# HW2-aut17
## CSE 583 Homework 2 - Debugging and Exceptions

You are writing a program that analyzes weather data. The data are structured as a CSV that has the columns "City", "State", and "RainInches". The user provides the file path on the command line. The program replies with the city that has the most rain. If two cities have the same amount of rain, then both should be reported.

Below is incomplete and buggy code that was implemented to provide the above features. The assignment is to do the following:
- Create a sample dataset structured as described above (1 point)
- Find the bugs in the existing code (2 points)
- Print a message if the file is not present (1 point)
- Print a help message that describes how to use the program if no arguments are provided on the command line or the argument is "--help" or "-h" (1 point)

```python
"""This Program Analyzes Weather Data."""

import pandas as pd
import sys 

def analyze(df):
  """ 
  Computes the city and state with the maximum rain.
  :param pd.DataFrame df: Columns - City, State, RainInches
  :returns str: Result of analysis
  """
  rain_max = df.RainInches.max()
  for _, row in df.iterrows():
    if row['RainInches'] == rain_max:
      rainy_city = row['City']
  return "%s has %d inches of rain!" % (rainy_city, rain_max)

df = pd.read_csv(sys.argv[0])
print(analyze(df))
```
