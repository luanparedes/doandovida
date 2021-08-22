from Control.ScreenManager import Screens
from kivy.app import App
from View.LoginScreen import LoginScreen
from View.MainScreen import MainScreen


class MainProgram(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MainProgram().run()
