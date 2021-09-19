from kivymd.app import MDApp
from Presenter.ScreenManagement import ScreenManagement
from kivy.lang import Builder


#Register KV files
Builder.load_file('View/MainScreen.kv')
Builder.load_file('View/LoginScreen.kv')
Builder.load_file('View/CreateUser.kv')
Builder.load_file('View/Settings.kv')
Builder.load_file('View/MapScreen.kv')


class MainProgram(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.accent_palette = 'Indigo'
        self.theme_cls.theme_style = 'Dark'
        return ScreenManagement()


if __name__ == '__main__':
    MainProgram().run()
