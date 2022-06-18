from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS_util(self, v, visited):
        visited[v] = True
        print(v,)
        for i in self.graph[v]:
            if visited[i] is False:
                self.DFS_util(i, visited)

    def fill_order(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] is False:
                self.fill_order(i, visited, stack)
        stack.append(v)

    def get_transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_SCCs(self):

        stack = []
        visited = [False] * self.V
        for i in range(self.V):
            if visited[i] is False:
                self.fill_order(i, visited, stack)

        gr = self.get_transpose()

        visited = [False] * self.V

        while stack:
            i = stack.pop()
            if visited[i] is False:
                gr.DFS_util(i, visited)
                print("")


g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

print("Following are strongly connected components " +
      "in given graph")
g.print_SCCs()
