import random
import time


def shell_sort(test_list: list, n: int) -> list:
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = test_list[i]
            j = i
            while j >= h and test_list[j - h] > t:
                test_list[j] = test_list[j - h]
                j -= h

            test_list[j] = t
        h = h // 2
    return test_list


def result(n: int) -> list:
    data = [random.randint(0, 100) for _ in range(n)]
    print(f"unsorted list: {data}")
    return shell_sort(data, len(data))


timer = time.time()
print(result(1000))
print(time.time() - timer)