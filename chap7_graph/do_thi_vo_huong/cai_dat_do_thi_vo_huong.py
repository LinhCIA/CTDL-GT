class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for i in range(vertices)]

    def add_edge(self, src, dest):
        # Thêm cạnh giữa hai đỉnh src và dest
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def print_graph(self):
        for i in range(self.V):
            print("Danh sách kề của đỉnh {}: ".format(i), end="")
            for j in self.adj_list[i]:
                print(j, end=" ")
            print()


# Sử dụng Graph Class để tạo đồ thị vô hướng
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()
