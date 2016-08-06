import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


cols = ['City', 'Color', 'Shape', 'State', 'Time']
ufo = pd.read_csv('http://bit.ly/uforeports', names=cols)


diskCount, lightCount, triangleCount, cigarCount = [], [], [], []
shapes = ["disk", "light", "triangle", "cigar"]
yearDisk, yearLight, yearTriangle, yearCigar = [], [], [], []

for shape in shapes:
  startYear, diskYear, lightYear, triangleYear, cigarYear = 1930, 1930, 1930, 1930, 1930
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
    startYear += 1


plt.plot(yearDisk, diskCount, linewidth=2, c="red")
plt.plot(yearLight, lightCount, linewidth=2, c="blue")
plt.plot(yearTriangle, triangleCount, linewidth=2, c="black")
plt.plot(yearCigar, cigarCount, linewidth=2, c="orange")
plt.xlabel("Year", fontsize=14)
plt.ylabel("Count of UFO Shape", fontsize=12)
plt.show()


# diskCount, lightCount = [], []
# shapes = ["disk", "light"]



