from kivy.uix.screenmanager import Screen


class CreateUser(Screen):
    def __init__(self):
        super(CreateUser, self).__init__()
        self.name = 'newuser'

        back_button = self.ids.btn_back