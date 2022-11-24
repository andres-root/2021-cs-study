

def binary_search_iterative(nums, target):
    """
    Iterative binary search
    """
    l = 0
    h = len(nums)

    while l < h:
        mid = (l + h)//2
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            l = mid + 1
        else:
            h = mid

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
