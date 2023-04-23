from cai_dat_danh_sach_lien_ket_don import SingleLinkedList


def main():
    lkd = SingleLinkedList()
    arr = [int(i) for i in input("Nhập các phần tử cảu mảng: ").split()]
    for i in arr:
        lkd.add_node(i)
    lkd.output()


if __name__ == "__main__":
    main()
