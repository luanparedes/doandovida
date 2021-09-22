from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class WrongLoginDialog(MDDialog):
    def __init__(self):
        super(WrongLoginDialog, self).__init__()

        self.text = "Login ou senha incorretos!\nTente novamente..."
        self.size_hint_x = .3
        self.radius = [30, 30, 30, 30]

        self.buttons = [MDFlatButton(text="OK", pos_hint=.01, on_release=self.back_login)]

        self.add_widget(self.buttons[0])
        self.open()

    def back_login(self, value):
        self.dismiss()
