import random
import time


def selection_sort(test_list: list) -> list:
    for i in range(0, len(test_list) - 1):
        smallest = i
        for j in range(i + 1, len(test_list)):
            if test_list[j] < test_list[smallest]:
                smallest = j
        test_list[i], test_list[smallest] = test_list[smallest], test_list[i]

    return test_list


def result(n: int) -> list:
    data = [random.randint(0, 100) for _ in range(n)]
    # print(f"unsorted list: {data}")
    return selection_sort(data)


timer = time.time()
print(result(100000), "\n")
print(time.time() - timer)
