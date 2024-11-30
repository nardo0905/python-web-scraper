import constants

def send_message_with_header(message, sender):
    message_to_send = message.encode(constants.FORMAT)
    
    message_length = len(message_to_send)
    
    send_length = str(message_length).encode(constants.FORMAT)
    send_length += b' ' * (constants.HEADER - len(send_length))
    
    sender.send(send_length)
    sender.send(message_to_send)