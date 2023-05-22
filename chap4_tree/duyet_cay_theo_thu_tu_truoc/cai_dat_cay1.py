# Mã nguồn python cài đặt cây - duyệt cây theo thứ tự trước
# pre - order traversal
class Node:         # Lớp Node đại diện cho một nút trong cây
    def __init__(self, value):
        self.value = value         # Thuộc tính value => lưu giá trị của nút
        self.left = None         # Thuộc tính left => lưu giá trị cây con bên trái
        self.right = None        # Thuộc tính right => lưu giá trị cây con bên phải
    # Nguyên lí hoạt động của thuật toán:
    # nút gốc được duyệt đầu tiên -> duyệt cây con bên trái -> duyệt cây con bên phải


def pre_order_traversal(node):      # Sử dụng đệ quy để duyệt cây
    if node:
        print(node.value)                   # duyệt nút gốc
        pre_order_traversal(node.left)      # duyệt cây bên trái
        pre_order_traversal(node.right)     # duyệt cây bên phải
