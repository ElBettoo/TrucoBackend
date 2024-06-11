from Network.eventHandler import EventHandler
from Game.GameService import GameService
from Game.UserHandler import UserHandler
from Game.SalaWrapper import SalaWrapper
from Network.socketWrapper import WRAPPER as socket
from Network.SocketsConnectedWrapper import SocketsConnectedWrapper

from Game.Implementations.SocketImplementations import SocketImplementation
from Game.Implementations.ConsoleImplementations import ConsoleImplementation


user_handler = UserHandler()
sala_wrapper = SalaWrapper()
sockets_connected_wrapper = SocketsConnectedWrapper()

socket_implementation = SocketImplementation(socket, sala_wrapper, sockets_connected_wrapper)
console_implementation = ConsoleImplementation()

game = GameService(socket, user_handler, sala_wrapper,sockets_connected_wrapper, socket_implementation)
app = EventHandler(game)

app.run_game()


