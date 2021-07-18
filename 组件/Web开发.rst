*******************************
Web开发
*******************************

依赖的第三方库

* django

-------------------------------

模型层(Model)
===============================

Select
-------------------------------

`检索单个对象<https://docs.djangoproject.com/zh-hans/3.2/topics/db/queries/#retrieving-a-single-object-with-get>`_ ::

    one_entry = Entry.objects.get(pk=1)

如果没有满足查询条件的结果， get() 会抛出一个 DoesNotExist 异常。

-------------------------------

插件
===============================

定时任务
-------------------------------

依赖的第三方库

* `celery`_
* `django-celery-beat`_

.. _celery: https://github.com/celery/celery
.. _django-celery-beat: https://github.com/celery/django-celery-beat

.. warning::

    官方不支持在win10运行，因此需要使用变通的 `方法`_

.. _方法: https://stackoverflow.com/questions/37255548/how-to-run-celery-on-windows

*资料参考*

* celery在django的使用 https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
* django-celery-beat入门 https://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html

*启动程序*

在manage.py目录下启动django后，继续执行:

.. code-block::  shell

    celery -A [project-name] worker --loglevel=info

Windows环境加上 `-P gevent`

.. code-block:: shell

    celery -A [project-name] beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

代码创建任务::

    >>> PeriodicTask.objects.create(
    ...     interval=schedule,                  # we created this above.
    ...     name='Importing contacts',          # simply describes this periodic task.
    ...     task='proj.tasks.import_contacts',  # name of task.
    ... )

    >>> import json
    >>> from datetime import datetime, timedelta

    >>> PeriodicTask.objects.create(
    ...     interval=schedule,                  # we created this above.
    ...     name='Importing contacts',          # simply describes this periodic task.
    ...     task='proj.tasks.import_contacts',  # name of task.
    ...     args=json.dumps(['arg1', 'arg2']),
    ...     kwargs=json.dumps({
    ...        'be_careful': True,
    ...     }),
    ...     expires=datetime.utcnow() + timedelta(seconds=30)
    ... )

