from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapView, MapSource


class MainScreen(Screen):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.name = 'mainpage'

        self.map = MapView()
        self.map.lat = -21
        self.map.lon = 12
        self.map.zoom = 20
        self.map.map_source = "osm"
        self.map.size_hint = (1, .3)
        self.map.bind(on_touch_up=self.teste)

        self.ids.mapbox.add_widget(self.map)

    def teste(self, touch, obj):
        print('TESTE')
