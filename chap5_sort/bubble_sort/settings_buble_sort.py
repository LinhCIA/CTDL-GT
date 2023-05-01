# Mã nguồn python thuật toán sắp xếp nổi bọt
# Sắp xếp nổi bọt là thay đổi vị trí hai phần tử liên tiếp nếu chúng không phải tăng hoặc giảm dần
# Sắp xếp này sẽ lặp đi lặp lại cho đến khi mảng được sắp xếp

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


