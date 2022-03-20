import random
import time


def insertion_sort(test_list: list) -> list:
    for item in range(1, len(test_list)):
        temp = test_list[item]
        j = item - 1
        while j >= 0 and temp < test_list[j]:
            test_list[j + 1] = test_list[j]
            j -= 1
        test_list[j + 1] = temp

    return test_list


def binary_insertion_sort(test_list: list) -> list:
    for item in range(len(test_list)):
        key = test_list[item]
        low, high = 0, item - 1
        while low < high:
            mid = low + (high - low) // 2
            if key < test_list[mid]:
                high = mid
            else:
                low = mid + 1
        for i in range(item, low + 1, -1):
            test_list[i] = test_list[i - 1]
        test_list[low] = key
    return test_list


def result(n: int) -> list:
    data = [random.randint(0, 100) for _ in range(n)]
    print(f"unsorted list: {data}")
    return binary_insertion_sort(data)


timer = time.time()
print(result(10000), "\n")
print(time.time() - timer)
