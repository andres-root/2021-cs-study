import math


def jumping_clouds_old(arr):
    jumps = 0
    i = 0
    while i < len(arr):
        if i == 0 and arr[i] == 1:
            return 0
        if i == len(arr) - 1:
            break
        if arr[i] == 0:
            jumps += 1

            if i > 0 and arr[i - 1] != 1 and i + 1 < len(arr) and arr[i + 1] == 0:
                i += 2
            else:
                i += 1
        else:
            i += 1
    return jumps

def jumping_clouds(arr):
    jumps = 0
    acc = 0
    for i, n in enumerate(arr):
        if i == len(arr) - 1:
            break
        if n == 0:
            acc += 1
        else:
            jumps += math.ceil(acc / 2)
            acc = 0
            
    return jumps

# arr = [0, 1, 0, 0, 0, 1, 0]
arr = [0, 0, 1, 0, 0, 1, 0]
result = jumping_clouds(arr)
print(result)

