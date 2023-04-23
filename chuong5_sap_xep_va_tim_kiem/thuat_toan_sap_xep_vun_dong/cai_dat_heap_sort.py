# Mã nguồn python thuật toán sắp xếp vun đống (heap_sort)


# Vun đống cho 1 đỉnh
def vun_dong(arr, n, i):
    # Tìm vị trí lớn nhất giữa nút hiện tại và các nút con
    largest = i             # lưu vị trí lớn nhất ban đầu là i( đỉnh cần vun đống)
    left = 2 * i + 1        # các phần con tử bên trái
    right = 2 * i + 2       # các phần con tử bên phải
    if left < n and arr[left] > arr[largest]:       # nếu tồn tại phần tử con bên trái lớn hơn phần tử cha
        largest = left                              # => gán largest = left
    if right < n and arr[right] > arr[largest]:     # ngược lại, nếu tồn tại phần tử con bên phải lớn hơn p.tử cha
        largest = right                             # => gán largest = right
    # Nếu nút cha hiện tại không lớn nhất, đổi chỗ với nút lớn nhất và tiếp tục vun đống
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]     # đổi chổ phần tử lớn nhất làm cha
        vun_dong(arr, n, largest)       # đệ quy các None phía trước


def sx_heap_sort(arr):      # Hàm sắp xếp vun đống
    n = len(arr)
    # Tạo một heap tối ưu từ mảng đầu vào
    for i in range(n // 2 - 1, -1, -1):
        vun_dong(arr, n, i)
    # Trích xuất lần lượt các phần tử từ heap và sắp xếp lại
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        vun_dong(arr, i, 0)

