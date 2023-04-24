from cai_dat_danh_sach_lien_ket_kep import DoublyLinkedList


# ví dụ chạy thử
def main():
    lk_doi = DoublyLinkedList()
    arr = [int(i) for i in input("Nhập các phần tử của mảng: ").split()]
    for i in arr:
        lk_doi.add_node(i)
    # Nếu bạn muốn test các phương thức của tôi thì chỉ cần tắt dấu # là ok vip
    # lk_doi.delete_at_start()
    # lk_doi.delete_at_end()
    # lk_doi.insert()
    # Ở đây tôi chỉ cần nhập và in ra danh sách liên kết đôi là được
    lk_doi.output()


if __name__ == "__main__":
    main()
