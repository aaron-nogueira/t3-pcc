class DirectedEdge:
    def __init__(self, v, w, weight):
        self._v = v
        self._w = w
        self._weight = weight

    def from_vertex(self):
        return self._v

    def to_vertex(self):
        return self._w

    def weight(self):
        return self._weight

    def __str__(self):
        return f"{self._v}->{self._w} ({self._weight})"