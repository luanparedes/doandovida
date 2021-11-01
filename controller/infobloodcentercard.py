from kivy.properties import ObjectProperty
from kivymd.uix.card import MDCard


class InfoBloodCenterCard(MDCard):
    title = ObjectProperty()
    email = ObjectProperty()
    street = ObjectProperty()
    number = ObjectProperty()
    complement = ObjectProperty()
    neighborhood = ObjectProperty()
    city = ObjectProperty()
    estate = ObjectProperty()
    tel1 = ObjectProperty()
    tel2 = ObjectProperty()
    next_date = ObjectProperty()

    def __init__(self, model, **kwargs):
        super(InfoBloodCenterCard, self).__init__(**kwargs)

        self.title.text = model.company
        self.email.text = f'E-mail: {model.email}'
        self.street.text = f'Rua: {model.adress.street}'
        self.number.text = f'Nª: {str(model.adress.number)}'
        self.complement.text = f'Complemento: {model.adress.complement}'
        self.neighborhood.text = f'Bairro: {model.adress.neighborhood}'
        self.city.text = f'Cidade: {model.adress.city}'
        self.estate.text = f'Estado: {model.adress.state}'
        self.tel1.text = f'Tel: {model.tel}'
        self.tel2.text = f'Tel2: {model.tel2}'
        self.next_date.text = f'Próxima data: {model.next_date}'
