from Model.Adress import Adress

class BloodCenter:
    adress = Adress()

    def __init__(self):
        self.email = ''
        self.password = ''
        self.company = ''
        self.cnpj = ''
        self.adress.cep = ''
        self.adress.street = ''
        self.adress.number = 0
        self.adress.complement = ''
        self.adress.neighborhood = ''
        self.adress.city = ''
        self.adress.state = ''
        self.tel = ''
        self.tel2 = ''
