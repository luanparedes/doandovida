from Presenter.ScreenManagement import ScreenManagement
from kivy.app import App
from kivy.lang import Builder


#Register KV files
Builder.load_file('View\\MainScreen.kv')
Builder.load_file('View\\LoginScreen.kv')
Builder.load_file('View\\CreateUser.kv')


class MainProgram(App):
    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    MainProgram().run()
