*******************************
ORM
*******************************

依赖的第三方库

* `sqlalchemy`_ - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

.. _sqlalchemy: https://www.osgeo.cn/sqlalchemy/tutorial/index.html

执行Select语句
===============================

.. code-block:: python

    >>> with engine.connect() as conn:
    ...     result = conn.execute(text("SELECT x, y FROM some_table"))
    ...     for row in result:
    ...         print(f"x: {row.x}  y: {row.y}")
    # x: 1  y: 1
    # x: 2  y: 4
    # x: 6  y: 8
    # x: 9  y: 10