from typing import List


class Graph:
    def __init__(self):
        self.nodes = [
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0]
        ]
        self.count = len(self.nodes)

    def get_input_nodes(self) -> List[int]:
        stack = []
        for i in range(self.count):
            step = 0
            for j in range(self.count):
                if self.nodes[i][j] == 1:
                    step += 1
            stack.insert(i, step)
        return stack

    def topologic_sort(self) -> List[int]:
        self.levels = []
        data = self.get_input_nodes()
        counter = 0
        curr_self.level = 0

        while counter != self.count:
            for i in range(self.count):
                if data[i] == 0:
                    ind = 0
                    self.levels.insert(counter, i)
                    for node in self.nodes:
                        if node[i] == 1:
                            data[ind] -= 1
                        ind += 1

                    data[i] = -1  # mark the top as used
                    counter += 1
            curr_self.level += 1
        self.levels.reverse()
        return self.levels


if __name__ == '__main__':
    ex = Graph()
    res = ex.topologic_sort()
    print(res)
