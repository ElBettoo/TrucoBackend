from Network.eventHandler import EventHandler
from Game.Game import Game
from Game.UserHandler import UserHandler

user_handler = UserHandler()
game = Game(user_handler)
app = EventHandler(game)

app.run_game()


