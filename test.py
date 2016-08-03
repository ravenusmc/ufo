#This file is where I will test out other things that I want to look at. 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from datetime import datetime

cols = ['City', 'Color', 'Shape', 'State', 'Time']
ufo = pd.read_csv('http://bit.ly/uforeports', names=cols)

#print(ufo.dtypes)


#print(ufo[(ufo.Time > "12/24/2000 18:00")])

# value = input("please give me a value: ")

# test = ufo[ufo.Time.str.contains(value)]

# print(test.City.count())

#CONTAINS LINE
#print(ufo[ufo.Time.str.contains('1999')])

# year = [] 

# year.append(2)
# print(year)

# yr = int(input("Enter Year:"))
# print(type(yr))
# x = str(yr)
# print(type(x))
# year.append(yr)
# print(year)

######The below example can get the UFO count for one specific year. 

#I need to ask user for the year.
# value = input("please give me a value: ")
#I then need to convert that year into a str and put it into the contains line (see above)
# test = ufo[ufo.Time.str.contains(value)]
#Once I have the year I need to get the count of the sighting for that year 
# count = test.City.count()
#I push the count into an array 
# year = [] 
# year.append(int(count))
# print(year)
#All of this, or most of it, should be in a loop that adds one to the year, which will have to be an int. 

# value = input("please give me a value: ")
# test = ufo[ufo.Time.str.contains(value)]
# count = test.City.count()
# year = [] 
# year.append(int(count))
# print(year)

#print("test value is: " + str(number))


#######UFO count from specific year to year in which data ends. 
value = input("Please give me a starting year: ")
count = int(value)
year, date = [], []
while count < 2001:
  test = ufo[ufo.Time.str.contains(value)]
  date.append(value)
  number = test.City.count()
  year.append(int(number))
  newValue = int(value)
  newValue += 1
  value = str(newValue)
  count += 1

# print(date)
# print(year)
plt.plot(date, year, linewidth=2)

plt.title("UFO Sightings By Year", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Count", fontsize=12)


plt.show()

#plt.plot(year, linewidth=5)
# plot.show()

# squares = [1,2,4,9,16,25]
# plt.plot(squares)
# plt.show()



# x = 0
# nums = []
# while x < 4:
#   nums.append(x)
#   x += 1

# print(nums)























