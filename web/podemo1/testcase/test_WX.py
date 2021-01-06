from web.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = 'zzsuccess'
        id = 'readsuccess10'
        phone = '13452812182'
        addmember = self.main.goto_addmember()
        addmember.addmember(username, id, phone)
        assert username in addmember.get_member(username)
