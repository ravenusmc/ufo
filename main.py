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
    start();
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
    start(ufo)
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
    start(ufo)
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
    start(ufo)

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
    start(ufo)

def start(ufo):
  print("\033c")
  print("Here there will be where you select what you want to look at")
  choice = input("Do you want to look at UFO's by 'city', 'state', 'shape' or 'other': ")
  while not validStart(choice):
    choice = input("Do you want to look at UFO's by 'city', 'state', 'shape' or 'other': ")
  if choice == 'city':
    city(ufo)
  elif choice == "state":
    state(ufo)
  elif choice == 'shape':
    shape(ufo)
  elif choice == "other":
    other(ufo)

#This function is where all of the data will be pulled in from.
def main():
  print("\033c")
  cols = ['City', 'Color', 'Shape', 'State', 'Time']
  ufo = pd.read_csv('http://bit.ly/uforeports', names=cols)
  print("Thank you for using the program!")
  choice = input("If you need to see directions on how to use this type 'help' or 'next' to move on. " )
  while not validMain(choice):
    choice = input("If you need to see directions on how to use this type 'help' or 'next' to move on. " )
  if choice == 'help':
    help(ufo)
  elif choice == 'next':
    start(ufo)

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
