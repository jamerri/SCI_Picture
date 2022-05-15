# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Fig3
   Description :
   Author :       Jamerri
   date：          2022/5/16
-------------------------------------------------
   Change Activity:
                   2022/5/16:
-------------------------------------------------
"""


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MultipleLocator

# 定义数据
x_1 = [1.5, ]
y_1 = [0.5, ]
z_1 = [3.5, ]
x_2 = [1, ]
y_2 = [1, ]
z_2 = [4.5, ]
x_3 = [0.5, ]
y_3 = [1.5, ]
z_3 = [5.5, ]

# 导入Times New Roman字体
plt.rc('font', family='Times New Roman', size=12)

# 设置3d图纸
fig = plt.figure()
ax = Axes3D(fig)

# # 初始化视角
# ax.view_init(elev=10., azim=20)

# 设置坐标轴标题
ax.set_xlabel('X (m)', fontsize=12)  # x轴标题
ax.set_ylabel('Y (m)', fontsize=12)  # y轴标题
ax.set_zlabel('Z (m)', fontsize=12)  # z轴标题

# 设置坐标轴范围
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_zlim(0, 6)

# # 绘制折线图，添加数据点，设置点的大小
# figure1 = ax.plot(x_1, y_1, z_1, 'b-', marker='o', markersize=3, linewidth=0.5)
# figure2 = ax.plot(x_2, y_2, z_2, 'r-', marker='s', markersize=3, linewidth=0.5)
# figure3 = ax.plot(x_3, y_3, z_3, 'k-', marker='^', markersize=3, linewidth=0.5)
#
# # 起点位置图案
# plt.plot(x_1[0], y_1[0], z_1[0], 'k-', marker='o', markersize=4)
# plt.plot(x_2[0], y_2[0], z_2[0], 'k-', marker='s', markersize=4)
# plt.plot(x_3[0], y_3[0], z_3[0], 'k-', marker='^', markersize=4)

# 设置figure_size尺寸
plt.rcParams['figure.figsize'] = (6.0, 8.0)

# # 保存图片
# plt.savefig(r'./fig2.tiff', bbox_inches='tight', dpi=300)
plt.show()


## 学习资料 https://zhuanlan.zhihu.com/p/258421290?ivk_sa=1024320u