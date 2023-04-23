# Mã nguồn python thuật toán sắp xếp nổi bọt


def sx_noi_bot(arr):
    n = len(arr)

    # Lặp lại từng phần tử của mảng
    for i in range(n):
        # lặp lại các phần tử còn lại trong mảng
        for j in range(0, n-i-1):
            # nếu phần tử hiện tại lớn hơn phần tử kế tiếp
            if arr[j] > arr[j+1]:
                # hoán đổi chỗ hai phần tử này
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # Trả về mảng sau khi đã sắp xếp
    return arr


def main():     # Hàm chạy thử thuật toán
    arr = [int(i) for i in input("Nhập các phần tử của mảng: ").split()]
    print(sx_noi_bot(arr))
    print("Mảng đã sắp xếp là:")
    for i in range(len(arr)):
        print("%d" % arr[i])


