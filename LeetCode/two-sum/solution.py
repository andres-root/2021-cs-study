
def two_sum(nums, target):
    
    mem = {}
    
    for i, n in enumerate(nums):
        rest = target - n
        print(mem)
        print(rest)
        print(mem.get(rest))
        
        if mem.get(rest) is not None:
            return [mem.get(rest), i]
        
        mem[n] = i



nums = [2,7,11,15]
target = 9
result = two_sum(nums, target)
print(result)
