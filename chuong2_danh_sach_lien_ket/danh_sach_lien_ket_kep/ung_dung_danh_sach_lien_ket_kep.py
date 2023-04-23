from cai_dat_danh_sach_lien_ket_kep import DoublyLinkedList


# ví dụ chạy thử
def main():
    lk_doi = DoublyLinkedList()
    arr = [int(i) for i in input("Nhập các phần tử của mảng: ").split()]
    for i in arr:
        lk_doi.add_node(i)

    lk_doi.output()


if __name__ == "__main__":
    main()
