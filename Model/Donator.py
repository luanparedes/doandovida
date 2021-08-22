from Model.Adress import Adress

class Donator:
    adress = Adress()

    def __init__(self):
        self.email = ''
        self.password = ''
        self.name = ''
        self.cpf = ''
        self.rg = ''
        self.adress.cep = ''
        self.adress.street = ''
        self.adress.number = 0
        self.adress.complement = ''
        self.adress.neighborhood = ''
        self.adress.city = ''
        self.adress.state = ''
        self.tel = ''
        self.cel = ''
        self.height = 0.00
        self.weight = 00
        self.blood_type = ''
