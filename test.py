#This file is where I will test out other things that I want to look at. 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


cols = ['City', 'Color', 'Shape', 'State', 'Time']
ufo = pd.read_csv('http://bit.ly/uforeports', names=cols)

######## Attempting to sort out most common shape by year ######

# shape = input("Please enter in a shape: ")
# print(ufo[ufo.Shape == shape.upper()])
# print(ufo[(ufo.Shape == shape.upper()) & (ufo.Time == '3/15/1946 15:30')])

### Specific Year version:
# count = []
# year = input("please enter in a year: ")
# shape = input("Please enter in a shape: ")
# df = ufo[ufo.Time.str.contains(year)]
# specificShape = df[df.Shape == shape.upper()]
# number = specificShape.Shape.count()
# count.append(int(number))
# print(count)

######### I HAVE TO BUILD A LINE GRAPH THAT SHOWS ALL OF THE UFO TYPES COMPARED TO EACH OTHER!

### Loop Version
count = []
year = int(input("please enter in a year: "))
shape = input("Please enter in a shape: ")
while year < 2001:
  yearString = str(year)
  df = ufo[ufo.Time.str.contains(yearString)]
  specificShape = df[df.Shape == shape.upper()]
  number = specificShape.Shape.count()
  count.append(int(number))
  year += 1

print(count)

# df.Shape.value_counts().plot(kind="bar")
# plt.show()

# count = test.City.count()
# year = [] 
# year.append(int(count))
# print(year)

###




##### Working on pulling the number of sightings for city

## This works!!!
# city = str(input("Please enter a city to look at: "))
# df = ufo[ufo.City == city.title()]
# count = df.City.count()
# print("The city of " + city + " has " + str(count) + " ufos")


#######

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
# value = input("Please give me a starting year: ")
# count = int(value)
# year, date = [], []
# while count < 2001:
#   test = ufo[ufo.Time.str.contains(value)]
#   date.append(value)
#   number = test.City.count()
#   year.append(int(number))
#   newValue = int(value)
#   newValue += 1
#   value = str(newValue)
#   count += 1

# print(date)
# print(year)
# plt.plot(date, year, linewidth=2)

# plt.title("UFO Sightings By Year", fontsize=24)
# plt.xlabel("Year", fontsize=14)
# plt.ylabel("Count", fontsize=12)


# plt.show()


# value = input("Please give me a starting year: ")
# count = int(value)
# year, date = [], []
# while count < 2001:
#   test = ufo[ufo.Shape.str.contains(value)]
#   date.append(value)
#   number = test.City.count()
#   year.append(int(number))
#   newValue = int(value)
#   newValue += 1
#   value = str(newValue)
#   count += 1

# print(date)
# print(year)
# plt.plot(date, year, linewidth=2)

# plt.title("UFO Sightings By Year", fontsize=24)
# plt.xlabel("Year", fontsize=14)
# plt.ylabel("Count", fontsize=12)


# plt.show()



























