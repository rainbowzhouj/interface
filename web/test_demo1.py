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
        # print(cookies)
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'sTzLZS2Bx8bXIlrmAE_S9sYBhrpEH2vtENtW4MWXTvMZrRPImWLH567n7hhU_PIrPxx4Ycj70f8Ph-OMCn5BvVkYqR4GUyGuXrH3qT7skZmV3YWuoFjH1AWzcz88shKJKXkYFfnlA1TB_m8bgT0xDUR67-OUjci6X9PlNWLzKSWEspuX73ZCJKUtyICEphTkIiTgtxLKsJfk68nePBtwxBssXh_DFgAiGlQX7AwjCY6hSF2sGQgjZqN3gKDLsqOsSQKC4pVv1qH4yVz-vTzkFw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': True, 'value': '1609231781'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1640767781, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1609231215'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1609262405, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': True, 'value': '964u6pr'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853131096915'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853131096915'},
            {'domain': '.qq.com', 'expiry': 1609341642, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.583006214.1609231061'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1609262405, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '964u6pr'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '7XGEjnZAEoEJacHBxTki7FCQ4u9RmUFxVSeFJ2gtpRCY3Ph4v1MsOwho_QCkzJNi'},
            {'domain': '.qq.com', 'expiry': 1911470500, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': True, 'value': '0_5f22b6a456b8d'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1640766869, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1672327242, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.419104819.1609231061'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
             'value': '5b315b281e5ec6717655a08c1a5b26c7edbf913e31e2ecee80028f07664225ed'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a355959'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
             'value': 'OVSY4udnGz'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1911736129, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': True, 'value': 'f92881bfdb8355d9'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '9864661754'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True,
             'value': '02069422'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1611849418, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325014198621'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': True, 'value': '4031836160'}]
        '''
        shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        可以通过 key，value 的形式把数据保存到shelve中
        '''
        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()
        #
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.refresh()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            'C:\\Users\\10043\\Documents\\WXWork\\1688853721922796\\Cache\\File\\2020-04\\rtod3.xlsx')
        filename = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert "rtod3.xlsx" == filename
        sleep(3)

    def test_shelve(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'sTzLZS2Bx8bXIlrmAE_S9sYBhrpEH2vtENtW4MWXTvMZrRPImWLH567n7hhU_PIrPxx4Ycj70f8Ph-OMCn5BvVkYqR4GUyGuXrH3qT7skZmV3YWuoFjH1AWzcz88shKJKXkYFfnlA1TB_m8bgT0xDUR67-OUjci6X9PlNWLzKSWEspuX73ZCJKUtyICEphTkIiTgtxLKsJfk68nePBtwxBssXh_DFgAiGlQX7AwjCY6hSF2sGQgjZqN3gKDLsqOsSQKC4pVv1qH4yVz-vTzkFw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': True, 'value': '1609231781'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1640767781, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1609231215'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1609262405, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': True, 'value': '964u6pr'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853131096915'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853131096915'},
            {'domain': '.qq.com', 'expiry': 1609341642, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.583006214.1609231061'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1609262405, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '964u6pr'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '7XGEjnZAEoEJacHBxTki7FCQ4u9RmUFxVSeFJ2gtpRCY3Ph4v1MsOwho_QCkzJNi'},
            {'domain': '.qq.com', 'expiry': 1911470500, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': True, 'value': '0_5f22b6a456b8d'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1640766869, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1672327242, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.419104819.1609231061'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
             'value': '5b315b281e5ec6717655a08c1a5b26c7edbf913e31e2ecee80028f07664225ed'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a355959'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
             'value': 'OVSY4udnGz'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1911736129, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': True, 'value': 'f92881bfdb8355d9'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '9864661754'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True,
             'value': '02069422'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1611849418, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325014198621'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': True, 'value': '4031836160'}]
        '''
        shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        可以通过 key，value 的形式把数据保存到shelve中
        '''
        db = shelve.open('cookies')
        # 存储后如何更新？？
        db['cookie'] = cookies
        db.close()
        # db = shelve.open('cookies')
        # cookies=db['cookie']
        # db.close()
        self.driver.get('"https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        # self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_item_title:nth-child(2)').click()
        # self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # self.driver.find_element(By.CSS_SELECTOR,'.ww_fileImporter_fileContainer_uploadInputMask').send_keys('C:\\Users\\10043\\Documents\\WXWork\\1688853721922796\\Cache\\File\\2020-04\\rtod3.xlsx')
        # filename=self.driver.find_element(By.CSS_SELECTOR,'.ww_fileImporter_fileContainer_fileNames').text
        # assert "rtod3.xlsx"==filename
        #sleep(3)
