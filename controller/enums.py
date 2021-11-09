from enum import Enum
from os import environ
from platform import system


class BloodType(Enum):
    a_positive = 'A+'
    a_negative = 'A-'
    b_positive = 'B+'
    b_negative = 'B-'
    ab_positive = 'AB+'
    ab_negative = 'AB-'
    o_positive = 'O+'
    o_negative = 'O-'


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
    hospital = 'assets/bloodcenter.png'
    person = 'assets/gps_user.png'
    house = 'assets/house.png'
    emergency = 'assets/warning.png'
