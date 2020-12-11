import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'ww342c4e9a1d9b5638'
        corpsecret = 'uVivGfU7O7MrbumFBC77kfkqEw_FS8j5qADaAYOFBGs'
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params": {'corpid': corpid, 'corpsecret': corpsecret}
        }
        r = self.send(data)
        token = r.json()['access_token']
        return token

    # def get_token(self):
    #     ID = 'ww342c4e9a1d9b5638'
    #     SECRET = 'uVivGfU7O7MrbumFBC77kfkqEw_FS8j5qADaAYOFBGs'
    #     r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
    #                      params={"corpid": ID,
    #                              "corpsecret": SECRET})
    #     print(json.dumps(r.json(), indent=2))
    #     token = r.json()['access_token']
    #     return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=2))
        return r