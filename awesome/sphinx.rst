######################
sphinx - 编写电子文档
######################

:中文版docs: https://www.sphinx-doc.org/zh_CN/master/contents.html

命令行工具
******************************

* **sphinx-quickstart** 初始化文档项目

reStructuredText
******************************

基础语法
=============================

* 表格 - 适合使用于纯英文表格或者简单表格

指令
=============================

* **.. image:: __static/file.png** 显示图像, 相对路径引用
* **.. _自定义名称** 引用
* `.. include:: contents.rst.inc` - 插入contents.rst.inc文件的内容

配置文件
******************************

* **html_theme** HTML主题
    - **classic** 经典主题
    - **alabaster** 默认主题
    - **sphinx_rtd_theme** 非常流行的主题
    - **nature**
* source_suffix - 源文件的文件拓展名
    - 应用案例: django的conf.py

常见问题
*****************************

如何生成PDF文档
=============================

`快速入门 <https://www.sphinx-doc.org/zh_CN/master/usage/quickstart.html>`_ 有简单介绍，
原理是Sphinx 生成 PDF 的过程先将 rst 转换为 tex，再生产PDF，需要安装latex环境。

.. seealso::

  `rinohtype`_ 提供了一个PDF构建器，以替换LaTeX构建器(有时间就研究下这个库)

   .. _rinohtype: https://github.com/brechtm/rinohtype
