#!/usr/bin/env python3

from typing import Generic, Iterator, TypeVar

T = TypeVar("T", int, float)

class Stack(Generic[T]):
    """Class that models a stack data structure."""

    _container: list[T]
    
    def __init__(self) -> None:
        self._container = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)
    
    def __str__(self) -> str:
        max_length = len(str(max(self._container)))
        sep = '-' * (max_length + 4)
        return (
            f"\n{sep}\n"
            + "\n".join([f"|{i:>{max_length + 2}.1f}|" for i in reversed(self._container)]) 
            + f"\n{sep}"
        )
    

if __name__ == "__main__":
    s: Stack[int] = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(100)

    print("s:", s)

    t: Stack[float] = Stack()
    t.push(10.2)
    t.push(20.9)
    t.push(50.4)

    print("t:", t)
