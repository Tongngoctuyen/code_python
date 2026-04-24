import socket

HOST = '127.0.0.1'
PORT = 8092

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

pw_input = input("Nhập mật khẩu (cách nhau bằng dấu phẩy): ")

client.send(pw_input.encode())

result = client.recv(1024).decode()

print("Mật khẩu hợp lệ:", result)

client.close()