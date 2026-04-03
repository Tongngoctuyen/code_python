def tong2so(a, b):
    return a + b

def tongNhieuSo(*args):
    return sum(args)

def laSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def laSoHoanHao(n):
    if n <= 0:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n


while True:
    print("\n===== MENU =====")
    print("1. Tổng 2 số")
    print("2. Tổng nhiều số")
    print("3. Kiểm tra số nguyên tố")
    print("4. Tìm số nguyên tố [a, b]")
    print("5. Kiểm tra số hoàn hảo")
    print("6. Tìm số hoàn hảo [a, b]")
    print("0. Thoát")

    chon = int(input("Chọn: "))

    if chon == 1:
        a, b = map(int, input("Nhập a b: ").split())
        print("KQ =", tong2so(a, b))

    elif chon == 2:
        ds = list(map(int, input("Nhập các số: ").split()))
        print("KQ =", tongNhieuSo(*ds))

    elif chon == 3:
        n = int(input("Nhập n: "))
        print("Nguyên tố" if laSoNguyenTo(n) else "Không phải")

    elif chon == 4:
        a, b = map(int, input("Nhập a b: ").split())
        print([i for i in range(a, b+1) if laSoNguyenTo(i)])

    elif chon == 5:
        n = int(input("Nhập n: "))
        print("Hoàn hảo" if laSoHoanHao(n) else "Không phải")

    elif chon == 6:
        a, b = map(int, input("Nhập a b: ").split())
        print([i for i in range(a, b+1) if laSoHoanHao(i)])

    elif chon == 0:
        break

    else:
        print("Chọn sai!")