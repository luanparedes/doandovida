from kivymd.uix.menu import MDDropdownMenu

from Controller.CustomMap import CustomMap
from kivy.uix.screenmanager import Screen


class MainScreen(Screen):
    menu_items = []
    menu = ''

    def __init__(self):
        super(MainScreen, self).__init__()
        self.name = 'mainpage'

        self.map = CustomMap()
        self.ids.mapbox.add_widget(self.map)

    def open_menu(self, button):
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

    def open_settings(self):
        self.parent.screen = 'settings'
        self.menu.dismiss()

'''
class MainScreen(Screen):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.name = 'mainpage'

        self.locator = Nominatim(user_agent="myGeocoder")
        self.location = self.locator.geocode("Rua Campos Salles, 241, Valinhos, SP")

        self.map = MapView(lat=self.location.latitude, lon=self.location.longitude, zoom=15)
        self.map_source = "osm"
        self.size_hint = (1, .37)

        self.mark = MapMarker(lat=self.location.latitude, lon=self.location.longitude)
        self.mark.source = 'Assets/mapview_location.png'

        self.map.add_marker(self.mark)

        self.ids.mapbox.add_widget(self.map)


    def open_menu(self):
        print('teste')
#'''