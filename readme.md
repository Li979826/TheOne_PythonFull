﻿#py01_hello

    同样的代码块要保持同样的缩进值
    python由行的 缩进 来构成语法块
    print("ddd")  # python中所有的字符都是英文符号，而不是中文符号
    print("2222")  # 起标识符名字的时候最好使用有意义的英语名称
         name,Name,nAme 是三个不同的标识符
         以单下划线开头的，代表是不能直接访问的类  比如_foo
         以双下划线的，代表类的私有成员 __foo
     33个保留字，不能作为标识符来使用
     and   exec    not assert  finally or  break   for pass
     class from    None    continue    global  raise   def if
      return   del Import  try elif    In  while   else    is  with
       except  lambda  yield   false   true    as
     
     引号 必须成对出现！！！！  ""  ''   ''' ''' """ """
    
    '''三个单引号，可以用于多行注释！！！'''
     =  等号  用于赋值   将值放在等号右边
     备注：
     要加入代码串在markdown中
     可以用 ```（反引号） 包裹一段代码，并指定一种语言（也可以不指定）
#py02_变量

    数值的内容交换的写法a,b=b,a（python独有）
    可以同时赋值  写法如下：
    1（不采用）        2(最好)            3               4
    a=b=c=20      a=20;b=20;c=20      a,b=20,30       a=20;b=20
>**标识符的命名特点**

    Linux命名法
    file_name    dir_name
    小驼峰命名法
    fileName  dirName   
    大驼峰命名法
    FileName   DirName
   
>变量定义
    
    python中，每个变量在使用前都必须要进行赋值
    
   
#py03_买苹果
    
    关于 sum = sum -5
    这里的公式，先把sum的值减去5，再将得到的结果赋值给左边的sum
*debug模式*
    
    debug模式中  断点是必须的
    被断点包括的行会 转变为红色，即将执行的行为蓝色
    
#py04_05_06_数据类型及运算符表达式

    python中能狗直接处理的数据类型有：
    Number 数字
    String 字符串
    写法有：'a'  "a"  """a"""
    List   列表
    写法：[a,b,c]
    Tuple  元组
    写法：｛a,b,c｝
    Sets   集合
    写法：（a，b，c）
    Dictionary   字典
    写法：Map()
    当两个不同类型的数据进行计算时，是一种隐式计算数据转换。通常要表面隐式计算
    
>表达式
    
    值，变量，和操作符的组合。单独的一个值也可以看作是表达式，单独的变量也可以看作是是一个表达式
    分类：算术表达式，关系表达式，逻辑表达式，赋值表达式
>运算符
>
    Python可以支持的运算符
    算术运算符：+ - * / %(取模) **(幂次方)  //(取整除)
    关系（比较运算符）：==（等于） ！=（不等于） > < >= <=
    赋值运算符:= -=(c-=a等同于c=c-a) +=(c+=a等同于c=c+a) *= /= %= **= //=
    逻辑运算符:and(布尔 与) or(布尔 或) not(布尔 非)
    位运算符，成员运算符：in  not in
    身份运算符：is（两个标识符是否引用自同一对象）
               is not（两个标识符是否引用自不同的对象）
    ——————————————————————————————————————————————————
    优先级：我们可以通过括号来改变优先级
    
    
#py07_字符串
```python
# 访问单个字符串的方法： 变量[索引值]
#索引值从0开始计算 0~无限 
# 索引序列顺序
# a   b   c   d   e   f   从后面索引
# 0   1   2   3   4   5   从前面索引
# -6  -5  -4  -3  -2  -1
# :   1   2   3   4   5   :   从前面截取
# :   -5  -4  -3  -2  -1  :   从后面截取
s1="abcdefge"
# 提取第一个字符串
print(s1[0])
#单个字符索引为负数（-x），则表示最后x个字符
#提取子字符串 ：变量[头下标:尾下标]
print(s1[0:4])
#如果省略下标，则取出后续的所有字符串 
print(s1[-1])
#如果下标为负数，则表示 截取到倒数第x个字符
print(s1[:-1])
#重复字符串 ：变量*n
print(s1*2)
#连接字符串： 变量+变量
print(s1+s1)
```
    