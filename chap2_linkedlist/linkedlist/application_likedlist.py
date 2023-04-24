from cai_dat_danh_sach_lien_ket_don import SingleLinkedList


def main():
    # gọi class
    lk_don = SingleLinkedList()
    # Nhập phần tử của các mảng vào danh sách
    arr = [int(i) for i in input("Nhập các phần tử cảu mảng: ").split()]
    # Thêm các phần tử vào danh sách
    for i in arr:
        lk_don.add_node(i)
    # Nếu bạn muốn test các phương thức của tôi thì chỉ cần tắt dấu # là ok vip
    # lk_don.add_at_start()
    # lk_don.add_at_end()
    # lk_don.add_in_between()
    # lk_don.remove()
    # Ở đây tôi chỉ nhập và in ra danh sách liên kết đơn là được
    lk_don.output()


if __name__ == "__main__":
    main()
