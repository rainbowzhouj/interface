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