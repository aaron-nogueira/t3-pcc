class DirectedEulerianCycle:
    def __init__(self, G):
        self._cycle = []
        
      
        for v in range(G.V()):
            if G.outdegree(v) != G.indegree(v):
                return

        
        adj = [iter(G.adj(v)) for v in range(G.V())]
        stack = [0] # Começa do vértice 0
        
        while stack:
            v = stack[-1]
            try:
                edge = next(adj[v])
                stack.append(edge.to_vertex())
            except StopIteration:
                self._cycle.append(stack.pop())

       
        if len(self._cycle) != G._E + 1:
            self._cycle = None

    def cycle(self):
        return self._cycle[::-1] if self._cycle else None

    def has_cycle(self):
        return self._cycle is not None