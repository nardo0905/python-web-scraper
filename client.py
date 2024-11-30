import socket
import constants
import send_with_header

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(constants.ADDRESS)

def send(message):
    send_with_header.send_message_with_header(message, client)

send("Hello world!")
send("Hello world!")
send("Hello world!")
send(constants.DISCONNECT_MESSAGE)