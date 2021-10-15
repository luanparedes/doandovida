from Controller.GeoLocator import GeoLocator
from Controller.CustomGPS import CustomGPS
from Controller.CustomMapMarker import CustomMapMarker
from Controller.Enums import OS
from Controller.Enums import MarkMap
from Model.BloodCenter import BloodCenter
from Model.Donator import Donator
from Model.Dao import Dao
from kivy_garden.mapview import MapView, MapMarker
from kivy.properties import StringProperty
from platform import system


class CustomMap(MapView):
    donator_model = Donator()
    center_model = BloodCenter()

    centers_list = []
    markers = []
    is_full_map = False

    # Properties
    size_button = StringProperty('/Assets/maximizar.png')

    def __init__(self):
        super(CustomMap, self).__init__()

        self.geo_locator = GeoLocator()
        self.dao = Dao()

        self.get_bloodcenters()
        self.get_all_address()

        self.verify_os()

        self.zoom = 15
        self.map_source = "osm"
        self.size_hint = (1, .37)

    def get_markers_to_map(self):
        self.markers.append(MapMarker(lat=self.lat, lon=self.lon, source=MarkMap.house.value))
        for mark in self.markers:
            self.add_marker(mark)

    def get_my_address(self):
        self.geo_locator.set_location(self.dao.get_address())
        self.lat = self.geo_locator.location.latitude
        self.lon = self.geo_locator.location.longitude

        self.get_markers_to_map()

    def get_geolocator(self, address, model):
        self.geo_locator.set_location(address)
        self.markers.append(CustomMapMarker(model, lat=self.geo_locator.location.latitude,
                                            lon=self.geo_locator.location.longitude,
                                            source=MarkMap.hospital.value,
                                            ))

    def get_bloodcenters(self):
        self.centers_list = self.dao.get_all_bloodcenters()

    def get_all_address(self):
        address = ''

        for center in self.centers_list:
            address = address + f'{center.adress.street}, '
            address = address + f'{center.adress.number}, '
            address = address + f'{center.adress.city}, '
            address = address + f'{center.adress.state}'

            self.get_geolocator(address, center)
            address = ''

    def verify_os(self):
        # Se não for Android ou IOS, mostrará o endereço da casa do usuário
        if system() != OS.android.value and system() != OS.ios.value:
            self.get_my_address()

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

