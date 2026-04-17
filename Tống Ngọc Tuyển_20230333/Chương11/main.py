import sys
import pyodbc
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QDate
from gt import Ui_App

# Kết nối SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ACER\\SQLEXPRESS;"
    "DATABASE=QL_NhanSu;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# phần mềm 
class App(QWidget):
    def __init__(self):
        super().__init__()

        # load giao diện
        self.ui = Ui_App()
        self.ui.setupUi(self)

        # setup thêm
        self.ui.cbGT.addItems(["Nam", "Nữ"])
        self.ui.dateNS.setDate(QDate.currentDate())

        # connect sự kiện
        self.ui.btnThem.clicked.connect(self.them)
        self.ui.btnSua.clicked.connect(self.sua)
        self.ui.btnXoa.clicked.connect(self.xoa)
        self.ui.btnTim.clicked.connect(self.tim)
        self.ui.table.cellClicked.connect(self.load_row)

        self.load_data()

    # load dữ liệu lên table
    def load_data(self):
        cursor.execute("SELECT * FROM NhanSu")
        data = cursor.fetchall()

        self.ui.table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                self.ui.table.setItem(i, j, QTableWidgetItem(str(val)))

    # thực hiện thêm
    def them(self):
        try:
            cursor.execute(
                "INSERT INTO NhanSu VALUES (?, ?, ?, ?, ?)",
                (
                    self.ui.txtCCCD.text(),
                    self.ui.txtHoTen.text(),
                    self.ui.dateNS.date().toPyDate(),
                    self.ui.cbGT.currentText(),
                    self.ui.txtDiaChi.text(),
                ),
            )
            conn.commit()
            QMessageBox.information(self, "OK", "Thêm thành công")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", str(e))

    # thực hiện sửa
    def sua(self):
        cursor.execute(
            """
            UPDATE NhanSu
            SET HoTen=?, NgaySinh=?, GioiTinh=?, DiaChi=?
            WHERE CCCD=?
            """,
            (
                self.ui.txtHoTen.text(),
                self.ui.dateNS.date().toPyDate(),
                self.ui.cbGT.currentText(),
                self.ui.txtDiaChi.text(),
                self.ui.txtCCCD.text(),
            ),
        )
        conn.commit()
        QMessageBox.information(self, "OK", "Sửa thành công")
        self.load_data()

    # thực hiện xóa
    def xoa(self):
        cursor.execute(
            "DELETE FROM NhanSu WHERE CCCD=?",
            (self.ui.txtCCCD.text(),)
        )
        conn.commit()
        QMessageBox.information(self, "OK", "Xóa thành công")
        self.load_data()

    # ===== TÌM =====
    def tim(self):
        keyword = "%" + self.ui.txtTim.text() + "%"
        cursor.execute(
            """
            SELECT * FROM NhanSu
            WHERE CCCD LIKE ? OR HoTen LIKE ? OR DiaChi LIKE ?
            """,
            (keyword, keyword, keyword),
        )

        data = cursor.fetchall()
        self.ui.table.setRowCount(len(data))

        for i, row in enumerate(data):
            for j, val in enumerate(row):
                self.ui.table.setItem(i, j, QTableWidgetItem(str(val)))

    # load dữ liệu từ table lên form khi click
    def load_row(self, row, col):
        self.ui.txtCCCD.setText(self.ui.table.item(row, 0).text())
        self.ui.txtHoTen.setText(self.ui.table.item(row, 1).text())
        # chuyển chuỗi ngày tháng về QDate
        date_str = str(self.ui.table.item(row, 2).text())
        self.ui.dateNS.setDate(QDate.fromString(date_str, "yyyy-MM-dd"))
        # set giới tính
        self.ui.cbGT.setCurrentText(self.ui.table.item(row, 3).text())
        self.ui.txtDiaChi.setText(self.ui.table.item(row, 4).text())
# chạy ứng dụng
app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec())