****************
Pip使用
****************

所有受支持的Python 3版本都包含pip，因此请确保它是最新的:

.. code-block:: doscon

    python -m pip install -U pip

常用指令

.. code-block:: text

    pip install <模块名>

    指定版本
    pip install <模块名> == <版本号>

    安装requirements.txt指定的包
    pip install -r requirements.txt

    设置超时时间
    pip --default-timeout=100 install <模块名>

    卸载模块
    pip uninstall <模块名>

    查看已安装的模块及其版本
    pip freeze

    生成requirements.txt
    pip freeze > requirements.txt

    查看已安装模块
    pip list

    查看模块的信息
    pip show <模块名>

    查看可升级的模块
    pip list -o

    升级指定模块
    pip install -U <包名>

    升级pip
    python -m pip install --upgrade pip