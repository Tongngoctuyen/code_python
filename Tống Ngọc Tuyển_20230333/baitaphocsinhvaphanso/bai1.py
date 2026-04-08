# Khai báo lớp học viên
class HocVien:
 # Phương thức khởi tạo đối tượng
 def __init__(self,ht,ns,email,dt,dc,lop):
    self.hoten=ht
    self.ngaysinh=ns
    self.email=email
    self.dienthoai=dt
    self.diachi=dc
    self.lop=lop
# Phương thức hiển thị thông tin học viên
 def showInfo(self):
    print("Họ tên: ", self.hoten)
    print("Ngày sinh: ", self.ngaysinh)
    print("E-Mail: ", self.email)
    print("Điện thoại : ", self.dienthoai)
    print("Địa chỉ: ", self.diachi)
    print("Lớp: ", self.lop)
# Hàm thay đổi thông tin có giá trị mặc định
 def changeInfo(self, ht= "Phan Đình Thi", dc="Hà Nội", lop="IT14.1"):
    self.hoten=ht
    self.diachi=dc
    self.lop=lop
# Chương trình chính
class Main:
    # Tạo đối tượng học viên
    hv1=HocVien("Phan Đình Thi","11/11/2005","20230442@gmail.com","190010011","Hà Tĩnh","IT12.4")
    hv1.showInfo()
    print("------------")
    # Gọi phương thức thay đổi thông tin với giá trị mặc định
    hv1.changeInfo()
    hv1.showInfo()
    print("------------")
    # Gọi phương thức thay đổi thông tin với giá trị mới
    hv1.changeInfo("Vũ Văn Nam","Ninh Bình","IT14.4")
    hv1.showInfo()