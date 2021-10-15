from Controller.LoginScreen import LoginScreen
from Controller.MainScreen import MainScreen
from Controller.CreateUser import CreateUser
from Controller.Settings import Settings
from Controller.MapScreen import MapScreen
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
        self.map_screen = MapScreen()

        # Adding screens at screen manager
        self.add_widget(self.login_screen)
        self.add_widget(self.user_screen)
        self.add_widget(self.main_screen)
        self.add_widget(self.settings_screen)
        self.add_widget(self.map_screen)

        self.before_screen = ''

        self.current = 'login'
        self.before_screen = self.current
        self.bind(screen=self.action_swipe_screen)

    # Actions
    def action_swipe_screen(self, obj, value):
        print(self.screen)
        self.current = value
