from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    driver: WebDriver
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 第一次初始化
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=options)
        else:
            # 进行页面跳转操作
            self.driver = driver

        if self.base_url != "":
            self.driver.get(self.base_url)
            self.driver.implicitly_wait(3)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)
