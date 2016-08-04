import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

from valid import *
# print(ufo[(ufo.State == "GA") & (ufo.City == "Atlanta")])

  # option = input("Do you want to save this data stream to refine it more?(y/n) ")
  # if option == 'y':
  #   citySave = ufo[ufo.City == city]
  # else: 
  #   print("Data not saved moving on!")

#### Main Program Functions #######

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

def city(ufo):
  print("\033c")
  city = str(input("Please enter a city to look at: "))
  print("Here is the data on " + city.title())
  print(ufo[ufo.City == city.title()])
  option = input("Do you want to look at more data?(y/n) ")
  if option == 'y':
    mainMenu(ufo)
  elif option == 'n':
    print("Thank you for using the program!")
    print("Remember the truth is out there!")

def state(ufo):
  print("\033c")
  state = str(input("Please enter the state abbreviation: "))
  print("Here is the data on " + state.upper())
  print(ufo[ufo.State == state.upper()])
  option = input("Do you want to look at more data?(y/n) ")
  if option == 'y':
    mainMenu(ufo)
  elif option == 'n':
    print("Thank you for using the program!")
    print("Remember the truth is out there!")

def shape(ufo):
  print("\033c")
  print("Here are common shapes to examine: ")
  print("disk, cigar, sphere, light, other, circle")
  shape = str(input("Please enter the shape you want to examine: "))
  print("Here is the data on ufo's shaped as a: " + shape.upper())
  print(ufo[ufo.Shape == shape.upper()])
  graph = input("Would you like to see a bar graph of this data? ")
  if graph == "y":
    ufo.Shape.value_counts().plot(kind="bar")
    plt.show()
  else:
    mainMenu(ufo)

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


def mainMenu(ufo):
  print("\033c")
  print("1. UFO's by City")
  print("2. UFO's by State")
  print("3. UFO by Shape")
  print("4. UFO's by Year")
  print("5. Other")
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

#This function is where all of the data will be pulled in from.
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
    

#This is the main function that introduces the user to the program. 
def intro():
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

intro()
