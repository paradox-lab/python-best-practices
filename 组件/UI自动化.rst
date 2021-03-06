*******************************
UI自动化
*******************************

依赖的第三方库

* `selenium`_ Selenium is an umbrella project encapsulating a variety of tools and libraries enabling web browser automation.
    - selenium官方文档: https://www.selenium.dev/documentation/en/
    - selenium docs文档: https://selenium-python.readthedocs.io/
    - docs中文版: https://selenium-python-zh.readthedocs.io/en/latest/

.. _selenium: http://github.com/SeleniumHQ/selenium/

**演示代码的前置动作**

以使用Firefox为例

* 下载Firefox web驱动 `geckodriver` 并加入到环境变量
* 导入selenium相关模块

.. code-block:: python

    from selenium.webdriver import Firefox

----------------------------------------------------------------

等待
======================================

有强制等待、显式等待和隐式等待。一般是强制等待和显式等待搭配使用，隐式等待使用较少

.. warning::

    官方说显式等待和隐式等待不要同时使用

显式等待
--------------------------------------

等待元素可见并点击
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    ele = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'td'))
          )
    ele.click()

等待同一节点下的第二个元素可见
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    WebDriverWait(driver, 5).until(
            lambda x: x.find_elements(By.TAG_NAME, 'img')[1].is_displayed() is True
    )

等待加载元素消失
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

假设前端是使用element ui框架，加载元素使用的是 `class="el-loading-mask"`

.. code-block:: python

    # 收集当前页面的所有等待元素
    waits = driver.find_elements_by_class_name('el-loading-mask')
    # 显式等待使用的方法，所有wait元素任意一个出现在页面显式loading时返回True，否则返回False
    method = any(list(map(lambda ele: ele.is_displayed(), waits)))

    # 前置动作，点击刷新按钮触发加载等待页面
    driver.find_element_by_xpath('//span[text()="Refresh"]').click()

    # 确保loading遮罩层先出现，再等待消失
    WebDriverWait(self.driver, 30).until(lambda driver: method)
    WebDriverWait(self.driver, 30).until_not(lambda driver: method)

-----------------------------------------------------------

常见问题
===========================================================

带cookies登录
-----------------------------------------------------------

* 第一次先手工登录，然后保存好cookies( :ref:`get_cookies <selenium_util>` )
* 后续每次打开目标页面后，调用一次 :ref:`add_cookies <selenium_util>`

