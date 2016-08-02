#This file is where I will test out other things that I want to look at. 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

cols = ['City', 'Color', 'Shape', 'State', 'Time']
ufo = pd.read_csv('http://bit.ly/uforeports', names=cols)


ufo.Shape.value_counts().plot(kind="bar")
plt.show()