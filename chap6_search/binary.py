# Tìm kiếm nhị phân
import timeit

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return None


def main():
    arr = [int(i) for i in input("Nhập các phần tử của mảng: ").split(",")]
    low = int(input("Chỉ số bắt đầu của mảng là: "))
    high = int(input("Chỉ số kết thúc của mảng là: "))
    x = int(input("Giá trị cần tìm kiếm là: "))
    if binary_search(arr, low, high, x) == None:
        print("Không tìm thấy!")
    else:
        print("Vị thứ thứ: ", binary_search(arr, low, high, x))


def time():
    elapsed_time = timeit.timeit(main, number=1)
    print("Thời gian thực thi của hàm là:", elapsed_time, "giây")


if __name__ == "__main__":
    time()