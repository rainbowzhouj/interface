import json

import requests


class Tag:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        ID = 'ww342c4e9a1d9b5638'
        SECRET = 'uVivGfU7O7MrbumFBC77kfkqEw_FS8j5qADaAYOFBGs'
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={"corpid": ID,
                                 "corpsecret": SECRET})
        print(json.dumps(r.json(), indent=2))
        token = r.json()['access_token']
        return token

    def add(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={"access_token": self.token},
            json={
                "group_name": 'app',
                "order": 6,
                "tag": [
                    {
                        "name": 'Appnium',
                        "order": 1
                    }
                ]
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def list(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list'
        r = requests.post(url=url, params={"access_token": self.token}, json={'tag_id': []})
        print(json.dumps(r.json(), indent=2))
        return r

    def update(self, id, tag_name):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={"access_token": self.token},
            json={
                'id': id,
                'name': tag_name
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete(self):
        r = requests.post(
            'hhttps://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={"access_token": self.token},
            json={
                "group_name": 'app',
                "order": 6,
                "tag": [
                    {
                        "name": 'Appnium',
                        "order": 1
                    }
                ]
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r
