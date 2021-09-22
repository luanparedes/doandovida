from enum import Enum


class BloodType(Enum):
    a_positive = 0
    a_negative = 1
    b_positive = 2
    b_negative = 3
    ab_positive = 4
    ab_negative = 5
    o_positive = 6
    o_negative = 7


class Screens(Enum):
    login = 'login'
    newuser = 'newuser'
    main = 'main'
    settings = 'settings'


class OS(Enum):
    android = 'Android'
    ios = 'iOS'
    windows = 'Windows'
    linux = 'Linux'
    os_x = 'OS X'


class MarkMap(Enum):
    hospital = 'Assets/bloodcenter.png'
    person = 'Assets/mapview_location.png'
    house = 'Assets/house.png'
    emergency = 'Assets/warning.png'