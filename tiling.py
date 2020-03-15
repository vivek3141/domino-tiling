class Graph:
    def __init__(self, V):
        self.graph = [[] for i in range(V)]
        self.v = V

    def add_edge(self, a1, a2):
        self.graph[a1].append(a2)
        self.graph[a2].append(a1)

    def remove_edge(self, a1, a2):
        self.graph[a1].remove(a2)
        self.graph[a2].remove(a1)

    def count_edges(self):
        s = 0
        for i in range(self.V):
            s += len(self.graph[i])
        return s // 2

    def count_faces(self):
        # F = 2 + E - V
        return 2 + self.count_edges() - self.V


def T(m, n):
    g = Graph(m * n)
    
