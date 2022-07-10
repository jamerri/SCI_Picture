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


from brokenaxes import brokenaxes
import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook
import math
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# fig = plt.figure(figsize=(5,2))
# bax = brokenaxes(xlims=((0, .1), (.4, .7)), ylims=((-1, .7), (.79, 1)), hspace=.05, despine=False)
# x = np.linspace(0, 1, 100)
# bax.plot(x, np.sin(10 * x), label='sin')
# bax.plot(x, np.cos(10 * x), label='cos')
# bax.legend(loc=3)
# bax.set_xlabel('time')
# bax.set_ylabel('value')



# 图像制作

# 导入Times New Roman字体
plt.rc('font', family='Times New Roman', size=15)

# 设置xtick和ytick的方向：in、out、inout
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

# X数据
x = np.linspace(0, 900, 90000)

y = []
i = 0
k = 0
t = 6
for j in x:
    if (k * t) < j <= (2.5 + k * t):
        y = 12.5
        y = np.append(y, np.linspace(12.5, 12.5, 1))
    if (2.5 + k * t) < j <= (6 + k * t):
        y = 0
        y = np.append(y, np.linspace(0, 0, 1))



print(y)

# # 设置坐标轴标题
# plt.xlabel('Time (s)', fontsize=15)  # x轴标题
# plt.ylabel('Release rate (mg/s)', fontsize=15)  # y轴标题
#
# # 设置坐标轴范围
# plt.xlim(0, 900)
# plt.ylim(0, 15)
#
# # 坐标轴隐藏
# ax = plt.gca()
# ax.spines['top'].set_visible(False)  # 隐藏上端脊梁
# ax.spines['right'].set_visible(False)  # 隐藏右端脊梁
#
# # 画折线图
# l1, = plt.plot(x, concentration1, ls='-', linewidth=1.5, c='#12c2e9')
# l2, = plt.plot(x, concentration2, ls='-', linewidth=1.5, c='#c471ed')
# l3, = plt.plot(x, concentration3, ls='-', linewidth=1.5, c='#f64f59')
#
# # 保存图片
# plt.rcParams['figure.figsize'] = (8.0, 6.0)  # 设置figure_size尺寸
# plt.savefig(r'pic/source_release.tiff', bbox_inches='tight', dpi=300)
# plt.show()

