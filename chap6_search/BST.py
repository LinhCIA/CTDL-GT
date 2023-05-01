# Cây nhị phân tìm kiếm
# Thuật toán BST
class Node:                         # Class biểu diễn một nút
    def __init__(self, val):
        self.left = None            # Khởi tạo cây con trái
        self.right = None           # Khởi tạo cây con phải
        self.value = val            # Giá trị của nút


def insert(root, key):              # Thêm một phần tử
    if root is None:
        return Node(key)
    else:
        if root.value == key:
            return root
        elif root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def search(root, key):              # Tìm một phần tử trong cây
    if root is None or root.value == key:
        return root
    if root.value < key:
        return search(root.right, key)
    return search(root.left, key)


arr = [int(i) for i in input("Nhập các phần tử của mảng: ").split(",")]
n = len(arr)
root = None

for i in range(n):
    root = insert(root, arr[i])

key = int(input("Nhập số cần tìm: "))
res = search(root, key)

if res:
    print("Có số", key)
else:
    print("Không có số", key, "trong mảng!")

