from Graph.graph import *
from DataStructure.queue import Queue

UNDISCOVERED = 'WHITE'
DISCOVERED = 'GREY'
EXPLORED = 'BLACK'


class GraphSearch:
    def __init__(self, graph):
        self.graph = graph

    def search(self):
        raise NotImplementedError


class BFS(GraphSearch):
    def __init__(self, graph, source_index):
        super().__init__(graph)
        for vertex in self.graph.vertices:
            vertex.color = UNDISCOVERED
            vertex.d = float('inf')
            vertex.parent = None
        source = self.graph.vertices[source_index]
        source.color = DISCOVERED
        source.d = 0
        source.parent = None
        Q = Queue()
        Q.enqueue(source)
        adj_list = graph.get_adjacency_list()
        while not Q.is_empty():
            u = Q.dequeue()
            for v in adj_list[u.index]:
                vertex = graph.vertices[v]
                if vertex.color == UNDISCOVERED:
                    vertex.d = u.d + 1
                    vertex.parent = u
                    Q.enqueue(vertex)
            u.color = EXPLORED

    def visualize(self):
        result = {}
        for i in range(len(self.graph.vertices)):
            curr_v = self.graph.vertices[i]
            parents = []
            while curr_v.parent is not None:
                parents.append(curr_v.parent.index)
                curr_v = curr_v.parent
            result[i] = parents

        return result


class DFS(GraphSearch):
    def __init__(self, graph):
        super().__init__(graph)

    def search(self):
        pass


if __name__ == '__main__':
    vertices, edges = gen_random_simple_graph(5, 5)
    graph = Graph(vertices, edges)
    bfs = BFS(graph, 4)
    print(graph.adjacency_list_tostring())
    print(bfs.visualize())