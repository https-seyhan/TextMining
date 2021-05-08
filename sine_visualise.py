import numpy as np
import pandas as pd
import random
#import tkinter
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams

# Sine function visualisation
def visualise():
	print('Test')
	%matplotlib inline

rcParams['figure.figsize'] = 12, 10

#Define input array with angles from 60deg to 300deg converted to radians
x = np.array([i*np.pi/180 for i in range(60,300,4)])
np.random.seed(10)  #Setting seed for reproducability
y = np.sin(x) + np.random.normal(0,0.15,len(x))
data = pd.DataFrame(np.column_stack([x,y]),columns=['x','y'])
plt.plot(data['x'],data['y'],'.')

if __name__ == '__main__':
	visualise()
