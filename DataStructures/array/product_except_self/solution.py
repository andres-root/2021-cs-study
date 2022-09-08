

def product_except_self_first(arr):
    new_arr = []
    for i, _ in enumerate(arr):
        if i == 0 or i == 1:
            new_arr.append(arr[0])
            continue
            
        
        new_arr.append(arr[i - 1] * new_arr[i - 1])
    
    i = len(arr) - 2
    acc = arr[len(arr)  - 1]
    
    while i >= 0:
        if i == 0:
            new_arr[i] = acc
            acc *= arr[i]
        else:
            new_arr[i] *= acc
            acc *= arr[i]

        i -= 1

    return new_arr

arr = [4, 3, 2, 1, 2]
result = product_except_self_first(arr)
print(result)


def product_except_self(nums: list[int]) -> list[int]:
        length = len(nums)
        result = [0] * length
        result[0] = 1
        
        # Compute left products
        for i in range(length):
            if i > 0:
                result[i] = nums[i - 1] * result[i - 1]

        # Compute right products
        m = 1
        for i in range(length - 1, -1, -1):
            if i < length - 1:
                m = m * nums[i + 1]
                result[i] = result[i] * m
        return result
