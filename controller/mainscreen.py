from controller.aboutcard import AboutCard
from controller.custommap import CustomMap
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import StringProperty
from kivy.metrics import dp


class MainScreen(Screen):
    #Properties
    quiz_points = StringProperty()

    menu_items = []
    menu = ''

    def __init__(self):
        super(MainScreen, self).__init__()
        self.name = 'mainpage'

        self.card = AboutCard()
        self.card.bind(isOpen=self.on_change_card)

        self.map = CustomMap()
        self.ids.mapbox.add_widget(self.map)

    # Actions
    def open_menu(self, button):
        self.menu_items.clear()
        self.fill_menu()

        self.menu = MDDropdownMenu(
            items=self.menu_items,
            width_mult=4,
        )
        self.menu.caller = button
        self.menu.open()

    def open_settings(self):
        self.parent.screen = 'settings'
        self.menu.dismiss()

    def exit_login(self):
        self.parent.screen = 'login'
        self.menu.dismiss()

    def on_change_card(self, obj, value):
        if self.card.isOpen:
            self.add_widget(self.card)
        else:
            self.remove_widget(self.card)
        self.menu.dismiss()

    # Privates
    def fill_menu(self):
        self.menu_items.append({
            "text": "Configurações",
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "on_release": self.open_settings
        })
        self.menu_items.append({
            "text": "Sobre...",
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "on_release": self.set_isOpen
        })
        self.menu_items.append({
            "text": "Sair",
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "on_release": self.exit_login
        })

    def set_isOpen(self):
        self.card.isOpen = True
