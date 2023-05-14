# Mã nguồn Python cho biết số lần xuất hiện của từng số trong dãy số
def dem():
    arrs = [int(i) for i in input("Input: \n").split()]
    frequency = {}      # Tạo một danh sách (kiểu từ điển) đếm tần số xuất hiện của từng số trong dãy 
    for num in arrs:    # Dùng vòng lặp for duyệt qua các phần tử trong mảng đầu vào
        if num in frequency:        # Nếu phần tử num đó có trong danh sách
            frequency[num] += 1     # Tần số xuất hiện của phần tử đó trong danh sách tăng lên 1
        else:                       # Nếu không
            frequency[num] = 1      # Tần số xuất hiện của phần tử đó trong danh sách mặc định là 1

    print("Output:")
    for num, freq in frequency.items():
        print(f"({num},{freq})", end=" ")


dem()