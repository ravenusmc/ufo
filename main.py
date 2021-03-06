import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from prettytable import PrettyTable 

#All of the functions to ensure that valid information is entered by the user are kept in a 
#separate file. 
from valid import *

###### TO DO:
### 1. ADD Key to shape's graph

#### Main Program Functions #######

#This is the main function that introduces the user to the program. 
def intro():
  print("\033c")
  print("--------------------")
  print("Welcome to UFO Data!")
  print("--------------------")
  choice = input("Do you want to use it?(y/n) ")
  while not valid(choice):
    choice = input("Do you want to use it?(y/n) ")
  if choice == 'y':
    main()
  elif choice == 'n':
    print('Thank you for using the program! Hope you come again!')
    print('Remember that the truth is out there!')

#This function pulls all of the data from the web. It will then pass it from function to function.
def main():
  print("\033c")
  cols = ['City', 'Color', 'Shape', 'State', 'Time']
  ufo = pd.read_csv('http://bit.ly/uforeports', names=cols)
  print("Here are your options:")
  print("1. Main Menu")
  print("2. Help")
  print("3. Quit")
  choice = int(input("What do you choose? " ))
  while not validMain(choice):
    choice = input("If you need to see directions on how to use this type 'help' or 'next' to move on. " )
  if choice == 1:
    mainMenu(ufo)
  elif choice == 2:
    help(ufo) 
  elif choice == 3:
    print("Thank you for using the program!")
    print("The Truth is out there!")

#This is the main menu of the program. The user will be taken back here if they so desire. 
def mainMenu(ufo):
  print("\033c")
  print("1. UFO's by City")
  print("2. UFO's by State")
  print("3. UFO by Shape")
  print("4. UFO's by Year")
  print("5. Other")
  print("6. Conclusion of Results")
  choice = int(input("Please enter the number of what you want to look at: "))
  while not validStart(choice):
    choice = int(input("Please enter the number of what you want to look at: "))
  if choice == 1:
    city(ufo)
  elif choice == 2:
    state(ufo)
  elif choice == 3:
    shape(ufo)
  elif choice == 4:
    yearGraph(ufo)
  elif choice == 5:
    other(ufo)
  elif choice == 6:
    conclusion()

#This function will explain to the user how to use UFO. 
def help(ufo):
  print("\033c")
  print("Welcome to the help section")
  print("This project uses Python Pandas to analyze UFO data")
  print('\n')
  print("The data has five columns, which are the following: ")
  print('City, State, Shape, Color, and Time')
  print('Please be sure to type in the commands exactly as you see them.')
  print('\n')
  print("This is how the data will appear:")
  print(ufo.head())
  print('\n')
  choice = input("Do you still want to use the program?(y/n) ")
  while not valid(choice):
    choice = input("Do you still want to use the program?(y/n) ")
  if choice == 'y':
    mainMenu();
  elif choice == 'n':
    print("Thank you for using it!")
    print("Remember, the truth is out there!!")

#This function shows the UFO sightings, over the years, by city.
def city(ufo):
  print("\033c")
  city = str(input("Please enter a city to look at: "))
  print("Here is the data on " + city.title())
  print(ufo[ufo.City == city.title()])
  df = ufo[ufo.City == city.title()]
  count = df.City.count()
  print("The city of " + city + " has " + str(count) + " ufos")
  option = input("Do you want to look at more data?(y/n) ")
  if option == 'y':
    mainMenu(ufo)
  elif option == 'n':
    print("Thank you for using the program!")
    print("Remember the truth is out there!")

#This function shows the UFO sightings, over the years, by state.
def state(ufo):
  print("\033c")
  state = str(input("Please enter the state abbreviation: "))
  print("Here is the data on " + state.upper())
  print(ufo[ufo.State == state.upper()])
  df = ufo[ufo.State == state.upper()]
  count = df.State.count()
  print("This state has " + str(count) + " ufos")
  option = input("Do you want to look at more data?(y/n) ")
  if option == 'y':
    mainMenu(ufo)
  elif option == 'n':
    print("Thank you for using the program!")
    print("Remember the truth is out there!")

#This is one of the longest functions in the program. I wrote this function over the course of about 
#two days. It is where the user can see the UFOs by shape as well as by shape and their count over 
#the years. I do repeat myself a few times in it but trust me, how I had it originally it was 
#much much longer.
def shape(ufo):
  print("\033c")
  print("Here are the shapes to examine: ")
  print("Disk")
  print("Cigar")
  print("Light")
  print("Triangle")
  print("Sphere")
  print("Other")
  print('\n')
  print("1. See a chart of the shape you select with other data.")
  print("2. A graph where you select what shapes you want and their count since 1930.")
  print('\n')
  option = int(input("How do you want to look at the information: "))
  if option == 1:
    shape = str(input("Please enter the shape you want to examine: "))
    print("Here is the data on ufo's shaped as a: " + shape.upper())
    print(ufo[ufo.Shape == shape.upper()])
  elif option == 2:
    print("\033c")
    print("Here are the shapes to examine: ")
    print("Disk")
    print("Cigar")
    print("Light")
    print("Triangle")
    print("Sphere")
    print("Other")
    print('\n')
    #A shapes list is initialized. This is what will hold the shapes that the user wants to look at.
    shapes = []
    print("You choose to look at the graph.")
    print("Remember, after your done with examining the graph it must be closed before moving on.")
    print("Enter the shapes you want included. Type 'done' when finished entering what you want to look at.")
    while True:
      #Here the user enters the shapes that the user wants included on the graph. 
      view = input("Please enter the shape you want included on the graph: ")
      if view == "done":
        break
      else: 
        #The shapes will then be placed into the shapes list.
        shapes.append(view)
    #These lists will hold the count, each year, for each spcific shape that the user wants to look at.
    diskCount, lightCount, triangleCount, cigarCount, sphereCount, otherCount = [], [], [], [], [], []
    #These lists will hold the year for each shape. I could not get the graph in matplotlib to work without
    #doing this.
    yearDisk, yearLight, yearTriangle, yearCigar, yearSphere, yearOther = [], [], [], [], [], []
    #I then have a for loop that will loop through the shapes list. 
    for shape in shapes:
      #The start year, for each shape is set as the same year-1930
      startYear, diskYear, lightYear, triangleYear, cigarYear, sphereYear, otherYear = 1930, 1930, 1930, 1930, 1930, 1930, 1930
      #This while loop will go through each year, for each shape getting the count of that shape for that
      #year. 
      while startYear < 2001:
        #I have to convert the start year to a string to use it in the next line.
        yearString = str(startYear)
        #I am setting up a dataframe that will hold all the information for a specific year. 
        df = ufo[ufo.Time.str.contains(yearString)]
        if shape == "disk":
          #This line uses the df created above and search's for every entry that has the spcific shape 
          #that the user wanted. 
          specificShape = df[df.Shape == shape.upper()]
          #The specific shape variable is then taken and a count is done on the Shape column.
          number = specificShape.Shape.count()
          #That count is then pushed into the diskcount List.
          diskCount.append(int(number))
          #The specific year that is currently being cycled through is appended to the year List.
          yearDisk.append(diskYear)
          diskYear += 1
        elif shape == "light":
          specificShape = df[df.Shape == shape.upper()]
          number = specificShape.Shape.count()
          lightCount.append(int(number))
          yearLight.append(lightYear)
          lightYear += 1
        elif shape == "triangle":
          specificShape = df[df.Shape == shape.upper()]
          number = specificShape.Shape.count()
          triangleCount.append(int(number))
          yearTriangle.append(triangleYear)
          triangleYear += 1
        elif shape == "cigar":
          specificShape = df[df.Shape == shape.upper()]
          number = specificShape.Shape.count()
          cigarCount.append(int(number))
          yearCigar.append(cigarYear)
          cigarYear += 1
        elif shape == "sphere":
          specificShape = df[df.Shape == shape.upper()]
          number = specificShape.Shape.count()
          sphereCount.append(int(number))
          yearSphere.append(sphereYear)
          sphereYear += 1
        elif shape == "other":
          specificShape = df[df.Shape == shape.upper()]
          number = specificShape.Shape.count()
          otherCount.append(int(number))
          yearOther.append(otherYear)
          otherYear += 1
        startYear += 1
    #All of these below lines are for matplotlib to actually graph the data. 
    plt.plot(yearDisk, diskCount, linewidth=2, c="red")
    plt.plot(yearLight, lightCount, linewidth=2, c="blue")
    plt.plot(yearTriangle, triangleCount, linewidth=2, c="black")
    plt.plot(yearCigar, cigarCount, linewidth=2, c="green")
    plt.plot(yearSphere, sphereCount, linewidth=2, c="orange")
    plt.plot(yearOther, otherCount, linewidth=2, c="purple")
    plt.title("UFO SHAPES BY YEAR", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Count of UFO Shape", fontsize=12)
    plt.show()
    print("Where do you want to do to now: ")
    print("1. Main Menu")
    print("2. Quit")
    choice = int(input("Please enter a number: "))
    if choice == 1:
      mainMenu(ufo)
    elif choice == 2:
      print("Thank you for using the program!")
      print("Remember the TRUTH is out THERE!")

#This function basically tells the user the basic count of how many ufo's are in a city or the shape. 
def other(ufo):
  print("\033c")
  print("Do you want to look at UFO count by city? ")
  print("Looking at count, you will see which cities have the most UFO sightings!")
  print("You can also look at which shapes are the most common.")
  option = input("Please type 'city', 'shape' or 'back': ")
  if option == "city":
    print(ufo.City.value_counts())
  elif option == "shape":
    print(ufo.groupby('Shape').Shape.count())
  elif option == 'back':
    mainMenu(ufo)
  print("Where do you want to do to now: ")
  print("1. Main Menu")
  print("2. Quit")
  choice = int(input("Please enter a number: "))
  if choice == 1:
    mainMenu(ufo)
  elif choice == 2:
    print("Thank you for using the program!")
    print("Remember the TRUTH is out THERE!")

#This function will plot the ufo count from the year the user enters to 2001. 
def yearGraph(ufo):
  print("\033c")
  print("Here you will have two options.")
  print("1. UFO count in a specific year.")
  print("2. Enter in a year and see count, graphed, until 2001.")
  option = int(input("What would you like to choose? "))
  while not validyearGraph(option):
    option = int(input("What would you like to choose? "))
  if option == 1:
    value = input("please give me a year to look at data: ")
    test = ufo[ufo.Time.str.contains(value)]
    count = test.City.count()
    year = [] 
    year.append(int(count))
    print("The number of UFO's in " + value + " was: " + str(year))
  elif option == 2:
    print('\n')
    print("Please be aware that the graph must be closed before moving on!!!")
    print("The years go from 1930 to 2001")
    print('\n')
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
    plt.plot(date, year, linewidth=2)
    plt.title("UFO Sightings By Year", fontsize=24)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Count", fontsize=12)
    plt.show()
  print("Where do you want to do to now: ")
  print("1. Main Menu")
  print("2. Quit")
  choice = int(input("Please enter a number: "))
  if choice == 1:
    mainMenu(ufo)
  elif choice == 2:
    print("Thank you for using the program!")
    print("Remember the TRUTH is out THERE!")

#I decided to add this function so that the user can see the conclusions that I pulled from working 
#on this program. Yes, I have to fix the formatting issues here.
def conclusion():
  print("\033c")
  print("Since I was a small child, I have been interested in UFO's.")
  print("However, as I entered college I started to lose interest in them.")
  print("I felt that they simply were not real.")
  print("It was actually a comment, from steven spielberg that started to kill my belief.")
  print("He stated something along the lines of:")
  print("With everyone having a camera on thier phones why are")
  print("we not seeing more high quality images of UFO's.")
  print("The data in this program shows that the number of UFO sighting is going up.")
  print("However, the number of sightings also shot way up in the early to mid 90's.")
  print("This was when I was growing up and UFO's were all the rage with shows like the")
  print("X-Files, Sightings, Unsolved Mysteries. UFOs became a cultural phenomenon.")
  print("Looking at the shape data, the types of shapes also increased dramatically in the same time period")
  print("The only shape that was common to see in the 1960's and 70's was the 'disk' shape.")
  print("Again, I believe that cultural aspects like the Twilight Zone, the Outer Limits and other ")
  print("sci-fi shows from this time period led to UFO's becoming popular, briefly. ")
  print("Thus, we are not being invaded but instead UFOs are invading pop culture.")
  print("As Dana Scully use to say on the X-Files: 'I want to Believe'. Yet, the data does not support it.")        
  print("1. Main Menu")
  print("2. Quit")
  choice = int(input("What is your choice: "))
  while not validConclu(choice):
    choice = int(input("What is your choice: "))
  if choice == 1:
    mainMenu(ufo)
  elif choice == 2:
    print("Thank you for using the program")
    print("Remember, The Truth is Out There")

intro()
