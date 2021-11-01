from model.address import Adress
from model.time import Time


class Donator:
    def __init__(self):
        self.adress = Adress()
        self.time = Time()

        self.email = None
        self.password = None
        self.name = None
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
