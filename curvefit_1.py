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


model_1 = lambda t,a,b : a*t + b
popt, pcov = optimize.curve_fit(model_1, x, y)
print(popt)
xx = np.linspace(0,10,2)
yy = popt[0] * xx + popt[1]
ax.plot(xx,yy)



