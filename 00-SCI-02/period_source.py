# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     period_source
   Description :
   Author :       Jamerri
   date：          2022/7/10
-------------------------------------------------
   Change Activity:
                   2022/7/10:
-------------------------------------------------
"""


import numpy as np
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes


def sgn(value, value_i, values_t):
    if value < 2.5 + (value_i * values_t):
        return 12.5
    else:
        return 0


# 导入Times New Roman字体
plt.rc('font', family='Times New Roman', size=15)

# 设置xtick和ytick的方向：in、out、inout
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

i = 0
t = 6
y = np.array([])

for i in range(150):
    x = np.linspace(0 + (i * t), 6 + (i * t), 100)
    for v in x:
        y = np.append(y, np.linspace(sgn(v, i, t), sgn(v, i, t), 1))

x = np.linspace(0, 900, 15000)

bax = brokenaxes(xlims=((0, 25), (875, 900)), hspace=.05, despine=True)

# 设置坐标轴范围
plt.xlim(0, 900)
plt.ylim(0, 15)

# 设置坐标轴标题
bax.set_xlabel('Time (s)', fontsize=15)  # x轴标题
bax.set_ylabel('Release rate (mg/s)', fontsize=15)  # y轴标题

l = bax.plot(x, y, c='#6e9ece')

# 保存图片
plt.rcParams['figure.figsize'] = (8.0, 6.0)  # 设置figure_size尺寸
plt.savefig("source_release.tiff", bbox_inches='tight', dpi=600)
plt.show()
