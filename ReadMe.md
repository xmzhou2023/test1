![transsion1](http://10.250.112.151:18888/Evan/AutoTest/raw/master/tools/Transsioner20220721-151005.jpg)

# AutoTest自动化平台

## Introduction - 设计简介

### 一、框架结构简述：

已附在当前文档最后

### 二、框架设计思想---POM模式

##### 1、POM简介

**      即引入了POM设计模式，即Page Object Model**，这也是是目前最为经典的一种设计思想，用大白话说就是：**将页面UI元素对象、逻辑、业务、数据等分离开来，使得代码逻辑更加清晰，复用性，可维护性更高的一种方法。**

##### 2、POM模式的优点

- 让UI自动化更早介入项目中，可项目开发完再进行元素定位的适配与调试
- POM 将页面元素定位和业务操作流程分开，分离了测试对象和测试脚本
- 如果UI页面元素更改，测试脚本不需要更改，只需要更改页面对象中的某些代码就可以
- POM能让我们的测试代码变得可读性更好，高可维护性，高复用性，
- 可多人共同维护开发脚本，利于团队协作

##### 3、POM模式设计之元素、页面、用例三层

- **元素层**：如下图统一将一个页面的元素定位规范到一个文件中

![transsion2](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/v2/cover/boxcn0qAaGilWpm5blCaoBV0gkf/?mount_node_token=doccn6IMEzfzCiZ057psRJMFKrf&mount_point=doc_image&policy=equal)

- **页面层**：本类中主要实现页面元素、业务逻辑所需要的步骤方法的封装

![transsion3](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/v2/cover/boxcnswCFfTKfJnNNbQvtZEjBkd/?mount_node_token=doccn6IMEzfzCiZ057psRJMFKrf&mount_point=doc_image&policy=equal)

- **用例层**：这一层输入POM的业务数据层，主要实现测试步骤及测试数据的

![transsion4](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/v2/cover/boxcnvbNQa8xAciCx1P9cI6NoAh/?mount_node_token=doccn6IMEzfzCiZ057psRJMFKrf&mount_point=doc_image&policy=equal)

## UIPOMTest使用及常用api

### 一、快速使用框架

#### 1、创建本地project

- 克隆项目到本地

git clone 项目地址

- 安装库（前提是已经有Python环境, Python安装教程参看https://jingyan.baidu.com/article/f3e34a12af57cdb4ea653507.html

Pip install -r requirement.txt

- 新建项目远程分支（自动化平台的人完成）
- 将本地分支关联远程分支

####       2、配置项目基础环境

- copy DRP项目
- 修改项目名称，将project下面默认的DRP修改成为XXX，XXX须大写
- 修改conf.py 文件，如下图，将当前项目目录下面的DRP改成自己项目的名称

![img](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/v2/cover/boxcnUWzSD0WbPYUPk0hXM6cUQe/?mount_node_token=doccnAMEhPTv5SASQkRExa0agSc&mount_point=doc_image&policy=equal)

- 修改项目配置文件中的host和sql 连接串，路径：project-->env-->test&&uat-->config.ini

![img](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/v2/cover/boxcn92I4Ai0fWcWJgjvqZxEWOf/?mount_node_token=doccnAMEhPTv5SASQkRExa0agSc&mount_point=doc_image&policy=equal)

#### 3、创建testcase文件

3.1 生成测试模块文件

- 梳理系统中所有的菜单模块，按照框架中template中modle_name.csv进行编写
- 命名规则：一级菜单_二级菜单...最小菜单

![img](https://transsioner.feishu.cn/space/api/box/stream/download/asynccode/?code=MGQxZDI1NjE4YzQwYzQyOTZlMTYzNmUzY2NlY2U2MDJfR0xFaVRxR1RpeFdRRktOaEZQZ0ZKTGlDTEY1WXNOZ2NfVG9rZW46Ym94Y243Wm5aa3pIMjI0ZXc0dWFxMWtBbjNnXzE2NTgzODk3OTA6MTY1ODM5MzM5MF9WNA)

3.2 编写页面元素定位文件

- 路径：project-->xxx-->page_element
- 页面元素文件

新增：在libs-->tools-->create_dir.py, 调用generate_module("element")方法，生成对应页面元素文件, xxx.yaml

修改和删除：修改和删除modle_name.csv内容, 在libs-->tools-->create_dir.py, 再次调用generate_module("element")方法，即可修改名称

- 内容格式 元素名称：“元素路径”
- 例：人员列表-新增人员搜索框: "xpath==//input[@placeholder='请输入姓名或工号']"

​     3.3 编写页面元素操作文件

- 路径：project-->xxx-->page_object
- 页面对象文件****

新增：在libs-->tools-->create_dir.py, 调用generate_module("object")方法，生成对应页面元素文件, xxx.py****

修改和删除：修改和删除modle_name.csv内容, 在libs-->tools-->create_dir.py, 再次调用generate_module("object")方法，即可修改名称

- 内容:将页面定义成类，并将常用的元素操作封装成类方法暴露给testcase调用
- 例：

![img](https://transsioner.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2Q2MjM1YzIxMzI5OTAzNjQzNzMzMWJmZTdmMTM5YmZfM2padmJ6am13YTY4TUVIVUZiM1FDVnd1Zk80R1J4VmVfVG9rZW46Ym94Y25YSGQ4dkpKUlI4RlVZREljS2hjTXpjXzE2NTgzODk3OTA6MTY1ODM5MzM5MF9WNA)

3.4 编写测试用例

- 路径：project-->xxx-->test_case
- 用例文件：

新增：在libs-->tools-->create_dir.py, 调用generate_module("case")方法，生成对应页面元素文件, xxx.py****

修改和删除：修改和删除modle_name.csv内容, 在libs-->tools-->create_dir.py, 再次调用generate_module("case")方法，即可修改名称

- 测试类:包含类名和一个测试场景为一个测试类
- 测试用例：

![img](https://transsioner.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTY3OTVmY2I3ZTVmOTA5YzFmYmMwMWVjNTYzOTM1M2NfY09wc2sxOVoyVTJucUY5N3FQSUNUa0g3eFBYZGwwRUFfVG9rZW46Ym94Y25Fb1pTQWFkbVdBZ2dQWHNSTG42VDdmXzE2NTgzODk3OTA6MTY1ODM5MzM5MF9WNA)

3.5 用例调试运行

- 在根目录下面的pytest.ini文件中配置 对应的运行路径和Python文件、测试类和测试方法，然后运行pytest即可

![img](https://transsioner.feishu.cn/space/api/box/stream/download/asynccode/?code=OGZmNWMyY2Y5NGM3OGY4MGE1NTEwNTljZGJkMDY5ZmZfYnZHNVRMZ2gyNmhQNElQbkJtWkxUQmdndVcwTmxrZzdfVG9rZW46Ym94Y25mZGpoTUJtZFI0TjZqV3VRRW5XNEFmXzE2NTgzODk3OTA6MTY1ODM5MzM5MF9WNA)

3.6 查看报告

allure serve 报告目录位置，例如：allure serve ./allure-reports

3.7 提交代码

git add .

git  commit -m "新增xxx"

git push

### 二、常用元素操作方法

路径：public-->base-->basic.py

##### 1.打开浏览器

​     **get_url（url)**

- 入参： url ，例：url = "http://10.250.112.57/#/dashboard"
- 功能：打开浏览器之前，会进行窗口最大化处理，并且在请求网页之后，加了显示等待
- 返参：无

##### 2. yaml 文件的元素转化成元素定位

**Element(name)**

- 入参：

 name, 传page_element 目录下面的相关yaml的文件名，例：Element('user')

- 功能：实例化Element 类，得到Element对象，调用Element('user')["关键字"]能得到元素定位

![img](https://transsioner.feishu.cn/space/api/box/stream/download/asynccode/?code=MmQ2NWFjYjIyYjQwYmNlOTEwOTkzZWExMGI1OWVjYTZfalQ5Z2EwcXRaSU1NbVpjcjNsTDhYMHE3TFFLd2RQckJfVG9rZW46Ym94Y25FbjROeFkya3dxTTZ5bVJZWmxkSDVlXzE2NTgzODk3OTA6MTY1ODM5MzM5MF9WNA)

如图：Element('user')["提报管理->DRP0"] 可以得到--->("xpath","//span[contains(text(),'DRP0报表')]")

- 返参：无

##### 3.查找单个元素

**find_element (locator，choice)**

- 入参：

locator 必填，元素定位 ,例如：Element('user')["提报管理->DRP0"]

choice 选填，元素的索引，int 类型

- 功能：直到元素可见，才视为找到该元素
- 返参：单个元素对象

##### 4.查找多个元素

**find_elements(locator)**

- 入参：

locator 必填，元素定位 ,例如：Element('user')["提报管理->DRP0"]

- 功能：直到所有被找元素显示，才视为找到这些元素
- 返参：以列表的形式返回多个元素对象

##### 5.获取多个相同定位元素的数量

**elements_num（locator）**

- 入参：

locator：必填，元素定位 ,例如：Element('user')["提报管理->DRP0"]

- 功能：*获取相同元素的个数*
- 返参：number *相同元素的个数*

##### 6.文本框输入文本

**input_text (locator, txt)**

- 入参：

locator：必填，元素定位 ,例如：Element('user')["提报管理->DRP0"]

- txt: 必填 , 要输入的文本内容
- 功能：先将文本框进行清除，再在输入框输入文本txt
- 返参：无

##### 7.只读文本框输入文本

**  readonly_input_text（locator, txt）**

- 入参：

locator：必填，元素定位 ,例如：Element('user')["提报管理->DRP0"]

txt: 必填 , 要输入的文本内容

- 功能：先去掉文本框的只读属性，再对文本框输入文本
- 返参：无

##### 8.元素点击操作

**is_click（locator,choice）**

- 入参：

locator：必填，元素定位 ,例如：Element('user')["提报管理->DRP0"]

choice:  选填，元素的索引，int 类型

- 功能：当只传入一个locator, 则点击locator，当传入choice，则需要先获取目标locator, 再点击元素
- 返参：无

##### 9.点击空白处

**click_blank()**

- 入参：无
- 功能：点击页面空白处
- 返参：无

##### 10.js点击操作

**force_click（xpath, force=False):**

- 入参：

xpath：必填，元素定位 ,例如：Element('user')["提报管理->DRP0"]

force:  选填，布尔类型，默认False

- 功能：当force=True, 可以使用js 进行强制点击，否则进行普通点击
- 返参：无

##### 11.获取文本值

**element_text（locator）**

- 入参：

locator：必填，元素定位 ,例如：Element('user')["提报管理->DRP0"]

- 功能：获取当前元素的文本值
- 返参：文本值

##### 12.alert 确定框

**alert_ok()**

- 入参：无
- 功能：先等待alert框的出现，再点击alert框的确定按钮
- 返参：无

##### 13.页面滑动，寻找元素

**scroll_into_view（locator, choice=None）**

- 入参：

locator 必填，元素定位 ,例如：Element('user')["提报管理->DRP0"]

choice 选填，元素的索引，int 类型

- 功能：先定位目标元素，再滑动直至出现目标元素（locator ）元素
- 返参：无

##### 14.切换iframe

**frame_enter（xpath）**

- 入参：

xpath 必填，元素定位 ,例如：Element('user')["提报管理->DRP0"]

- 功能：先查找元素, 再判断元素的tag 是不是iframe, 最后切换到对应的iframe
- 返参：无

##### 15.返回上一层iframe

**frame_exit()**

- 入参：无
- 功能：退出当前的frame，返回上一层iframe
- 返参：无

##### 16.返回最外层的iframe

**frame_top()**

- 入参：无
- 功能：退出当前的frame，返回最外层的iframe
- 返参：无

##### 17.刷新页面

**refresh**

- 入参：无
- 功能：页面刷新，并等待30秒
- 返参：无

##### 18.窗口切换

**switch_window(n)**

- 入参

n：表示窗口的索引，当前窗口的索引为0, 再往右一个窗口为1，依次类推

- 功能：切换窗口
- 返参：无

##### 19.关闭窗口

**close_switch（n）**

- 入参

n：表示窗口的索引，当前窗口的索引为0, 再往右一个窗口为1，依次类推

- 功能：先切换到新目标(索引为n的窗口)，关闭此窗口，再切换到原始窗口
- 返参：无

##### 20.鼠标悬停

**hover（locator）**

- 入参

locator：必填，元素定位 ,例如：Element('user')["提报管理->DRP0"]

- 功能：先查找目标元素，再将鼠标移动到目标元素
- 返参：无

##### 21.文件下载

**check_download（locator, content）**

- 入参

locator：必填，元素定位 ,例如：Element('user')["提报管理->DRP0"]

content：文件路径

- 功能：先判断是否存在该文件，有则清除文件，再执行点击文件，最后断言下载文件是否成功
- 返参：无

### 三、常用断言方法

路径：public-->base-->assert_ui.py

##### 值校验方法

1.断言俩值相等

- **value_assert_equal(a,b)**
- 入参：a,b
- 功能：断言俩值相等，当俩值不相等的时候，断言失败，抛出异常
- 返参：无

2.断言俩值不等

- **value_assert_Notequal（a,b）**
- 入参：a,b
- 功能：断言俩值不相等，当俩值相等的时候，断言失败，抛出异常
- 返参：无

3.断言值为True

- **value_assert_True(x)**
- 入参：x
- 功能：断言x为True, 当x的值为False的时候，断言失败，抛出异常
- 返参：无

\4. 断言值为False

- **value_assert_False(x)**
- 入参：x
- 功能：断言x为False, 当x的值为True的时候，断言失败，抛出异常
- 返参：无

5.断言是否是本身

- **value_assert_Is(a,b)**
- 入参：(a,b)
- 功能：断言a对象的内存地址是b对象的内存地址, 当a对象的内存地址是b对象的内存地址，断言失败，抛出异常
- 返参：无

6.断言是否是本身

- **value_assert_IsNot(a,b)**
- 入参：(a,b)
- 功能：断言a对象的内存地址不是b对象的内存地址, 当a对象的内存地址是b对象的内存地址，断言失败，抛出异常
- 返参：无

7.断言值为None

- **value_assert_IsNone(x)**
- 入参：(x)
- 功能：断言x为None, 当x不为None，断言失败，抛出异常
- 返参：无

8.断言值不为None

- **value_assert_IsNoneNot(x)**
- 入参：(x)
- 功能：断言x不为None, 当x为None，断言失败，抛出异常
- 返参：无

9.断言包含

- **value_assert_In(a,b)**
- 入参：(a,b)
- 功能：断言a 被b 包含，当a不被b 包含，断言失败，抛出异常
- 返参：无

10.断言不包含

- **value_assert_InNot(a,b)**
- 入参：(a,b)
- 功能：断言a 不被b 包含，当a被b 包含，断言失败，抛出异常
- 返参：无

11.断言值为指定类型

- **value_assert_Instance(a,b)**
- 入参：a,对象，b为类型
- 功能：断言a 是b 类型，当a不是b类型，断言失败，抛出异常
- 返参：无

12.断言值不是指定类型

- **value_assert_Instance(a,b)**
- 入参：a,对象，b为类型
- 功能：断言a 不是b 类型，当a是b类型，断言失败，抛出异常
- 返参：无

##### 页面元素校验

1.断言运行系统

- **assert_platform（word）**
- 入参：
  - word 预期运行系统
- 功能：断言实际运行系统是预期运行系统，当实际运行系统不是预期运行系统，断言失败，抛出异常
- 返参：无

2.断言页面是否存在某文字

- **assert_att（word）**
- 入参：
  - Word 预期文字
- 功能：断言当前页面包含预期文字word，当前页面不包含预期文字word，断言失败，抛出异常
- 返参：无

3.断言当前页面title是否符合预期

- **assert_title（word）**
- 入参：
  - Word 预期title
- 功能：断言当前页面title等于预期title word，当前页面title不等于预期title，断言失败，抛出异常
- 返参：无

\4. 断言当前页面title是否为指定url

- **assert_url(word)**
- 入参：
  - Word 预期url
- 功能：断言当前页面url等于预期url word，当前页面url不等于预期url，断言失败，抛出异常
- 返参：无

\5. 断言当前页面title是为该标识

- **assert_page_source(word)**
- 入参：
  - Word 预期标识
- 功能：断言当前页面元素不包含预期标识，当前页面元素包含预期标识，断言失败，抛出异常
- 返参：无

6.断言当前下拉选择值是否符合预期

- **assert_select(element, word)**
- 入参：
  - Element 下拉项元素定位
  - word 预期值
- 功能：断言当下拉项元素等于预期值 word ，当下拉项元素不等于预期值 word，断言失败，抛出异常
- 返参：无

7.在校验文件名和预期是否一致

- **assert_filename（element，word）**
- 入参：
  - Element 被断言的文件元素
  - Word 预期文件名
- 功能：断言被断言的文件名等于预期文件名，当被断言的文件名等于预期文件名，断言失败，抛出异常
- 返参：无

8.断言元素颜色

- **assert_domcolor（element, color）**
- 入参：
  - Element 被断言的元素
  - color 预期颜色
- 功能：断言element的颜色等于预期颜色 ，当element的颜色不等于预期颜色，断言失败，抛出异常
- 返参：无

9.断言当前alert文字

- **assert_alerttext（element,content）**
- 入参：
  - Element 被click的元素
  - content 预期文字
- 功能：断言alert框内容等于预期文字 ，当alert框内容不等于预期文字，断言失败，抛出异常
- 返参：无

##### 数据库断言

1.页面是否存在某文字

- **assert_sql（word, sql）**
- 入参：
  - sql 查询语句
  - word 预期值
- 功能：断言预期值是否在数据库查询表中 ，当预期值不在数据库查询表中，断言失败，抛出异常
- 返参：无

UIPOMTest编码规范

### 一、数据文件规范（元素定位文件，测试数据文件，测试用例，场景，前后置，关联场景）

##### 1、元素定位文件 

- 主要涵盖**元素名称和元素定位路径**
- **文件路径**: page_element文件夹下面
- **页面元素文件生成**

新增：在libs-->tools-->create_dir.py, 调用generate_module("element")方法，生成对应页面元素文件, xxx.yaml

修改和删除：修改和删除modle_name.csv内容, 在libs-->tools-->create_dir.py, 再次调用generate_module("element")方法，即可修改名称

- 内容规范注意点

  ： 

  - 元素定位名称:"定位方式==元素路径"
  - 相同属性的定位可以放置在一起，用空行隔开，便于查找

##### 2、测试数据文件

推荐--》测试数据与测试用例分隔

测试数据规范：

- 路径：public-->data-->datasource
- 编写规范：模板如下图一

![img](https://transsioner.feishu.cn/space/api/box/stream/download/asynccode/?code=OGE4MWYzMmIzYWJmOTllOWY1NmViODIyMjIzMTg1NWJfdEY3VmN0YktQYVFZYjRURGd5cWJIRVI4Wkl4cTBHcExfVG9rZW46Ym94Y24xM216RTlJUDYwSmw1Rk9PaEJDanhlXzE2NTgzODk4NjM6MTY1ODM5MzQ2M19WNA)

图一

- 数据注册：在unified_login.py 中仿照实例进行注册，如下图二

![img](https://transsioner.feishu.cn/space/api/box/stream/download/asynccode/?code=Mjg4NWY2MGJmYTM4MTNmNTdlMDBhZDNiMjVkYTM3YmZfeHdQQmRZZzAzYVZlME9rRndsalc2Y0dJQ09xVjcwdVJfVG9rZW46Ym94Y251RERRendEZzc0SzVtT0xlcHFPdHdlXzE2NTgzODk4NjM6MTY1ODM5MzQ2M19WNA)

图二

- 测试数据调用：如图二，account 对象为含字典类型对象的列表，如需调用图一中的第二行的username，调用account[0]["username"]

##### 3、测试用例

![img](https://transsioner.feishu.cn/space/api/box/stream/download/asynccode/?code=MmIxZDkxNjQ5OWNlNjllYzJmZThkMzg2YzNlZjFlYThfbkRRdnZGM0xmVnJVV0RsSFZwa2dDcVhMUWpZcjZYVTJfVG9rZW46Ym94Y25aclhxaFZCNEI1dnpURUhiUjAxWXBkXzE2NTgzODk4NjM6MTY1ODM5MzQ2M19WNA)

图三

- 文件路径：test_case文件夹下面
- 用例文件：

新增：在libs-->tools-->create_dir.py, 调用generate_module("case")方法，生成对应页面元素文件, xxx.py****

修改和删除：修改和删除modle_name.csv内容, 在libs-->tools-->create_dir.py, 再次调用generate_module("case")方法，即可修改名称

- 测试类：一个测试类代表一个测试场景
  - 测试类别主要包含增(Create)、删(Delete)、改(Update)、查(Search)、上传(Upload)、下载(Download)、导入(Import)、导出(Export)


- 测试类名称：以Test+测试类别英文名称+主要测试功能，例如：TestSearchArea


- 模块名称：标记在测试类的@allure.feature("")，该文件的中文名


- 场景名称: 标记在测试方法的@allure.story("")，测试类的中文名称


- 测试用例：

  - - 测试用例名称：以test+tapd测试用例的编号


- 用例等级：如图三包含五个等级,分别blocker（中断缺陷）、critical（临界缺陷）、normal（普通缺陷）、minor（次要缺陷）、trival（轻微缺陷），标记在用例的@allure.serverity()


- 用例标记：主要包含 smoke(冒烟)、RT（回归）


- 用例名称：标记在用例的@allure.title()


- 用例描述：标记在用例的@allure.description()


- 测试方法中的步骤统一封装到page_object的对应对象操作文件中，在方法中只需要传对应的参数进行调用即可


- 每个测试用例都必须包含断言，主要调用assert_ui.py 文件中的断言方法

##### 4、前后置（conftest.py）

- 文件路径：test_case文件夹下面

使用详解参考链接：https://blog.csdn.net/sinat_30329151/article/details/122901409

##### 5、页面对象文件规范

- 如图四需要针对每个操作添加@allure.step()，用于注释

![img](https://transsioner.feishu.cn/space/api/box/stream/download/asynccode/?code=NDk3MmY0YzQ5NWQzM2Y2NTFmNzllM2JkMGJhNDczMTlfR2owVG9VOG91V0k2Q2QyUFBhT2FpSEp2aEdrQ0ZJRlhfVG9rZW46Ym94Y25IZ1Z0UEE2cHFjM3o3M2loWU5Zb3JmXzE2NTgzODk4NjM6MTY1ODM5MzQ2M19WNA)

​                                                图四

##### 6、日志使用

日志分为四个等级（error、warning、info、debug）

- DEBUG 10 一些较为详细的调试信息
- INFO 20 主体功能信息、做了些什么
- WARNING 30 警告，下次可能要出错了
- ERROR 40 报错

一般常用的是**debug 和info **级别的log日志

### **二、编码规范**

##### 1、声明编码格式

-  一般来说，声明编码格式在脚本中是必需的。
-  如果Python源码文件没有声明编码格式，Python解释器会默认使用ASCII编码。但出现非ASCII编码的字符，Python解释器就会报错。

##### 2、缩进规则

-  Python 采用代码缩进和冒号（ : ）来区分代码块之间的层次。
-  在 Python 中，对于类定义、函数定义、流程控制语句、异常处理语句等，行尾的冒号和下一行的缩进，表示下一个代码块的开始，而缩进的结束则表示此代码块的结束。
-  Python 中实现对代码的缩进，可以使用空格或者 Tab 键实现。但无论是手动敲空格，还是使用 Tab 键，通常情况下都是采用 4 个空格长度作为一个缩进量（默认情况下，一个 Tab 键就表示 4 个空格）。
-  对于 Python 缩进规则，初学者可以这样理解，Python 要求属于同一作用域中的各行代码，它们的缩进量必须一致，但具体缩进量为多少，并不做硬性规定。

 **正确示例代码:**

```
if a==1:

    print("正确")  # 缩进4个空白占位

else:              # 与if对齐

    print("错误")   # 缩进4个空白占位

```

 **错误示例代码:**

```
if a==1:

    print("正确") 

else:              

    print("错误")   

 print("end")   # 改正只需将这行代码前面的空格删除即可

```

>  只需要记住一点：统一使用 4 个空格进行缩进，不要用tab, 也不要tab和空格混用

>  

##### 3、注释部分

 Python中使用 # 进行注释，我们在使用# 的时候，# 号后面要空一格

 在行内注释的时候，中间应该至少加两个空格

```
    # 

    # 注释部分 

```

 `print("你好，世界") # 注释`

 

##### 4、空格

-  ** 使用的一般性原则：**
-  在二元运算符两边各空一格，算术操作符两边的空格可灵活使用，但两侧务必要保持一致
-  不要在逗号、分号、冒号前面加空格，但应该在它们后面加（除非在行尾）
-  函数的参数列表中，逗号之后要有空格
-  函数的参数列表中，默认值等号两边不要添加空格
-  左括号之后，右括号之前不要加添加空格
-  参数列表， 索引或切片的左括号前不应加空格

>  通常情况下，在运算符两侧、函数参数之间以及逗号两侧，都建议使用空格进行分隔。

> 

##### 5、空行使用

 **使用的一般性原则：**

-  编码格式声明、模块导入、常量和全局变量声明、顶级定义和执行代码之间空两行
-  顶级定义之间空两行，方法定义之间空一行
-  在函数或方法内部，可以在必要的地方空一行以增强节奏感，但应避免连续空行

>  使用必要的空行可以增加代码的可读性，通常在顶级定义（如函数或类的定义）之间空两行，而方法定义之间空一行，另外在用于分隔某些功能的位置也可以空一行。

##### 6、模块导入部分

-  导入总应该放在文件顶部，位于模块注释和文档字符串之后，模块全局变量和常量之前。
-  导入应该按照从最通用到最不通用的顺序分组，分组之间空一行：

```
标准库导入

第三方库导入

应用程序指定导入

```

-  每个 import 语句只导入一个模块，尽量避免一次导入多个模块

```
#推荐

import os

import sys



#不推荐

import os,sys

```

##### 7、命名规范

 命名规范这一块的大家应该都比较熟悉了，但是不同的编程语言之间的明明规范也是有所区别的~

 **Python命名建议遵循的一般性原则：**

-  模块尽量使用小写命名，首字母保持小写，尽量不要用下划线
-  类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
- 函数名一律小写，如有多个单词，用下划线隔开
- 私有函数可用一个下划线开头
- 变量名尽量小写, 如有多个单词，用下划线隔开
- 常量采用全大写, 如有多个单词，使用下划线隔开

##### 8、引号用法

 引号使用的一般性原则：

- 自然语言使用双引号
- 机器标识使用单引号
- 正则表达式使用双引号
- 文档字符串 (docstring) 使用三个双引号

##### 9、分号用法

-  Python跟其他几个主流编程语言的分号使用区别很大
-  Python的代码末尾不需要加分号，而Java和C#等都需要添加
-  不要在行尾添加分号，也不要用分号将两条命令放在同一行，例如：

```
# 不推荐

print("Hello") ;  print("World") 

```

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

### Contact - 联系
    自动化测试小组

