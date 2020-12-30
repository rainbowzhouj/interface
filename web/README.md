## web 企业微信实战（一）

### 目标

- selenium简介
- selenium IDE
- 使用remote复用已有的浏览器
- 使用cookie登陆

脚本编写

```
selenium 官网：https://www.selenium.dev/ 7
selenium python 网址： https://seleniumhq.github.io/selenium/docs/api/py/ 6
```

复用浏览器

1. 需要退出当前所有的谷歌浏览器（特别注意）
1. 找到chrome的启动路径
1. 配置环境变量
1. 启动命令
    - windows：chrome --remote-debugging-port=9222
    - mac：Google\ Chrome --remote-debugging-port=9222
1. 访问http://localhost:9222/

作业

    使用cookie 登录企业微信，完成导入联系人，加上断言验证
    
## web 企业微信实战（二）
### 目标

- PageObject 原理及六大原则
- PageObject 封装思想
- 使用分层思想封装框架
- 三种等待方式
- 企业微信实战

六大原则
公共方法代表整个页面
不要将页面细节暴露
不要封装整个页面
不要将断言与方法放在一起
返回结果可以封装到下个页面
同一方法有不同结果分别进行封装