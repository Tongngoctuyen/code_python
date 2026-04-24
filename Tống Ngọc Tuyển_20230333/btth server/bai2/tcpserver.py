import socket

HOST = '127.0.0.1'
PORT = 8091

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(1)

print("Server đang chờ kết nối...")

conn, addr = server.accept()
print("Kết nối từ:", addr)

data = conn.recv(1024).decode()
print("Server nhận:", data)

try:
    a, b = map(int, data.split())
    tong = a + b
    conn.send(str(tong).encode())
except:
    conn.send("Dữ liệu không hợp lệ".encode())

conn.close()
server.close()