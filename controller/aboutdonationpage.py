from controller.basescreen import BaseScreen
from kivymd.uix.bottomnavigation import MDBottomNavigationItem


class AboutDonationPage(MDBottomNavigationItem, BaseScreen):
    def __init__(self, **kwargs):
        super(AboutDonationPage, self).__init__(**kwargs)

