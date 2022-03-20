import random
import time
import pandas as pd


def bubble_sort(test_list: list) -> list:
    for i in range(0, len(test_list) - 1):
        for j in range(len(test_list) - 1):
            if test_list[j] > test_list[j + 1]:
                temp = test_list[j]
                test_list[j] = test_list[j + 1]
                test_list[j + 1] = temp
    return test_list


def bubble_sort_opt(test_list: list) -> list:
    has_swapped = True

    while has_swapped:  # останавливаем итерацию после заверешения перестановки
        has_swapped = False
        for i in range(len(test_list) - 1):
            if test_list[i] > test_list[i + 1]:
                test_list[i], test_list[i + 1] = test_list[i + 1], test_list[i]
                has_swapped = True
    return test_list


def result(n: int) -> list:
    data = [random.randint(0, 100) for _ in range(n)]
    print(f"unsorted list: {data}")
    return bubble_sort_opt(data)


timer = time.time()
print(result(10000))
print(time.time() - timer)
