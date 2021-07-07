.. _venv-ref:

虚拟环境
====================

.. image:: https://farm5.staticflickr.com/4290/35294660055_42c02b2316_k_d.jpg

创建虚拟环境

.. code-block:: shell

    python3 -m venv tutorial-env

激活

在Windows上，运行:

.. code-block:: shell

    tutorial-env\Scripts\activate.bat

在Unix或MacOS上，运行:

.. code-block:: shell

    source tutorial-env/bin/activate

移动虚拟环境目录
-----------------------

* 直接移动至其他位置后，其实仍然是指向旧位置，需要修改脚本。

* 假定虚拟环境位置为/home/user/venv,修改目录名为new-venv后，修改以下脚本：

new-venv/bin/pip & new-venv/bin/pip3 & new-venv/bin/pip3.7

.. code-block:: text

    #!/home/user/venv/bin/python3.7 -> #!/home/user/new-venv/bin/python3.7

active

.. code-block:: text

    VIRTUAL_ENV="/home/user/venv" -> VIRTUAL_ENV="/home/user/new-venv"
