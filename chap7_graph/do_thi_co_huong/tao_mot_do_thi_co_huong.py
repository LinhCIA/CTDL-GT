import networkx as nx

# Khởi tạo đồ thị
G = nx.DiGraph()

# Thêm các đỉnh và các cạnh vào đồ thị
G.add_nodes_from([1, 2, 3, 4])
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)

# In ra số đỉnh và số cạnh của đồ thị
print("Số đỉnh của đồ thị:", G.number_of_nodes())
print("Số cạnh của đồ thị:", G.number_of_edges())

# In ra danh sách các đỉnh và cạnh trong đồ thị
print("Danh sách các đỉnh trong đồ thị:", list(G.nodes()))
print("Danh sách các cạnh trong đồ thị:", list(G.edges()))

# In ra bậc của mỗi đỉnh trong đồ thị
print("Bậc của mỗi đỉnh trong đồ thị:")
for node in G.nodes():
    print(f"Đỉnh {node} có bậc {G.degree(node)}")

# In ra ma trận kề của đồ thị
print("Ma trận kề của đồ thị:")
print(nx.adjacency_matrix(G).todense())
