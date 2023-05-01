# Mã nguồn python cách cài đặt danh sách liên kết kép

class Node:     # Class Node
    # Hàm tạo node
    def __init__(self, data):
        self.data = data  # Gán dữ liệu
        self.next = None
        self.prev = None
        # next và prev mặc định là None


class DoublyLinkedList:     # Class DoublyLinkedList dùng để quản lý và thao tác trên các Node
    def __init__(self):
        self.head = None   # Thuộc tính head để lưu trữ nút đầu tiên trong danh sách

    # Thêm nút vào đầu danh sách
    def add_node(self, value):
        new_node = Node(value)  # Tạo nút mới
        new_node.next = self.head   # Trỏ next của nút vào nút đầu head
        if self.head is not None:   # Nếu nút head tồn tại, trỏ phần prev vào nút mới
            self.head.prev = new_node
        self.head = new_node    # Gán head cho nút mới

    # Chèn nút vào danh sách
    def insert(self, prev_node, value):
        if prev_node is None:   # Nếu prev_node không tìm thấy thì kết thúc
            print("Dùng push() nếu muốn thêm nút vào đầu danh sách")
            return
        new_node = Node(value)  # Tạo nút mới
        new_node.next = prev_node.next  # Trỏ phần next của nút mới vào nút mà phần next của prev_node trỏ vào
        prev_node.next = new_node   # Trỏ phần next của prev_node vào nút mới
        new_node.prev = prev_node   # Trỏ phần prev của nút mới vào prev_node
        if new_node.next is not None:   # Nếu có nút nằm sau nút mới, cho phần prev của nút nằm sau đó trỏ vào nút mới
            new_node.next.prev = new_node

    # Xóa nút ở đầu danh sách
    def delete_at_start(self):
        if self.head is None:   # Không có nút head
            print("Danh sách rỗng!")
            return
        if self.head.next is None:  # Chỉ có nút head
            self.head = None
            return
        self.head = self.head.next  # Gán head là nút tiếp theo
        self.head.prev = None   # Xóa con trỏ prev của nút head

    # Xóa nút ở cuối danh sách
    def delete_at_end(self):
        if self.head is None:   # Không có nút head
            print("Danh sách rỗng!")
            return
        if self.head.next is None:  # Chỉ có nút head
            self.head = None
            return
        n = self.head
        while n.next is not None:   # Kiểm tra nếu nút tiếp theo tồn tại
            n = n.next
        n.prev.next = None  # Xóa nút

    # In list
    def output(self):
        node = self.head    # Bắt đầu từ nút đầu head
        print("Output: ")
        while node is not None:  # Kiểm tra nếu nút có tồn tại
            print(node.data)    # In dữ liệu nút
            node = node.next    # Trỏ sang nút tiếp theo