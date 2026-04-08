import math

class PhanSo:
    def __init__(self, tu, mau=1):
        if mau == 0:
            raise ValueError("Mẫu số không được bằng 0!")
        self.tu = tu
        self.mau = mau
        self.toi_gian()

    def toi_gian(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
        if self.mau < 0:
            self.tu *= -1
            self.mau *= -1

    def cong(self, ps):
        return PhanSo(self.tu * ps.mau + ps.tu * self.mau,
                      self.mau * ps.mau)

    def tru(self, ps):
        return PhanSo(self.tu * ps.mau - ps.tu * self.mau,
                      self.mau * ps.mau)

    def nhan(self, ps):
        return PhanSo(self.tu * ps.tu,
                      self.mau * ps.mau)

    def chia(self, ps):
        if ps.tu == 0:
            raise ValueError("Không thể chia cho phân số có tử = 0!")
        return PhanSo(self.tu * ps.mau,
                      self.mau * ps.tu)

    def __str__(self):
        return f"{self.tu}/{self.mau}"

def nhap_phan_so(ten):
    print(f"\nNhập phân số {ten}:")
    tu = int(input("Tử số: "))
    mau = int(input("Mẫu số: "))
    return PhanSo(tu, mau)


def main():
    ps1 = nhap_phan_so("thứ nhất")
    ps2 = nhap_phan_so("thứ hai")

    while True:
        print("\n===== MENU =====")
        print("1. Cộng")
        print("2. Trừ")
        print("3. Nhân")
        print("4. Chia")
        print("0. Thoát")

        chon = input("Chọn: ")

        try:
            if chon == "1":
                print("Kết quả:", ps1.cong(ps2))
            elif chon == "2":
                print("Kết quả:", ps1.tru(ps2))
            elif chon == "3":
                print("Kết quả:", ps1.nhan(ps2))
            elif chon == "4":
                print("Kết quả:", ps1.chia(ps2))
            elif chon == "0":
                print("Thoát chương trình!")
                break
            else:
                print("Chọn sai!")
        except Exception as e:
            print("Lỗi:", e)


if __name__ == "__main__":
    main()