class SubRonda:
    def __init__(self, num_players) -> None:
        self.cartas_jugadas_subronda = [] # esto se tiene que ver asi [{porky: 2 espada}, {joaquin caca: 10 de oro}, ]
        self.num_players = num_players
        

    def append_to_cartas_jugadas_subronda(self, carta_jugada):
        self.cartas_jugadas_subronda.append(carta_jugada)
        #self.trigger_win_checker()

    def restore_cartas_jugadas_subronda(self):
        self.cartas_jugadas_subronda = []

    def get_numPlayers(self):
        return self.num_players
    
    def get_cartas_jugadas_subronda(self):
        return self.cartas_jugadas_subronda


    def trigger_win_checker(self): #este metodo se puede borrar pqe se triguera cuando se guardaron las mismas cartas que personas pero la verdad es medio xD pq se puede hacer lo mismo pero despeus V: 
        if len(self.cartas_jugadas_subronda) == self.num_players:
            return self.get_winner_sub_round()
    
    def get_winner_sub_round(self):

        win_card = "NOS VAMOS AL PINGO URA"
        win_player = ""
        empate = []


        for par in self.cartas_jugadas_subronda: #par es una tupla que contiene el usuario y la carta que jugó. Con un dictionario era super explosive asi qeu mejro no lo hagamos con dict  
            

            player, card = par
           
            if card > win_card:
                win_card = card
                win_player = player
                empate = []
            elif card.valor == win_card.valor:
                empate.append([(win_card, win_player), (card, player)])
                
        if len(empate) > 0:
            return empate
        else:
            return (win_player, win_card)

