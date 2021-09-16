from geopy.geocoders import Nominatim


class GeoLocator:
    def __init__(self):
        super(GeoLocator, self).__init__()

        self.locator = Nominatim(user_agent="myGeocoder")
        self.location = self.locator.geocode("Rua Campos Salles, 241, Valinhos, SP")
