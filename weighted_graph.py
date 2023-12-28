import networkx as nx
import matplotlib.pyplot as plt
import sys
import random
class WeightedGraph:
    def __init__(self):
        self.graph = {}
        self.num_vertices = 0
    def get_num_vertices(self):
        return self.num_vertices

    def add_edge(self, node1, node2, weight):
        if node1 in self.graph:
            self.graph[node1].append((weight, node2))
        else:
            self.graph[node1] = [(weight, node2)]
            self.num_vertices += 1

        if node2 in self.graph:
            self.graph[node2].append((weight, node1))
        else:
            self.graph[node2] = [(weight, node1)]
            self.num_vertices += 1
    
    def display(self):
        print(self.graph)

    def visualize(self):
        G = nx.Graph()
        for node, edges in self.graph.items():
            for weight, neighbor in edges:
                G.add_edge(node, neighbor, weight=weight)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', font_color='black')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def rud_dijkstra(self, start):
        dist = [sys.maxsize] * self.num_vertices
        pred = [None] * self.num_vertices
        S = []
        dist[start] = 0
        #need to make sure all of the vertices are processed
        while len(S) != self.num_vertices:
            #find vertex in G - S that has the smallest distance
            min_dist_vtx = random.choice(list(self.graph.keys()))
            for vtx in range(len(dist)):
                if vtx not in S and dist[vtx] < dist[min_dist_vtx]:
                    min_dist_vtx = vtx
            
            #go through each vertex adjacent to min_dist_vtx
            for weight, neighbor in self.graph[min_dist_vtx]:
                if dist[min_dist_vtx] + weight < dist[neighbor]:
                    dist[neighbor] = dist[min_dist_vtx] + weight
                    pred[neighbor] = min_dist_vtx

            S.append(min_dist_vtx)
        return pred



if __name__ == "__main__":
    weighted_graph = WeightedGraph()

    # Test Case 1: A simple connected graph with weights
    weighted_graph.add_edge(0, 1, weight=3)
    weighted_graph.add_edge(1, 2, weight=2)
    weighted_graph.add_edge(2, 3, weight=1)
    weighted_graph.add_edge(3, 0, weight=4)
    weighted_graph.add_edge(0, 2, weight=5)

    # Test Case 2: A disconnected graph with multiple components
    weighted_graph.add_edge(4, 5, weight=2)
    weighted_graph.add_edge(6, 7, weight=3)

    # Test Case 3: A graph with loops and dense connections
    weighted_graph.add_edge(8, 9, weight=1)
    weighted_graph.add_edge(9, 10, weight=2)
    weighted_graph.add_edge(10, 11, weight=3)
    weighted_graph.add_edge(11, 8, weight=4)
    weighted_graph.add_edge(12, 13, weight=2)
    weighted_graph.add_edge(13, 14, weight=3)
    weighted_graph.add_edge(14, 12, weight=1)

    # Test Case 4: A graph with a single node
    weighted_graph.add_edge(15, 15, weight=0)

    # Visualize the complex graph
    weighted_graph.visualize()