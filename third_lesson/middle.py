import math


class Middle:

    def __init__(self):
        pass

    def gold_section(self, n: int):
        sqrt = math.sqrt(5)
        phi = (sqrt + 1)/2
        return int(phi ** n / sqrt + 0.5)

    class MatrixEvaluation:

        def n_power(self,x, n, I, mult):
            if n == 0:
                return I
            elif n == 1:
                return x
            else:
                y = self.n_power(x, n // 2, I, mult)
                y = mult(y, y)
                if n % 2:
                    y = mult(x, y)
                return y

        def identity_matrix(self, n):
            r = list(range(n))
            return [[1 if i == j else 0 for i in r] for j in r]

        def matrix_multiply(self, A, B):
            BT = list(zip(*B))
            return [[sum(a * b
                         for a, b in zip(row_a, col_b))
                     for col_b in BT]
                    for row_a in A]

        def fib(self, n):
            F = self.n_power([[1, 1], [1, 0]], n, self.identity_matrix(2), self.matrix_multiply)
            return F[0][1]


m = Middle()
print(m.gold_section(100))
print(m.MatrixEvaluation().fib(100))