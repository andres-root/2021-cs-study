

def min_subarray_sum_k(arr, k):
    window_sum = 0
    acc = 0
    l = 0
    h = 0
    min_sum = float('inf')
    mem = []

    while l <= len(arr) - 1:
        print(window_sum)
        window_sum += arr[h]
        acc += 1
        if h < len(arr) - 1:
            h += 1
        while window_sum >= k:
            print('while 2')
            mem.append(arr[l:h])
            if window_sum < min_sum:
                min_sum = window_sum
            
            window_sum -= arr[l]
            l += 1
            acc -= 1
    
    return acc, mem


arr = [1, 2, 3, 4, 5, 6]
k = 7
result = min_subarray_sum_k(arr, k)
print(result)