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
y = 10*x**3 + 0.3*x**2 + 0.5*x + 100* np.random.rand(30)

ax.scatter(x,y)

popt = np.polyfit(x, y, 3)
yy = popt[0]*x**3 + popt[1]*x**2 + popt[2]*x

ax.plot(x,yy)



