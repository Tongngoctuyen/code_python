import sys, socket, threading
from PyQt6.QtWidgets import QApplication, QMainWindow
from server_ui import Ui_MainWindow

HOST = '0.0.0.0'
PORT = 8094

clients = []

class ServerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSend.clicked.connect(self.send_msg)
        threading.Thread(target=self.start_server, daemon=True).start()
    def log(self, msg):
        self.ui.chatBox.append(msg)
    def broadcast(self, msg, sender=None):
        for c in clients:
            if c != sender:
                try:
                    c.send(msg.encode())
                except:
                    pass
    def handle_client(self, conn, addr):
        self.log(f"Kết nối: {addr}")
        while True:
            try:
                msg = conn.recv(1024).decode()
                if not msg:
                    break
                self.log(f"{addr}: {msg}")
                self.broadcast(msg, conn)
            except:
                break
        clients.remove(conn)
        conn.close()
        self.log(f"Ngắt: {addr}")

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()
        self.log("Server đang chạy...")

        while True:
            conn, addr = server.accept()
            clients.append(conn)
            threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True).start()

    def send_msg(self):
        msg = self.ui.input.text()
        if msg:
            self.log("SERVER: " + msg)
            self.broadcast("SERVER: " + msg)
            self.ui.input.clear()

app = QApplication(sys.argv)
window = ServerApp()
window.show()
sys.exit(app.exec())