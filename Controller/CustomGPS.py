from Controller.Enums import MarkMap
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy_garden.mapview import MapMarkerPopup, MapMarker
from plyer import gps


class CustomGPS(Widget):
    lat = NumericProperty(0)
    lon = NumericProperty(0)
    mark = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CustomGPS, self).__init__(**kwargs)

        self.gps = gps
        self.gps.configure(on_location=self.on_gps_location)

        self.mark = MapMarker(source=MarkMap.person.value)

        self.gps.start(minTime=1000, minDistance=0.001)

    def on_gps_location(self, **kwargs):
        self.lat = kwargs['lat']
        self.lon = kwargs['lon']
        self.mark.lat = self.lat
        self.mark.lon = self.lon
