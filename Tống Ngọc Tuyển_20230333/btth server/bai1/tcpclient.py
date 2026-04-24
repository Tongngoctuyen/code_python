import socket

HOST = '127.0.0.1'
PORT = 8090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = "From CLIENT TCP"
client.send(message.encode())

data = client.recv(1024).decode()
print("Client nhận:", data)

client.close()