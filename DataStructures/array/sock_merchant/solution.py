

def sock_merchant(arr):
    mem = {}
    c = 0
    for n in arr:
        if mem.get(n, False):
            mem[n] += 1
            
            if mem[n] % 2 == 0:
                c += 1
        else:
            mem[n] = 1
    return c

# arr = [1, 2, 1, 2, 1, 3, 2]
arr = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
result = sock_merchant(arr)
print(result)