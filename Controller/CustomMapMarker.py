from Controller.InfoBloodCenterCard import InfoBloodCenterCard
from kivy_garden.mapview import MapMarker


class CustomMapMarker(MapMarker):
    is_open = False

    def __init__(self, model, **kwargs):
        super(CustomMapMarker, self).__init__(**kwargs)

        self.card = InfoBloodCenterCard(model)

    # Events
    def on_press(self):
        if self.is_open:
            self.is_open = False
            self.remove_widget(self.card)
        else:
            self.is_open = True
            self.card.pos = (self.pos[0] + 25, self.pos[1] + 25)
            self.add_widget(self.card)

    # Methods
    def create_model(self):
        pass
