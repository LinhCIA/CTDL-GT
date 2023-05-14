class Node:
    def __init__(self, coeff=0, exp=0, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

def add_polynomials(poly1, poly2):
    head = Node()   # Đặt nút ban đầu là head
    curr = head     # Đặt con trỏ tại head 
    
    while poly1 and poly2:
        if poly1.exp == poly2.exp:
            coeff_sum = poly1.coeff + poly2.coeff
            if coeff_sum != 0:
                curr.next = Node(coeff_sum, poly1.exp)
                curr = curr.next
            poly1 = poly1.next
            poly2 = poly2.next
        elif poly1.exp > poly2.exp:
            curr.next = Node(poly1.coeff, poly1.exp)
            curr = curr.next
            poly1 = poly1.next
        else:
            curr.next = Node(poly2.coeff, poly2.exp)
            curr = curr.next
            poly2 = poly2.next
    
    while poly1:
        curr.next = Node(poly1.coeff, poly1.exp)
        curr = curr.next
        poly1 = poly1.next
        
    while poly2:
        curr.next = Node(poly2.coeff, poly2.exp)
        curr = curr.next
        poly2 = poly2.next
        
    return head.next   # trả về nút đầu thực tế

# hàm tạo danh sách liên kết đa thức từ danh sách các hệ số
def create_polynomial(coefficients):
    head = Node()
    curr = head
    for exp, coeff in enumerate(coefficients):
        if coeff != 0:
            curr.next = Node(coeff, exp)
            curr = curr.next
    return head.next

# Hàm in ra một đa thức
def print_polynomial(poly):
    if not poly:
        print("0")
    else:
        while poly:
            if poly.coeff != 0:
                if poly.exp == 0:
                    print(poly.coeff, end="")
                elif poly.exp == 1:
                    print(poly.coeff, "x", end=" + ")
                else:
                    print(poly.coeff, "x^", poly.exp, end=" + ")
            poly = poly.next
        print("\n")
        
# Chạy chương trình 
poly1 = create_polynomial([2, 0, 3, 0, 1])  # 2 + 3x^2 + x^4
poly2 = create_polynomial([3, 1, 0, 2])     # 3x + 2x^3
print("Đa thức thứ nhất là:")
print_polynomial(poly1)
print("Đa thức thứ hai là:")
print_polynomial(poly2)
result = add_polynomials(poly1, poly2)
print("Tổng hai đa thức là:")
print_polynomial(result)