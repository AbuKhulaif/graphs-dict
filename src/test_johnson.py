#!/usr/bin/python

import unittest
from johnson import *
from graphs import Graph
from edges import Edge


class TestJohnson(unittest.TestCase):

    def setUp(self):
        self.N = 5           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = [0, 1, 2, 3, 4]
        self.edges = [Edge(0, 2, 6), Edge(0, 3, 3),
        Edge(1, 0, 3), Edge(2, 3, 2), Edge(3, 1, 1),
        Edge(3, 2, 1), Edge(4, 1, 4), Edge(4, 3, 2)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_johnson(self):
        algorithm = Johnson(self.G)
        algorithm.run()
        expected_dist = {
        0: {0: 0, 2: 4, 1: 4, 4: float('inf'), 3: 3},
        1: {0: 3, 2: 7, 1: 0, 4: float('inf'), 3: 6},
        2: {0: 6, 2: 0, 1: 3, 4: float('inf'), 3: 2},
        3: {0: 4, 2: 1, 1: 1, 4: float('inf'), 3: 0},
        4: {0: 6, 2: 3, 1: 3, 4: 0, 3: 2}}
        self.assertEqual(algorithm.dist, expected_dist)

    def test_johnson_faster(self):
        algorithm = JohnsonFaster(self.G)
        algorithm.run()
        expected_dist = {
        0: {0: 0, 2: 4, 1: 4, 4: float('inf'), 3: 3},
        1: {0: 3, 2: 7, 1: 0, 4: float('inf'), 3: 6},
        2: {0: 6, 2: 0, 1: 3, 4: float('inf'), 3: 2},
        3: {0: 4, 2: 1, 1: 1, 4: float('inf'), 3: 0},
        4: {0: 6, 2: 3, 1: 3, 4: 0, 3: 2}}
        self.assertEqual(algorithm.dist, expected_dist)

    def test_negative_cycle(self):
        self.G.add_edge(Edge(1, 3, -2))
        algorithm = Johnson(self.G)
        self.assertRaises(ValueError, algorithm.run)

class TestJohnsonNegativeEdges(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = [0, 1, 2, 3]
        self.edges = [Edge(0, 1, 3), Edge(0, 2, 6),
        Edge(1, 2, 4), Edge(1, 3, 5), Edge(2, 3, 2),
        Edge(3, 0, -5), Edge(3, 1, -3)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_johnson(self):
        algorithm = Johnson(self.G)
        algorithm.run()
        expected_dist = {
        0: {0: 0, 2: 6, 1: 3, 3: 8}, 
        1: {0: 0, 2: 4, 1: 0, 3: 5}, 
        2: {0: -3, 2: 0, 1: -1, 3: 2},
        3: {0: -5, 2: 1, 1: -3, 3: 0}}
        self.assertEqual(algorithm.dist, expected_dist)

    def test_johnson_faster(self):
        algorithm = JohnsonFaster(self.G)
        algorithm.run()
        expected_dist = {
        0: {0: 0, 2: 6, 1: 3, 3: 8}, 
        1: {0: 0, 2: 4, 1: 0, 3: 5}, 
        2: {0: -3, 2: 0, 1: -1, 3: 2},
        3: {0: -5, 2: 1, 1: -3, 3: 0}}
        self.assertEqual(algorithm.dist, expected_dist)

    def test_negative_cycle(self):
        self.G.add_edge(Edge(0, 3, 2))
        algorithm = Johnson(self.G)
        self.assertRaises(ValueError, algorithm.run)

class TestJohnsonWiki(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = [0, 1, 2, 3]
        self.edges = [Edge(0, 1, 3), Edge(0, 3, 6),
        Edge(1, 3, 4), Edge(1, 2, 5), Edge(3, 2, 2),
        Edge(2, 0, -7), Edge(2, 1, -3)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_johnson(self):
        algorithm = Johnson(self.G)
        algorithm.run()
        expected_dist = {
        1: {1: 0, 0: -2, 2: 5, 3: 4}, 
        0: {1: 3, 0: 0, 2: 8, 3: 6}, 
        2: {1: -4, 0: -7, 2: 0, 3: -1}, 
        3: {1: -2, 0: -5, 2: 2, 3: 0}}
        self.assertEqual(algorithm.dist, expected_dist)

    def test_johnson_faster(self):
        algorithm = JohnsonFaster(self.G)
        algorithm.run()
        expected_dist = {
        1: {1: 0, 0: -2, 2: 5, 3: 4}, 
        0: {1: 3, 0: 0, 2: 8, 3: 6}, 
        2: {1: -4, 0: -7, 2: 0, 3: -1}, 
        3: {1: -2, 0: -5, 2: 2, 3: 0}}
        self.assertEqual(algorithm.dist, expected_dist)

if __name__ == '__main__':

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestJohnson)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestJohnsonNegativeEdges)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestJohnsonWiki)
    suite = unittest.TestSuite([suite1, suite2, suite3])
    unittest.TextTestRunner(verbosity=2).run(suite)