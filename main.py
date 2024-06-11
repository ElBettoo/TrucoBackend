from Network.eventHandler import EventHandler
from Game.GameService import GameService
from Game.UserHandler import UserHandler
from Game.SalaWrapper import SalaWrapper
from Network.socketWrapper import SocketIOApp
from Network.SocketsConnectedWrapper import SocketsConnectedWrapper

from Game.Implementations.SocketImplementations import SocketImplementation
from Game.Implementations.ConsoleImplementations import ConsoleImplementation




user_handler = UserHandler()
sala_wrapper = SalaWrapper()
sockets_connected_wrapper = SocketsConnectedWrapper()

socket_wrapper = SocketIOApp(sockets_connected_wrapper)
socket_implementation = SocketImplementation(socket_wrapper, sala_wrapper, sockets_connected_wrapper)

console_implementation = ConsoleImplementation() #actualmente esta implementacion tira error, pero muestra el mensaje de "join_room" y sirve como demostracion

game = GameService(socket_implementation)
app = EventHandler(game, socket_wrapper)

app.run_game()


