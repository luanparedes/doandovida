from Presenter.LoginScreen import LoginScreen
from kivy.app import App
from kivy.lang import Builder


#Register KV files
Builder.load_file('View\\MainScreen.kv')
Builder.load_file('View\\LoginScreen.kv')


class MainProgram(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MainProgram().run()
