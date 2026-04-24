import socket
import re

HOST = '127.0.0.1'
PORT = 8092

def check_password(pw):
    if (len(pw) >= 6 and len(pw) <= 12 and
        re.search("[a-z]", pw) and
        re.search("[A-Z]", pw) and
        re.search("[0-9]", pw) and
        re.search("[$#@]", pw)):
        return True
    return False

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(1)

print("Server đang chờ kết nối...")

conn, addr = server.accept()
print("Kết nối từ:", addr)

data = conn.recv(1024).decode()
print("Server nhận:", data)

passwords = data.split(",")

valid = []
for pw in passwords:
    pw = pw.strip()
    if check_password(pw):
        valid.append(pw)

result = ",".join(valid)
conn.send(result.encode())

conn.close()
server.close()