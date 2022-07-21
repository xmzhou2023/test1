![transsion](http://10.250.112.151:18888/Evan/AutoTest/raw/master/tools/Transsioner20220721-151005.jpg)

# AutoTest自动化平台

[Badges]

## Introduction - 介绍
    基于pytest+requests+Allure设计所应用在DRP项目上的实现方案，集成了日志管理，数据库连接，case管理等功能
    框架结构：Python+requests+pytest+log+allure+yaml+mysql+git+jenkins+

### Summary - 概要
    基于DRP项目RAP2生成的接口文档运行脚本生成基础yaml文件所设计的脚手架，分离了业务逻辑，代码逻辑，运行数据，可通过直接修改数据来执行多个case，并对各接口进行管理

## Requirements - 必要条件（环境，对所有项目，和所有子模块和库的描述。）
    DRP项目对自动化的应用中，可通过修改config.ini配置文件，对环境的全局切换

## Configuration - 配置（配置信息。）
![transsion](http://10.250.112.151:18888/Evan/AutoTest/raw/master/tools/UML.jpg)


## Severity - 用例等级

    blocker　　  阻塞缺陷
    critical    严重缺陷
    normal      一般缺陷
    minor       次要缺陷
    trivial     轻微缺陷　

## Usage - 用法（用法。）
    三种运行方式，1、通过命令方式运行，2、通过命令方式+ini文件运行，3、通过main()运行

## Development - 开发（关于怎样开发的文档信息。（API 等。））
    基于DRP主要有13个模块，每个模块提供了多个接口，每个接口具体请求方式，传参，断言后期会不断优化

## FAQ - 常见问题（常见问题。）
    1、自动化环境的全局切换暂未完成开发
    2、各接口的调用方式未完善

## Support - 支持
    LiuYong,HuangQin

### Contact - 联系
    yong.liu7@transsion.com

### unit_assert - 断言
