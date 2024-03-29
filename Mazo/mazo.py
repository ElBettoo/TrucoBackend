from .carta import Carta
import random

class Mazo: 
    
    def __init__(self) -> None:
        self.mazo = [
            Carta(('011', '1 de espada', 1)),
            Carta(('012', '1 de oro', 7)),
            Carta(('013', '1 de basto', 2)),
            Carta(('014', '1 de copa', 7)),
            Carta(('021', '2 de espada', 6)),
            Carta(('022', '2 de oro', 6)),
            Carta(('023', '2 de basto', 6)),
            Carta(('024', '2 de copa', 6)),
            Carta(('031', '3 de espada', 5)),
            Carta(('032', '3 de oro', 5)),
            Carta(('033', '3 de basto', 5)),
            Carta(('034', '3 de copa', 5)),
            Carta(('041', '4 de espada', 14)),
            Carta(('042', '4 de oro', 14)),
            Carta(('043', '4 de basto', 14)),
            Carta(('044', '4 de copa', 14)),
            Carta(('051', '5 de espada', 13)),
            Carta(('052', '5 de oro', 13)),
            Carta(('053', '5 de basto', 13)),
            Carta(('054', '5 de copa', 13)),
            Carta(('061', '6 de espada', 12)),
            Carta(('062', '6 de oro', 12)),
            Carta(('063', '6 de basto', 12)),
            Carta(('064', '6 de copa', 12)),
            Carta(('071', '7 de espada', 3)),
            Carta(('072', '7 de oro', 4)),
            Carta(('073', '7 de basto', 11)),
            Carta(('074', '7 de copa', 11)),
            Carta(('101', '10 de espada', 10)),
            Carta(('102', '10 de oro', 10)),
            Carta(('103', '10 de basto', 10)),
            Carta(('104', '10 de copa', 10)),
            Carta(('111', '11 de espada', 9)),
            Carta(('112', '11 de oro', 9)),
            Carta(('113', '11 de basto', 9)),
            Carta(('114', '11 de copa', 9)),
            Carta(('121', '12 de espada', 8)),
            Carta(('122', '12 de oro', 8)),
            Carta(('123', '12 de basto', 8)),
            Carta(('124', '12 de copa', 8))
        ]

    def repartir_cartas(self, banned_cards) -> list : 
        i = 0 
        player_cards = []
        
        while i < 3:
            current_card = random.choice(self.mazo).__dict__
            if current_card not in banned_cards:
                player_cards.append(current_card)
                banned_cards.append(current_card) # medio troll esto
                i += 1
        
        return player_cards
