# Mã nguồn python thuật toán sắp xếp (quick sort)


def vach_ngan(arr, l, r, p):   # Kí hiệu: p = pivot = trục chia; l = left = p.tử bên trái; r = right = p.tử bên phải
    while l <= r:
        # Tìm phần tử bên trái cần được đổi chỗ
        while arr[l] < p:
            l += 1
        # Tìm phần tử bên phải cần được đổi chỗ
        while arr[r] > p:
            r -= 1
        # Nếu phần tử bên trái lớn hơn phần tử bên phải, đổi chỗ 2 phần tử đó
        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    # Trả về chỉ số của phần tử chốt
    return l


def sx_quick_sort(arr, l, r):
    if l < r:
        # Chọn phần tử chốt p là phần tử giữa
        p = arr[(l + r) // 2]
        # Phân hoạch mảng và lấy chỉ số phần tử chốt
        index = vach_ngan(arr, l, r, p)
        # Gọi đệ quy sắp xếp phần mảng trước phần tử chốt
        sx_quick_sort(arr, l, index - 1)
        # Gọi đệ quy sắp xếp phần mảng sau phần tử chốt
        sx_quick_sort(arr, index, r)

