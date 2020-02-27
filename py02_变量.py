#!/usr/bin/env python
# encoding: utf-8
'''
@author: Carl
        ｛源前｝
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 520liyuan1314@gmail.com 源前
          291437965@qq.com 
@SoftWare: PyCharm
@FileName: py02_变量.py
@Time: 2020/2/26 20:26
@desc:
'''

# 变量的名称必须符合标准。由字母，下划线。数字组成.大小写是不同的
name = "字符串"  # 字符串
age = 23  # 数值
sex = True  # 布尔，同样为数值。可以用0/1来表示。 一般用1表示真，0表示假
Score = 97.6  # 双精度

'''
'''
qqName=123456
qqPassword=7654321
print(qqName);print(qqPassword)

qqName=111111
qqPassword=2333
print(qqName);print(qqPassword)
#由于python是逐步执行的，所以每一次定义变量都会使得变量的值发生变换
