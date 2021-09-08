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
