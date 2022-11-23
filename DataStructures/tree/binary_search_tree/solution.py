

def binary_search_iterative(nums, target):
    """
    Iterative binary search
    """
    mid = nums[(len(nums) - 1)//2]
    sub_arr = nums

    while len(sub_arr) > 0:
        # import ipdb; ipdb.set_trace()
        if len(sub_arr) == 1:
            if sub_arr[0] == target:
                return nums.index(sub_arr[0])
            else:
                return -1

        if target == mid:
            return nums.index(mid)
        
        if target < mid:
            sub_arr = sub_arr[:len(sub_arr)//2]
        
        if target > mid:
            sub_arr = sub_arr[len(sub_arr)//2:]
        
        if len(sub_arr) > 0:
            mid = sub_arr[(len(sub_arr) - 1)//2]
    
    return -1

def binary_search_recursive(nums, target):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        if nums[0] == target:
            return nums.index(nums[0])

    mid = nums[(len(nums) - 1)//2]
    sub_arr = nums

    if target == mid:
        return mid
    
    if target < mid:
        sub_arr = sub_arr[:len(nums)//2]
        
    if target > mid:
        sub_arr = sub_arr[len(nums)//2:]
    
    return binary_search_recursive(sub_arr, target)
     


if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 13
    result = binary_search_iterative(nums, target)
    print('Result:', result)
