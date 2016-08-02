#This file is where I will test out other things that I want to look at. 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

cols = ['City', 'Color', 'Shape', 'State', 'Time']
ufo = pd.read_csv('http://bit.ly/uforeports', names=cols)

#print(ufo.dtypes)


#print(ufo[(ufo.Time > "12/24/2000 18:00")])

# test = ufo[ufo.Time.str.contains('1950')]

# print(test.City.count())

#CONTAINS LINE
#print(ufo[ufo.Time.str.contains('1999')])

year = [] 

# year.append(2)
# print(year)

yr = int(input("Enter Year:"))
print(type(yr))
x = str(yr)
print(type(x))
year.append(yr)
print(year)

#I need to ask user for the year-which will be an int.
#I then need to convert that year into a str and put it into the contains line (see above)
#Once I have the year I need to get the count of the sighting for that year 
#I push the count into an array 
#All of this, or most of it, should be in a loop that adds one to the year, which will have to be an int. 