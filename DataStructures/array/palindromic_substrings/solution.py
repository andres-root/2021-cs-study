

def is_palindrome(s):
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

def is_palindrome_recursive(s):
    if len(s) < 2:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return is_palindrome_recursive(s[1:-1])

def is_palindrome_one_liner(s):
    return s == s[::-1]

def count_substrings(s):
    c = 0
    length = len(s)
    mem = {}
    
    for i in range(length):
        for j in range(i, length):
            sliced = s[i:j + 1]
            mem_is_palindrome = mem.get(sliced, None)
            
            if mem_is_palindrome is not None:
                is_palindrome_str = mem_is_palindrome
            else:
                is_palindrome_str = is_palindrome_recursive(sliced)
                mem[sliced] = is_palindrome_str

            if is_palindrome:
                c += 1
    return c


sl = [
    'anna',
    'anax',
    'civic',
    'kayak',
    'madam',
    'aaa',
    'abc',
    'aaaaa',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
]
for s in sl:
    result = count_substrings(s)
    print(s, result)
    print('============')
