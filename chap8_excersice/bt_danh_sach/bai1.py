# Mã nguồn Python để sắp xếp một dãy số tăng dần hoặc giảm giần
def sap_xep_tang_dan(arrs):
    sorted_arrs = sorted(arrs, reverse = False)
    print("Output: ", end="")
    for element in sorted_arrs:
        print(element, end=" ")


def sap_xep_giam_dan(arrs):
    sorted_arrs = sorted(arrs, reverse = True)
    print("Output: ", end="")
    for element in sorted_arrs:
        print(element, end=" ")


def main():
    arrs = [int(i) for i in input("Input: ").split()]
    choice = str(input("Bạn muốn tôi sắp xếp Tăng dần hay Giảm dần?\nLựa chọn của bạn là: "))
    print("Vui lòng đợi trong giây lát!")
    if (choice == "Tăng dần") or (choice == "tăng dần"):
         sap_xep_tang_dan(arrs)
    elif choice == "Giảm dần" or (choice == "giảm dần"):
        sap_xep_giam_dan(arrs)
    else:
        print("Tôi không hiểu ý bạn là gì! Vui lòng nhập lại yêu cầu của bạn!")
    

if __name__ == "__main__":
    main()