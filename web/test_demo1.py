import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestTestdemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        # remote 复用的方式
        # self.driver=webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("https://cn.bing.com/")
        sleep(3)

    def test_qiyeweixin(self):
        # self.driver.get("https://open.work.weixin.qq.com/api/doc")
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.ID, "menu_contacts").click()
        sleep(3)

    def test_cookie(self):
        '''
        使用cookie登陆
        1、先获取cookies
        2、打开目标页面
        3、添加cookies到目标页面
        get_coookies()可以获取当前打开页面的cookies 信息
        add_cookie()可以把cookie加入到当前页面中去
        :return:
        '''

        # cookies =self.driver.get_cookies()
        cookies = [
            {'domain': '.qq.com', 'expiry': 1672303903, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.419104819.1609231061'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853131096915'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325014198621'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853131096915'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '7XGEjnZAEoEJacHBxTki7NLgH87ZZPh_77gRbpr-Cx214pFWz3eUJXNDoOM6eQBA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'UjRh3yL1L2Dlga9SK16w98-8h5lGp6ONG2MJwSwFdHisjeK3DdCvRQyX802u0341EKhfcYeRW9yrgLWNuOOJq6UpQoUdZceejLpR0G8yNSiDEVRWZYN_VX2MGYWUiQ-3sbzyY88MjZDNDOfz4JMWQuEUHZOKs-sX8QT4WejgWCASkz2bimNInoqL8er1Ouz17mfxZAVnLPDIDKLILsPKPcJvmw1UZfOY8ItTBjEPXWEwzPcO8gUyzryIrFPQ-qDJd2L-fYayQc6rJuBpwv6ZaA'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1640766869, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '5b315b281e5ec6717655a08c1a5b26c7edbf913e31e2ecee80028f07664225ed'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1640767781, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1609231215'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '9864661754'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'OVSY4udnGz'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1609231781'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '02069422'},
            {'domain': '.qq.com', 'expiry': 1609318303, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.583006214.1609231061'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1609262405, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '964u6pr'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '4031836160'},
            {'domain': '.qq.com', 'expiry': 1911736129, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': 'f92881bfdb8355d9'},
            {'domain': '.qq.com', 'expiry': 1911470500, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_5f22b6a456b8d'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1611824131, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]
        # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 可以通过 key，value 的形式把数据保存到shelve中
        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.refresh()
        sleep(3)
        # print(cookies)
