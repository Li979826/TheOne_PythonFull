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
list1 = [11, 22, 33, 44, 55]  # 数值列表

list2 = ['aa', 'bb', 'cc', 'dd']  # 字符串

list3 = ['aaa', 123, True, 3.14]  # 多数据类型
print(list1)
print(list2)
print(list3)
print(list1[0:4])
print(list1[8:5])
print(type(list2))  # 返回列表值
print(type(3.147))  # 返回float值

# 列表内容的修改
str = ['ABCDE', 222, 333]
# str[0]='a' 用于将列表当中的第一个数据变为 后方'a'的值，也就是将这个值给赋值给第一个
# str[0]=['a','2',222]
# print(str)

# 追加元素到列表末尾
str.append('11111')
print(str)

if str[1]>1:
    print('傻吊')
else:
    print("111")

a=input("请输入a的值")
b=input("请输入b的值")
if a>b:
    print("a>b")
elif a==b:
    print("a=b")
else:
    print('a<b')


'''判断奇偶数'''
sst = int(input("请输入任意一个数字:"))
if sst % 2 == 1:
    print("该数字%s为奇数"%sst)
else:
    print("该数字%s为偶数"%sst)

'''判断闰年与否'''
r_year = int(input("请输入一个四位数的年份"))
if (r_year % 4 == 0) and (r_year % 400 == 0):
    print('该年份为闰年')
elif (r_year % 100 != 0):
    print('该年份不是闰年')


'''计算BMI指数'''
weight=float(input("请输入你的体重！单位：kg\n"))
height=float(input("请输入你的身高！单位：m\n"))
B_M_I=(weight/(height**2))
print("B_M_I=%s"%B_M_I)
if  B_M_I<18.2:
    print("你太轻了")
elif B_M_I>=18.5 and B_M_I<25:
    print("你是正常的")
elif B_M_I>=25 and B_M_I<28:
    print("你已经开始在向变胖的方向发展了！")
elif B_M_I>=28 and B_M_I <32:
    print("你有点胖啊！还不赶紧注意身体健康！！")
elif B_M_I>32:
    print("你已经严重超标了！！！")

