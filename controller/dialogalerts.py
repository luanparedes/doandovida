from kivy.uix.widget import Widget
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class WrongLoginDialog(MDDialog):
    def __init__(self):
        super(WrongLoginDialog, self).__init__()

        self.dialog = MDDialog(
            text="Login ou senha inválidos\nTente novamente!",
            buttons=[MDFlatButton(text="OK", on_release=self.back_login)],
        )

        self.dialog.open()

    def back_login(self, value):
        self.dialog.dismiss()


class AlreadyHaveEmailDialog(MDDialog):
    def __init__(self):
        super(AlreadyHaveEmailDialog, self).__init__()

        self.dialog = MDDialog(
            text="Login ou senha inválidos\nTente novamente!",
        )


class QuizDialogs(Widget):
    def __init__(self, **kwargs):
        super(QuizDialogs, self).__init__(**kwargs)

    def right_answer(self, answer):
        self.dialog = MDDialog(
            text=f"Resposta certa! 10 Quiz points\n{answer}!",
            buttons=[MDFlatButton(text="OK", on_release=self.close_dialog)],
        )

        self.dialog.open()

    def wrong_answer(self, right_answer):
        self.dialog = MDDialog(
            text=f"Resposta errada! A certa é:\n{right_answer}!",
            buttons=[MDFlatButton(text="OK", on_release=self.close_dialog)],
        )

        self.dialog.open()

    def close_dialog(self, value):
        self.dialog.dismiss()
