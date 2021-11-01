from controller.enums import OS
from model.dao import Dao
from controller.webbrowser import WebBrowser
from kivymd.uix.picker import MDThemePicker
from kivy.properties import BooleanProperty, NumericProperty, ListProperty
from kivy.uix.screenmanager import Screen


class Settings(Screen):
    hyperlink_size = NumericProperty(0)
    button_text_size = NumericProperty(0)
    system_label_size = NumericProperty(0)
    button_size = ListProperty([0, 0])

    def __init__(self):
        super(Settings, self).__init__()
        self.name = 'settings'

        self.menu_items = []

        self.os_differences()

    # Actions
    def to_main_screen(self):
        self.parent.screen = 'mainpage'

    def show_theme_picker(self, obj):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def open_web_saude(self):
        WebBrowser('https://www.gov.br/saude/pt-br/composicao/saes/sangue')

    # Privates
    def fill_menu(self):
        self.theme_colors = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue',
                             'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime',
                             'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']

        for theme in self.theme_colors:
            self.menu_items.append({
                "text": theme,
                "viewclass": "OneLineListItem"
            })

    def os_differences(self):
        if OS.is_android.value or OS.is_ios.value:
            self.hyperlink_size = 24
            self.system_label_size = 30
            self.button_size = [.22, .20]
            self.button_text_size = 25
        else:
            self.hyperlink_size = 14
            self.system_label_size = 18
            self.button_size = [.22, .35]
            self.button_text_size = 15
