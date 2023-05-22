from cai_dat_cay1 import Node, pre_order_traversal


# Ví dụ chạy thử
def main():
    root = Node(1)          # tạo cây => nút gốc root = 1
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # duyệt cây theo thứ tự trước
    pre_order_traversal(root)


if __name__ == "__main__":
    main()


# cây được cài đặt như sau
"""
        1
      /   \ 
     2      3
    / \ 
   4   5 
"""

# Kết quả
"""
1
2
4
5
3
"""
