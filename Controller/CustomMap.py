from Controller.GeoLocator import GeoLocator
from Controller.CustomGPS import CustomGPS
from Controller.CustomMapMarker import CustomMapMarker
from Controller.Enums import OS
from Controller.Enums import MarkMap
from Model.BloodCenter import BloodCenter
from Model.Donator import Donator
from Model.Dao import Dao
from kivy_garden.mapview import MapView, MapMarker
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock


class CustomMap(MapView):
    # Properties
    size_button = StringProperty('/Assets/maximizar.png')

    def __init__(self):
        super(CustomMap, self).__init__()

        # Variables
        self.donator_model = Donator()
        self.center_model = BloodCenter()

        self.centers_list = []
        self.markers = []
        self.is_full_map = False
        self.is_init = True

        self.geo_locator = GeoLocator()
        self.dao = Dao()

        if OS.is_android.value or OS.is_ios.value:
            self.gps = CustomGPS()
            Clock.schedule_interval(self.on_update_gps, 0)
        else:
            self.map_initial_position()

        self.addressing_bloodcenters()
        self.set_user_to_markers()
        self.set_markers_to_map()

        self.zoom = 15
        self.map_source = "osm"
        self.size_hint = (1, .37)

    def map_initial_position(self):
        self.geo_locator.set_location(self.dao.get_address())
        self.lat = self.geo_locator.location.latitude
        self.lon = self.geo_locator.location.longitude

    def set_user_to_markers(self):
        if OS.is_android.value or OS.is_ios.value:
            self.add_marker(self.gps.mark)
        else:
            self.markers.append(MapMarker(lat=self.lat, lon=self.lon, source=MarkMap.house.value))

    def addressing_bloodcenters(self):
        address = ''

        self.get_bloodcenters_from_db()

        for center in self.centers_list:
            address = address + f'{center.adress.street}, '
            address = address + f'{center.adress.number}, '
            address = address + f'{center.adress.city}, '
            address = address + f'{center.adress.state}'

            self.set_bloodcenters_markers(address, center)
            address = ''

    def get_bloodcenters_from_db(self):
        self.centers_list = self.dao.get_all_bloodcenters()

    def set_bloodcenters_markers(self, address, model):
        self.geo_locator.set_location(address)
        self.markers.append(CustomMapMarker(model, lat=self.geo_locator.location.latitude,
                                            lon=self.geo_locator.location.longitude, source=MarkMap.hospital.value,))

    def set_markers_to_map(self):
        for marker in self.markers:
            self.add_marker(marker)

    # Actions
    def on_update_gps(self, value):
        self.lat = self.gps.lat
        self.lon = self.gps.lon

        if self.is_init and self.lat != 0:
            self.center_on(self.lat, self.lon)
            self.is_init = False

        self.do_update(self)

    def maximize_map(self):
        if self.is_full_map:
            self.size_hint_y = .37
            self.is_full_map = False
            self.ids.size_map.icon = 'fullscreen'
            self.ids.size_map.tooltip_text = 'Maximizar'
        else:
            self.size_hint_y = 1
            self.is_full_map = True
            self.ids.size_map.icon = 'close-circle'
            self.ids.size_map.tooltip_text = 'Minimizar mapa'
