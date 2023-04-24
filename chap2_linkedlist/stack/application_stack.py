"""
    Với file này ta sẽ ứng dụng cách cài đặt hàng đợi Stack 1 (Dùng mảng Array) để test chương trình.

"""

from cai_dat_ngan_xep_stack import StackArray


def main():
    # Gọi class ngắn xếp
    stack = StackArray()
    # Nhập các phần tử của mảng từ bàn phím
    arr = [int(i) for i in input("Nhập các phần tử của mảng: ").split()]
    # Lưu các phần tử vào ngăn xếp
    for u in arr:
        stack.push(u)
    # Thực hiện các yêu cầu của người dùng
    print("Bạn muốn kiểm tra ngăn xếp có còn trống không, vui lòng nhấn phím 1")
    print("Bạn muốn kiểm tra kích thước của ngăn xếp, vui lòng nhấn phím 2")
    print("Bạn muốn xem giá trị trên cùng của ngăn xếp, vui lòng nhấn phím 3")
    print("Bạn muốn in ra danh sách các phần tử của ngăn xếp, vui lòng nhấn phím 4")
    n = abs(int(input("Nhập phím mà bạn muốn: ")))
    if n == 1:
        print(stack.is_empty())
    elif n == 2:
        print(stack.size())
    elif n == 3:
        print(stack.peek())
    elif n == 4:
        stack.print_stack()
    else:
        print("Tôi không hiểu yêu cầu của bạn. Vui lòng nhập lại")


if __name__ == "__main__":
    main()
