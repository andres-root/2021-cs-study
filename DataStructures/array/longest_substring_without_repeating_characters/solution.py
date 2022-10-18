from typing import List
from collections import OrderedDict


def main(s: List[str]) -> int:
    if s == '':
        return 0
    
    if len(s) == 1:
        return 1
    l = 0
    h = 0
    longest_substring = float('-inf')

    while h < len(s):
        current_char = s[h]

        while l < h and current_char in s[l:h]:
            l += 1
        
        longest_substring = max(longest_substring, h - l + 1)
        h += 1

    return longest_substring


print('===========================')
s = 'abcabcbb'
result = main(s)
print(f'Input: s = "{s}"')
print(f'Output: {result}. Expected: 3')
print('===========================')

s = 'bbbbb'
result = main(s)
print(f'Input: s = "{s}"')
print(f'Output: {result}. Expected: 1')
print('===========================')

s = 'pwwkew'
result = main(s)
print(f'Input: s = "{s}"')
print(f'Output: {result}. Expected: 3')
print('===========================')

s = ' '
result = main(s)
print(f'Input: s = "{s}"')
print(f'Output: {result}. Expected: 1')
print('===========================')

s = '   '
result = main(s)
print(f'Input: s = "{s}"')
print(f'Output: {result}. Expected: 1')
print('===========================')

s = 'au'
result = main(s)
print(f'Input: s = "{s}"')
print(f'Output: {result}. Expected: 2')
print('===========================')

