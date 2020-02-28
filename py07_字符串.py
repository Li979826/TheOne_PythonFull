#!/usr/bin/env python
# encoding: utf-8
'''

@author: Carl
        ｛源前｝
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 520liyuan1314@gmail.com 源前
          291437965@qq.com 
@SoftWare: PyCharm
@FileName: py07_字符串.py
@Program：TheOne_PythonFull
@Time: 2020/2/27 14:31
@desc:
'''
s1 = 'abddefg'
s2 = '''123456'''
s3 = "9785223"
str = "djdsljflsjdkj"

print(s1)
print(s2)
print(s3)
# 提取字符串中的索引值
print(s1[0])
print(s2[1])
print(s3[2])
print(s1[0:4])
print(s1[1] * 2)
print(s1 * 2)
print(s2 + s1)
print(s1[:-1])  # 前面的-1是用于从后面第一位开始索引，后面的是从后面开始截取

print("该字符串%s的长度为：%d" % (str, len(str)) )
