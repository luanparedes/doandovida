from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen


class MainScreen(Screen):
    label_wid = ObjectProperty()
    info = StringProperty()

    def change_text(self):
        self.label_wid.text = 'Opaaa deu certo finalmente!!!'
