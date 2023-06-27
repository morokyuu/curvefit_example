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
y = x**2 + 50* np.random.rand(30)

ax.scatter(x,y)

popt = np.polyfit(x, y, 1)
yy = popt[0]*x + popt[1]

ax.plot(x,yy)



