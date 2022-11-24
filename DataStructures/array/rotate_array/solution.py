

def main(nums, k):
    """
    TODO: Optimize for very garge inptus. Currently, this solution breaks with large inputs.
    """
    l = 0
    h = len(nums) - 1
    prev_val = nums[l]
    i = 1

    while i <= k:
        nums[l], nums[h] = nums[h], nums[h - 1]
        l =+ 1

        while l < h:
            nums[l], prev_val = prev_val, nums[l]
            l += 1
        
        l = 0
        h = len(nums) - 1
        i += 1
        prev_val = nums[0]
            
    return nums

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    result = main(nums, k)
    print('Result 1:', result)
    print('====================')
    nums = [-1, -100, 3, 99]
    k = 1
    result = main(nums, k)
    print('Result 2:', result)
    print('====================')
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    result = main(nums, k)
    print('Result 3:', result)
    print('====================')
