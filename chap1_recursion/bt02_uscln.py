# Mã nguồn bài toán tìm ước số lớn nhất của 2 số nguyên được viết bởi Thanh Linh Lê

# Mã nguồn được viết bằng ngôn ngữ Python
# Mã nguồn được viết bằng phương pháp Euclid
def tim_uscln(a:int, b:int):
    if (b == 0):
        return a
    else:
        return tim_uscln(b, a % b)
def main():
    a = int(input("Nhập số nguyên thứ nhất: "))
    b = int(input("Nhập số nguyên thứ hai: "))
    print("Ước số chung lớn nhất của", a, "và", b, "là:", tim_uscln(a, b))
if __name__=="__main__":
    main()