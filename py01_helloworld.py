#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ====#====#====#====
# __author__ = "Jacson.Bai"
# HomePage:http://blog.csdn.net/jacson_bai
# QQ:
# FileName: *.py
# Version:1.0.0
# ====#====#====#====

# python 是一种解释性语言，逐句解释！！
# print("dddd 你是傻吊")
# name = input("请输入姓名！\n")
# print(name)
# print(name)


a = 5
str1list = ["aa",
            "bb",
            "cc"]
if a > 0:
    print("aaa")  # 同样的代码块要保持同样的缩进值
    print("ddd")  # python中所有的字符都是英文符号，而不是中文符号
    print("2222")  # 起标识符名字的时候最好使用有意义的英语名称
    #     name,Name,nAme 是三个不同的标识符
    #     以单下划线开头的，代表是不能直接访问的类  比如_foo
    #       以双下划线的，代表类的私有成员 __foo
    # 33个保留字，不能作为标识符来使用
    # and   exec    not assert  finally or  break   for pass
    # class from    None    continue    global  raise   def if
    #  return   del Import  try elif    In  while   else    is  with
    #   except  lambda  yield   false   true    as
    # [] 列表 例子  {}集合，site   ()元组
    # 引号 必须成对出现！！！！  ""  ''   ''' ''' """ """
    '''三个单引号，可以用于多行注释！！！'''
    # =  等号  用于赋值   将值放在变量中
else:

    print("bbbb")
    print(str1list)

# import keyword
# print(keyword.kwlist)   用于查看python当中的关键字
# 变量：指的是向各类型值的名字，以后再用到这个值时，直接饮用名字即可，不用再写具体的值
# python中的变量赋值不用声明类型，会自动识别。以你定义的值来自动变换
a1=100 #整形变量
a2=100.0 #双精度
a3=True #布尔