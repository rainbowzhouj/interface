from address_list.base_api import BaseApi


class Tongxun(BaseApi):
    def __init__(self):
        super().__init__()

    def add(self, userid, name, mobilephone, department, **kwargs):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {"access_token": self.token},
            "json": {"userid": userid,
                     "name": name,
                     "mobile": mobilephone,
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

    def delete(self, userid):
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/user/delete',
            "params": {"access_token": self.token, 'userid': userid},
            "json": {
            }
        }
        return self.send(data)

    def find_userid_exist(self, user_id):
        # 查询元素id是否存在，如果不存在，报错
        for user in self.list().json()["userid"]:
            if user_id in user["userid"]:
                return user["userid"]
        print("userid not in user")
        return ""

    def delete_and_detect_user(self, user_ids):
        deleted_user_ids = []
        r = self.delete(user_ids)
        if r.json()["errcode"] == 60111:
            # 如果用户不存在，就添加一个用户，将它的 userid存储进来
            for userid in user_ids:
                if not self.find_userid_exist(userid):
                    user_id_tmp = self.add(userid="hechenxin", name="zy", mobilephone="1345280872", department=1)
                    deleted_user_ids.append(user_id_tmp)
                    # 如果标签存在，就将它存入标签组
                else:
                    deleted_user_ids.append(userid)
        r = self.delete(deleted_user_ids)
        return r
