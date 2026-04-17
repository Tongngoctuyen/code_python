import sys
import os
import pyodbc
from PyQt6 import uic
from PyQt6.QtWidgets import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()


        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "main.ui")
        uic.loadUi(ui_path, self)

        self.conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=ACER\\SQLEXPRESS;"   # sửa nếu cần
            "DATABASE=QL_BanHang;"
            "Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()


        # Mặt hàng
        self.btnAddHang.clicked.connect(self.addHang)
        self.btnEditHang.clicked.connect(self.editHang)
        self.btnDelHang.clicked.connect(self.delHang)
        self.txtSearchHang.textChanged.connect(self.loadHang)
        self.tblHang.cellClicked.connect(self.fillHang)

        # Khách hàng
        self.btnAddKH.clicked.connect(self.addKH)
        self.btnEditKH.clicked.connect(self.editKH)
        self.btnDelKH.clicked.connect(self.delKH)
        self.txtSearchKH.textChanged.connect(self.loadKH)
        self.tblKH.cellClicked.connect(self.fillKH)

        # Hóa đơn
        self.txtSearchHD.textChanged.connect(self.loadHD)
        self.tblHD.cellClicked.connect(self.loadCTHD)

        # Load dữ liệu ban đầu
        self.loadHang()
        self.loadKH()
        self.loadHD()


    def loadHang(self):
        key = self.txtSearchHang.text()
        self.cursor.execute(f"""
        SELECT * FROM MatHang
        WHERE TenHang LIKE N'%{key}%'
        OR NguonGoc LIKE N'%{key}%'
        OR CAST(MaHang AS NVARCHAR) LIKE '%{key}%'
        """)
        data = self.cursor.fetchall()

        self.tblHang.setRowCount(len(data))
        self.tblHang.setColumnCount(4)
        self.tblHang.setHorizontalHeaderLabels(["Mã", "Tên", "Nguồn", "Giá"])

        for i, row in enumerate(data):
            for j, val in enumerate(row):
                self.tblHang.setItem(i, j, QTableWidgetItem(str(val)))

    def fillHang(self):
        row = self.tblHang.currentRow()
        if row < 0: return
        self.txtTenHang.setText(self.tblHang.item(row,1).text())
        self.txtNguon.setText(self.tblHang.item(row,2).text())
        self.txtGia.setText(self.tblHang.item(row,3).text())

    def addHang(self):
        self.cursor.execute(
            "INSERT INTO MatHang(TenHang,NguonGoc,Gia) VALUES(?,?,?)",
            self.txtTenHang.text(),
            self.txtNguon.text(),
            self.txtGia.text()
        )
        self.conn.commit()
        self.loadHang()

    def editHang(self):
        row = self.tblHang.currentRow()
        if row < 0: return
        ma = self.tblHang.item(row,0).text()

        self.cursor.execute(
            "UPDATE MatHang SET TenHang=?,NguonGoc=?,Gia=? WHERE MaHang=?",
            self.txtTenHang.text(),
            self.txtNguon.text(),
            self.txtGia.text(),
            ma
        )
        self.conn.commit()
        self.loadHang()

    def delHang(self):
        row = self.tblHang.currentRow()
        if row < 0: return
        ma = self.tblHang.item(row,0).text()

        self.cursor.execute("DELETE FROM MatHang WHERE MaHang=?", ma)
        self.conn.commit()
        self.loadHang()



    def loadKH(self):
        key = self.txtSearchKH.text()
        self.cursor.execute(f"""
        SELECT * FROM KhachHang
        WHERE TenKH LIKE N'%{key}%'
        OR DiaChi LIKE N'%{key}%'
        OR SDT LIKE '%{key}%'
        """)
        data = self.cursor.fetchall()

        self.tblKH.setRowCount(len(data))
        self.tblKH.setColumnCount(4)
        self.tblKH.setHorizontalHeaderLabels(["Mã", "Tên", "Địa chỉ", "SĐT"])

        for i, row in enumerate(data):
            for j, val in enumerate(row):
                self.tblKH.setItem(i, j, QTableWidgetItem(str(val)))

    def fillKH(self):
        row = self.tblKH.currentRow()
        if row < 0: return
        self.txtTenKH.setText(self.tblKH.item(row,1).text())
        self.txtDiaChi.setText(self.tblKH.item(row,2).text())
        self.txtSDT.setText(self.tblKH.item(row,3).text())

    def addKH(self):
        self.cursor.execute(
            "INSERT INTO KhachHang(TenKH,DiaChi,SDT) VALUES(?,?,?)",
            self.txtTenKH.text(),
            self.txtDiaChi.text(),
            self.txtSDT.text()
        )
        self.conn.commit()
        self.loadKH()

    def editKH(self):
        row = self.tblKH.currentRow()
        if row < 0: return
        ma = self.tblKH.item(row,0).text()

        self.cursor.execute(
            "UPDATE KhachHang SET TenKH=?,DiaChi=?,SDT=? WHERE MaKH=?",
            self.txtTenKH.text(),
            self.txtDiaChi.text(),
            self.txtSDT.text(),
            ma
        )
        self.conn.commit()
        self.loadKH()

    def delKH(self):
        row = self.tblKH.currentRow()
        if row < 0: return
        ma = self.tblKH.item(row,0).text()

        self.cursor.execute("DELETE FROM KhachHang WHERE MaKH=?", ma)
        self.conn.commit()
        self.loadKH()



    def loadHD(self):
        key = self.txtSearchHD.text()
        self.cursor.execute(f"""
        SELECT hd.MaHD, hd.MaKH,
        ISNULL(SUM(ct.SoLuong*ct.DonGia),0)
        FROM HoaDon hd
        LEFT JOIN ChiTietHoaDon ct ON hd.MaHD=ct.MaHD
        WHERE CAST(hd.MaHD AS NVARCHAR) LIKE '%{key}%'
        OR CAST(hd.MaKH AS NVARCHAR) LIKE '%{key}%'
        GROUP BY hd.MaHD, hd.MaKH
        """)
        data = self.cursor.fetchall()

        self.tblHD.setRowCount(len(data))
        self.tblHD.setColumnCount(3)
        self.tblHD.setHorizontalHeaderLabels(["Mã HD", "Mã KH", "Tổng"])

        for i, row in enumerate(data):
            for j, val in enumerate(row):
                self.tblHD.setItem(i, j, QTableWidgetItem(str(val)))

    def loadCTHD(self):
        row = self.tblHD.currentRow()
        if row < 0: return
        ma = self.tblHD.item(row,0).text()

        self.cursor.execute("""
        SELECT TenHang, SoLuong, DonGia, SoLuong*DonGia
        FROM ChiTietHoaDon ct
        JOIN MatHang mh ON ct.MaHang=mh.MaHang
        WHERE MaHD=?
        """, ma)

        data = self.cursor.fetchall()

        self.tblCT.setRowCount(len(data))
        self.tblCT.setColumnCount(4)
        self.tblCT.setHorizontalHeaderLabels(["Tên", "SL", "Giá", "Thành tiền"])

        for i, row in enumerate(data):
            for j, val in enumerate(row):
                self.tblCT.setItem(i, j, QTableWidgetItem(str(val)))


# ===== RUN =====
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec())