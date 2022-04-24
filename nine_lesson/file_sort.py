import re
import time


def merge_sort(left_list: list, right_list: list) -> list:
    sorted_list = []
    left_ind = right_ind = 0
    left_len, right_len = len(left_list), len(right_list)

    for _ in range(left_len + right_len):
        if left_ind < left_len and right_ind < right_len:
            if left_list[left_ind] <= right_list[right_ind]:
                sorted_list.append(left_list[left_ind])
                left_ind += 1
            else:
                sorted_list.append(right_list[right_ind])
                right_ind += 1
        elif left_ind == left_len:
            sorted_list.append(right_list[right_ind])
            right_ind += 1
        elif right_ind == right_len:
            sorted_list.append(left_list[left_ind])
            left_ind += 1
    return sorted_list


def merge(nums: list) -> list:

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_list = merge(nums[:mid])
    right_list = merge(nums[mid:])

    return merge_sort(left_list, right_list)


file = "./binary.bin"
sort = []

with open(file, "rb") as f:
    # print(f)
    alist = f.readlines()
    for item in alist:
        sort.append(item)

if __name__ == "__main__":
    timer = time.time()
    merge(sort)
    print(time.time() - timer)

