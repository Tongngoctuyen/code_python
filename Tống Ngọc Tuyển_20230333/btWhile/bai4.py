n = int(input("Nhập n: "))
i = 1
tong = 0
while i < n:
    if i % 2 == 0:
        tong = tong + i
    i = i + 1
print("danh sách số chẵn nhỏ hơn n:")
for j in range(2, n, 2):
    print(j, end=" ")
print("Tổng =", tong)