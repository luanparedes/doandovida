import Control.LoginScreenViewModel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):
    _image = Image()
    _layout = BoxLayout()
    _button = Button()

    def __init__(self, **kw):
        super().__init__(**kw)

        self.name = 'LoginScreen'
        self._layout.orientation = 'horizontal'
        self._image.source = 'C:\\Users\\luan\\PycharmProjects\\DoandoVida\\Assets\\logo.png'
        self._button.on_press = self._image.remove_widget(self)
        self._layout.add_widget(self._image)
        self._layout.add_widget(self._button)
