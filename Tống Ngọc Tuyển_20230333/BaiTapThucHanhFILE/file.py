while True:
    print("\n===== MENU FILE =====")
    print("1. Đọc n dòng đầu của file")
    print("2. Ghi văn bản vào file và hiển thị")
    print("3. Tạo file demo_file1.txt và in nội dung")
    print("0. Thoát")

    chon = int(input("Chọn: "))

    #  B1
    if chon == 1:
        filename = input("Nhập tên file: ")
        n = int(input("Nhập số dòng cần đọc: "))

        try:
            with open(filename, "r", encoding="utf-8") as f:
                for i in range(n):
                    line = f.readline()
                    if not line:
                        break
                    print(line.strip())
        except:
            print("Không mở được file!")

    # B2 
    elif chon == 2:
        filename = input("Nhập tên file để ghi: ")
        text = input("Nhập đoạn văn: ")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)

        with open(filename, "r", encoding="utf-8") as f:
            print("Nội dung file:")
            print(f.read())

    # B3
    elif chon == 3:
        filename = "demo_file1.txt"

        # tạo file
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Thuc\nhanh\nvoi\nfile\nIO\n")

        print("\n--- a) In trên 1 dòng ---")
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read().replace("\n", " "))

        print("\n--- b) In theo từng dòng ---")
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())

    elif chon == 0:
        print("Thoát chương trình.")
        break

    else:
        print("Chọn sai!")