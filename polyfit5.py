# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:02:28 2023

@author: square
"""

import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt


ax = plt.subplot(1,1,1)

x = np.linspace(0, 10, 30)
y = 0.001*x**5 + 9*x**4 + 2*x**3 + 10*x**2 + 0.3*x + 3000*np.random.rand(30)

ax.scatter(x,y)

# popt = np.polyfit(x, y, 5)
# yy = popt[0]*x**5 + popt[1]*x**4 + popt[2]*x**3 + popt[3]*x**2 + popt[4]

popt = np.polyfit(x, y, 4)
yy =  popt[0]*x**4 +popt[1]*x**3 + popt[2]*x**2 + popt[3]

ax.plot(x,yy)



