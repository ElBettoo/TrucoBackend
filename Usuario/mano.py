class Mano:
    def __init__(self) -> None:
        self.cards = []

    def set_cards(self,cartas):
        self.cards = cartas

    def get_cards(self):
       return self.cards