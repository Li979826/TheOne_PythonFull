 # !/usr/bin/env python
# encoding: utf-8
'''

@author: Carl
        ｛源前｝
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 520liyuan1314@gmail.com 源前
          291437965@qq.com 
@SoftWare: PyCharm
@FileName: Xpath.py
@Program：TheOne_PythonFull
@Time: 2020/3/18 9:13
@desc:
'''
import parsel

html_str = """
        <div> 
              <ul> 
                  <li class="item-1">
                      <a href="link1.html">第一个</a>
                  </li> 
                  
                  <li class="item-2">
                      <a href="link2.html">第二个</a>
                  </li> 
                  
                  <li class="item-3">
                      <a href="link3.html">第三个</a>
                  </li> 
                  
                  <li class="item-4">
                      <a href="link4.html">第四个</a>
                  </li> 
                  
                  <li class="item-5">
                      <a href="link5.html">第五个</a> 
                  </li>
              </ul>
        </div>
        """
#转换数据类型,parsel将html代码进行了补全
data=parsel.Selector(html_str)
# print(data)
#数据解析
#2、1从根节点开始，获取所有 < a > 标签
re_1=data.xpath('/html/body/div/ul/li/a')
# 2、2 跨节点获取所有<a>标签
re_2=data.xpath('//a')
# print(re_2)
# 2、3 选取当前节点   使用场景：需要对选取的标签的下一级标签进行多次提取
re_3=data.xpath('//ul')
re_3_1=re_3.xpath('./li')
# 2、4 选取当前节点的父节点,获取父节点的class属性值
re_3_2=re_2.xpath('../@*').extract()
# print(re_3_2)
# 2、5 获取第三个<li>标签的节点（两种方法）
re_3_1_1=re_3.xpath('./li[3]').extract()
# print(re_3_1_1)
re_3_1_2=data.xpath('//li')[2].extract()#索引法
# print(re_3_1_2)
# 2、6 通过定位属性的方法获取第四个<a>标签
re_4=data.xpath('//a[@href="link4.html"]').extract()
# 2、7 用属性定位标签，获取第四个<a>标签包裹的文本内容
re_5=data.xpath('//a[@href="link4.html"]/text').extract()
# print(re_5)
# 2、8 获取第五个<a>标签的href属性值
re_6=data.xpath('//li[5]/a/@href').extract()
print(re_6)