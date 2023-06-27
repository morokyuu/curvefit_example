# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 20:36:03 2023

@author: square
"""

import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt


ax = plt.subplot(1,1,1)

x = np.linspace(0, 10, 30)
y = x**2 + 50* np.random.rand(30)

ax.scatter(x,y)


model_2 = lambda t,a,b : a*t**2 + b*t
popt, pcov = optimize.curve_fit(model_2, x, y)
print(popt)
xx = np.linspace(0,10,10)
yy = popt[0]*xx**2 + popt[1]*xx
ax.plot(xx,yy)



