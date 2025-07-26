#!/usr/bin/env python3

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
    

if __name__ == "__main__":
    n = 50
    print(fib_memo(n))
    print(memo)