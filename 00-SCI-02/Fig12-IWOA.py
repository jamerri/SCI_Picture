# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Fig12-IWOA.py
   Description :
   Author :       Jamerri
   date：          2022/10/28
-------------------------------------------------
   Change Activity:
                   2022/10/28:
-------------------------------------------------
"""

import matplotlib.pyplot as plt
import xlrd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# 源位置参数
X_position = 7.35
Y_position = 3.05
Z_position = 1.35

# 源定位步数
step_num = 30

# 读取路径
book = xlrd.open_workbook(filename=r"../data/IWOA-3D-INV-135.xlsx")

# 读取名字为Sheet1的表
sheet1 = book.sheet_by_name("1_robot")

# 读取名字为Sheet2的表
sheet2 = book.sheet_by_name("2_robot")

# 读取名字为Sheet3的表
sheet3 = book.sheet_by_name("3_robot")


# 判断此次实验的步数
rowamount = sheet1.nrows
step_total = rowamount - 12

# 用于存储1号机器人的数组
robot_1_x = []
robot_1_y = []
robot_1_z = []

row_num = 8
while row_num <= (step_total + 8):
    # 将表中第一列的1-100行数据写入wind_speed数组中
    robot_1_x.append(4.97 - float(sheet1.cell_value(row_num, 2)))
    robot_1_y.append(2.38 + float(sheet1.cell_value(row_num, 1)))
    robot_1_z.append(float(sheet1.cell_value(row_num, 3)))
    row_num = row_num + 1
# # print(robot_1_x)
# print("This experimental points are " + str(len(robot_1_x)) + "!!!!")

# 用于存储2号机器人的数组
robot_2_x = []
robot_2_y = []
robot_2_z = []
row_num = 8

while row_num <= (step_total + 8):
    # 将表中第一列的1-100行数据写入wind_speed数组中
    robot_2_x.append(4.97 - float(sheet2.cell_value(row_num, 2)))
    robot_2_y.append(2.38 + float(sheet2.cell_value(row_num, 1)))
    robot_2_z.append(float(sheet2.cell_value(row_num, 3)))
    row_num = row_num + 1

# 用于存储3号机器人的数组
robot_3_x = []
robot_3_y = []
robot_3_z = []
row_num = 8

while row_num <= (step_total + 8):
    # 将表中第一列的1-100行数据写入wind_speed数组中
    robot_3_x.append(4.97 - float(sheet3.cell_value(row_num, 2)))
    robot_3_y.append(2.38 + float(sheet3.cell_value(row_num, 1)))
    robot_3_z.append(float(sheet3.cell_value(row_num, 3)))
    row_num = row_num + 1

# 图像制作

# 画圆线函数
def plot_circle(center=(7.35, 3.05), r=0.5):
    x = np.linspace(center[0] - r, center[0] + r, 5000)
    y1 = np.sqrt(r**2 - (x-center[0])**2) + center[1]
    y2 = -np.sqrt(r**2 - (x-center[0])**2) + center[1]
    plt.plot(x, y1, 'k--')
    plt.plot(x, y2, 'k--')


# 导入Times New Roman字体
plt.rc('font', family='Times New Roman', size=12)

# 设置xtick和ytick的方向：in、out、inout
# plt.rcParams['xtick.direction'] = 'in'
# plt.rcParams['ytick.direction'] = 'in'
# plt.rcParams['ztick.direction'] = 'in'

# new a figure and set it into 3d
fig = plt.figure(figsize=(8, 6))
# ax = fig.gca(projection='3d')
ax = fig.add_subplot(projection='3d')

# 隐藏坐标轴的面
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

# 设置各个坐标轴下限和上限
ax.set_xlim3d(xmin=0, xmax=8)
ax.set_ylim3d(ymin=0, ymax=5)
ax.set_zlim3d(zmin=0.4, zmax=1.6)

tmp_planes = ax.zaxis._PLANES
ax.zaxis._PLANES = (tmp_planes[2], tmp_planes[3],
                    tmp_planes[0], tmp_planes[1],
                    tmp_planes[4], tmp_planes[5])

# 设置坐标轴标题
ax.set_xlabel('X (m)', fontsize=12)  # x轴标题
ax.set_ylabel('Y (m)', fontsize=12)  # y轴标题
ax.set_zlabel('Z (m)', fontsize=12)  # y轴标题

ax.grid(False)  # 默认True，风格线
# ax.set_xticks([])#不显示x坐标轴
# ax.set_yticks([])#不显示y坐标轴
# ax.set_zticks([])#不显示z坐标轴
# plt.axis('off')#关闭所有坐标轴

# # 绘制框线
# x_1 = [8, 8]
# y_1 = [0, 0]
# z_1 = [1.6, 0.4]
# ax.plot(x_1, y_1, z_1, c='k')
#
# x_2 = [8, 8]
# y_2 = [5, 5]
# z_2 = [1.6, 0.4]
# ax.plot(x_2, y_2, z_2, c='k')

# 设置视角
ax.view_init(5, 300)

# 绘制折线图，添加数据点，设置点的大小
ax.plot(robot_1_x, robot_1_y, robot_1_z, c='#f7903d', marker='o', markersize=3, linewidth=0.5)
ax.plot(robot_2_x, robot_2_y, robot_2_z, c='#4d85bd', marker='s', markersize=3, linewidth=0.5)
ax.plot(robot_3_x, robot_3_y, robot_3_z, c='#59a95a', marker='^', markersize=3, linewidth=0.5)

# 源位置图案
plot_circle((X_position, Y_position), r=0.5)
plt.plot(X_position, Y_position, Z_position, c='r', marker='o', markersize=6, alpha=0.4)

# 起点位置图案
plt.plot(robot_1_x[0], robot_1_y[0], robot_1_z[0], 'k-', marker='o', markersize=4)
plt.plot(robot_2_x[0], robot_2_y[0], robot_2_z[0], 'k-', marker='s', markersize=4)
plt.plot(robot_3_x[0], robot_3_y[0], robot_3_z[0], 'k-', marker='^', markersize=4)

# 终点位置图案
plt.plot(robot_1_x[-1], robot_1_y[-1], robot_1_z[-1], 'k-', marker='o', markersize=4)
plt.plot(robot_2_x[-1], robot_2_y[-1], robot_2_z[-1], 'k-', marker='s', markersize=4)
plt.plot(robot_3_x[-1], robot_3_y[-1], robot_3_z[-1], 'k-', marker='^', markersize=4)

# # 烟羽发现点位置图案
# plt.plot(robot_1_x[-1], robot_1_y[-1], 'k-', marker='o', markersize=4)
#
# # 烟羽跟踪点位置图案
# plt.plot(robot_1_x[-1], robot_1_y[-1], 'k-', marker='o', markersize=4)
#
# # 源确认点位置图案
# plt.plot(robot_1_x[-1], robot_1_y[-1], 'k-', marker='o', markersize=4)

plt.savefig(r'./3D_trajectory_111.tiff', bbox_inches='tight', dpi=300)  # 保存图
plt.show()
