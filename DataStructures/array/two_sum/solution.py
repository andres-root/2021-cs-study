

def two_sum_ordered(arr, k):
    i = 0
    j = len(arr) - 1

    while i < j:
        acc = arr[i] + arr[j]

        if acc == k:
            return True
        elif acc < k:
            i += 1
        else:
            j -= 1
    
    return False

arr = [1, 2, 3, 9]
k = 8
result = two_sum_ordered(arr, k)
assert result == False

arr = [1, 2, 4, 4]
k = 8
result = two_sum_ordered(arr, k)
assert result == True


def two_sum(arr, k):
    mem = {}

    for i, v in enumerate(arr):
        rest = k - v
        if mem.get(rest, False):
            return [int(mem[rest]), i]
        else:
            mem[v] = str(i)
    
    return False

arr = [1, 2, 4, 4]
k = 8
result = two_sum(arr, k)
print(result)
assert result == [2, 3]

arr = [2, 7, 11, 15]
k = 9
result = two_sum(arr, k)
print(result)
assert result == [0, 1]
