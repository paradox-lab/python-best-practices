.. _install3-linux:


############################
在Linux上安装Python 3
############################

.. image:: https://farm5.staticflickr.com/4276/34435689480_2e6f358510_k_d.jpg

这份文档描述了如何在Ubuntu Linux机器上安装Python 3.6。

想要获取已安装的Python 3版本号，可以通过终端运行命令：

.. code-block:: console

    $ python3 --version

如果您使用的是其他版本的Ubuntu（比如LTS发行版），我们推荐使用 `deadsnakes PPA <https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa>`_
来安装 Python 3.9::

    $ sudo apt-get install software-properties-common
    $ sudo add-apt-repository ppa:deadsnakes/ppa
    $ sudo apt-get update
    $ sudo apt-get install python3.9

如果您使用的是其他Linux发行版，有可能已经预装了Python 3。如果没有，使用发行版的包管理器。
比如，在Fedora上您可以使用 `dnf`：

.. code-block:: console

    $ sudo dnf install python3

.. tip::

    默认的安装目录在 ``/usr/lib``

安装pip
********************

.. code-block:: console

    $ sudo apt-get install python3-pip

如果存在多个python版本, 可以只安装一次pip，然后cp一个pip执行文件，修改里面指向的python版本即可

.. code-block:: console

    $ cd /usr/bin
    $ cp pip pip3.9
    $ vi pip

将 首行 ``#!/usr/bin/python3`` 改为 ``#!/usr/bin/python3.9``

.. tip::

    pip安装的第三方包默认的安装路径在 ``/usr/local/lib/python3.X/dist-packages``

源码构建Python 3
********************

linux自动安装并没有安装pip包，源码构建python3能解决这个问题

Ubuntu
-------------

.. code-block:: shell

    $ wget https://www.python.org/ftp/python/3.7.10/Python-3.7.10.tgz
    $ tar -zxvf Python-3.7.10.tgz
    $ cd Python-3.7.10/
    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get dist-upgrade
    $ sudo apt-get install python-dev
    $ sudo apt-get install libffi-dev
    $ sudo apt-get install libssl-dev
    $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev
    $ ./configure
    $ make
    $ make install

如果缺失依赖包，下载完依赖包后，重新编译和安装

.. code-block:: shell

    $ make
    $ make install

*********************
修改pip源
*********************

.. code-block:: shell

   $ cd ~
   $ mkdir .pip
   $ sudo vim .pip/pip.conf

使用阿里源

.. code-block:: text

    [global]
    index-url = http://mirrors.aliyun.com/pypi/simple/
    [install]
    trusted-host = mirrors.aliyun.com

*********************
使用Python 3
*********************

这个时候，在您系统上可能Python 2.7也是可用的。

.. code-block:: console

    $ python

将打开Python 2解释器。

.. code-block:: console

    $ python3

将打开Python 3解释器。


****************
Setuptools & Pip
****************

`setuptools <https://pypi.org/project/setuptools>`_ 和 `pip <https://pip.pypa.io/en/stable/>`_
是最重要的两个Python第三方软件包。一旦安装了它们，就可以通过一条指令下载、安装和卸载可获取到的
Python应用包，还可以轻松地将这种网络安装的方式加入到自己开发的Python应用中。

Python 2.7.9 以及之后版本(Python2 系列)，和Python 3.4以及之后版本均默认包含pip。

运行以下命令行代码检查pip是否已经安装：

.. code-block:: console

    $ command -v pip

`参考官方pip安装指南 <https://pip.pypa.io/en/latest/installing/>`_ 获取pip工具，并自动安装最新版本的setuptools。

注意，在某些Linux发行版（包括Ubuntu和Fedora）上， ``pip`` 用于Python 2的，而 ``pip3`` 用于Python 3。

.. code-block:: console

    $ command -v pip3

不过，使用虚拟环境（下面描述）就无需担心这个问题。


*****************************
Pipenv & 虚拟环境
*****************************

下一步安装 Pipenv，然后就可以安装依赖关系并管理虚拟环境。

虚拟环境工具通过为不同项目创建专属的 Python 虚拟环境，以实现其依赖的库独立保存在不同的路径。
这解决了“项目X依赖于 1.x 版本，但项目 Y 需要 4.x”的难题，并且维持全局的 site-packages 目录干净、易管理。 

举个例子，通过这个工具可以实现依赖 Django 1.10 的项目与依赖 Django 1.8 的项目共存。

所以，向前！进入到 :ref:`Pipenv & 虚拟环境 <virtualenvironments-ref>` 文档中！

--------------------------------

该页是 `另一份指南 <https://www.stuartellis.name/articles/python-development-windows/>`_ 的混合版本，可通过同一份许可获取。

