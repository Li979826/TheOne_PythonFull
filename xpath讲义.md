## xpath讲义

### 1、为什么要学习xpath和parsel

​		**parsel**是一款高性能的 Python HTML/XML 解析器。将字符串转化为Selector对象,Selector对象具有xpath的方法,返回结果的列表，能够接受bytes类型的数据和str类型的数据。我们可以利用XPath，来快速的定位特定元素以及获取节点信息



### 2、什么是xpath

​		**XPath** (XML Path Language) 是一门在 HTML\XML 文档中查找信息的**语言**，可用来在 HTML\XML 文档中对**元素和属性进行遍历**。



### 3、xpath的节点关系

知识点：

- 认识xpath中的节点
- 了解xpath中节点之间的关系



节点是什么东西？

* 每个html的标签我们都称之为节点。（根节点、子节点、同级节点）

![Snipaste_节点的关系](Snipaste_节点的关系.png)



### 4、xpath语法

​		**XPath** 使用路径表达式来选取 XML 文档中的节点或者节点集。这些路径表达式和我们在常规的**电脑文件系统中看到的表达式**非常相似。

| 表达式   | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| nodename | 选中该元素。                                                 |
| /        | 从根节点选取、或者是元素和元素间的过渡。                     |
| //       | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。跨节点获取标签 |
| .        | 选取当前节点。                                               |
| ..       | 选取当前节点的父节点。                                       |
| @        | 选取属性。                                                   |
| text()   | 选取文本。                                                   |

* 选取未知节点

| 通配符 | 描述                 |
| ------ | -------------------- |
| *      | 匹配任何元素节点。   |
| @*     | 匹配任何属性节点。   |
| node() | 匹配任何类型的节点。 |

| /div/*      | 选取 div元素的所有子元素。      |
| ----------- | ------------------------------- |
| //*         | 选取文档中的所有元素。          |
| //title[@*] | 选取所有带有属性的 title 元素。 |

* 案例

  ~~~html
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
  ~~~
  
  ~~~python
  # 2、1 从根节点开始，获取所有<a>标签
  
  # 2、2 跨节点获取所有<a>标签
  
  # 2、3 选取当前节点   使用场景：需要对选取的标签的下一级标签进行多次提取
  
  # 2、4 选取当前节点的父节点,获取父节点的class属性值
  
  # 2、5 获取第三个<li>标签的节点（两种方法）
  
  # 2、6 通过定位属性的方法获取第四个<a>标签
  
  # 2、7 用属性定位标签，获取第四个<a>标签包裹的文本内容
  
  # 2、8 获取第五个<a>标签的href属性值
  
  # 了解 模糊查询
  ~~~

* 如何选取多个标签？

  通过在路径表达式中使用“|”运算符，您可以选取若干个路径。（逻辑运算符）

  ~~~python
  # 同时获取<li>标签的属性以及<a>标签的文本
  ~~~

### 5、xpath中节点选择的工具

* 案例：猫眼top100 ，使用xpath匹配（片名、主演、上映时间、评分）

* Chrome 插件 XPath Helper

  **注意**： 这些工具是用来**学习xpath语法**的，他们都是**从elements中**匹配数据，elements中的数据和url地址对应的响应不相同，所以在代码中，不建议使用这些工具进行数据的提取（一切以代码为准）

  **使用chrome插件选择标签时候，选中时，选中的标签会添加属性class="xh-highlight"**

### 6、小结

1. xpath的概述XPath (XML Path Language),解析查找提取信息的语言
2. xpath的节点关系:根节点,子节点,同级节点
3. xpath的重点语法获取任意节点:`//`
4. xpath的重点语法根据属性获取节点:`标签[@属性 = '值']`
5. xpath中获取节点的文本：`text（）`
6. xpath的获取节点属性值:`@属性名`