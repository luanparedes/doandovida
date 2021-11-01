from enum import Enum
from os import environ
from platform import system


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
    is_android = True if 'ANDROID_STORAGE' in environ else False
    is_ios = True if system() == 'iOS' else False
    is_windows = True if system() == 'Windows' else False
    is_linux = True if system() == 'Linux' else False
    is_os_x = True if system() == 'OS X' else False


class MarkMap(Enum):
    hospital = 'Assets/bloodcenter.png'
    person = 'Assets/gps_user.png'
    house = 'Assets/house.png'
    emergency = 'Assets/warning.png'
