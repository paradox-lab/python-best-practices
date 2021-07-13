######################
fabric - 自动化部署工具
######################

:github地址: https://github.com/fabric/fabric

:手册: https://www.fabfile.org/index.html

依赖模块

* Invoke
* Paramiko

源码理解
*********************

* [fabric/group.py] - 实现分组批量执行shell命令的功能
    - Group - 实现Group方法的超类
    - SerialGroup - Group的子类，以简单、串行的方式执行
    - ThreadingGroup - Group的子类，使用多线程并发执行
    - GroupResult - 从Group实例收集执行任务返回的结果/异常




