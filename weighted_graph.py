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
    fully_connected_graph = WeightedGraph()

    # Define the number of vertices
    num_vertices = 5

    # Add edges with unique weights to create a fully connected graph
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            weight = random.randint(1, 10)  # Random weight between 1 and 10
            fully_connected_graph.add_edge(i, j, weight=weight)

    # Visualize the fully connected graph
    fully_connected_graph.visualize()
    print(fully_connected_graph.rud_dijkstra(0))