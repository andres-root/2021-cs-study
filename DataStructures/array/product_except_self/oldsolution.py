

class Solution:        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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


def countSubstrings(self, s: str) -> int:
        c = 0
        length = len(s)
        for i in range(length):
            for j in range(length):
                sliced = s[i:j + 1]
                if self.is_palindrome(sliced):
                    c += 1
        return c