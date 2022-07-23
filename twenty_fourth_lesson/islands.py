
class Main:
    def __init__(self, line):
        self.line = line
        self.map = [[(self.line[i:i+8])] for i in range(0, len(self.line), 8)]
        self.map_len = len(self.map)
        self.n = 0

    def solution(self) -> int:
        islands = 0
        for i in range(self.map_len):
            for j in range(len(self.map[i])):
                print(islands)
                if self.map[i][j] == 1:
                    islands += 1
                    self.delete_island(i, j)
        return islands

    def delete_island(self, x: int, y: int):
        if x < 0 or x >= self.map_len:
            return
        if y < 0 or y >= self.map_len:
            return
        if self.map[x][y] == 0:
            return
        self.map[x][y] = 0
        self.delete_island(x - 1, y)
        self.delete_island(x + 1, y)
        self.delete_island(x, y - 1)
        self.delete_island(x, y + 1)


if __name__ == '__main__':
    ex = Main("1 1 1 1 0 1 0 1 0 0 0 0 1 0 1 1")
    print(ex.solution())