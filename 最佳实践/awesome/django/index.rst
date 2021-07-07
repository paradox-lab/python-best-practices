Django - Web框架
==============================

:中文版: https://docs.djangoproject.com/zh-hans/3.2/

:github: https://github.com/django/django

模型层
*************************

关联对象

* ⭐ **正向访问** 若模型有个 ForeignKey，该模型的实例能通过其属性访问关联（外部的）对象。

视图层
*************************

URL配置

------------------------------------------

* **路径转换器**
    - **str** 匹配除了 '/' 之外的非空字符串。如果表达式内不包含转换器，则会默认匹配字符串。
    - **int** 匹配 0 或任何正整数。返回一个 int 。
    - slug  匹配任意由 ASCII 字母或数字以及连字符和下划线组成的短标签。比如，building-your-1st-django-site
    - uuid 匹配一个格式化的 UUID 。为了防止多个 URL 映射到同一个页面，必须包含破折号并且字符都为小写。比如，075194d3-6885-417e-a8a8-6c931e272f00。返回一个 UUID 实例。
    - path 匹配非空字段，包括路径分隔符 '/' 。它允许你匹配完整的 URL 路径而不是像 str 那样匹配 URL 的一部分。

表单
*************************
* **表单代码放在在app/forms.py** django/contrib/auth/forms.py
* **forms.CharField**  表单字符串字段
  - label参数
  - max_length参数
* **form.is_valid** 验证数据
* **Form类** 🍔
* **ModelForm类** 🍔🍔

-------------------------------------------------------------

表单字段

* **required** 要指定一个字段是 不必填 的，传递 required=False 给 Field 构造函数

-------------------------------------------------------------

部件

* **PasswordInput** django.contri.auth.forms.UserCreationForm.password1 | pydqe.dqe.forms.DataSourceCreationForm.password 等同于<input type="password" ...>

后台管理系统
*************************

* **register装饰器** 🍕🍕 django/contrib/auth/admin.py pydqe 注册模型类
* **admin.site.register** 🍕  注册模型类

-------------------------------------------------------

* **ModelAdmin.form** 动态创建一个 ModelForm
* **ModelAdmin.get_form** 返回一个 ModelForm 类
* **ModelAdmin.get_urls** 与 URLconf 相同的方式返回用于该 ModelAdmin 的 URL | pydqe/dqe/admin.py

------------------------------------------------------

* **AdminSite对象** Django管理站点的实例
* **site_header** 要放在每个管理页面顶部的文字，作为 <h1> （一个字符串） | pydqe/dqe/admin.py
* **将AdminSite实例挂到你的URLconf中** 注册默认的adminsite
* **覆盖默认的管理站点** 覆盖默认的 django.contrib.admin.site | pydqe/pydqe/admin.py
* **get_app_list** 可以重写方法以改变模型排序的顺序，默认是按字母排序

* 自定义AdminSite对象类 可以自由地将 AdminSite 子类化，并覆盖或添加任何你喜欢的内容

----------------------------------------------------------

* **ModelAdmin 静态资源定义** 在添加／更改视图时添加一点 CSS 和／或 JavaScript。 pydqe/dqe/admin.py

安全
*********************************************************

* **AJAX携带CSRF令牌** 在每个 XMLHttpRequest 上，设置一个自定义的 X-CSRFToken 头为 CSRF 标记的值 | pydqe/dqe/static/admin/js/mu_code.js

配置
*********************************************************

* **DEFAULT_AUTO_FIELD** 默认的主键字段类型，用于没有带有 primary_key=True 字段的模型。默认：'django.db.models.AutoField'