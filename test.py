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
# count = []
# year = int(input("please enter in a year: "))
# shape = input("Please enter in a shape: ")
# while year < 2001:
#   yearString = str(year)
#   df = ufo[ufo.Time.str.contains(yearString)]
#   specificShape = df[df.Shape == shape.upper()]
#   number = specificShape.Shape.count()
#   count.append(int(number))
#   year += 1

# print(count)


diskCount = []
years = []
startYear = 1930
shape = "disk"
while startYear < 2001:
  yearString = str(startYear)
  df = ufo[ufo.Time.str.contains(yearString)]
  specificShape = df[df.Shape == shape.upper()]
  number = specificShape.Shape.count()
  diskCount.append(int(number))
  years.append(startYear)
  startYear += 1

lightCount = []
years = []
startYear = 1930
shape = "light"
while startYear < 2001:
  yearString = str(startYear)
  df = ufo[ufo.Time.str.contains(yearString)]
  specificShape = df[df.Shape == shape.upper()]
  number = specificShape.Shape.count()
  lightCount.append(int(number))
  years.append(startYear)
  startYear += 1

triangleCount = []
years = []
startYear = 1930
shape = "triangle"
while startYear < 2001:
  yearString = str(startYear)
  df = ufo[ufo.Time.str.contains(yearString)]
  specificShape = df[df.Shape == shape.upper()]
  number = specificShape.Shape.count()
  triangleCount.append(int(number))
  years.append(startYear)
  startYear += 1

cigarCount = []
years = []
startYear = 1930
shape = "triangle"
while startYear < 2001:
  yearString = str(startYear)
  df = ufo[ufo.Time.str.contains(yearString)]
  specificShape = df[df.Shape == shape.upper()]
  number = specificShape.Shape.count()
  cigarCount.append(int(number))
  years.append(startYear)
  startYear += 1

plt.plot(years, diskCount, linewidth=2, c="red")
plt.plot(years, lightCount, linewidth=2, c="blue")
plt.plot(years, triangleCount, linewidth=2, c="black")
plt.plot(years, cigarCount, linewidth=2, c="green")
plt.xlabel("Year", fontsize=14)
plt.ylabel("Count of UFO Shape", fontsize=12)
plt.show()

# plt.title("UFO Sightings By Year", fontsize=24)


# df.Shape.value_counts().plot(kind="bar")
# plt.show()


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




        
    
        
        This was when I was growing up and UFO's were all the rage with shows like the
        X-Files, Sightings, Unsolved Mysteries. UFOs became a culture aspect.
        Looking at the shape data, the types of shapes also increased dramatically in the same time period
        The only shape that was common to see in the 1960's and 70's was the 'disk' shape.
        Again, I believe that cultural aspects like the Twilight Zone, the Outer Limits and other  
        sci-fi shows from this time period led to UFO's becoming popular, briefly. 
        Thus, we are not being invaded but instead UFOs are invading pop culture.
        As Dana Scully use to say on the X-Files: 'I want to Believe'. Yet, the data does not support it.






















