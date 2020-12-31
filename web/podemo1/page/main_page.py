from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.podemo1.page.add_member_page import AddMemberPage
from web.podemo1.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = '127.0.0.1:9222'
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     self.driver.implicitly_wait(3)

    # 添加成员
    def goto_addmember(self):
        # click addmember

        # self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()

        # 点击联系人，
        self.driver.find_element_by_id('menu_contacts').click()
        sleep(2)
        # 再点击 addmember
        self.driver.find_element_by_css_selector('.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return AddMemberPage(self.driver)
