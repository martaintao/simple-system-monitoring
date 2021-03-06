# 简单的模拟系统状态监控系统

## 前言

该项目为参照贵司全栈工程师（python）题目所完成的简单的一个系统。

阅读了贵司题目要求，经过我的思考并没能直接思考出一个背景来完成题目中的要求，非常抱歉我对题目做了一些修改，来完成我这个简陋的程序的背景——系统状态监控。

我做出了如下修改：

* 题目中要求程序要包含两个页面，而我使用了标签页`（Tabs）`的方式来分别展示了两个模块。
* 题目中要求每10秒刷新一次数据，由于我实现了一个"实时性能监控"的模块，将每10秒改成了每秒来达到程序所需要的效果。
* 题目中要求提供一个按钮将数据保存到一个历史表中记录，该需求我直接使用使用获取数据时保存的数据来实现该类似的功能

非常抱歉未经贵司许可擅自修改贵司题目，我本着尽可能更好的完成题目的出发点，题目只是检验能力的初衷，希望贵司可以认真查看我所完成的任务，非常感谢！

## 环境说明

|    库名    |  版本  |             作用             |
| :--------: | :----: | :--------------------------: |
|    vue     | 2.6.12 |         前端开发框架         |
|   axios    | 0.21.0 |          前端请求库          |
| Highcharts | 8.2.2  |            图表库            |
| element-ui | 2.12.0 |          前端UI框架          |
|   python   | 3.8.5  |              -               |
|   flask    | 1.1.2  |       python web微框架       |
|   gevent   | 20.9.0 | 高性能web服务，部署flask作用 |
|  pymongo   | 3.11.2 |         mongo连接库          |
|   mongo    | 4.4.2  |         mongo数据库          |

## 程序说明

### 项目结构

```bash
└─visual
    │  main.py  # 程序入口文件
    │  requirements.txt # 依赖包列表
    ├─static # 静态文件夹
    │  └─lib
    │      │  axios.min.js # axios库
    │      │  vue.js  # vue 库
    │      ├─el  # element-ui 库
    │      └─highcharts  # highcharts 库
    └─templates # 模板文件夹
            index.html # 前端页面
```

### 部署方式

```bash
pip install -r requirements.txt # 安装gevent如果失败请升级pip
python main.py
```

> 访问 http://127.0.0.1:8089

### 功能说明

#### 实时监控

![实时监控](https://gitee.com/MartainTao/pic/raw/master/20201209212157.png)

> 实时监控功能实现了对CPU和内存的监控（虽然后台是模拟的，其实也可以用`psutil`库很容易来实现），前端分别轮询后端接口来实现图表实时数据的填充。



#### 历史记录

![历史记录程序](https://gitee.com/MartainTao/pic/raw/master/20201209212151.png)

> 历史记录中通过请求后台接口，获取最近的100次记录。

## 总结

该系统使用前后端分离的模式开发，出于从简出发的目的，前端使用嵌入`vue`的方式开发而不是使用单页面的方式开发，后端使用`Flask`开发接口，该项目中没有用到蓝图以及配置文件相关模块，数据库使用的是`mongodb`提供数据的存取，因为能力原因，系统中还存在许多问题以及可优化的地方，还望贵司指出,谢谢。

## 附文

[在线demo地址](https://demo.martaintao.club/)

> 为了方便部署，该项目中前端所有的依赖都所有的本地库的方式引入，所以访问在线demo会比较慢以及卡顿。

[Github地址](https://github.com/martaintao/simple-system-monitoring)

[Gitee地址](https://gitee.com/martainTao/simple-system-monitoring)

[简书主页](https://www.jianshu.com/u/f1a625d3d89d)

[个人博客站点](https://blog.martaintao.club/)

