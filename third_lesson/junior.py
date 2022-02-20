import math


class Junior:
    def __init__(self):
        self.number = 1.0
        self.N = 100
        self.hashmap = {0: 0, 1: 1}

    def iterative_way(self):
        for item in range(1000):
            self.number *= 1.001
        return self.number

    def BFS(self):
        d = self.number
        while self.N > 1:
            self.N /= 2
            d *= d
            if self.N % 2 == 1:
                self.number *= d
        self.number *= d
        return self.number

    def fib_iter_way(self, n: int):
        fib1 = fib2 = 1
        stack = []
        for item in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
            stack.append(fib2)
        return stack[-1]

    def fib_recursive_way(self, n: int):
        if n in self.hashmap:
            return self.hashmap[n]
        self.hashmap[n] = self.fib_recursive_way(n - 1) + self.fib_recursive_way(n - 2)

        return self.hashmap[n]




f = Junior()


