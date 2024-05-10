class Mano:
    def __init__(self) -> None:
        #caca en el crebo
        self.cards = []

    def set_cards(self,cartas) -> list:
        self.cards = cartas

    def get_cards(self):
       return self.cards
    
    def get_one_card(self, card_index):
        return self.get_cards()[card_index]
    
    