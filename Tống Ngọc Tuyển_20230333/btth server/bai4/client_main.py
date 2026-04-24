import sys, socket, threading
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer
from client_ui import Ui_MainWindow

HOST = '127.0.0.1'
PORT = 8094

class ClientApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

        self.ui.btnSend.clicked.connect(self.send_msg)

        # ⏱️ connect sau khi form hiện
        QTimer.singleShot(500, self.connect_server)

    def connect_server(self):
        try:
            self.client.connect((HOST, PORT))
            self.connected = True
            self.ui.chatBox.append("Đã kết nối server")
            threading.Thread(target=self.receive_msg, daemon=True).start()
        except:
            self.ui.chatBox.append("Không kết nối được server")

    def send_msg(self):
        if not self.connected:
            self.ui.chatBox.append("Chưa kết nối server")
            return

        msg = self.ui.input.text()
        if msg:
            self.client.send(msg.encode())
            self.ui.chatBox.append("Bạn: " + msg)
            self.ui.input.clear()

    def receive_msg(self):
        while True:
            try:
                msg = self.client.recv(1024).decode()
                self.ui.chatBox.append(msg)
            except:
                break

app = QApplication(sys.argv)
window = ClientApp()
window.show()
sys.exit(app.exec())