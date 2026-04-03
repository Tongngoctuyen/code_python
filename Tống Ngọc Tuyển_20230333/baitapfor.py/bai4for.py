n = int(input("Nhập n (n < 20): "))

if n >= 20 or n <= 0:
    print("Giá trị n không hợp lệ!")
else:
    print("Các số chia hết cho 5 hoặc 7 là:")
    for i in range(1, n + 1):
        if i % 5 == 0 or i % 7 == 0:
            print(i, end=" ")