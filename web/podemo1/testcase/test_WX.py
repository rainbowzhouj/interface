from web.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = '封装成功'
        id = 'read'
        phone = '13452802292'
        addmember = self.main.goto_addmember()
        addmember.addmember(username, id, phone)
        assert username in addmember.get_member(username)
