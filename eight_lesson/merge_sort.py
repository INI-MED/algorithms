import random
import time


def merge_sort(nums: list) -> list:
    nums_len = len(nums)
    if nums_len > 1:
        mid = nums_len // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0  # i = left, j = right, k = nums indexes
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    return nums


def result(n: int) -> list:
    data = [random.randint(0, 100) for _ in range(n)]
    return merge_sort(data)


timer = time.time()
result(10000000)
print(time.time() - timer)
