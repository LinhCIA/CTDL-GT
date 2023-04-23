"""
Chương trình này sẽ là tổng hợp lại các thuật toán trong chương 5 và lập trình theo yêu cầu của người dùng
"""

# Gọi các hàm sắp xếp từ các thư mục và các file
from chuong5_sap_xep_va_tim_kiem.thuat_toan_sap_xep_chon.cai_dat_sx_chon import sx_chon
from chuong5_sap_xep_va_tim_kiem.thuat_toan_sap_xep_chen.cai_dat_sx_chen import sx_chen
from chuong5_sap_xep_va_tim_kiem.thuat_toan_sap_xep_noi_bot.cai_dat_sx_noi_bot import sx_noi_bot
from chuong5_sap_xep_va_tim_kiem.thuat_toan_sap_xep_nhanh.cai_dat_quick_sort import sx_quick_sort
from chuong5_sap_xep_va_tim_kiem.thuat_toan_sap_xep_vun_dong.cai_dat_heap_sort import sx_heap_sort
from chuong5_sap_xep_va_tim_kiem.thuat_toan_sap_xep_tron.cai_dat_merge_sort import sx_merge_sort
import sys
import timeit


def main():
    # Nhập các phần tử của mảng từ bàn phím
    arr = [int(i) for i in input("Nhập các phần tử của mảng cần sắp xếp: ").split()]
    # In ra mảng trước khi sắp xếp
    print("Mảng trước khi sắp xếp là: ", arr)
    # Đưa ra những lựa chọn để giúp người dùng dễ thao tác
    print("Bạn muốn sắp xếp mảng này theo thuật toán gì?")
    print("*************************MENU**************************")
    print("**  Phím 0 => Thoát                                  **")
    print("**  Phím 1 => Thuật toán sắp xếp chọn.               **")
    print("**  Phím 2 => Thuật toán sắp xếp chèn.               **")
    print("**  Phím 3 => Thuật toán sắp xếp nổi bọt.            **")
    print("**  Phím 4 => Thuật toán sắp xếp nhanh.              **")
    print("**  Phím 5 => Thuật toán sắp xếp vun đống.           **")
    print("**  Phím 6 => Thuật toán sắp xếp trộn.               **")
    print("*******************************************************")
    # Người dùng nhập sự lựa chọn
    key = abs(int(input("Nhấn phím: ")))
    if key == 0:
        return sys.exit(0)
    elif key == 1:
        print("Mảng sau sắp xếp là:", sx_chon(arr))
    elif key == 2:
        print("Mảng sau khi sắp xếp là:", sx_chen(arr))
    elif key == 3:
        print(sx_noi_bot(arr))
        print("Mảng sau khi sắp xếp là:")
        for i in range(len(arr)):
            print("%d" % arr[i])
    elif key == 4:
        n = len(arr)  # độ dài của mảng <=> số phần tử của mảng
        sx_quick_sort(arr, 0, n - 1)  # đệ quy mảng
        print("Mảng sau khi sắp xếp là:")
        for i in range(n):
            print("{:5}".format(arr[i]), end="")
        print()
    elif key == 5:
        sx_heap_sort(arr)
        n = len(arr)
        print("Mảng sau khi đã sắp xếp là:")
        for i in range(len(arr)):
            print("%d" % arr[i])
    elif key == 6:
        sx_merge_sort(arr)
        print("Mảng đã sắp xếp:")
        for i in range(len(arr)):
            print("%d" % arr[i])
    else:
        print("Tôi không hiểu yêu cầu của bạn. Xin vui lòng nhấn lại phím!")


def time():  # Hàm đo thời gian thực của thuật toán
    elapsed_time = timeit.timeit(main, number=1)
    print("Thời gian thực thi của hàm là:", elapsed_time, "giây")


if __name__ == "__main__":
    time()




