from DirectedEdge import DirectedEdge

class Digraph:
    def __init__(self, V):
        self._V = V
        self._E = 0
        self._adj = [[] for _ in range(V)]
        self._indegree = [0] * V

    def add_edge(self, v, w, weight=0.0):
        edge = DirectedEdge(v, w, weight)
        self._adj[v].append(edge)
        self._indegree[w] += 1
        self._E += 1

    def V(self):
        return self._V

    def adj(self, v):
        return self._adj[v]

    def outdegree(self, v):
        return len(self._adj[v])

    def indegree(self, v):
        return self._indegree[v]