import subprocess
import sys
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

server_path = os.path.join(BASE_DIR, "tcpserver.py")
client_path = os.path.join(BASE_DIR, "tcpclient.py")

print("Đang khởi động server...")

# chạy server nền
server = subprocess.Popen([sys.executable, server_path], creationflags=subprocess.CREATE_NEW_CONSOLE)

time.sleep(2)

print("Đang chạy client...")

# chạy client (có input)
subprocess.run([sys.executable, client_path])

# tắt server
server.terminate()

print("Hoàn thành!")