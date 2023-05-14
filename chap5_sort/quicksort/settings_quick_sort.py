# Mã nguồn Python thuật toán sắp xếp nhanh(quick sort) phiên bản clean code nhất
def sx_quick_sort(arr):
    # Nếu dãy không quá một phần tử => trả về dãy mà không cần làm gì cả
    if len(arr) <= 1:
        return arr
    # Nếu không thì chia ra 3 phần nhỏ hơn, bằng với, và lớn hơn pivot để trị (để sắp xếp)
    pivot = arr[0]                                              # Chọn phần tử pivot (thường là phần tử đầu tiên hoặc cuối cùng, ở đây tôi chọn đầu tiên)
    left = [x for x in arr if x < pivot]                        # Phần bên trái chứa các phần tử nhỏ hơn pivot
    middle = [x for x in arr if x == pivot]                     # Phần ở giữa chứa phần tử bằng với pivot
    right = [x for x in arr if x > pivot]                       # Phần bên phải chứa các phần tử lớn hơn pivot
    return sx_quick_sort(left) + middle + sx_quick_sort(right)  # Vừa Đệ quy sắp xếp hai dãy con lại Vừa Tổng hợp dãy sau khi đã sắp xếp là LpR
