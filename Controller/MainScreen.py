from kivymd.uix.menu import MDDropdownMenu
from Controller.CustomMap import CustomMap
from kivy.uix.screenmanager import Screen

from Controller.InfoBloodCenterCard import InfoBloodCenterCard


class MainScreen(Screen):
    menu_items = []
    menu = ''

    def __init__(self):
        super(MainScreen, self).__init__()
        self.name = 'mainpage'

        self.map = CustomMap()
        self.ids.mapbox.add_widget(self.map)

    def open_menu(self, button):
        self.menu_items.clear()
        self.fill_menu()

        self.menu = MDDropdownMenu(
            items=self.menu_items,
            width_mult=4,
        )
        self.menu.caller = button
        self.menu.open()

    def fill_menu(self):
        self.menu_items.append({
            "text": "Configurações",
            "viewclass": "OneLineListItem",
            "on_release": self.open_settings
        })
        self.menu_items.append({
            "text": "Sair",
            "viewclass": "OneLineListItem",
            "on_release": self.exit_login
        })

    def open_settings(self):
        self.parent.screen = 'settings'
        self.menu.dismiss()

    def exit_login(self):
        self.parent.screen = 'login'
        self.menu.dismiss()
