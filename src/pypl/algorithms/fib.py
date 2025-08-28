#!/usr/bin/env python3

import timeit
from functools import lru_cache
from typing import Iterator

def fib(n: int) -> int:
    """Get the n-th element of the Fibonacci sequence. (naive recursive
    implementation)"""
    if n < 2:
        return n

    return fib(n - 2) + fib(n - 1)


memo: dict[int, int] = {0: 0, 1: 1}
def fib_memo(n: int) -> int:
    """Get the n-th element of the Fibonacci sequence. (implementation
    using memoization)"""
    if n not in memo:
        memo[n] = fib_memo(n - 2) + fib_memo(n - 1)
    return memo[n]


@lru_cache(maxsize=None) # all results of calls with unknown arguments are cached
def fib_auto_memo(n: int) -> int:
    """Get the n-th element of the Fibonacci sequence using automatic
    memoization with the ``lru_cache`` decorator."""
    if n < 2:
        return n
    
    return fib_auto_memo(n - 1) + fib_auto_memo(n - 2)


def fib_iter(n: int) -> int:
    """Get the n-th element of the Fibonacci sequence using an iterative 
    approach, which is the more efficient. O(n)."""
    if n == 0: return n
    prev: int = 0
    current: int = 1
    for _ in range(1, n):
        current, prev = current + prev, current

    return current


def generate_fib(n: int) -> Iterator[int]:
    """Genrate all Fibonacci numbers up to and including the n-th
    number."""
    yield 0
    if n > 0: yield 1
    prev: int = 0
    current: int = 1
    for _ in range(1, n):
        current, prev = current + prev, current
        yield current


if __name__ == "__main__":
    n = 30
    assert fib_memo(n) == fib_auto_memo(n) == fib_iter(n), ("Not all functions "
        "return the same result")
    
    t_naive = timeit.timeit(lambda: fib(n), number=1)
    t_memo = timeit.timeit(lambda: fib_memo(n), number=1)
    t_auto_memo = timeit.timeit(lambda: fib_auto_memo(n), number=1)
    t_iter = timeit.timeit(lambda: fib_iter(n), number=1)

    print(f"Naive implementation: {t_naive:>25.7f}s")
    print(f"Memoization implementation: {t_memo:>19.7f}s")
    print(f"Automatic Memoization implementation: {t_auto_memo:>2.7f}s")
    print(f"Iterative implementation: {t_iter:>21.7f}s")

    fib_to_n = [i for i in generate_fib(3)]
    print(fib_to_n)