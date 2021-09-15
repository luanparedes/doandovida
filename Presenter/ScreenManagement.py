from Presenter.LoginScreen import LoginScreen
from Presenter.MainScreen import MainScreen
from Presenter.CreateUser import CreateUser
from Presenter.Settings import Settings
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.properties import StringProperty, ObjectProperty


class ScreenManagement(ScreenManager):
    screen = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = FadeTransition()
        self.transition.duration = 0.7

        # Instancing views
        self.login_screen = LoginScreen()
        self.user_screen = CreateUser()
        self.main_screen = MainScreen()
        self.settings_screen = Settings()

        # Adding screens at screen manager
        self.add_widget(self.login_screen)
        self.add_widget(self.user_screen)
        self.add_widget(self.main_screen)
        self.add_widget(self.settings_screen)

        self.before_screen = ''

        self.current = 'login'
        self.before_screen = self.current
        self.bind(screen=self.action_swipe_screen)

    # Actions
    def action_swipe_screen(self, obj, value):
        print(self.screen)
        self.current = value

