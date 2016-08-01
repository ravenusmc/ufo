import pandas as pd 

cols = ['City', 'Color', 'Shape', 'State', 'Time']
ufo = pd.read_csv('http://bit.ly/uforeports', names=cols)
#print(ufo.head())


# print(ufo[(ufo.State == "GA") & (ufo.City == "Atlanta")])

####### UFO Program ##############

#### Helper Functions #############

#This function is for validation for user input. 
def valid(choice):
  if choice == 'y' or choice == 'n':
    return True 
  else:
    return False


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
  state = str(input("Please enter the state abbreviation: "))
  print("Here is the data on " + state.upper())
  print(ufo[ufo.State == state.upper()])
  option = input("Do you want to look at more data?(y/n) ")
  if option == 'y':
    start(ufo)
  elif option == 'n':
    print("Thank you for using the program!")
    print("Remember the truth is out there!")

  # option = input("Do you want to save this data stream to refine it more?(y/n) ")
  # if option == 'y':
  #   citySave = ufo[ufo.City == city]
  # else: 
  #   print("Data not saved moving on!")

def other(ufo):
  option = input("Do you want to look at UFO count by city?(y) ")
  if option == "y":
    print(ufo.City.value_counts())

def start(ufo):
  print("\033c")
  print("Here there will be where you select what you want to look at")
  choice = input("Do you want to look at UFO's by 'city', 'state' or 'other': ")
  if choice == 'city':
    city(ufo)
  elif choice == "state":
    state(ufo)
  elif choice == "other":
    other(ufo)

def main():
  print("\033c")
  cols = ['City', 'Color', 'Shape', 'State', 'Time']
  ufo = pd.read_csv('http://bit.ly/uforeports', names=cols)
  print("Thank you for using the program!")
  choice = input('If you need to see directions on how to use this type help or next to move on. ' )
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
  if choice == 'y':
    main()
  elif choice == 'n':
    print('Thank you for using the program! Hope you come again!')
    print('Remember that the truth is out there!')

intro()
