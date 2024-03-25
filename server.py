from aiohttp import web
import socketio
import tracemalloc
import random

from Mazo import mazo as NIGGER
from Mazo import carta 

sio = socketio.AsyncServer(cors_allowed_origins="*",)
app = web.Application()
sio.attach(app)
tracemalloc.start()

mazo = NIGGER.Mazo()

@sio.event
def connect(sid, environ):
    print("el socket:  ", sid, 'se conecto')

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
async def repartir_cartas(sid):
    card_list = []
    for i in range(0,3):
        cartaPapu = random.choice(mazo.mazo)
        rnd_card = carta.Carta(cartaPapu)  
        print(rnd_card.__dict__)
        card_list.append(rnd_card.__dict__)
        mazo.mazo.remove(cartaPapu)

        await sio.emit('cartas_jugador', card_list, to=sid)


if __name__ == '__main__':
    web.run_app(app)



