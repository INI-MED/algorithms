"""
Занятие от 08.02.2022
"""
import time


def first_counter():

    result = 0
    for item in range(0, 10):
        for i in range(0, 10):
            for j in range(0, 10):
                first_sum = item + i + j
                for k in range(0, 10):
                    for l in range(0, 10):
                        m = first_sum - (k + l)
                        if 0 <= m <= 9:
                            result += 1
    return result


def time_decor(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        return time.time() - start
    return wrapper


class SecondCounter:
    def __init__(self):
        self.counter = 0

    def recursive_counter(self, n: int, sum_a: int, sum_b: int):
        if n == 0:
            if sum_a == sum_b:
                self.counter += 1
            return

        for a in range(10):
            for b in range(10):
                self.recursive_counter(n - 1, sum_a + a, sum_b + b)

    def main(self):
        self.recursive_counter(5, 0, 0)


f = SecondCounter()
f.main()
print(f.counter)
