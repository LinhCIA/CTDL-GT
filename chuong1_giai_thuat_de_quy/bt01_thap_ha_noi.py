# The source code for the Tower of Hanoi problem was written by Thanh Linh Le

# Mã nguồn được viết bằng ngôn ngữ lập trình Python
# Mã nguồn được viết bằng phương pháp đệ quy
# Mã nguồn cho bài toán tháp Hà Nội với trường hợp n tổng quát
def thap_ha_noi(n, source, destination, auxiliary):  #  source: cột bắt đầu; destination: cột đích đến; auxiliary: cột trung gian
    # khi n = 1 đĩa
    if n == 1:
        print("Di chuyển đĩa 1 từ", source, "sang", destination)
        return
    # khi n = nhiều đĩa => sử dụng phương pháp đệ quy
    else:
        thap_ha_noi(n - 1, source, auxiliary, destination)
        print("Di chuyển đĩa", n, "từ", source, "sang", destination)
        thap_ha_noi(n - 1, auxiliary, destination, source)


def main():
    n = abs(int(input("Nhập số đĩa: ")))
    thap_ha_noi(n, 'A', 'C', 'B')  # với A : cột nguồn, B: cột trung gian, C: cột đích
if __name__ == "__main__":
    main()