
from typing import Dict
from functools import lru_cache


@lru_cache(maxsize=None)
def fib_recursive(n: int) -> int:
    if n < 2:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


memo: Dict[int, int] = {0: 0, 1: 1}

def fib_recursive_memoized(n: int) -> int:
    if n not in memo:
        memo[n] = fib_recursive(n - 1) + fib_recursive(n - 2)

    return memo[n]


def fib_iterative(n: int) -> int:
    if n == 0: return n

    l: int = 0
    h: int = 1

    for _ in range(1, n):
        l, h = h, l + h
    
    return h

if __name__ == '__main__':
    print(fib_iterative(5))
    print(fib_iterative(10))
    print(fib_iterative(50))
