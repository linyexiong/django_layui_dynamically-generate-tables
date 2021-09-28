# django_layui_dynamically-generate-tables

Click on the layui interface of Django to pop up a dialog box and request logic to generate paged dynamic tables 

django之Layui界面点击弹出个对话框并请求逻辑生成分页的动态表格

1、首先，创建一个django项目，名为djangotest，新建相关的目录，还有app模块，如下图所示：

![image](https://user-images.githubusercontent.com/10420128/135014480-4439ea79-4bd8-439b-85d0-96b1b27159e5.png)


2、接着，在本地数据连接mysql中，创建一个test数据库，后面项目将连接这个数据库

3、接着，django连接mysql，需要安装mysqlclient库，输入命令：pip install mysqlclient

![image](https://user-images.githubusercontent.com/10420128/135015248-9db17f35-2542-4b0a-855b-ad9734b8ffcb.png)

4、接着，修改setting底下数据库的配置，具体看项目的setting.py文件

5、新建一个user模块，输入命令：python manage.py startapp user

6、把user目录移到app模块底下，如下图所示：

![Uploading image.png…]()

之前在csdn写了博客，简单粗略的写了，地址：https://blog.csdn.net/u012561176/article/details/104008766
