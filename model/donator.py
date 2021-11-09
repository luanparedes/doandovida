from model.address import Adress
from model.dao import Dao
from model.time import Time


class Donator:
    def __init__(self):
        self.adress = Adress()
        self.time = Time()

        self.email = None
        self.password = None
        self.name = None
        self.gender = None
        self.cpf = None
        self.rg = None
        self.adress.cep = None
        self.adress.street = None
        self.adress.number = None
        self.adress.complement = None
        self.adress.neighborhood = None
        self.adress.city = None
        self.adress.state = None
        self.tel = None
        self.cel = None
        self.height = None
        self.weight = None
        self.blood_type = None
        self.time.day = None
        self.time.month = None
        self.time.year = None
        self.time.hour = None
        self.time.minute = None
        self.energy = None
        self.quiz_points = None
        self.year_donations = None

    def get_user_info(self):
        info = Dao.take_all_user_info(Dao())

        self.email = info[1]
        self.password = info[2]
        self.name = info[3]
        self.gender = info[4]
        self.cpf = info[5]
        self.rg = info[6]
        self.adress.cep = info[7]
        self.adress.street = info[8]
        self.adress.number = info[9]
        self.adress.complement = info[10]
        self.adress.neighborhood = info[11]
        self.adress.city = info[12]
        self.adress.state = info[13]
        self.tel = info[14]
        self.cel = info[15]
        self.height = info[16]
        self.weight = info[17]
        self.blood_type = info[18]
        self.time.day = info[19]
        self.time.month = info[20]
        self.time.year = info[21]
        self.time.hour = info[22]
        self.time.minute = info[23]
        self.energy = info[24]
        self.quiz_points = info[25]
        self.year_donations = info[26]

