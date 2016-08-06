import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


cols = ['City', 'Color', 'Shape', 'State', 'Time']
ufo = pd.read_csv('http://bit.ly/uforeports', names=cols)

print("\033c")
print("Here are the shapes to examine: ")
print("Disk")
print("Cigar")
print("Light")
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
  print("Sphere")
  print("Other")
  print('\n')
  shapes = []
  print("You choose to look at the graph.")
  print("Enter the shapes you want included. Type 'quit' to exit.")
  while True:
    view = input("Please enter the shape you want included on the graph: ")
    if view == "quit":
      break
    else: 
      shapes.append(view)
  diskCount, lightCount, triangleCount, cigarCount, sphereCount, otherCount = [], [], [], [], [], []
  yearDisk, yearLight, yearTriangle, yearCigar, yearSphere, yearOther = [], [], [], [], [], []
  for shape in shapes:
    startYear, diskYear, lightYear, triangleYear, cigarYear, sphereYear, otherYear = 1930, 1930, 1930, 1930, 1930, 1930, 1930
    while startYear < 2001:
      yearString = str(startYear)
      df = ufo[ufo.Time.str.contains(yearString)]
      if shape == "disk":
        specificShape = df[df.Shape == shape.upper()]
        number = specificShape.Shape.count()
        diskCount.append(int(number))
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
  plt.plot(yearDisk, diskCount, linewidth=2, c="red")
  plt.plot(yearLight, lightCount, linewidth=2, c="blue")
  plt.plot(yearTriangle, triangleCount, linewidth=2, c="black")
  plt.plot(yearCigar, cigarCount, linewidth=2, c="green")
  plt.plot(yearSphere, sphereCount, linewidth=2, c="orange")
  plt.plot(yearOther, otherCount, linewidth=2, c="purple")
  plt.xlabel("Year", fontsize=14)
  plt.ylabel("Count of UFO Shape", fontsize=12)
  plt.show()


# shapes = ["disk", "light", "triangle", "cigar", "sphere", "other" ]


def shape(ufo):
  print("\033c")
  print("Here are common shapes to examine: ")
  print("Disk")
  print("Cigar")
  print("Sphere")
  print("Light")
  print("Circle")
  print("Other")
  shape = str(input("Please enter the shape you want to examine: "))
  print("Here is the data on ufo's shaped as a: " + shape.upper())
  print(ufo[ufo.Shape == shape.upper()])
  graph = input("Would you like to see a bar graph of this data?(y/n) ")
  if graph == "y":
    ufo.Shape.value_counts().plot(kind="bar")
    plt.show()
  else:
    mainMenu(ufo)
