from controller.enums import OS
from kivy.properties import BooleanProperty, NumericProperty, ListProperty
from kivymd.uix.card import MDCard


class AboutCard(MDCard):
    isOpen = BooleanProperty(False)
    card_size = ListProperty([0, 0])
    button_size = ListProperty([0, 0])
    text_button_size = NumericProperty()

    def __init__(self, **kwargs):
        super(AboutCard, self).__init__(**kwargs)

        self.set_card_size()
        self.set_button_size()
        self.set_text_button_size()

    def isOpen_check(self):
        self.isOpen = False

    # Properties setters
    def set_card_size(self):
        if OS.is_android.value or OS.is_ios.value:
            self.card_size = [.6, .2]
        else:
            self.card_size = [.7, .7]

    def set_button_size(self):
        if OS.is_android.value or OS.is_ios.value:
            self.button_size = [.22, .15]
        else:
            self.button_size = [.1, .1]

    def set_text_button_size(self):
        if OS.is_android.value or OS.is_ios.value:
            self.text_button_size = 20
        else:
            self.text_button_size = 16

    # on_<property_name> vai fazer o que precisa quando for alterado
    def on_isOpen(self, obj, value):
        print('NOSSA')