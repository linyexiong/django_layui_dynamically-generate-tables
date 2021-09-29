# django_layui_dynamically-generate-tables

Click on the layui interface of Django to pop up a dialog box and request logic to generate paged dynamic tables 

django之Layui界面点击弹出个对话框并请求逻辑生成分页的动态表格

一、django项目环境搭建

1、首先，创建一个django项目，名为djangotest，新建相关的目录，还有apps目录，里面放置多个app模块，如下图所示：

![image](https://user-images.githubusercontent.com/10420128/135018542-3cfd413d-4e20-4099-b8f2-ba3951f7c61b.png)

2、接着，在本地数据连接mysql中，创建一个test数据库，后面项目将连接这个数据库

3、接着，django连接mysql，需要安装mysqlclient库，输入命令：pip install mysqlclient

![image](https://user-images.githubusercontent.com/10420128/135015248-9db17f35-2542-4b0a-855b-ad9734b8ffcb.png)

4、接着，修改setting底下数据库的配置，具体看项目的setting.py文件

5、新建一个user模块，输入命令：python manage.py startapp user

6、把user模块移到apps底下，如下图所示：

![image](https://user-images.githubusercontent.com/10420128/135018642-6271aad0-6d83-446c-9373-86398811d0a8.png)

7、接着在setting.py文件中，安装user这个app模块，并修改底下相关的配置，具体看项目下的setting.py文件，如下图所示：

![image](https://user-images.githubusercontent.com/10420128/135018001-bb98e566-c9f0-4f72-a619-afb96006ba73.png)

![image](https://user-images.githubusercontent.com/10420128/135018878-ff75508e-54a6-4e48-a9db-6423e68348eb.png)

8、接着打开user下的model.py文件，创建一个Class UserInfo，如下图所示：

![image](https://user-images.githubusercontent.com/10420128/135017627-93934d92-d932-4745-8c44-5857900ead5f.png)

9、执行命令，python manage.py makemigrations user

![image](https://user-images.githubusercontent.com/10420128/135019032-243ada3d-2408-4db7-a25a-a02016be9fb1.png)

10、再执行命令：python manage.py sqlmigrate user 0001

![image](https://user-images.githubusercontent.com/10420128/135019270-ab33d271-8e64-430e-be6e-d79c39ca69bf.png)

11、再执行命令：python manage.py migrate

![image](https://user-images.githubusercontent.com/10420128/135019423-08cabc29-b7d8-4870-b840-bfba43912bf9.png)

12、这时，可以看到本地的数据库test已经有了tbl_user_info的表，如下图所示：

![image](https://user-images.githubusercontent.com/10420128/135019548-371eb626-b177-4147-b952-ced46c2fea92.png)

二、接着，开始写相关代码

1、首先，在user模块底下的views.py下，定义一个UserQuery类，写相关的逻辑处理代码：

![image](https://user-images.githubusercontent.com/10420128/135225694-546f3382-cbd4-4d75-90c3-ac1bdd2bbe38.png)

2、接着，在user模块下新建一个urls.py文件，相当于一个路径请求，到时候界面调用时用到：

![image](https://user-images.githubusercontent.com/10420128/135226390-11ec8dd8-57b6-44d9-8115-b9bdf516313f.png)

3、接着要在django_test底下的urls.py中，配置user模块url的相关路径，这样页面才能正常调用：

![image](https://user-images.githubusercontent.com/10420128/135235153-1ee99d35-7b17-4535-96d5-0d16e4346722.png)

4、接着，在template目录下，新建一个user目录，新建界面user_list.html，就一个空的表格，底下有个按钮，点击后查询用户的数据，产生一个动态表格，其中用了layui


之前在csdn写了博客，简单粗略的写了，地址：https://blog.csdn.net/u012561176/article/details/104008766
