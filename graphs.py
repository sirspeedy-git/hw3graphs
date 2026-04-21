import networkx as nx
import matplotlib.pyplot as plt

class matrixGraph:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def add_undirected_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def add_directed_edge(self, u, v):
        self.matrix[u][v] = 1

    def display(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))

    def bfs():
        

class ajjacencyListGraph:
    def __init__(self, size):
        self.size = size
        self.adjacency_list = {i: [] for i in range(size)}

    def add_undirected_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def add_directed_edge(self, u, v):
        self.adjacency_list[u].append(v)

    def display(self):
        for key, value in self.adjacency_list.items():
            print(f"{key}: {' '.join(map(str, value))}")

if __name__ == "__main__":
    size = 12
    matrix_graph = matrixGraph(size)
    adjacency_list_graph = ajjacencyListGraph(size)

    graph_A_edges = [(0,3),(0,2),(0,7),(0,8),(1,3),(1,2),(1,4),(4,6),(6,9),(6,11),(11,9),(8,10),(3,5),(5,7)]
    
    for u, v in graph_A_edges:
        matrix_graph.add_undirected_edge(u, v)
        adjacency_list_graph.add_undirected_edge(u, v)


    print("Matrix Graph:")
    matrix_graph.display()

    print("\nAdjacency List Graph:")
    adjacency_list_graph.display()

    #networkx used to visualize the graph
    G = nx.Graph()
    G.add_edges_from(graph_A_edges)
    nx.draw_networkx(G)
    plt.show()