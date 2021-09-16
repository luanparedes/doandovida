from Presenter.CustomMap import CustomMap
from kivy.uix.screenmanager import Screen


class MapScreen(Screen):
    def __init__(self):
        super(MapScreen, self).__init__()

        self.name = 'map'

        CustomMap()
