#!/usr/bin/env python
# encoding: utf-8
'''

@author: Carl
        ｛源前｝
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 520liyuan1314@gmail.com 源前
          291437965@qq.com 
@SoftWare: PyCharm
@FileName: py_08列表到分支.py
@Program：TheOne_PythonFull
@Time: 2020/2/28 21:35
@desc:
'''

# 创建列表
list1=[11,22,33,44,55] #数值列表

list2=['aa','bb','cc','dd'] #字符串

list3=['aaa',123,True,3.14]  #多数据类型
print(list1)
print(list2)
print(list3)
print(list1[0:4])
print(list1[8:5])
print(type(list2))  #返回列表值
print(type(3.147))  #返回float值

#列表内容的修改
str=['ABCDE',222,333]
#str[0]='a' 用于将列表当中的第一个数据变为 后方'a'的值，也就是将这个值给赋值给第一个
str[0]=['a','2',222]
print(str)
