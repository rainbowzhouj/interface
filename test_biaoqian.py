import json

import requests


def test_tag_list():
    ID = 'ww342c4e9a1d9b5638'
    SECRET = 'uVivGfU7O7MrbumFBC77kfkqEw_FS8j5qADaAYOFBGs'
    r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                     params={"corpid": ID,
                             "corpsecret": SECRET})
    print(json.dumps(r.json(), indent=2))
    token = r.json()['access_token']
    url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list'
    r = requests.post(url=url, params={"access_token": token}, json={'tag_id': []})
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
