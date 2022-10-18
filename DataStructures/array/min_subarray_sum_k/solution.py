from typing import List


def min_subarray_sum_k(arr: List[int], k: int) -> int:
    min_lenhgth = float('inf')
    window_sum = 0
    l = 0
    h = 0

    while h < len(arr):
        window_sum += arr[h]
        h += 1
        
        while l < h and window_sum >= k:
            window_sum -= arr[l]
            l += 1
            min_lenhgth = min(min_lenhgth, h - l + 1)
        
    return min_lenhgth


arr = [1, 2, 3, 4, 5, 6, 7]
k = 7
result = min_subarray_sum_k(arr, k)
print(result)
print('===========================')

arr = [1, 1, 1, 1, 1, 1, 5, 2]
k = 7
result = min_subarray_sum_k(arr, k)
print(result)