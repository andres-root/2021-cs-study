

def solution(n):
    """
    """
    arr = [x for x in range(n+1)]
    mid = arr[(len(arr) - 1)//2]
    sub_arr = arr

    while len(sub_arr) > 0:
        if len(sub_arr) == 1:
            if sub_arr[0] == target:
                return arr.index(sub_arr[0])
            else:
                return -1

        if target == mid:
            return arr.index(mid)
        
        if target < mid:
            sub_arr = sub_arr[:len(sub_arr)//2]
        
        if target > mid:
            sub_arr = sub_arr[len(sub_arr)//2:]
        
        if len(sub_arr) > 0:
            mid = sub_arr[(len(sub_arr) - 1)//2]
    
    return -1