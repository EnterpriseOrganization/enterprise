# enterprise

| 小组名     | 成员                             | 小组负责人 |
| ---------- | -------------------------------- | ---------- |
| 哈氏控股   | 严骅、唐鹏森、樊文杰、  刘艺玲   | 严骅       |
| 企业毁灭者 | 赵永赫、肖飞、高钰洋、  章文达   | 赵永赫     |
| 吴彦组     | 赵欣璇、陈齐翔、盛晓颖、  杨豪   | 赵欣璇     |
| 吴彦组     | 孟宇航、刘利卓、李皓、  魏辰芸   | 孟宇航     |
| 三人组     | 杨茗凯、汪庭盛、詹明鑫、  朱龙臻 | 杨茗凯     |

[TOC]



##一、仓库说明

**目录结构**

```tree
─backend
│  ├─enterprise
│  │  ├─migrations
│  │  │  └─__pycache__
│  │  └─__pycache__
│  └─mysite
│      └─__pycache__
├─database
└─frontend
    └─WeAdmin
        ├─lib
        │  ├─layui
        │  │  ├─css
        │  │  │  └─modules
        │  │  │      ├─laydate
        │  │  │      │  └─default
        │  │  │      └─layer
        │  │  │          └─default
        │  │  ├─font
        │  │  ├─images
        │  │  │  └─face
        │  │  └─lay
        │  │      └─modules
        │  └─layui2.0.2
        │      ├─css
        │      │  └─modules
        │      │      ├─laydate
        │      │      │  └─default
        │      │      └─layer
        │      │          └─default
        │      ├─font
        │      ├─images
        │      │  └─face
        │      └─lay
        │          └─modules
        ├─pages
        │  ├─BOM
        │  ├─echarts
        │  ├─information
        │  ├─order
        │  ├─purchase
        │  └─store
        └─static
            ├─css
            │  └─zTreeStyle
            │      └─img
            │          └─diy
            ├─fonts
            ├─images
            ├─js
            │  └─extends
            └─webfonts
```



- 此项目分为三个文件夹 <u>frontend 、 backend 和 database</u>.

  frontend内存放前端所需要的所有文件，包括资源文件、代码文件等等。

  backend内存放后端所需要的所有文件，包括资源文件、代码文件等等。

  database内存放有生成数据的脚本文件，以及前期生成的er图。

- 大家上传和下拉文件的时候，不要拉错文件夹。

- 前端和后端都要有更加详细的README文件介绍。



## 二、分工说明

| 小组       | 工作内容              |
| ---------- | --------------------- |
| 吴彦组(孟) | 采购信息管理          |
| 三人组     | 订单管理              |
| 吴彦组(赵) | 生产信息              |
| 企业毁灭者 | 用户管理和BOM信息管理 |
| 哈氏控股   | 成本和仓库            |

## 三、环境配置

###1. 环境要求：

- python == 3.5.*
- mysql ==5.*
- pip >=8.1.*

###2. 前端指南：

本次前端是基于Layui搭建的，具体使用方法可以参考[Layui官方文档](http://www.layui.com/doc/)或咨询**吴彦组（赵）**以获取帮助。

### 3.后端指南

在 git-bash命令行下,进入到 **database/** 完成下述工作

```sql
mysql -uroot -p [password]
create database enterprise;
exit;
mysql -uroot -p [password] enterprise < db.sql	
```

完成上述工作之后，将路径切换到**backend/**目录下

1. 将项目从本仓库拉倒本地之后需要安装Django

2. 安装Django：

   两种方式：

   1）pip 

   2）用easy_install

   上述命令没有的小组，自己查询，或者找**严骅或者唐鹏森**询问。

   命令

   ```shell
   pip install django==1.11.*
   ```

   上述过程中可能会报错,此时执行下述命令：

   ```shell
   pip install mysqlclient
   ```


3. 修改settings

   ```shell 
   vim mysite/settings.py
   ```

   将下面语段中的user和password改成如下：

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'enterprise',
           'USER': 'root',
           'PASSWORD':'enterprise',
           'HOST'：'localhost',
           'PORT':'3306',
       }
   }
   ```
   在linux环境下，可能发生下述问题，

   ```shell
   cannot connect to database througn mysql.sock//记不清了,好像大概是这个意思
   ```

   则将上面的**HOST**字段改成：

   ```python
   'HOST':'127.0.0.1'
   ```

   ​

4. 之后需要同步数据库操作如下

    - 如果之前已经git pull（5.24之前）过的同学，需要将models中以**AUTH**和**DJANGO**的class（其实就是一张表）删掉，之后将
    ```python
    managed = False
    ```
    修改成如下形式
    ```python
    managed = True
    ```
    然后进行之后的操作
    - 如果之前没有git pull过，或者重新git clone 下来的同学，直接进行下面步骤

5. 删除掉<text style="color:#f00">backend/enterprise/migrations/</text>文件夹中所有的.py文件删除，然后退回到目录<text style="color:#0f0">backend</text>下执行后面的步骤

6. 如果原本mysql中没有东西，则执行如下命令进行创建数据库
   ```shell
   mysql -uroot -p[密码]
   ```
   ```mysql
   create database enterprise；
   exit
   ```

7. 在目录<text style="color:#0f0">backend</text>下执行下述命令(在linux环境下python manage.py 可以用 ./manage.py代替)

   ```shell
   python manage.py migrate
   ```
   如果出现
   ```shell
   Applying xxx
   ```
   字样，且没有error的提示，说明成功，则继续下面步骤

8. 同级目录下执行

   ```shell
   python manage.py makemigrations enterprise
   ```

   如果出现

   	<text style="color:#00f">Create model xxx</text>

​       字样，且无error则说明成功，继续下面的步骤
9. 执行
    ```shell
    python manage.py migrate
    ```
    即可完成上述操作

10. 确认数据库已经成功创建

   ```shell 
   mysql -uroot -p[密码]
   ```

   ```mysql
   use enterprise
   show tables
   ```

   如果显示出来的表名字，与models.py的内容都一样，那么就成功了。
   或者说表的数量大约为20多个

11. 测试是否成功

   ```shell
   ./manage.py runserver 0:8000
   ```

**后端配置有问题，找严骅/唐鹏森/孟宇航咨询**

## 四、各组需求说明

![需求](https://github.com/EnterpriseOrganization/enterprise/blob/master/images/%E9%9C%80%E6%B1%82.png)

## 五、规范性要求

### A.git规范

1. 一个team创建一个team的主分支，每次组员（有自己的分支）提交的时候，有小组负责人进行merge操作。
2. 时间上，应该2~3天进行merge一次，每个team应该5天发起一个merge请求。
3. 每个team的主分支命名应该以小组的名字或者负责人的名字为主分支名字前缀或者就作为小组主分支的名字。
4. 小组内部由负责人负责，将小组内的issue尽量提交完整。
5. 每次push之前，要先对远端分支进行pull操作

### B.命名规范

1. 内部函数命名同意使用小驼峰的形式，
2. 变量命名使用全部小写单词与单词之间用下划线连接的形式(如a_b)
3. 变量名字避免使用数字作为区分，除非实在有必要
4. 前后端方法要做到REST风格，有困难的可以放宽要求

## 六、各个小组操作的远端分支部分

<text style="color:#f00">每个小组只能操作自己对应的小组文件夹内部的文件，不能够操作别的小组的文件夹</text>

各小组与其文件夹的操作关系如下：

哈氏控股		————————app_cost_warehouse

三人组		————————app_order

企业毁灭者	————————app_bom_permission

吴彦组（孟）———————— app_purchase

吴彦组（赵）———————— app_product



一个文件夹内部的结构举例有：

```shell
tree
│  admin.py

│  apps.py

│  models.py

│  tests.py

│  views.py

│  init.py

│

├─migrations

│  │  0001_initial.py

│  │  init.py

│  │

│  └─pycache

│          0001_initial.cpython-36.pyc

│          init.cpython-36.pyc

│

└─pycache

        admin.cpython-36.pyc

        models.cpython-36.pyc

        init.cpython-36.pyc

```

## 七、时间进度安排

![时间序列](https://github.com/EnterpriseOrganization/enterprise/blob/master/images/%E6%97%B6%E9%97%B4%E5%BA%8F%E5%88%97.png)
