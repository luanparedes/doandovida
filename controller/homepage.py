from controller.basescreen import BaseScreen
from kivymd.uix.bottomnavigation import MDBottomNavigationItem


class HomePage(MDBottomNavigationItem, BaseScreen):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)

