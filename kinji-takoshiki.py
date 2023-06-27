# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 20:29:45 2023

@author: square

https://qiita.com/trickre/items/0eabe7f57ab82d4b8631
"""

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10, 10, 20)
y = 0.0001*x**10 + 0.01*x**7 + 1000*x**3 + 10000*x

#近似式の係数
res1=np.polynomial.Polynomial.fit(x, y, deg=1)
res2=np.polynomial.Polynomial.fit(x, y, deg=2)
res3=np.polynomial.Polynomial.fit(x, y, deg=3)
res4=np.polynomial.Polynomial.fit(x, y, deg=4)
res10=np.polynomial.Polynomial.fit(x, y, deg=10)

print("10次近似式")
print(res10)

#近似式の計算
y1 = res1(x)
y2 = res2(x)
y3 = res3(x)
y4 = res4(x)
y10 = res10(x)

#グラフ表示
plt.scatter(x, y, label='original')
plt.plot(x, y1, label='1deg')
plt.plot(x, y2, label='2deg')
plt.plot(x, y3, label='3deg')
plt.plot(x, y10, label='10deg')
plt.legend()
plt.show()

