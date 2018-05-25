# enterprise

| 小组名     | 成员                             | 小组负责人 |
| ---------- | -------------------------------- | ---------- |
| 哈氏控股   | 严骅、唐鹏森、樊文杰、  刘艺玲   | 严骅       |
| 企业毁灭者 | 赵永赫、肖飞、高钰洋、  章文达   | 赵永赫     |
| 吴彦组     | 赵欣璇、陈齐翔、盛晓颖、  杨豪   | 赵欣璇     |
| 吴彦组     | 孟宇航、刘利卓、李皓、  魏辰芸   | 孟宇航     |
| 三人组     | 杨茗凯、汪庭盛、詹明鑫、  朱龙臻 | 杨茗凯     |

##一、仓库说明

- 此项目分为三个文件夹 <u>frontend 、 backend 和 database</u>.

  frontend内存放前端所需要的所有文件，包括资源文件、代码文件等等。

  backend内存放后端所需要的所有文件，包括资源文件、代码文件等等。

  database内存放有生成数据的脚本文件，以及前期生成的er图。

- 大家上传和下拉文件的时候，不要拉错文件夹。

- 前端和后端都要有更加详细的README文件介绍。



## 二、分工说明

| 小组       | 工作内容              |
| ---------- | --------------------- |
| 吴彦组(孟) | 采购信息管理                |
| 三人组     | 生产信息  |
| 吴彦组(赵) | 订单管理              |
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

   两种方式：1）pip 

​		          2）用easy_install

​	上述命令没有的小组，自己查询，或者找**严骅或者唐鹏森**询问。

​	命令

```
pip install django==1.11.*
```

上述过程中可能会报错,此时执行下述命令：

```
pip install mysqlclient
```

3. 修改数据库

```
vim mysite/settings.py
```

将下面语段中的user和password改成如下：

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'enterprise',
        'USER': 'root',
        'PASSWORD':'enterprise',
    }
}
```

4. 在运行Django之前要先进行migrate，在后端目录下执行下述命令

   ```
   ./manage.py migrate
   ```


5. 测试是否成功

   ```shell
   ./manage.py runserver 0:8000
   ```

   ​
