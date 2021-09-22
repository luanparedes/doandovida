from Presenter.GeoLocator import GeoLocator
from Presenter.CustomGPS import CustomGPS
from Presenter.Enums import OS
from Presenter.Enums import MarkMap
from kivy_garden.mapview import MapView, MapMarker
from kivy.properties import StringProperty
from platform import system


class CustomMap(MapView):
    coordinates = []
    markers = []
    is_full_map = False

    # Properties
    size_button = StringProperty('/Assets/maximizar.png')

    def __init__(self):
        super(CustomMap, self).__init__()

        self.verify_os()

        self.lat = self.coordinates[0]
        self.lon = self.coordinates[1]

        print(self.coordinates)

        self.zoom = 15
        self.map_source = "osm"
        self.size_hint = (1, .37)

        self.set_markers()
        self.get_markers_to_map()


    def get_markers_to_map(self):
        self.markers.append(MapMarker(lat=self.coordinates[0], lon=self.coordinates[1]))
        for mark in self.markers:
            mark.source = MarkMap.house.value
            self.add_marker(mark)

    def set_markers(self):
        #self.markers.append(MapMarker(lat=self.coordinates[0], lon=self.coordinates[1]))
        pass

    def verify_os(self):
        # Se não for Android, mostrará o endereço da casa do usuário
        if system() != OS.android.value and system() != OS.ios.value:
            self.geo_locator = GeoLocator()
            self.geo_locator.set_location("Rua Campos Salles, 241, Valinhos, SP")
            self.coordinates.append(self.geo_locator.location.latitude)
            self.coordinates.append(self.geo_locator.location.longitude)

        # Sendo Android, mostra o local onde o usuário está pelo GPS
        else:
            self.gps = CustomGPS()
            self.coordinates = self.gps.on_location()

    def maximize_map(self):
        if self.is_full_map:
            self.size_hint_y = .37
            self.is_full_map = False
            self.ids.size_map.icon = 'fullscreen'
            self.ids.size_map.tooltip_text = 'Maximizar'
        else:
            self.size_hint_y = 1
            self.is_full_map = True
            self.size_button = '/Assets/close.png'
            self.ids.size_map.icon = 'close-circle'
            self.ids.size_map.tooltip_text = 'Minimizar mapa'

