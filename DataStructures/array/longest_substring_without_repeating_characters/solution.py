from typing import List


def min_subarray_sum_k(s: List[str]) -> int:
    window_sum = 0
    l = 0
    h = 0
    mem = []

    while h < len(arr):
        window_sum += arr[h]
        h += 1
        
        while l < h and window_sum > k:
            window_sum -= arr[l]
            l += 1
        
        if window_sum == k:
            mem.append(len(arr[l:h]))
        
    return min(mem)


arr = [1, 2, 3, 4, 5, 6, 7]
k = 7
result = min_subarray_sum_k(arr, k)
print(result)
print('===========================')

arr = [1, 1, 1, 1, 1, 1, 5, 2]
k = 7
result = min_subarray_sum_k(arr, k)
print(result)