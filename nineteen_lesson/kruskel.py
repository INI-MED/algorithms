class Edge:

    def __init__(self):
        self.nodes = {}
        self.level = {}

    def make_set(self, point) -> None:
        self.nodes[point] = point
        self.level[point] = 0
        
    def find(self, point):
        if self.nodes[point] != point:
            self.nodes[point] = self.find(self.nodes[point])
        return self.nodes[point]

    def merge(self, point1, point2) -> None:
        r1 = self.find(point1)
        r2 = self.find(point2)
        if r1 != r2:
            if self.level[r1] > self.level[r2]:
                self.nodes[r2] = r1
            else:
                self.nodes[r1] = r2
                if self.level[r1] == self.level[r2]:
                    self.level[r2] += 1

    def kruskel(self, verticals: list, edges: list) -> list:
        for vertical in verticals:
            self.make_set(vertical)
        min_tree = []
        edges.sort()
        for edge in edges:
            weight, vertical1, vertical2 = edge
            if self.find(vertical1) != self.find(vertical2):
                self.merge(vertical1, vertical2)
                min_tree.append(edge)
        return min_tree


if __name__ == '__main__':
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges = [(7, 'A', 'B'),
             (5, 'A', 'D'),
             (8, 'B', 'C'),
             (9, 'B', 'D'),
             (7, 'B', 'E'),
             (5, 'C', 'E'),
             (15, 'D', 'E'),
             (6, 'D', 'F'),
             (8, 'E', 'F'),
             (9, 'E', 'G'),
             (11, 'F', 'G'),
             ]
    ex = Edge()
    print(ex.kruskel(verticals=vertices, edges=edges))
