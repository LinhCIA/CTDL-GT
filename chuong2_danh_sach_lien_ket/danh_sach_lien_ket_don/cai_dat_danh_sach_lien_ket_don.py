# Mã nguồn python cách cài đặt danh sách liên kết đơn

class Node:     # lớp Node để đại diện cho mỗi nút trong danh sách

    def __init__(self, data):   # Mỗi nút(Node) là sẽ chứa một giá trị (Data) và một con trỏ (Next)
        self.data = data        # Thuộc tính data để lưu trữ giá trị của nút
        self.next = None        # Thuộc tính next để lưu trữ địa chỉ của nút tiếp theo trong danh sách


class SingleLinkedList:       # Sử dụng lớp LinkedList để quản lí các nút và các thao tác thực hiện trên chúng

    def __init__(self):
        self.head = None        # Thuộc tính head để lưu trữ nút đầu tiên trong danh sách

    def add_node(self, data):   # Phương thức add_node được sử dụng để thêm một nút mới vào trong danh sách liên kết
        new_node = Node(data)   # Tạo một nút mới với giá trị được truyền vào
        if self.head is None:   # Nếu head = None(NULL) thì => danh sách này rỗng
            self.head = new_node    # => đặt nút mới đó là nút đầu tiên
        else:                   # Nếu danh sách không rỗng => đặt nút mới này vào cuối danh sách
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def output(self):   # In ra giá trị
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next
        print()


