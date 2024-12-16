import socket
import constants
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(constants.ADDRESS)
    
def run():
    search_term = input('Въведи продукт: ')

    client.send(search_term.encode(constants.FORMAT))
    
    data = []
    while True:
        packet = client.recv(4096)
        if not packet: break
        data.append(packet)

    items = json.loads(b"".join(data))
        
    for item in items:
        print(item[0])
        print(f"${item[1]['price']}")
        print(item[1]['link'])
        print("-------------------------------")
            
run()