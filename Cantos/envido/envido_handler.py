from .envido import Envido
from .real_envido import RealEnvido
from .falta_envido import FaltaEnvido

class EnvidoHandler():
    def __init__(self, team1, team2):
        self._startingPoints = 1
        self._finalPoints = 2
        self._teams = [team1.players, team2.players]


def envido_handler(team1, team2):
    teams = [team1.players, team2.players]
    posiblesRespuestas = {"si": True, "no": False, "envido": Envido}
    puntos = 1

    SomeoneWin = False
    while not SomeoneWin:
        for teamTurn in teams:
            teamInput = input("si - no - envido - real envido - falta envido")



    
