# Python

**version**: 3.9.2(2021.2.19) & 3.8.8(2021.2.19) & 3.7.10(2021.2.15)

**资源**

- 官方资料 
  - 官网 - https://www.python.org/
  - 官方中文文档 - https://docs.python.org/zh-cn/3/
  - github地址 - https://github.com/python/cpython
- Python开发指导 
  - 手册 - https://docs.python-guide.org/
  - github地址 - https://github.com/realpython/python-guide
  - 中文版手册 - https://pythonguidecn.readthedocs.io/zh/latest/
  - 中文版github - https://github.com/Prodesire/Python-Guide-CN

## 版本差异对比
### 3.9
> 3.9的新变化:https://docs.python.org/zh-cn/3/whatsnew/3.9.html
#### 3.9.1 -> 3.9.2
collections.abc
```text
现在 collections.abc.Callable 泛型会将类型形参展平，类似于 typing.Callable 当前所做的那样。 
这意味着 collections.abc.Callable[[int, str], str] 的 __args__ 将为 (int, str, str)；
之前则为 ([int, str], str)。 为了允许这个改变，types.GenericAlias 现在可以被子类化，并且在抽取 
collections.abc.Callable 类型时将返回一个子类。 通过 typing.get_args() 或 __args__ 访问参数的代码需要
考虑到这个改变。 对于无效的 collections.abc.Callable 参数化形式可能会发出 DeprecationWarning，
这在 Python 3.9.1 中可能会静默地传递。 这个 DeprecationWarning 将在 Python 3.10 中变为 TypeError。 
（由 Ken Jin 在 bpo-42195 中贡献。）
```

urllib.parse
```text
早先的 Python 版本允许使用 ; 和 & 作为 urllib.parse.parse_qs() 和 urllib.parse.parse_qsl() 中 
query 形参的分隔键。 出于安全考虑，也为了遵循更新的 W3C 推荐设置，这已被改为只允许单个分隔键，默认为 &。 
这一改变还会影响 cgi.parse() 和 cgi.parse_multipart() 因为它们在内部使用了受影响的函数。 要了解更多细节，
请查看它们各自的文档。 （由 Adam Goldschmidt, Senthil Kumaran 和 Ken Jin 在 bpo-42967 中贡献。）
```

#### 3.9.X相比3.8.X的新特性
> 挑选研究:[PEP 584](https://www.python.org/dev/peps/pep-0584/) ，为 dict 增加合并运算符；

字典合并与更新运算符
> 合并 (|) 与更新 (|=) 运算符已被加入内置的 dict 类。 
> 它们为现有的 dict.update 和 {**d1, **d2} 字典合并方法提供了补充。
```text
>>> x = {"key1": "value1 from x", "key2": "value2 from x"}
>>> y = {"key2": "value2 from y", "key3": "value3 from y"}
>>> x | y
{'key1': 'value1 from x', 'key2': 'value2 from y', 'key3': 'value3 from y'}
>>> y | x
{'key2': 'value2 from x', 'key3': 'value3 from y', 'key1': 'value1 from x'}
```

- | - 合并 d 和 other 中的键和值来创建一个新的字典，两者必须都是字典。当 d 和 other 有相同键时， other 的值优先。
- |= - 用 other 的键和值更新字典 d ，other 可以是 mapping 或 iterable 的键值对。当 d 和 other 有相同键时， other 的值优先。
> |=可用于就地合并,类似于+=或者-=,其中原始变量(d1)被第二操作数(d2)的值更新。

#### 3.9.1相比3.9.0的新变化
**typing**
> typing.Literal 的行为被改为遵循 PEP 586 并匹配该 PEP 所描述的静态类型检查器的行为。

```text
笔者没用过typing.Literal,有时间就研究一番。

查阅文档，typing.Literal表示类型检查器对应变量或函数参数的值等价于给定字面量（或多个字面量之一）的类型。
```

## 安装Python
CentOS
```text
假设依赖包都已安装
假设3.9.2是当前最新的Python版本

安装Python 依赖包
yum -y groupinstall "Development tools"
yum install libffi-devel '解决ModuleNotFoundError: No module named '_ctypes'
下载
wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
解压
tar -zxvf  Python-3.8.3.tgz
cd Python-3.8.3.tgz
./configure
make
make install

下载依赖包后重新安装
make install
```

# 第一部分 基础

## pip
### 安装whl文件
> 如果pip远程下载超时，无法下载第三方库，可以直接下载第三方模块whl文件安装。
```commandline
pip install somewhat.whl
```

### 修改源
Ubuntu
```text
修改配置文件：~/.config/pip/pip.conf (Linux), (没有就创建一个)， 将 index-url改成至tuna，例如
在.config文件夹中创建pip/pip.conf

在pip.conf文件中添加以下内容

[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
```

> Ubuntu推荐用阿里源，清华源实测过不稳定，速度也不快。

CentOs
```text
mkdir ~/.pip

vim ~/pip.conf

在pip.conf文件中添加以下内容
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
```

> 完整指导：https://pythonguidecn.readthedocs.io/zh/latest/writing/structure.html#id1

## 模块
### 模块搜索目录
当使用import语句导入模块时，默认情况下，会按照以下顺序进行查找:
1. 在当前目录(即执行的Python脚本文件所在目录)查找。
1. 到PYTHONPATH(环境变量)下的每个目录中查找
1. 到Python的默认安装目录下查找。

> 以上各个目录的具体位置保存在标准模块sys的sys.path变量中

### 添加指定目录到sys.path
**方法一：临时添加**
```python
import sys
sys.path.append('path')
```

**方法二：.pth**
> 在Python安装目录下的"Lib\site-packages"子目录中，创建一个扩展名为.pth的文件，文件名任
意。这里创建一个mrpath.pth文件，在该文件中添加要导入模块所在的目录。

**方法三：在PYTHONPATH环境变量中添加**
> 注意:环境变量中添加模块目录后，需要重新打开要执行的导入模块的Python文件，否则新添加的目录不起
作用。

## 类属性和实例对象属性
```text
实例化类后，修改类属性，实例对象是属性会跟着修改
```
```python
class A:
    i = 1
    j = []


if __name__ == '__main__':
    a = A()
    print(a.i)  # -> 1
    A.i = 2
    A.j.append(1)
    print(a.i)  # -> 2 这是A.i，不是a.i
    print(a.j)  # -> [1]
    a.i = a.i  # 这是a.i，不是A.i了
    a.j = a.j.copy()
    A.i = 3
    A.j.append(2)
    print(a.i)  # -> 2
    print(a.j)  # -> [1]
```

## 上下文管理器with
> 参加官方说明：https://docs.python.org/zh-cn/3/reference/datamodel.html#with-statement-context-managers

实现：
```python
class ContextManager(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        退出关联到此对象的运行时上下文。 各个参数描述了导致上下文退出的异常。 
        如果上下文是无异常地退出的，三个参数都将为 None。
        """
        self.close()
    
    def close(self):
        pass

with ContextManager() as cm:
    pass
```

## 异常

**内置异常**: https://docs.python.org/zh-cn/3/library/exceptions.html#built-in-exceptions

### 处理多个异常
```python
try:
    raise RuntimeError
except (RuntimeError, TypeError, NameError):
    pass
```

### else子句
> try ... except 语句有一个可选的 else 子句，在使用时必须放在所有的 except 子句后面。对于在try 子句不引发异常
时必须执行的代码来说很有用。例如:
```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

### finally
```text
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```
> 如果存在 finally 子句，则 finally 子句将作为 try 语句结束前的最后一项任务被执行。 
> finally 子句不论 try 语句是否产生了异常都会被执行。 

### 异常链
> raise 语句允许可选的 from 子句，它启用了链式异常。 例如:
```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

**用途** : 转换异常

> 禁用异常链可使用 from None 习语

## 类型转换函数

函数|作用
-|-
int(x)|将x转换成整数类型
float(x)|将x转换成浮点数类型
complex(real[,imag])|创建一个复数
str(x)|将x转换为字符串
repr(x)|将x转换为表达式字符串
eval(str)|计算在字符串中的有效Python表达式，并返回一个对象
chr(x)|将整数x转换为一个字符
ord(x)|将一个字符x转换为它对应的整数值
hex(x)|将一个整数x转换为一个十六进制字符串
oct(x)|将一个整数x转换为一个八进制的字符串

## 修饰器

### 函数修饰器
#### 修饰带有返回值的函数
> 修改返回值

```python
def w_test(func):
    def inner():
        print('w_test inner called start')
        str = func()
        print('w_test inner called end')
        return str.lower()
    return inner
@w_test
def test():
    print('this is test fun')
    return 'hello'
ret = test()
print('ret value is %s' % ret)
```

#### 装饰器带参数，函数不带参数
```python
def func_args(pre='xiaoqiang'):
    def w_test_log(func):
        def inner():
            print('...记录日志...visitor is %s' % pre)
            func()
        return inner
    return w_test_log
# 带有参数的装饰器能够起到在运行时，有不同的功能
# 先执行func_args('wangcai')，返回w_test_log函数的引用
# @w_test_log
# 使用@w_test_log对test_log进行装饰
@func_args('wangcai')
def test_log():
    print('this is test log')
test_log()
```

#### 修饰器和函数带参数
> 修改返回值
```python
from inspect import signature
import ctypes
class GoString:
    pass
class GoInt:
    pass
def bego(libFunc):
    '''
    :param libFunc:lib对应的函数名称
    :return:
    '''
    def goFunc(func):
        def inner(*args):
            sig = signature(func)
            argtypes=[]
            args=list(args)
            for k,v in sig.parameters.items():
                t=sig.parameters[k].annotation
                if issubclass(t,str):
                    argtypes.append(GoString)
                    if str(v).find('=') != -1 and len(args) < len(sig.parameters):
                        args.append(str(v).split('=')[1].strip()[1:-1])
                elif issubclass(t,int):
                    argtypes.append(GoInt)
                    if str(v).find('=') != -1 and k not in args:
                        args.append(str(v).split('=')[1])

            libFunc.argtypes=argtypes
            libFunc.restype = ctypes.c_char_p
            args=tuple(map(lambda x:x.encode('utf-8'),args))
            return libFunc(*args).decode()
        return inner

    return goFunc
```

#### 修饰类的方法并传入self
```python
# 方法一
def dec(func):
    def inner(self):
        print(self.name)
        func(self)
    return inner

class C:

    def __init__(self):
        self.name = 'zhang san'

    # 方法二
    def dec(func):
        def inner(self):
            print(self.name)
            func(self)
        return inner

    @dec
    def method(self):
        print('修饰类中的方法')
```

### 类修饰器
#### 修饰器和函数不带参数
```python
class Test(object):
    def __init__(self,func): #func==test函数
        print('test init')
        print(func)
        print('func name is %s ' % func.__name__)
        self.__func=func
    def __call__(self, *args, **kwargs):
        print('装饰器中的功能')
        self.__func()
@Test
def test():
    print('this is test func')
test()
```

#### 函数带参数
```python
class Test(object):
    def __init__(self,func): #func==test函数
        print('test init')
        print(func)
        print('func name is %s ' % func.__name__)
        self.__func=func
    def __call__(self,f,*args, **kwargs): #f为test函数的入参
        print('装饰器中的功能')
        self.__func(f)
@Test
def test(f):
    print(f)
    print('this is test func')
test('111111fsaf')
```

#### 修饰器带参数
```python
class _Test(object):
    def __init__(self, target):  # func==test函数
        print('test init')
        print(target)

    def __call__(self, func, *args, **kwargs):  # f为test函数的入参
        print('装饰器中的功能')
        return func

def Test(target):
    return _Test(target)

@Test('os')
def test():
    print('this is test func')

test()
```

#### 修饰器和函数都带参数
```python
class _Test(object):
    def __init__(self, target):  # func==test函数
        print('test init')
        print(target)

    def __call__(self, func, *args, **kwargs):  # f为test函数的入参
        print('装饰器中的功能')
        return func

def Test(target):
    return _Test(target)

@Test('os')
def test(p):
    print(p)
    print('this is test func')

test('hibigii')
```

## 并发编程
### 协程
TODO

### 多线程
#### 快速上手
```python
import threading,time
print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')
```

输出
```text
Start of program.
End of program.
Wake up!
```

```text
多线程应用面临的主要挑战是，相互协调的多个线程之间需要共享数据或其他资源。为此，threading 模块提供了多个同步操作原语，包括线程锁、事件、条件变量和信号量。

尽管这些工具非常强大，但微小的设计错误却可以导致一些难以复现的问题。因此，
实现多任务协作的首选方法是将对资源的所有请求集中到一个线程中，然后使用 
queue 模块向该线程供应来自其他线程的请求。应用程序使用 Queue 对象进行线程间
通信和协调，更易于设计，更易读，更可靠。
```

**传递参数**
```python
# print('Cats','Dogs','Frogs',sep=' & ')
threadObj=threading.Thread(target=print,args=['Cats','Dogs','Frogs'],kwargs={'sep':' & '})
threadObj.start()
```
### 多进程
TODO

# 第二部分 最佳实践
> 标准库掌握:https://gitee.com/luzhenxiong/devdoc/tree/master/%E5%90%8E%E7%AB%AF/Python/%E6%A0%87%E5%87%86%E5%BA%93

## 单元测试
### doctest
```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```
```text
doctest 模块提供了一个工具，用于扫描模块并验证程序文档字符串中嵌入的测试。
测试构造就像将典型调用及其结果剪切并粘贴到文档字符串一样简单。这通过向用户
提供示例来改进文档，并且它允许doctest模块确保代码保持对文档的真实:
```

### unittest
**资料来源**
> 单元测试框架: https://docs.python.org/zh-cn/3/library/unittest.html

#### 测试脚手架(概念一)
> test fixture表示为了开展一项或多项测试所需要进行的准备工作，以及所有相关的清理操作。举个例子，这可能包含创建临时或代理的数据库、目录，再或者启动一个服务器进程。

> 可能同时存在多个前置操作相同的测试，我们可以把测试的前置操作从测试代码中拆解出来，并实现测试前置方法 setUp() 。
> 在运行测试时，测试框架会自动地为每个单独测试调用前置方法。

```python
import unittest
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')
        
    def tearDown(self):
        self.widget.dispose()

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
```
> 在测试运行时，若 setUp() 方法引发异常，测试框架会认为测试发生了错误，因此测试方法不会被运行。
相似的，我们提供了一个 tearDown() 方法在测试方法运行后进行清理工作。
若 setUp() 成功运行，无论测试方法是否成功，都会运行 tearDown() 。

#### 测试用例(概念二)
> 一个test case是一个独立的测试单元。它检查输入特定的数据时的响应。 unittest 提供一个基类： TestCase ，用于新建测试用例。
> 在 unittest 中，测试用例表示为 unittest.TestCase 的实例。
> 一个 TestCase 实例的测试代码必须是完全自含的，因此它可以独立运行，或与其它任意组合任意数量的测试用例一起运行。

#### 测试套件(概念三)
> test suite是一系列的测试用例，或测试套件，或两者皆有。它用于归档需要一起执行的测试。

> 如果你需要自定义你的测试套件的话，你可以参考以下方法组织你的测试:
```python
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

#### 测试运行器(概念四)
> test runner是一个用于执行和输出测试结果的组件。这个运行器可能使用图形接口、文本接口，或返回一个特定的值表示运行测试的结果。

#### 入门demo
> 这是一段简短的代码，来测试三种字符串方法:
```python

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

> 继承 unittest.TestCase 就创建了一个测试样例。上述三个独立的测试是三个类的方法，这些方法的命名都以 test 开头。 这个命名约定告诉测试运行者类的哪些方法表示测试。
每个测试的关键是：调用 assertEqual() 来检查预期的输出； 调用 assertTrue() 或 assertFalse() 来验证一个条件；调用 assertRaises() 来验证抛出了一个特定的异常。使用这些方法而不是 assert 语句是为了让测试运行者能聚合所有的测试结果并产生结果报告。
通过 setUp() 和 tearDown() 方法，可以设置测试开始前与完成后需要执行的指令。 在 组织你的测试代码 中，对此有更为详细的描述。

#### 复用已有的测试代码
> unittest 提供 FunctionTestCase 类。这个 TestCase 的子类可用于打包已有的测试函数，并支持设置前置与后置函数。

假定有一个测试函数：
```text
def testSomething():
    something = makeSomething()
    assert something.name is not None
    # ...
```

可以创建等价的测试用例如下，其中前置和后置方法是可选的。
```python
testcase = unittest.FunctionTestCase(testSomething,
                                     setUp=makeSomethingDB,
                                     tearDown=deleteSomethingDB)
```

#### 使用subTest区分测试迭代
> 当测试之间有非常小的差异时，例如一些参数，unittest允许您使用subTest()上下文管理器在测试方法体中区分它们。

```python
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
```
> 这将会测试每个输入i的结果，如果不使用subTest，执行将在第一次失败后停止，错误将不太容易诊断，因为i的值不会显示:

#### setup和setupclass的区别
- setUp():每个测试case运行之前运行
- tearDown():每个测试case运行完之后执行
- setUpClass():必须使用@classmethod 装饰器,  所有case运行之前只运行一次
- tearDownClass():必须使用@classmethod装饰器, 所有case运行完之后只运行一次

#### 命令行
执行当前目录所有测试文件
```commandline
python -m unittest
```
或
```commandline
python -m unittest discover
```

#### 测试报告输出到文件
```python
import unittest
class TestFunction(unittest.TestCase):
    def test_something(self):
      pass
    
if __name__ == '__main__':

    suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    suite.addTests(test_loader.loadTestsFromTestCase(TestFunction))
    with open('unittest result.txt', 'a') as file:
        runner = unittest.TextTestRunner(file, verbosity=2)
        file.write('\n')
        runner.run(suite)
```

#### 测试报告发送邮件
```python
import unittest
import io

class TestFunction(unittest.TestCase):
    def test_something(self):
      pass
    
if __name__ == '__main__':

    suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    suite.addTests(test_loader.loadTestsFromTestCase(TestFunction))
    
    with io.StringIO() as stream:
        runner = unittest.TextTestRunner(stream, verbosity=2)
        runner.run(unittest.defaultTestLoader.discover('start_dir'))

        stream.seek(0)
        with dev_smtp_sender() as yag:
            yag.send(to=[Developer], subject='冒烟测试',
                     contents=[stream.read()])
```


#### 断言方法
方法|检查项 
-|-
assertEqual(a, b)|a == b
assertNotEqual(a, b)|a != b
assertTrue(x)|bool(x) is True
assertFalse(x)|bool(x) is False
assertIs(a, b)|a is b
assertIsNot(a, b)|a is not b
assertIsNone(x)|x is None
assertIsNotNone(x)|x is not None
assertIn(a, b)|a in b
assertNotIn(a, b)|a not in b
assertIsInstance(a, b)|isinstance(a, b)
assertNotIsInstance(a, b)|not isinstance(a, b)
assertLess(a, b)|a < b
assertRaises(exc, fun, *args, **kwds)|fun(*args, **kwds) raises exc

code
```python
# 测试抛出异常
with self.assertRaises(SomeException):
    do_something()
```

#### 跳过测试
> https://docs.python.org/zh-cn/3/library/unittest.html#skipping-tests-and-expected-failures

修饰器
- unittest.skip
- unittest.skipIf
- unittest.skipUnless

### unittest.mock
> mock库允许使用模拟对象来替换受测系统的部分，并对它们如何已经被使用进行断言。

**资料来源**
- mock对象库 - https://docs.python.org/zh-cn/3/library/unittest.mock.html
- 上手指南 - https://docs.python.org/zh-cn/3/library/unittest.mock-examples.html

#### 修饰器patch
> [patch](https://docs.python.org/zh-cn/3/library/unittest.mock.html#patch)作为函数装饰器，为您创建mock并将其传递给装饰后的函数:

```python
from unittest import mock

class SomeClass:
    pass

@mock.patch('__main__.SomeClass')
def function(normal_argument, mock_class):
     print(mock_class is SomeClass)

function(None)
```

> 修补一个类用一个MagicMock实例替换这个类。如果类是在测试代码中实例化的，那么将使用mock的return_value。
如果类被实例化多次，那么每次都可以使用side_effect返回一个新的mock。或者，您可以将return_value设置为您想要的任何值。
要在修补过的类的实例的方法上配置返回值，您必须在return_value上执行此操作。例如:

```python
class Class:
    def method(self):
        pass
with mock.patch('__main__.Class') as MockClass:
    #模拟实例化
	instance = MockClass.return_value
	instance.method.return_value = 'foo'
	assert Class() is instance
	assert Class().method() == 'foo'
```

> 如果您使用spec或spec_set，并且patch()替换了一个类，那么创建的mock的返回值将具有相同的规范。
```python
Original = Class
patcher = mock.patch('__main__.Class', spec=True)
MockClass = patcher.start()
instance = MockClass()
assert isinstance(instance, Original)
patcher.stop()
```

> 当您希望为创建的模拟使用默认MagicMock的替代类时，new_callable参数非常有用。例如，如果你想使用一个非callablemock:
```python
thing = object()
with mock.patch('__main__.thing', new_callable=mock.NonCallableMock) as mock_thing:
    assert thing is mock_thing
    thing()

from io import StringIO
def foo():
    print("Something")

@mock.patch('sys.stdout', new_callable=StringIO)
def test(mock_stdout):
    foo()
    assert mock_stdout.getvalue() == 'Something\n'

test()
```

> 当patch()为您创建一个模拟时，通常需要做的第一件事就是配置模拟。其中一些配置可以在对patch的调用中完成。
传入调用的任意关键字都将用于设置创建的mock的属性:

```python
patcher = mock.patch('__main__.thing', first='one', second='two')
mock_thing = patcher.start()
mock_thing.first
mock_thing.second
```

> 还可以配置所创建的模拟属性(如return_value和side_effect)上的属性。这些在语法上是无效的，不能直接作为关键字参数传入，但是使用**仍然可以将这些作为键的字典扩展为patch()调用:

```python
config = {'method.return_value': 3, 'other.side_effect': KeyError}
patcher = mock.patch('__main__.thing', **config)
mock_thing = patcher.start()
mock_thing.method()
mock_thing.other()
```

> 默认情况下，试图修补模块中的函数(或类中的方法或属性)不存在将抛出AttributeError异常:
```python
import sys
@mock.patch('sys.non_existing_attribute', 42)
def test():
    assert sys.non_existing_attribute == 42

test()

@mock.patch('sys.non_existing_attribute', 42,create=True)
def test():
    assert sys.non_existing_attribute == 42
```

##### *target
> targe传入一个字符串，格式为'package.module.ClassName'。
> 基本原则是你在查找对象的地方做补丁，这个地方不一定和定义对象的地方相同。几个例子将有助于澄清这一点。
```text
a.py
    -> Defines SomeClass

b.py
    -> from a import SomeClass
    -> some_function instantiates SomeClass

test_b.py
    -> import b
```
假设测试b.py的some_function，mock SomeClass对象

**情况一：from a import SomeClass**
> 这个例子中，some_function在b.py被导入，因此：
```python
@patch('b.SomeClass')
```
> b.py -> from a import SomeClass，可假设为SomeClass在b.py定义了，因此是b.SomeClass

> 注意！以下代码是不正确的，依然会正常调用SomeClass
```python
@patch('a.SomeClass')
```
**情况二：import a**
> 在b.py导入a模块
```python
@patch('a.SomeClass')
```

**情况三：mock整个package**
> 例如在b.py import openpyxl,需要mock openpyxl
```text
b.py
    -> import openpyxl
    -> some_function instantiates openpyxl.Workboook
```
```python
@path('b.openpyxl')
```

**情况四：mock类中的一个属性**
> 场景：需要mock self._sftp
```python
from paramiko import Transport, SFTPClient
class Sftp:
    def __init__(self):
        self._ssh = Transport(('host', 22))
        self._ssh.connect(username='user', password='pwd')
        self._sftp = SFTPClient.from_transport(self._ssh)
```
```text
因为self._sftp是Sftp的一个属性，target不能直接指定__main__.DmsSftp._sftp
```

> 解决办法：添加一个方法把self._sftp修饰成类属性

```python
@property
def sftp(self):
    return self._sftp
```
> 被测试的函数使用self.sftp取代self._sftp，这时可以使用`target='__main__.Sftp.sftp'` mock
> SFTPClient对象

##### spec
> 创建指定的属性和方法

**传入一个列表**
```python
m = mock.Mock(spec=['attr1', 'attr2'])
print(m.attr1)
print(m.attr2)
```

**传入True值**
> 创建被Mock对象一样的方法, 属性需要自行手工创建

**传入一个class对象或者实例对象**
> 创建class对象或者实例对象一样的属性和方法

##### spec_set
> spec更严格的变体,功能一致。

> 指定spec参数，可以为mock对象创建不存在的属性赋值。
> 指定spec_set参数，为mock对象不存在的属性赋值则抛出异常。

##### return_value
```text
函数的返回值。
如果是设置属性的值，不要使用return_value，应该是"属性名称" = "想设置的值"
```

#### Mock对象
> Mock 是一个可以灵活的替换存根 (stubs) 的对象，可以测试所有代码。 
Mock 是可调用的，在访问其属性时创建一个新的 mock 1 。访问相同的属性只会返回相同的 mock 。 Mock 保存调用记录，可以通过断言获悉代码的调用。
MagicMock 是 Mock 的子类，它有所有预创建且可使用的魔术方法。在需要模拟不可调用对象时，可以使用 NonCallableMock  和 NonCallableMagicMock
patch() 装饰器使得用 Mock 对象临时替换特定模块中的类非常方便。 默认情况下 patch() 将为你创建一个 MagicMock。 你可以使用 patch() 的 new_callable 参数指定替代 Mock 的类。
```python
m=mock.Mock()
#断言没有被调用
m.hello.assert_not_called()
#断言调用并验证参数
m.hello('faef','fienf',key='value')
m.hello.assert_called_with('faef','fienf',key='value')
```

#### mock快速上手
##### 指定返回值或者限制可访问属性
```python
from unittest.mock import MagicMock
thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method(3, 4, 5, key='value')
thing.method.assert_called_with(3, 4, 5, key='value')

通过 side_effect 设置副作用(side effects) ，可以是一个 mock 被调用是抛出的异常
mock = Mock(side_effect=KeyError('foo'))
mock()

values = {'a': 1, 'b': 2, 'c': 3}
def side_effect(arg):
    return values[arg]

mock.side_effect = side_effect
mock('a'), mock('b'), mock('c')
mock.side_effect = [5, 4, 3, 2, 1]
mock(), mock(), mock()
```

> Mock 还可以通过其他方法配置和控制其行为。例如 mock 可以通过设置 spec 参数来从一个对象中获取其规格(specification)。
如果访问 mock 的属性或方法不在 spec 中，会报 AttributeError 错误。

##### patch() 装饰去/上下文管理器
> 你指定的对象会在测试过程中替换成 mock （或者其他对象），测试结束后恢复。

```python
from unittest.mock import patch
@patch('module.ClassName2')
@patch('module.ClassName1')
def test(MockClass1, MockClass2):
    module.ClassName1()
    module.ClassName2()
    assert MockClass1 is module.ClassName1
    assert MockClass2 is module.ClassName2
    assert MockClass1.called
    assert MockClass2.called
test()
```

> patch() 也可以 with 语句中使用上下文管理。

```python
with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(1, 2, 3)

mock_method.assert_called_once_with(1, 2, 3)
```

> 还有一个 patch.dict() 用于在一定范围内设置字典中的值，并在测试结束时将字典恢复为其原始状态：
```python
foo = {'key': 'value'}
original = foo.copy()
with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
    assert foo == {'newkey': 'newvalue'}

assert foo == original
```

> Mock支持 Python 魔术方法。它可以做如下事情：

```python
mock = MagicMock()
mock.__str__.return_value = 'foobarbaz'
str(mock)
mock.__str__.assert_called_with()
```

##### 指定函数为魔术方法
```python
mock = Mock()
mock.__str__ = Mock(return_value='wheeeeee')
str(mock)
```

> 使用 auto-speccing 可以保证测试中的模拟对象与要替换的对象具有相同的api 。
在 patch 中可以通过 autospec 参数实现自动推断，或者使用 create_autospec() 函数。
自动推断会创建一个与要替换对象相同的属相和方法的模拟对象，并且任何函数和方法（包括构造函数）都具有与真实对象相同的调用签名。

```python
from unittest.mock import create_autospec
def function(a, b, c):
    pass

mock_function = create_autospec(function, return_value='fishy')
mock_function(1, 2, 3)

mock_function.assert_called_once_with(1, 2, 3)
mock_function('wrong arguments')
```

> 在类中使用 create_autospec() 时，会复制 __init__ 的签名，另外在可调用对象上使用时，会复制 __call__ 的签名。

##### assert使用指定的参数调用了mock
> 如果mock调用过，断言就会通过，这与assert_called_with()和assert_called_once_with()不同，后者只有在调用是最近的时候才会通过，
而且对于assert_called_once_with()，它也必须是唯一的调用。
```python
mock = mock.Mock(return_value=None)
mock(1, 2, arg='thing')
mock('some', 'thing', 'else')
mock.assert_any_call(1, 2, arg='thing')

##修改mock对象返回值**
#方法一
m.hello.return_value='新返回值'
#方法二
attrs={'hello.return_value':'新返回值'}
m.configure_mock(**attrs)
#方法三，使用side_effect抛出异常
mock = mock.Mock(side_effect=KeyError('foo'))
mock()
#方法四，使用side_effect根据不同的单个参数返回值不同的值
values = {'a': 1, 'b': 2, 'c': 3}
mock.side_effect = values.get
mock('a'), mock('b'), mock('c')
#方法五，使用side_effect，根据列表按顺序返回返回值，列表的值全部返回完毕后会抛出异常
mock.side_effect = [5, 4, 3, 2, 1]
mock(), mock(), mock()
#方法六，使用side_effect根据不同的多个参数返回值不同的值
def side_effect(*args, **kwargs):
    if args == ('a','b','c') \
            and kwargs.get('jobid') == 50:
        return 1,2,3

mock.side_effect=side_effect

mock('a','b','c',jobid=50)

##模拟mock对象方法的属性值**
import requests
data={
    "errcode": 0,
    "errmsg": "ok",
    "job_id": 100074947
    }
with mock.patch('requests.post') as mp:
    mp().text=data
    r = requests.post('url')
    print(r.text)

##修改mock对象类/函数行为**
from unittest.mock import create_autospec
def function(a, b, c):
    print(a, b, c)
mock_function = create_autospec(function, side_effect=function)
mock_function(1, 2, 3)
```

##### mock实例的其中一个方法
```python
from unittest import mock
import openpyxl
with mock.patch('openpyxl.workbook.workbook.Workbook.save') as mock_save:
    wb = openpyxl.load_workbook('mock.xlsx')
    """
    wb handle logic
    """
    wb.save('mock.xlsx')  # MagicMock
```

##### mock with语句对象
```python
class Object:
  def __init__(self):
    pass
  def __enter__(self):
    pass
  def __exit__(self, exc_type, exc_val, exc_tb):
    pass
  def method(self):
    pass

# 断言
from unittest import mock

@mock.patch('__main__.Object', spec=True)
def test_method(mock_oj):
    with Object() as oj:
        oj.method()
    mock_oj().__enter__().method.assert_called_once()
```

### pytest
> https://gitee.com/luzhenxiong/devdoc/blob/master/%E5%90%8E%E7%AB%AF/awesome/py/pytest/README.md

### 如何导入需要测试的包
> 资料来源: https://pythonguidecn.readthedocs.io/zh/latest/writing/structure.html#test-suite
 
> 假定需要测试sample包

方法一:将您的包安装到site-packages中。
```python
import unittest
import sample
```

方法二:设置路径
- 先创建一个包含上下文环境的文件 tests/context.py。 file:
```python
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sample
```
- 然后，在每一个测试文件中，导入:
```python
from .context import sample
```

## 日志logging
[官方手册](https://docs.python.org/zh-cn/3/library/logging.html)

### 快速入门
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info('Hello World')
```

### 基础
1. [便利函数](#便利函数)
1. [记录日志到文件](#记录日志到文件)
1. [日志级别](#日志级别)
1. 其他
### 进阶
1. [记录器](#Logger)(暴露了应用程序代码直接使用的接口)
1. [处理程序Handler](#处理程序)(将日志记录发送到适当的目标)
   - SMTPHandler日志发送邮件
1. 格式化程序Formatter(指定最终输出中日志记录的样式)
1. 过滤器(提供更精细的附加功能，用于确定要输出的日志记录)   
1. 配置日志记录
1. LogRecord属性

#### 便利函数
debug()

info()

warning()

error()

critical()

#### 记录日志到文件
```python
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s- %(message)s',
                    datefmt='%m%d%Y%I:%M%S%p')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
```

对 basicConfig() 的调用应该在 debug() ， info() 等的前面。因为它被设计为一次性的配置，只有第一次调用会进行操作，随后的调用不会产生有效操作。

如果多次运行上述脚本，则连续运行的消息将追加到文件 example.log 。 如果你希望每次运行重新开始，而不是记住先前运行的消息，则可以通过将上例中的调用更改为来指定 filemode 参数:

```python
import logging
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
```

#### 日志级别
级别|数值|何时使用
-|-|-
CRITICAL|50|严重的错误，表明程序不能继续执行
ERROR|40|由于严重的错误，程序的某些功能已经不能正常执行
WARNING|30|表明有已经或即将发生的意外。程序仍按预期进行
INFO|20|确认按预期运行
DEBUG|10|细节信息，仅当诊断问题时适用
NOTSET|0|没有设置

#### 禁用日志

logging.disble()函数禁用了这些消息，这样就不必进入到程序中，手工删除所有日的日志调用。
只要向logging.disble()传入一个日志级别，它就会禁止该级别和更低级别的所有日志消息。所以，如果想
要禁用所有日志，只要在程序中添加logging.disable(logging.CRITICAL)。

---
### 记录器
#### 配置
- Logger.setLevel()指定记录器将处理的最低严重性日志消息。
- Logger.addHandler()和Logger.removeHandler()从记录器对象中添加和删除处理程序对象。
- Logger.addFilter()和Logger.removeFilter()可以添加或移除记录器对象中的过滤器。
### 处理程序Handler

#### SMTPHandler

该实例使用电子邮件的发件人、收件人地址和主题行进行初始化。 toaddrs 应当为字符串列表。 要指定一个非标准 SMTP 端口，请使用 (host, port) 元组格式作为 mailhost 参数。 如果你使用一个字符串，则会使用标准 SMTP 端口。 如果你的 SMTP 服务器要求验证，你可以指定一个 (username, password) 元组作为 credentials 参数。

要指定使用安全协议 (TLS)，请传入一个元组作为 secure 参数。 这将仅在提供了验证凭据时才能被使用。 元组应当或是一个空元组，或是一个包含密钥文件名的单值元组，或是一个包含密钥文件和证书文件的 2 值元组。 （此元组会被传给 smtplib.SMTP.starttls() 方法。）

demo
```python

import logging
import logging.handlers

logger = logging.Logger('email')

logger.setLevel(logging.WARNING)

eh = logging.handlers.SMTPHandler(mailhost=('smtp.exmail.qq.com',587),
                                  fromaddr='username',toaddrs=['username'],
                                  subject = 'logging测试',credentials= ('username','pwd'),
                                  secure =tuple(),timeout=300)
# 处理程序处理级别
eh.setLevel(logging.ERROR)
logger.addHandler(eh)

logger.warning('警告消息1')

# 发送邮件
logger.error('错误消息1')
# 发送第二封邮件
logger.error('错误消息2')


```
### 日志记录配置
#### 通过文件配置
> 资料: https://docs.python.org/zh-cn/3/library/logging.config.html#logging.config.fileConfig

## 类型注解
> 官方资料:https://docs.python.org/zh-cn/3/library/typing.html

### 入门级Demo
```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```
> 参数 name 预期是 str 类型，并且返回 str 类型。子类型允许作为参数。

# 性能
## 性能测试
```text
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```
> 元组封包和拆包功能相比传统的交换参数可能更具吸引力。

> 与 timeit 的精细粒度级别相反， profile 和 pstats 模块提供了用于在较大的代码块中
识别时间关键部分的工具。

# 内存管理
## 弱引用
```text
Python 会自动进行内存管理（对大多数对象进行引用计数并使用 garbage collection 
来清除循环引用）。 当某个对象的最后一个引用被移除后不久就会释放其所占用的内存。

此方式对大多数应用来说都适用，但偶尔也必须在对象持续被其他对象所使用时跟踪它
们。 不幸的是，跟踪它们将创建一个会令其永久化的引用。 weakref 模块提供的工具
可以不必创建引用就能跟踪对象。 当对象不再需要时，它将自动从一个弱引用表中被
移除，并为弱引用对象触发一个回调。 典型应用包括对创建开销较大的对象进行缓存:

>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
...
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python38/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```

# 重点关注的专业术语
> 资料来源：https://docs.python.org/zh-cn/3/glossary.html

- decorator -- 装饰器
> 返回值为另一个函数的函数，通常使用 @wrapper 语法形式来进行函数变换。

- descriptor -- 描述器 
> 任何定义了 __get__(), __set__() 或 __delete__() 方法的对象。

- iterator -- 迭代器
> 用来表示一连串数据流的对象。

- generator -- 生成器
> 返回一个 generator iterator 的函数。它看起来很像普通函数，不同点在于其包含 yield 表达式以便产生一系列值供给 for-循环使用或是通过 next() 函数逐一获取。

> 通常是指生成器函数，但在某些情况下也可能是指 生成器迭代器。如果需要清楚表达具体含义，请使用全称以避免歧义。

# 魔术方法
> https://docs.python.org/zh-cn/3/reference/datamodel.html#basic-customization

# 其他常见问题
## 后台运行python脚本
```commandline
nohup python myscript.py params1 > nohup.out 2>&1 &
```

只输出错误日志
```commandline
nohup python myscript.py params1 >/dev/null 2>nohup.out & 
```

什么信息都不要
```
nohup python myscript.py params1 >/dev/null 2>&1 & 
```

print语句输出到nohup.out
```commandline
nohup python -u myscript.py params1 > nohup.out 2>&1 &
```

# 优秀源码学习案例
- openpyxl库
  - openpyxl\worksheet\worksheet.py Worksheet类
    >  `__getitem__`和`__item__`、`__iter__`、`__delitem__`使用

```python
print(ws['A1'])
print(ws['A1:A5'])
```

- paramiko
  - paramiko\sftp_client.py的from_transport类方法
    > @classmethod使用
  - transport.py的Transport类
    > threading库使用
- django
  > 请自行阅读awesome系统的django库