#!/usr/bin/env python
# encoding: utf-8
'''

@author: Carl
        ｛源前｝
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 520liyuan1314@gmail.com 源前
          291437965@qq.com 
@SoftWare: PyCharm
@FileName: py04_Frist_def.py
@Program：TheOne_PythonFull
@Time: 2020/3/22 16:34
@desc:
'''
import math
'摄氏度转化公式,C >>>F '
# def F_1(C):
#     F = C * 9 / 5 + 32
#     return str(F) + ' F'
# C_F = F_1(55)
# print(C_F)

'重量转换器  g>>>kg'
# def weight(c):
#     zh = c / 1000
#     return str(zh) + 'kg'
#
#
# wei = weight(int(input('请输入物品的g数\n')))
# # input('请输入物品的g数')
# print(wei)
'''求直角三角形斜边长的函数
    
    这里要导入一个Math函数才能进行运算'''
#
# def XieBian(a, b):
#     xiebian = float(math.sqrt((pow(a, 2) + pow(b, 2))))
#     print('这个三角形的斜边长为：' + str(xiebian))
#
#
# Jisuan = XieBian(3, 4)

'设计我自己的函数 一个书写的函数 '
'用于在桌面进行符合条件的配比 ' \
'如果不满足  则创建一个相应的文件'

# file=open('D://配置/缓存/桌面/test.txt','w')
# file.write('see you again!!!')


# def text_create(name, msg):
#     # 定义函数的名称和参数
#     desktop_path = 'D://配置/缓存/桌面/'
#     # open函数打开的路径
#     full_path = desktop_path + name + '.txt'
#     # 我们给该文件取什么样的名字
#     file = open(full_path, 'w',encoding='utf-8')
#     # open函数的应用，参数为full_path，以及文本的写入语句 'w'
#     # 他是写入模式的意思，如果没有该文件则创建一个文件且符合名称要求
#     file.write(msg)
#     # 写入传入的参数 msg
#     file.close()
#     # 关闭文本并退出编辑
#
#
# print('Done')
# text_create('see you again', 'hello world！！！\n'
#                              'see you again!')

