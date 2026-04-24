import socket

HOST = '127.0.0.1'
PORT = 8091

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

message = f"{a} {b}"
client.send(message.encode())

result = client.recv(1024).decode()
print("Tổng từ server:", result)

client.close()