from typing import List
n = int(input())
list_s = list(map(int, input().split()))
q = int(input())
list_t = list(map(int, input().split()))


def binary_search(key: int, target_list: List[int]) -> bool:
    left_idx = 0
    right_idx = len(target_list) - 1
    while left_idx - right_idx != 1:
        mid_idx = (right_idx - left_idx)//2 + left_idx
        if target_list[mid_idx] == key:
            return True
        if target_list[mid_idx] > key:
            right_idx = mid_idx - 1
        else:
            left_idx = mid_idx+1
    return target_list[left_idx] == key or target_list[right_idx] == key


count = 0

for key in list_t:
    included = binary_search(key, list_s)
    if included:
        count += 1

print(count)
