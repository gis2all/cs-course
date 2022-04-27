from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM) # AF_INET: IPv4, SOCK_DGRAM: UDP
server_socket.bind(('', server_port)) # bind: bind the socket to a specific port
print("The server is ready to receive")

while True:
    message, client_address = server_socket.recvfrom(2048) # recvfrom: receive data from a connection-oriented socket
    print("reviced message: ", message.decode())
    modified_message = message.decode().upper()
    server_socket.sendto(modified_message.encode(), client_address) # sendto: send data to a connection-oriented socket
    print("sent message: ", modified_message)