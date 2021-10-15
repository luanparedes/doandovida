from kivy.uix.screenmanager import Screen


class Settings(Screen):
    def __init__(self):
        super(Settings, self).__init__()
        self.name = 'settings'

    def to_main_screen(self):
        self.parent.screen = 'mainpage'