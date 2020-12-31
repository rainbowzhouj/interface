from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo.register_page import RegisterPage


class LoginPage:
    '''
    复用浏览器
    如何在相同的页面使用一个浏览器？
    使用self.driver
    再使用init初始化
    '''

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 扫码
    def scan(self):
        pass

    # 进入到注册页面
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return RegisterPage(self.driver)
