import socket

HOST = '127.0.0.1'
PORT = 8090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server đang chờ kết nối...")

conn, addr = server.accept()
print("Kết nối từ:", addr)

data = conn.recv(1024).decode()
print("Server nhận:", data)

response = "From SERVER TCP"
conn.send(response.encode())

conn.close()
server.close()