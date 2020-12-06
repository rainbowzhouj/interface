import json
import datetime
import requests

# todo：与底层具体的实现框架代码耦合严重，无法适应变化
# todo: 代码冗余,需要封装
# todo：无法清晰的描述业务
from jsonpath import jsonpath


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

    '''
    - 避免重复命名
    - 重新命名过长，超过30个字段会报错
    '''
    tag_name = 'test_demo_' + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
        params={"access_token": token},
        json={
            'id': 'etXTmQCgAAEes0z0UDZBh_kBwovxScQQ',
            'name': tag_name
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    r = requests.post(url=url, params={"access_token": token}, json={'tag_id': []})
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    '''
    1.对请求里的内容进行断言
    for group in r.json()['tag_group']:
       if group['group_name']=='python15':
           for tag in group['tag']:
               if tag['name']=="test_demo"
    2.对断言方法进行合并改造
    tags = [
        tag
        for group in r.json()['tag_group'] if group['group_name'] == 'python15'
        for tag in group['tag'] if tag['name'] == tag_name
    ]
    '''

    assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name
