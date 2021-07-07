##########################
类型系统
##########################

使用类型注解的好处:

* 增强代码可维护性
* Pycharm方便跳转源码(不加导致Pycharm不知道这个方法来自哪个模块)

使用类型注解有两种方式
第一种::

    def test(num:int):
        s:str = "str"
        print(num)
        print(s)

第二种::

     def test(num):  # type int
        s = "str" # type str
        print(num)
        print(s)


在for循环使用类型注解
**************************

.. code-block:: python

    for i, df in enumerate(df):  # type: (int, pd.DataFrame)
        pass

