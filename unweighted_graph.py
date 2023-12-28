import networkx as nx
import matplotlib.pyplot as plt
import sys
from collections import deque #supports a double ended queue (can pop from beginning and end in O(1))
from functools import reduce
class UnweightedGraph:
    '''
    Undirected Graph
    - Represented as dictionary 
    - Mapping from node to list of nodes (destinations)
    '''
    def __init__(self):
        self.graph = {}
        self.num_vertices = 0
    def get_num_vertices(self):
        return self.num_vertices

    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]
            self.num_vertices += 1

        if node2 in self.graph:
            self.graph[node2].append(node1)
        else:
            self.graph[node2] = [node1]
            self.num_vertices += 1

    def display(self):
        # Display the graph
        for node in self.graph:
            print(node, ":", " -> ".join(map(str, self.graph[node])))

    def visualize(self):
        G = nx.Graph(self.graph)
        pos = nx.spring_layout(G)  # Choose layout algo (spring_layout, circular_layout, etc.)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        plt.show()

    def shortest_path(self,s,t):
        dist = [sys.maxsize]*self.num_vertices
        pred = [None]*self.num_vertices
        q = deque()
        dist[s] = 0
        q.appendleft(s)
        while q:
            x = q.popleft()
            #get all neighbors of x
            x_neighbors = self.graph[x]

            for y in x_neighbors:
                if dist[y] == sys.maxsize:
                    dist[y] = dist[x] + 1
                    pred[y] = x
                    if y == t:
                        return dist[y]
                    q.appendleft(y)
        return -1

if __name__ == "__main__":

    graph = UnweightedGraph()

    # Add interconnected components
    for i in range(5):
        for j in range(i * 5, (i + 1) * 5 - 1):
            graph.add_edge(j, j + 1)

    # Add loops
    for i in range(5):
        graph.add_edge(i * 5, (i + 1) * 5 - 1)

    # Add some additional edges
    graph.add_edge(2, 12)
    graph.add_edge(8, 17)
    graph.add_edge(17,2)
    graph.add_edge(12,24)
    graph.add_edge(0,22)


    # Visualize the complex graph
    print(graph.shortest_path(22,0))
    print(graph.shortest_path(24,2))
    print(graph.shortest_path(5,17))
    graph.visualize()

    
    