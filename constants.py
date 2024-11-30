import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)

HEADER = 64

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
