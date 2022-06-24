

def is_unique(string):
    mem = {}

    for c in string:
        if mem.get(c):
            return False
        
        mem[c] = c
    
    return True

def test():
    assert is_unique('abc') == True
    assert is_unique('a') == True
    assert is_unique('abccd') == False
    assert is_unique('abcbd') == False
    print('Tests passed!')


if __name__ == '__main__':
    test()
