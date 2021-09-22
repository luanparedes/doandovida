from plyer import gps
from plyer.utils import environ


class CustomGPS:
    def __init__(self):

        self.isPC = False
        self.gps = gps

        try:
            self.gps.configure(on_location=self.on_location)
            self.isPC = True
        except NotImplementedError:
            print("doesn't work")
        finally:
            print(f'GPS ativo: {self.isPC}')

        if not self.isPC:
            self.gps.start(minTime=1000, minDistance=1)

    def on_location(self, **kwargs):
        lat = str(kwargs['lat'])
        lon = str(kwargs['lon'])

        location = [lat, lon]

        return location
