import random
import time


def quicksort(xs: list) -> list:
    if xs:
        return quicksort([i for i in xs[1:] if i < xs[0]]) + [xs[0]] + quicksort([i for i in xs[1:] if i >= xs[0]])
    else:
        return xs


def hoar_quick_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return hoar_quick_sort(l_nums) + e_nums + hoar_quick_sort(b_nums)


def result(n: int) -> list:
    data = [random.randint(0, 100) for _ in range(n)]
    return hoar_quick_sort(data)


timer = time.time()
print(result(10000000), "\n")
print(time.time() - timer)
