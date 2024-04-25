from Graph.graph import *
from queue import PriorityQueue


class Vertex(Vertex):
    def __init__(self, coordinate):
        super().__init__(coordinate)
        self.d = 0
        self.parent = None

    def __lt__(self, other):
        return self.d < other.d


class SingleSourceShortestPath(WeightedGraph):
    def __init__(self, vertices, edges, weights, source_index):
        super().__init__(vertices, edges, weights, V=Vertex)
        self.source = self.vertices[source_index]
        self.initialize_single_source()

    def initialize_single_source(self):
        for vertex in self.vertices:
            vertex.d = float("inf")
            vertex.parent = None
        self.source.d = 0

    def relax(self, u: int, v: int):
        if (u, v) not in self.weight_dict:
            raise Exception
        if self.vertices[v].d > self.vertices[u].d + self.weight_dict[(u, v)]:
            self.vertices[v].d = self.vertices[u].d + self.weight_dict[(u, v)]
            self.vertices[v].parent = self.vertices[u]

    def bellman_ford(self):
        self.initialize_single_source()
        for _ in range(len(self.vertices) - 1):
            for edge in self.edges:
                self.relax(edge.edge[0], edge.edge[1])
        for edge in self.edges:
            u = edge.edge[0]
            v = edge.edge[1]
            if self.vertices[v].d > self.vertices[u].d + self.weight_dict[(u, v)]:
                return False
        return True

    def dijkstra(self):
        S = []
        Q = PriorityQueue()
        for v in self.vertices:
            Q.put(v)
        self.update_representation()

        while not Q.empty():
            u = Q.get()
            u_index = self.vertices.index(u)
            S.append(u_index)
            for v in self.adjacency_list[u_index]:
                self.relax(u_index, v)

    def print_path(self, i):
        vertex = self.vertices[i]
        result = str(i)
        weight = 0
        current_index = i
        while vertex.parent:
            vertex = vertex.parent
            parent_index = self.vertices.index(vertex)
            result = str(parent_index) + '->' + result
            weight += self.weight_dict[(parent_index, current_index)]
            current_index = parent_index
        print(result + "\t\t\tweight=" + str(weight))
        return result, weight


vertices, edges = gen_random_simple_graph(5, 10)
weights = gen_random_weights(10)
graph = SingleSourceShortestPath(vertices, edges, weights, 0)

graph.bellman_ford()
print(graph.get_adjacency_matrix())
print(graph.get_adjacency_list())
for i in range(5):
    graph.print_path(i)
graph2 = SingleSourceShortestPath(vertices, edges, weights, 0)
print()
graph2.dijkstra()
for i in range(5):
    graph2.print_path(i)
