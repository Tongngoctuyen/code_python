_list = ["python", "java", "c", "javascript", "go"]

n = int(input("Nhập n: "))

result = []

for word in _list:
    if len(word) > n:
        result.append(word)

print("Kết quả:", result)