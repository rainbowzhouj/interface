import datetime

import pytest
from jsonpath import jsonpath

from tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

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
