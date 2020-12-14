import datetime

import pytest
import yaml
from jsonpath import jsonpath

from tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    # @pytest.mark.parametrize("group,tags",[
    #     ['UI','selenium'],
    #     ['app','appnium'],
    # ])

    def test_tag_add(self):
        # todo ：测试数据要放到数据文件中
        # j=yaml.safe_load(open{"./tag_name.yml"})
        group_name = "UI"
        tag_name = [{"name": "web"}, {"name": "app"}, {"name": "H5"}]

        r = self.tag.add(group_name=group_name, tag_name=tag_name)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    @pytest.mark.parametrize("tag_id, tag_name", [
        ['etXTmQCgAAEes0z0UDZBh_kBwovxScQQ', 'tag1_new_'],
        ['etXTmQCgAAEes0z0UDZBh_kBwovxScQQ', 'tag1——中文'],
        ['etXTmQCgAAEes0z0UDZBh_kBwovxScQQ', 'tag1[中文]'],
    ])
    def test_tag_list(self, tag_id, tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.tag.list()
        r = self.tag.update(
            id=tag_id,
            tag_name=tag_name
        )
        r = self.tag.list()
        # tags = [
        #     tag
        #     for group in r.json()['tag_group'] if group['group_name'] == group_name
        #     for tag in group['tag'] if tag['name'] == tag_name
        # ]

        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name
        # assert tags != []

    def test_tag_list_fail(self):
        pass

    # 如果 40068 ，invalid tagid
    # 0. 添加 tag
    # 1. 删除 tag 有问题
    # 2. 再进行重试（重试次数： n）：手动实现，借助 pytest 钩子（rerun插件）
    #   a. 添加一个接口
    #   b. 对新添加的接口再删除
    #   c. 查询删除是否成功
    def test_delete_group(self):
        self.tag.delete_group(["etXTmQCgAAuw7_ljUIZ7yVkCFahzS6vw"])

    def test_delete_tag(self):
        self.tag.delete_tag(["etXTmQCgAAaIpEBNEoeSjkgd_WM4qLkA"])

    def test_delete_and_detect_group(self):
        r = self.tag.delete_and_detect_group(["et_6ElDwAAyvuY_HFzh0vHvy-yqYhVHA"])
        assert r.json()["errcode"] == 0
