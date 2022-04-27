from ast import While
from socket import *

server_name = 'earthserver.esri.com'
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM) # AF_INET: IPv4, SOCK_DGRAM: UDP

while True:
    message = input('Input lowercase sentence: ')
    client_socket.sendto(message.encode(), (server_name, server_port)) # send data from client to server port
    modified_message, server_address = client_socket.recvfrom(2048) # client receive data from server port
    print(modified_message.decode())

client_socket.close()