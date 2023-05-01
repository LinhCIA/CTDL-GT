import networkx as nx


class DirectedGraph:
    def __init__(self, nodes=[], edges=[]):
        # Khởi tạo đồ thị
        self.G = nx.DiGraph()

        # Thêm các đỉnh và các cạnh vào đồ thị
        self.G.add_nodes_from(nodes)
        self.G.add_edges_from(edges)

    def add_node(self, node):
        # Thêm một đỉnh vào đồ thị
        self.G.add_node(node)

    def add_edge(self, start, end):
        # Thêm một cạnh vào đồ thị
        self.G.add_edge(start, end)

    def get_nodes(self):
        # Lấy danh sách các đỉnh trong đồ thị
        return list(self.G.nodes())

    def get_edges(self):
        # Lấy danh sách các cạnh trong đồ thị
        return list(self.G.edges())

    def get_degree(self, node):
        # Lấy bậc của một đỉnh trong đồ thị
        return self.G.degree(node)

    def get_adjacency_matrix(self):
        # Lấy ma trận kề của đồ thị
        return nx.adjacency_matrix(self.G).todense()



