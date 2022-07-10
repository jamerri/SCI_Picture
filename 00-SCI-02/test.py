# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       Jamerri
   date：          2022/7/10
-------------------------------------------------
   Change Activity:
                   2022/7/10:
-------------------------------------------------
"""

# coding:utf-8

"""
Author: roguesir
Date: 2017/8/30
GitHub: https://roguesir.github.com
Blog: http://blog.csdn.net/roguesir
"""

import numpy as np
import matplotlib.pyplot as plt


def sgn(value, value_i, values_t):
    if value < 2.5 + (value_i * values_t):
        return 12.5
    else:
        return 0


plt.figure(figsize=(6, 4))
i = 0
t = 6
y = np.array([])

for i in range(150):
    x = np.linspace(0 + (i * t), 6 + (i * t), 100)

    for v in x:
        y = np.append(y, np.linspace(sgn(v, i, t), sgn(v, i, t), 1))
print(y)
l = plt.plot(x, y, 'b', label='type')
plt.legend()
plt.show()