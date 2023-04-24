# Mã nguồn python cách cài đặt danh sách liên kết đơn

class Node:     # lớp Node để đại diện cho mỗi nút trong danh sách

    def __init__(self, data):   # Mỗi nút(Node) là sẽ chứa một giá trị (Data) và một con trỏ (Next)
        self.data = data        # Thuộc tính data để lưu trữ giá trị của nút
        self.next = None        # Thuộc tính next để lưu trữ địa chỉ của nút tiếp theo trong danh sách
        # next mặc định là None


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

    # Hàm thêm node vào đầu danh sách
    def add_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Hàm thêm node vào cuối danh sách
    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Hàm thêm node vào giữa 2 node có sẵn trong danh sách
    def add_in_between(self, mid_node, data):
        if mid_node is None:
            print("Node không tồn tại")
            return
        new_node = Node(data)
        new_node.next = mid_node.next
        mid_node.next = new_node

    # Xóa 1 node
    def remove(self, value):
        head_val = self.head
        if head_val is not None:
            if head_val.data == value:
                self.head = head_val.next
                head_val.data = None
                return
        while head_val is not None:
            if head_val.data == value:
                break
            prev = head_val
            head_val = head_val.next
        if head_val is None:
            return
        prev.next = head_val.next
        head_val = None

    def output(self):   # In ra giá trị
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next
        print()


