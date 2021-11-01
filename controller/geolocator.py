from geopy.geocoders import Nominatim


class GeoLocator:
    def __init__(self):
        super(GeoLocator, self).__init__()

        self.locator = Nominatim(user_agent="doandovida")
        self.location = self.locator.geocode('')

    def set_location(self, value):
        self.location = self.locator.geocode(value)
