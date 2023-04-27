# Mã nguồn python thuật toán sắp xếp (quick sort)

def sx_quick_sort(arr, low, high):
    if low < high:
        # Chọn phần tử chốt
        pivot = arr[high]
        # Phân vùng mảng thành 3 phần: nhỏ hơn pivot, bằng pivot, lớn hơn pivot
        i, j, k = low, low, high
        while j <= k:
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            elif arr[j] == pivot:
                j += 1
            else:
                arr[j], arr[k] = arr[k], arr[j]
                k -= 1
        # Đệ quy sắp xếp các phần tử nhỏ hơn và lớn hơn pivot
        sx_quick_sort(arr, low, i - 1)
        sx_quick_sort(arr, k + 1, high)
    return arr



