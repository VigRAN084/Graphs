import unittest
from unweighted_graph import UnweightedGraph
class TestGraphs(unittest.TestCase):
    def test_linear_graph(self):
        linear_graph = UnweightedGraph()
        linear_graph.add_edge(0, 1)
        linear_graph.add_edge(1, 2)
        linear_graph.add_edge(2, 3)
        linear_graph.add_edge(3, 4)
        self.assertEqual(linear_graph.num_vertices, 5)
        self.assertEqual(linear_graph.shortest_path(0,4), 4)

    def test_binary_tree_graph(self):
        binary_tree_graph = UnweightedGraph()
        binary_tree_graph.add_edge(0, 1)
        binary_tree_graph.add_edge(0, 2)
        binary_tree_graph.add_edge(1, 3)
        binary_tree_graph.add_edge(1, 4)
        binary_tree_graph.add_edge(2, 5)
        binary_tree_graph.add_edge(2, 6)
        self.assertEqual(binary_tree_graph.shortest_path(4,6), 4)

    def test_disconnected_graph(self):
        disconnected_graph = UnweightedGraph()
        disconnected_graph.add_edge(0, 1)
        disconnected_graph.add_edge(2, 3)
        self.assertEqual(disconnected_graph.shortest_path(0,3), -1)

    def test_cycle_graph(self):
        cycle_graph = UnweightedGraph()
        cycle_graph.add_edge(0, 1)
        cycle_graph.add_edge(1, 2)
        cycle_graph.add_edge(2, 3)
        cycle_graph.add_edge(3, 0)
        self.assertEqual(cycle_graph.shortest_path(0,2),2)