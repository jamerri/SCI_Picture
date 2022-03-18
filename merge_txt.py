#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/18 1:32 下午
# @Author : Jamerri
# @FileName: merge_txt.py
# @Email : jamerri@163.com
# @Software: PyCharm


import pandas as pd
import shutil
import os

for i in range(3):
    file_txt_1 = str(i + 1) + '/' + '1.txt'
    file_txt_2 = str(i + 1) + '/' + '2.txt'
    file_txt_3 = str(i + 1) + '/' + '3.txt'

    file_excel = str(i + 1) + '/' + str(i + 1) + '.xlsx'
    writer = pd.ExcelWriter(file_excel)

    df1 = pd.read_table(file_txt_1)
    df2 = pd.read_table(file_txt_2)
    df3 = pd.read_table(file_txt_3)
    df1.to_excel(writer, 'sheet1')
    df2.to_excel(writer, 'sheet2')
    df3.to_excel(writer, 'sheet3')

    writer.save()
    writer.close()
