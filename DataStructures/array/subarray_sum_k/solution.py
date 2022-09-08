

def subarray_sum_k_old(arr, k):
    if k > len(arr):
        return False
    # i = 0
    l = 0
    acc = 0
    sum_array = []
    # while i < length:
    for i, v in enumerate(arr):
        acc += v
        i += 1
        if i >= k:
            sum_array.append(acc)
            acc -= arr[l]
            l += 1
    
    return sum_array
    

def subarray_sum_k(arr, k):
    if len(arr) == 0:
        return False

    if k > len(arr) or k == 0:
        return False

    acc = sum(arr[:k])
    sum_arr = [acc]
    l = 0

    for i in range(k, len(arr)):
        acc = acc - arr[l]
        acc = acc + arr[i]
        sum_arr.append(acc)
        l += 1

    return sum_arr
arr = [1, 2, 3, 4, 5, 6]
k = 7
result = subarray_sum_k_old(arr, k)
print(result)
print('-----------------------')
result = subarray_sum_k(arr, k)
print(result)
