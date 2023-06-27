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
y = 10*x**3 + 0.3*x**2 + 0.5*x + 100* np.random.rand(30)

ax.scatter(x,y)


model_5 = lambda t,a,b,c,d,e : a*t**5 + b*t**4 + c*t**3 + d*t**2 + e*t
popt, pcov = optimize.curve_fit(model_5, x, y)
print(popt)
print(pcov)
xx = np.linspace(0,10,100)
yy = popt[0]*xx**5 + popt[1]*xx**4 + popt[2]*xx**3 + popt[3]*xx*2 + popt[4]*xx
ax.plot(xx,yy)



