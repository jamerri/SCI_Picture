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
import numpy as np


# 定义点数据
x_1 = [1.5, 2.5, 3.5, 4.5, 5.5]
y_1 = [0.5, 0.7, 0.9, 1.1, 1.3]
z_1 = [1, 1.5, 2, 2.5, 3]
x_2 = [1, 2, 3, 4, 5]
y_2 = [1, 2, 3, 4, 5]
z_2 = [3, 3.5, 4, 4.5, 5]
x_3 = [0.5, 0.7, 0.9, 1.1, 1.3]
y_3 = [1.5, 2.5, 3.5, 4.5, 5.5]
z_3 = [5, 4.5, 4, 3.5, 3]

# 定义面数据
x = np.linspace(0, 8, 8)
y = np.linspace(0, 8, 8)
X, Y = np.meshgrid(x, y)

# 定义相交线
xx_1 = [1.5, 3.5]
yy_1 = [0.5, 0.9]
zz_1 = [1, 1]
xx_2 = [1, 3]
yy_2 = [1, 3]
zz_2 = [3, 3]
xx_3 = [0.5, 0.9]
yy_3 = [1.5, 3.5]
zz_3 = [5, 5]

# 定义垂直线
xxx_1 = [3.5, 3.5]
yyy_1 = [0.9, 0.9]
zzz_1 = [1, 2]
xxx_2 = [3, 3]
yyy_2 = [3, 3]
zzz_2 = [3, 4]
xxx_3 = [0.9, 0.9]
yyy_3 = [3.5, 3.5]
zzz_3 = [5, 4]


# 线条立方体
def plot_linar_cube(ax, x, y, z, dx, dy, dz, color='black'):
    # fig = plt.figure()
    # ax = Axes3D(fig)
    xx = [x, x, x + dx, x + dx, x]
    yy = [y, y + dy, y + dy, y, y]
    kwargs = {'alpha': 1, 'color': color}
    ax.plot3D(xx, yy, [z] * 5, **kwargs)
    ax.plot3D(xx, yy, [z + dz] * 5, **kwargs)
    ax.plot3D([x, x], [y, y], [z, z + dz], **kwargs)
    ax.plot3D([x, x], [y + dy, y + dy], [z, z + dz], **kwargs)
    ax.plot3D([x + dx, x + dx], [y + dy, +y + dy], [z, z + dz], **kwargs)
    ax.plot3D([x + dx, x + dx], [y, y], [z, z + dz], **kwargs)
    # plt.title('Cube')
    # plt.show()


# 导入Times New Roman字体
plt.rc('font', family='Times New Roman', size=12)

# 设置3d图纸
fig = plt.figure()
ax = Axes3D(fig)

# 设置坐标轴标题
ax.set_xlabel('X', fontsize=12)  # x轴标题
ax.set_ylabel('Y', fontsize=12)  # y轴标题
ax.set_zlabel('Z', fontsize=12)  # z轴标题

# 设置坐标轴范围
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_zlim(0, 6)

# 隐藏坐标轴刻度线
ax = plt.gca()
ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
ax.axes.zaxis.set_ticks([])

# 导入立方体框线
plot_linar_cube(ax, 0, 0, 0, 8, 8, 6)

# 绘制折线图，添加数据点，设置点的大小
ax.plot(x_1, y_1, z_1, '-', c='#f7903d', marker='o', markersize=3.5, linewidth=0.75)
ax.plot(x_2, y_2, z_2, '-', c='#4d85bd', marker='s', markersize=3.5, linewidth=0.75)
ax.plot(x_3, y_3, z_3, '-', c='#59a95a', marker='^', markersize=3.5, linewidth=0.75)

# 绘制折线图，添加数据点，设置点的大小
ax.plot(xx_1, yy_1, zz_1, 'k--', linewidth=1)
ax.plot(xx_2, yy_2, zz_2, 'k--', linewidth=1)
ax.plot(xx_3, yy_3, zz_3, 'k--', linewidth=1)

# 绘制折线图，添加数据点，设置点的大小
ax.plot(xxx_1, yyy_1, zzz_1, 'k--', linewidth=1)
ax.plot(xxx_2, yyy_2, zzz_2, 'k--', linewidth=1)
ax.plot(xxx_3, yyy_3, zzz_3, 'k--', linewidth=1)

# 绘制折线图，添加数据点，设置点的大小
ax.plot(x_1, y_1, '--', c='#f7903d', marker='o', markersize=3.5, linewidth=0.75)
ax.plot(x_2, y_2, '--', c='#4d85bd', marker='s', markersize=3.5, linewidth=0.75)
ax.plot(x_3, y_3, '--', c='#59a95a', marker='^', markersize=3.5, linewidth=0.75)

# 绘制平面
ax.plot_surface(X, Y, Z=X * 0 + 1, color='gray', alpha=0.22)
ax.plot_surface(X, Y, Z=X * 0 + 3, color='gray', alpha=0.22)
ax.plot_surface(X, Y, Z=X * 0 + 5, color='gray', alpha=0.22)

# 设置figure_size尺寸
plt.rcParams['figure.figsize'] = (6.0, 8.0)

# 调整视角(仰角， 方位角)
ax.view_init(elev=7, azim=-123)

# 保存图片
plt.savefig(r'./fig2.tiff', bbox_inches='tight', dpi=300)

plt.show()


## 学习资料 https://zhuanlan.zhihu.com/p/258421290?ivk_sa=1024320u