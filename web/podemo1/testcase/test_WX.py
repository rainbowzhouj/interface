from web.podemo1.page.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = '不要暴露页面细节'
        id = 'page_addttomethod'
        phone = '13452802242'
        addmember = self.main.goto_addmember()
        addmember.addmember(username, id, phone)
        assert username in addmember.get_member(username)
