# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Test_function
   Description :
   Author :       Jamerri
   date：          2022/3/19
-------------------------------------------------
   Change Activity:
                   2022/3/19:
-------------------------------------------------
"""

import os
import shutil
import xlwt
import pandas as pd

# 数据存储文件夹
dirs = './ddd'
# 文件数量
file_number = 9


# 数据分类函数
def class_files_function(f_num):
    # 获得文件名
    filelist = os.listdir(dirs)
    # print(filelist)

    # 按照实验组数对数据进行分类
    for i in range(int(f_num / 3)):
        path = './ddd/'
        new_dir = os.path.join(path, str(i + 1))
        os.mkdir(new_dir)
        # print(new_dir)
        source_1 = os.path.join(path, filelist[3 * i])
        shutil.move(source_1, new_dir)
        source_2 = os.path.join(path, filelist[3 * i + 1])
        shutil.move(source_2, new_dir)
        source_3 = os.path.join(path, filelist[3 * i + 2])
        shutil.move(source_3, new_dir)


# 对应的文件夹数据合并为Excel
def write_to_excel(f_num):
    for i in range(int(f_num / 3)):
        num = i + 1

        sub_dirs = './ddd/' + str(i + 1)
        sub_filelist = os.listdir(sub_dirs)

        file_path_1 = './ddd/' + str(i + 1) + '/' + sub_filelist[0]
        file_path_2 = './ddd/' + str(i + 1) + '/' + sub_filelist[1]
        file_path_3 = './ddd/' + str(i + 1) + '/' + sub_filelist[2]

        f1 = open(file_path_1, 'r', encoding='utf-8')
        f2 = open(file_path_2, 'r', encoding='utf-8')
        f3 = open(file_path_3, 'r', encoding='utf-8')

        wb = xlwt.Workbook(encoding='utf-8')

        ws1 = wb.add_sheet('1_robot')
        ws2 = wb.add_sheet('2_robot')
        ws3 = wb.add_sheet('3_robot')

        r_txt(f1, ws1, wb, num)
        r_txt(f2, ws2, wb, num)
        r_txt(f3, ws3, wb, num)
    print("Success!!")


# 遍历txt函数
def r_txt(f_n, ws_n, w_b, n):
    row = 1
    col = 0
    k = 1
    for lines in f_n:
        a = lines.split('\t')
        k += 1
        for j in range(len(a)):
            ws_n.write(row, col, a[j])
            col += 1
        row += 1
        col = 0
    w_b.save("./ddd/" + str(n) + "/robots.xls")


class_files_function(file_number)
write_to_excel(file_number)
