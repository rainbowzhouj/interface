from address_list.base_api import BaseApi


class Tongxun(BaseApi):
    def __init__(self):
        super().__init__()

    def add(self, userid, name, mobile, department, **kwargs):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {"access_token": self.token},
            "json": {"userid": userid,
                     "name": name,
                     "mobile": mobile,
                     "department": department,
                                   **kwargs
                     }}
        return self.send(data)

    def list(self,userid):
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/user/get',
            "params": {"access_token": self.token,'userid': userid},
            "json": {
                     }
                }
        return self.send(data)

    def update(self, userid, user_name):
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/user/update',
            "params": {"access_token": self.token},
            "json": {"userid": userid,
                     "name": user_name
                     }}
        return self.send(data)

    def delete(self,userid):
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/user/delete',
            "params": {"access_token": self.token,'userid': userid},
            "json": {
                     }
                }
        return self.send(data)
