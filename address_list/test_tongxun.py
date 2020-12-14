import datetime

import pytest
import requests
from jsonpath import jsonpath

from address_list.tongxun import Tongxun


class TestTongxun:
    def setup_class(self):
        self.user = Tongxun()

    def test_add_user(self):
        userid = "liumengqing"
        #名字为中文时，存在转义问题
        name = "Zz"
        mobile = "13452808721"
        department = "1"
        r = self.user.add(userid=userid, name=name, mobile=mobile, department=department)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0



    @pytest.mark.parametrize("userid, user_name",[
        ['liumengqing', 'Zreturn_'],
        ['liumengqing', 'UIAutomartor'],
        ['liumengqing', 'mitmproxy[中文]'],
    ])
    def test_update_user(self,userid, user_name):
        user_name = user_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.user.update(userid=userid, user_name=user_name)
        r = self.user.list(userid=userid)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0
        a=jsonpath(r.json(), f"$..name")
        print(a)
        assert "".join(a) == user_name



    def test_list_user(self):
        userid = "liumengqing"
        r = self.user.list(userid=userid)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0


    def test_delete_user(self):
        userid="liumengqing"
        r = self.user.delete(user_id=userid)
        assert r.status_code == 200