import random
import time


def heapify(array: list, heap_size: int, node: int) -> None:
    largest = node
    left = 2 * node + 1
    right = 2 * node + 2

    if left < heap_size and array[node] < array[left]:
        largest = left

    if right < heap_size and array[largest] < array[right]:
        largest = right

    if largest != node:
        array[node], array[largest] = array[largest], array[node]
        heapify(array, heap_size, largest)


def heap_sort(test_list: list) -> list:

    for item in range(len(test_list), -1, -1):
        heapify(test_list, len(test_list), item)

    for item in range(len(test_list) - 1, 0, -1):
        test_list[item], test_list[0] = test_list[0], test_list[item]
        heapify(test_list, item, 0)

    return test_list


def result(n: int) -> list:
    data = [random.randint(0, 100) for _ in range(n)]
    # print(f"unsorted list: {data}")
    return heap_sort(data)


timer = time.time()
print(result(1000000), "\n")
print(time.time() - timer)
