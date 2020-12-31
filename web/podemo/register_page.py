from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        self.driver.find_element_by_id('corp_name').send_keys('remote')
        self.driver.find_element_by_id('manager_name').send_keys('cookies')
        self.driver.find_element_by_id('register_tel').send_keys('13652825642')
        self.driver.find_element_by_id('submit_btn').click()
        return True

    def register_fail(self):
        self.driver.find_element_by_id('corp_name').send_keys('remote')
        self.driver.find_element_by_id('manager_name').send_keys('cookies')
        self.driver.find_element_by_id('register_tel').send_keys('13652825642')
        self.driver.find_element_by_id('submit_btn').click()
        return True
