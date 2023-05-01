# Mã nguồn python cho thuật toán sắp xếp chèn


def sx_chen(arr):

    n = len(arr)    # Độ dài của mảng <=> số phần tử ( n phần tử )

    # Dùng một vòng for lặp từ i = 1 -> n - 1
    for i in range(1, n):
        k = arr[i]      # lưu giá trị tại phần tử thứ [i] bằng biến k
        j = i - 1       # đặt một biến j = i - 1
        # dùng vòng lặp while gồm 2 điều kiện: j >= 0 và k < arr[j]
        while j >= 0 and k < arr[j]:
            arr[j + 1] = arr[j]     # di chuyển vị trí thứ j lên 1
            j -= 1                  # giảm j xuống -1
        arr[j + 1] = k              # gán k cho phần tử tiếp theo của mảng

    return arr





