

def lcm(a, b):
    i = 1
    ma = a
    mb = b
    hm = {}
    while True:
        ma = a * i
        mb = b * i
        if hm.get(ma, False):
            return ma
        if hm.get(mb, False):
            return mb
        hm[ma] = a
        hm[mb] = b
        
        i += 1
        
        if i > max(a, b):
            return False


if __name__ == '__main__':
    a = 185
    b = 25
    result = lcm(a, b)
    print(f'LCM of {a} and {b} is:', result)