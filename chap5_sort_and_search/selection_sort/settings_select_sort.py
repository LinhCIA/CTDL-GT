# Mã nguồn python thuật toán sắp xếp chọn (selection sort)

def sx_chon(arr):

    # Độ dài của mảng
    n = len(arr)

    # Dùng vòng for thứ nhất duyệt qua các phần tử của mảng
    for i in range(n):
        min_index = i       # giả sử đặt phần tử đầu tiên là phần tử nhỏ nhất
        # dùng vòng for thứ 2 duyệt từ phần tử thứ i + 1 -> hết mảng

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:     # So sánh phần tử thứ j với phần tử min_index(trong mảng đó).
                min_index = j               # Nếu j < min_index => gán j sẽ là min_index tiếp theo.

        # Hoán vị i và min_index

        # => chuyển lần lượt phần tử nhỏ nhất từ đoạn chưa được sắp xếp -> lên đầu đoạn đã được sắp xếp.
        arr[i], arr[min_index] = arr[min_index], arr[i]

    # Trả về mảng sau khi đã sắp xếp
    return arr



