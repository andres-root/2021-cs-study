

def main(nums):
    sorted_squares = [0 for x in range(len(nums))]
    l = 0
    h = len(nums) - 1
    i = h

    while l <= h:
        l_squared = nums[l] ** 2
        h_squared = nums[h] ** 2

        if l_squared > h_squared:
            sorted_squares[i] = l_squared
            l += 1
        else:
            sorted_squares[i] = h_squared
            h -= 1
        
        i -= 1

    return sorted_squares

if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    result = main(nums)
    print('Result:', result)
    print('====================')
    nums = [-7, -3, 2, 3, 11]
    result = main(nums)
    print('Result:', result)
    print('====================')
    nums = [-5, -3, -2, -1]
    result = main(nums)
    print('Result:', result)
    print('====================')
