"""
    Với file này ta sẽ ứng dụng cách cài đặt hàng đợi Queue 1 (Dùng mảng Array) để test chương trình.

"""

from cai_dat_hang_doi_queue import QueueArr


def main():
    # Gọi class hàng đợi
    q = QueueArr()
    # Nhập các phần tử của mảng từ bàn phím
    arr = [int(i) for i in input("Nhập các phần tử của mảng: ").split()]
    # Lưu các phần tử vào hàng đợi
    for u in arr:
        q.enqueue(u)
    # Thực hiện các yêu cầu của người dùng
    print("Bạn muốn kiểm tra hàng đợi có trống không, vui lòng nhấn phím 1")
    print("Bạn muốn lấy ra và loại bỏ một phần tử vui lòng nhấn phím 2")
    print("Bạn muốn in ra danh sách các phần tử của hàng đợi, vui lòng nhấn phím 3")
    n = abs(int(input("Nhập phím mà bạn muốn: ")))
    if n == 1:
        print(q.is_empty())     # Kiểm tra có còn trống hay không
    elif n == 2:
        print(q.dequeue())      # Lấy ra phần tử đầu tiên trong hàng đợi
        q.print_queue()         # In ra kết quả còn lại của hàng đợi sau khi đã lấy ra phần tử đó
    elif n == 3:
        q.print_queue()         # In ra tất các các phần tử của hàng đợi
    else:
        print("Tôi chưa hiểu yêu cầu của bạn. Vui lòng nhập lại!")


if __name__ == "__main__":
    main()