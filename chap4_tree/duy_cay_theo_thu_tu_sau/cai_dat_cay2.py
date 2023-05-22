# Mã nguồn python cài đặt cây - duyệt cây theo thứ tự sau
# post - order traversal

class Node:         # Lớp Node => đại diện cho một nút của cây

    def __init__(self, value):
        self.value = value              # Thuộc tính value => lưu giá trị của nút
        self.left = None                # Thuộc tính left => lưu các giá trị của cây con bên trái
        self.right = None               # Thuộc tính right => lưu các giá trị của cây con bên phải
    # Nguyên lí hoạt động của thuật toán:
    # đầu tiên là duyệt cây con bên trái -> duyệt cây con bên phải -> duyệt nút gốc


def post_order_traversal(node):             # Sử dụng đệ quy để duyệt cây
    if node:
        post_order_traversal(node.left)         # duyệt cây bên trái
        post_order_traversal(node.right)        # duyệt cây bên phải
        print(node.value)                       # duyệt nút gốc


root = Node(1)          # tạo cây
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# duyệt cây theo thứ tự sau
post_order_traversal(root)


# cây được cài đặt như sau
"""
        1
      /   \ 
    2      3
   / \ 
  4   5 
"""


# Kết quả đầu ra
'''
4
5
2
3
1
'''
