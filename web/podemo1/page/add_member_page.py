from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo1.page.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def addmember(self, username, id, phone):
        # 添加联系人
        self.find(By.ID, 'username').send_keys(username)
        self.find(By.ID, 'memberAdd_acctid').send_keys(id)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        # sleep(2)
        checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(checkbox)
        return self

    def get_member(self, value):
        # 验证联系人添加成功

        # contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # titlelist = [element.get_attribute("title") for element in contactlist]
        # print(titlelist)
        # titlelist = []
        # for element in contactlist:
        #     titlelist.append(element.get_attribute("title"))
        total_list = []
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute("title") for element in contactlist]
            print(titlelist)
            if value in titlelist:
                total_list = total_list + titlelist
                return total_list
            result: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = result.split('/', 1)

            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()

        return total_list
