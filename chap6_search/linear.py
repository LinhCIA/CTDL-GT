import timeit


def linear_search():    # Tìm kiếm tuần tự phiên bản nâng cấp
    big_arr = [int(i) for i in input("Big array: ").split(",")]  # nhập các phần tử của list lớn từ bàn phím
    small_arr = [int(i) for i in input("Small array: ").split(",")]  # nhập các phần tử của list nhỏ từ bàn phím
    found_indexes = []  # mảng chứa các vị trí cần tìm. ban đầu, mảng này rỗng

    for i in range(len(big_arr)):
        if big_arr[i] in small_arr:
            found_indexes.append(i)
    print("ví trí thứ", found_indexes)


def main():
    linear_search()


def time():
    elapsed_time = timeit.timeit(main, number=1)
    print("Thời gian thực thi của hàm là:", elapsed_time, "giây")


if __name__ == "__main__":
    time()