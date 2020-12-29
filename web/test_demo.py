from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTestdemo():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get('')
        self.driver.find_element(By.LINK_TEXT, '所有分类').click()
        # 断言
        element = self.driver.find_element(By.LINK_TEXT, '所有分类')
        result = element.get_attribute('class')
        assert '' == result
