from controller.geolocator import GeoLocator
from controller.customgps import CustomGPS
from controller.custommapmarker import CustomMapMarker
from controller.enums import OS
from controller.enums import MarkMap
from model.bloodcenter import BloodCenter
from model.donator import Donator
from model.dao import Dao
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivy_garden.mapview import MapView, MapMarker
from kivy.clock import Clock


class CustomMap(MDBottomNavigationItem):
    def __init__(self, **kwargs):
        super(CustomMap, self).__init__(**kwargs)

        self.map = MapView()
        self.add_widget(self.map)

        self.donator_model = Donator()
        self.center_model = BloodCenter()

        self.centers_list = []
        self.markers = []
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

        self.map.zoom = 15
        self.map.map_source = "osm"

    def map_initial_position(self):
        self.geo_locator.set_location(self.dao.get_address())
        self.map.lat = self.geo_locator.location.latitude
        self.map.lon = self.geo_locator.location.longitude

    def set_user_to_markers(self):
        if OS.is_android.value or OS.is_ios.value:
            self.map.add_marker(self.gps.mark)
        else:
            self.markers.append(MapMarker(lat=self.map.lat, lon=self.map.lon, source=MarkMap.house.value))

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
            self.map.add_marker(marker)

    # Actions
    def on_update_gps(self, value):
        self.map.lat = self.gps.lat
        self.map.lon = self.gps.lon

        if self.is_init and self.map.lat != 0:
            self.map.center_on(self.map.lat, self.map.lon)
            self.is_init = False

        self.map.do_update(self)
