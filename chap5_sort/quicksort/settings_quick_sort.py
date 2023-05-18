# Mã nguồn Python thuật toán sắp xếp nhanh(quick sort) phiên bản clean code nhất
def sx_quick_sort(arr):
    # Nếu dãy không quá một phần tử => trả về dãy mà không cần làm gì cả
    if len(arr) <= 1:
        return arr 
    # Nếu không thì chia ra 3 phần nhỏ hơn, bằng với, và lớn hơn pivot để trị (để sắp xếp)
    pivot = arr[len(arr)//2]                      # Chọn phần tử pivot(thường là phần tử đầu tiên, cuối cùng hoặc ở giữa nhưng ở đây tôi chọn pivot là phần tử trung tâm)
    left = [x for x in arr if x < pivot]          # Phần bên trái chứa các phần tử nhỏ hơn pivot
    middle = [x for x in arr if x == pivot]       # Phần ở giữa chứa phần tử bằng với pivot
    right = [x for x in arr if x > pivot]         # Phần bên phải chứa các phần tử lớn hơn pivot
    return sx_quick_sort(left) + middle + sx_quick_sort(right)  # Vừa đệ quy sắp xếp hai dãy con lại vừa tổng hợp hai dãy con lại thành dãy đầu ra hoàn chỉnh có dạng là LpR
