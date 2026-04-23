#import networkx as nx
#import matplotlib.pyplot as plt
from collections import deque

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



def bfs(src, dest, graph):
    visited = [False] * graph.size
    res = []
    explore_queue = deque()

    visited[src] = True
    explore_queue.append(src)

    while explore_queue:
        current_node = explore_queue.popleft()
        res.append(current_node)

        match graph:
            case ajjacencyListGraph():
                for neighbors in graph.adjacency_list[current_node]:
                    if not visited[neighbors]:
                        visited[neighbors] = True
                        explore_queue.append(neighbors)
                
            case matrixGraph():
                for i in range(graph.size):
                    if graph.matrix[current_node][i] == 1 and not visited[i]:
                        visited[i] = True
                        explore_queue.append(i)
    return res


if __name__ == "__main__":
    size = 12
    matrix_graph_A = matrixGraph(size)
    adjacency_list_graph_A = ajjacencyListGraph(size)
    graph_A_edges = [(0,3),(0,2),(0,7),(0,8),(1,3),(1,2),(1,4),(4,6),(6,9),(6,11),(11,9),(8,10),(3,5),(5,7)]
    
    for u, v in graph_A_edges:
        matrix_graph_A.add_undirected_edge(u, v)
        adjacency_list_graph_A.add_undirected_edge(u, v)

    print("Matrix Graph A:")
    matrix_graph_A.display()

    print("\nAdjacency List Graph A:")
    adjacency_list_graph_A.display()

    print("bfs traversal A mat:")
    print(bfs(0,11,matrix_graph_A))
    print("bfs traversal A adj:")
    print(bfs(0,11,adjacency_list_graph_A))

'''
    size = 15
    matrix_graph_B = matrixGraph(size)
    adjacency_list_graph_B = ajjacencyListGraph(size)
    graph_B_edges = [(0,1),(0,2),(1,3),(1,6),(2,3),(3,4),(4,5),(4,10)]
    
    for u, v in graph_B_edges:
        matrix_graph_B.add_directed_edge(u, v)
        adjacency_list_graph_B.add_directed_edge(u, v)

    print("Matrix Graph B:")
    matrix_graph_B.display()

    print("\nAdjacency List Graph B:")
    adjacency_list_graph_B.display()
'''
    # #networkx used to visualize the graph
    # G = nx.Graph()
    # G.add_edges_from(graph_A_edges)
    # nx.draw_networkx(G)
    # plt.show()