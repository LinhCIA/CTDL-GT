# Mã nguồn python thuật toán sắp xếp trộn (merge sort)


def sx_merge_sort(arr):
    n = len(arr)    # Độ dài của mảng <=> số phần tử trong mảng
    if n > 1:
        mid = n // 2    # Chỉ số giữa => chia đôi mảng ra làm 2 phần
        # Phân chia mảng thành hai phần
        left_half = arr[:mid]       # phần bên trái
        right_half = arr[mid:]      # phần bên phải
        # Gọi đệ quy để sắp xếp từng phần của mảng
        sx_merge_sort(left_half)
        sx_merge_sort(right_half)
        # Trộn các phần đã sắp xếp lại
        # khai báo 2 biến để chạy duyệt các mảng con. i là duyệt mảng bên trái, j là duyệt mảng bên phải
        # còn k là lưu vị trí bắt đầu của mảng chính
        i = j = k = 0
        # Trong khi cả hai mảng vẫn còn phần tử,
        # ta so sánh phần tử đầu tiên của từng mảng và đưa phần tử nhỏ hơn vào vị trí k của mảng đã sắp xếp
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            # Sau khi một mảng hết phần tử,
            # chúng ta đưa các phần tử còn lại của mảng kia vào vị trí k của mảng đã sắp xếp.
            k += 1
        # Trường hợp còn lại
        while i < len(left_half):   # Nếu mảng left chưa hết mà mảng right đã hết
            arr[k] = left_half[i]   # => cho toàn bộ các phần tử vào mảng chính
            i += 1
            k += 1
        while j < len(right_half):  # Nếu mảng right chưa hết mà mảng left đã hết
            arr[k] = right_half[j]  # => Cho toàn bộ các phần tử còn lại vào mảng chính
            j += 1
            k += 1


