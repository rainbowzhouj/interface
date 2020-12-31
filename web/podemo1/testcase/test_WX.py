from web.podemo1.page.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = '相同方法的不同返回分别封装'
        id = 'return_addto'
        phone = '13452802262'
        addmember = self.main.goto_addmember()
        addmember.addmember(username, id, phone)
        assert username in addmember.get_member(username)
