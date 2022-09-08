class Solution:
    def is_palindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False

        if len(s) == 1:
            return True

        l = 0
        h = len(s) - 1
        while l < h:
            if s[l] != s[h]:
                return False
            l += 1
            h -= 1

        return True
    
    def is_palindrome_recursive(self, s: str) -> bool:
        if len(s) < 2:
            return True

        if s[0] != s[-1]:
            return False

        return self.is_palindrome_recursive(s[1:-1])

    def is_palindrome_one_liner(self, s: str) -> bool:
        return s == s[::-1]

    def countSubstrings(self, s: str) -> int:
        c = 0
        length = len(s)
        mem = {}
        for i in range(length):
            for j in range(length):
                sliced = s[i:j + 1]
                if self.is_palindrome(sliced):
                    c += 1
        return c

