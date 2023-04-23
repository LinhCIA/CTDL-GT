# Mã nguồn python cách cài đặt danh sách liên kết kép

class Node:     # Sử dụng lớp Node để đại diện cho một nút trong danh sách

    def __init__(self, data):
        self.data = data        # Thuộc tính lưu trữ giá trị của nút
        self.prev = None        # Thuộc tính lưu trữ vị trí nút nằm trước nút hiện tại
        self.next = None        # Thuộc tính lưu trữ vị trí nút nằm sau nút hiện tại


class DoublyLinkedList:     # Sử dụng lớp DoublyLinkedList để quản lý danh sách và thực hiện các thao tác trên đó
    def __init__(self):
        self.head = None    # Thuộc tính head để lưu trữ nút đầu tiên trong danh sách

    def add_node(self, data):       # Phương thức add_node được sử dụng để thêm một mới vào danh sách liên kết
        new_node = Node(data)       # Tạo một nút mới với giá trị được truyền vào
        if self.head is None:       # Nếu head = None(NULL) => danh sách liên kết kép rỗng
            self.head = new_node    # => đặt nút mới này vào đầu danh sách
        else:                       # Nếu danh sách không rỗng => đặt nút mới này vào cuối sanh sách
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def output(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()
