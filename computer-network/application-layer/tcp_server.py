from socket import *

server_port = 11000
server_socket = socket(AF_INET, SOCK_STREAM) # AF_INET: IPv4, SOCK_STREAM: TCP
server_socket.bind(('', server_port)) # bind: bind the socket to a specific port
server_socket.listen(1) # listen: allow the server to accept incoming connections
print("The server is ready to receive")
connection_socket, client_address = server_socket.accept()

while True:
    sentence = connection_socket.recv(1024).decode()
    print("reviced message: ", sentence)
    modified_message = sentence.upper()
    connection_socket.send(modified_message.encode())
    print("sent message: ", modified_message)

connection_socket.close()