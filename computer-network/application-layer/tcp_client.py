from pydoc import cli
from socket import *

server_name = 'earthserver.esri.com'
server_port = 11000
client_socket = socket(AF_INET, SOCK_STREAM) # AF_INET: IPv4, SOCK_STREAM: TCP
client_socket.connect((server_name, server_port))

while True:
    sentence = input("Input lowercase sentence: ")
    client_socket.send(sentence.encode())
    modified_message = client_socket.recv(1024)
    print("From Server: ", modified_message.decode())

client_socket.close()
