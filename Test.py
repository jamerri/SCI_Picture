#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/18 4:48 下午
# @Author : Jamerri
# @FileName: Test.py
# @Email : jamerri@163.com
# @Software: PyCharm


import os
import shutil
import pandas as pd

dirs = './ddd'

myList = os.listdir(dirs)
print(myList)

for i in range(int(len(myList) / 3)):
    path = './ddd/'
    new_dir = os.path.join(path, str(i + 1))
    os.mkdir(new_dir)
    print(new_dir)
    source_1 = os.path.join(path, myList[3 * i])
    shutil.move(source_1, new_dir)
    source_2 = os.path.join(path, myList[3 * i + 1])
    shutil.move(source_2, new_dir)
    source_3 = os.path.join(path, myList[3 * i + 2])
    shutil.move(source_3, new_dir)

for i in range(3):
    path = './ddd/'
    file_txt_1 = path + str(i + 1) + '/' + myList[3 * i]
    file_txt_2 = path + str(i + 1) + '/' + myList[3 * i + 1]
    file_txt_3 = path + str(i + 1) + '/' + myList[3 * i + 2]

    file_excel = path + str(i + 1) + '/' + '2d_robot_data.xlsx'
    writer = pd.ExcelWriter(file_excel)

    df1 = pd.read_table(file_txt_1)
    df2 = pd.read_table(file_txt_2)
    df3 = pd.read_table(file_txt_3)
    df1.to_excel(writer, 'sheet1')
    df2.to_excel(writer, 'sheet2')
    df3.to_excel(writer, 'sheet3')

    writer.save()
    writer.close()