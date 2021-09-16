from Presenter.GeoLocator import GeoLocator
from kivy_garden.mapview import MapView, MapMarker


class CustomMap(MapView):
    def __init__(self):
        super(CustomMap, self).__init__()

        self.geo_locator = GeoLocator()

        print(self.geo_locator.location.latitude)
        self.lat = self.geo_locator.location.latitude
        self.lon = self.geo_locator.location.longitude
        self.zoom = 15
        self.map_source = "osm"
        self.size_hint = (1, .37)

        self.mark = MapMarker(lat=self.geo_locator.location.latitude, lon=self.geo_locator.location.longitude)
        self.mark.source = 'Assets/mapview_location_2.png'

        self.add_marker(self.mark)