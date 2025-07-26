#!/usr/bin/env python3

import math

# How does Python pass these types:
# - For an int:
# 10, 10, 20, 10 (pass-by-value)
# - for a str:
# "Bye", "Bye", "Hello", "Bye" (pass-by-value)
# - for a custom class Point
# Point(1, 1), Point(1, 1), Point(8, 2), Point(1, 1) (pass-by-value)
# - for a list 
# pass-by-value
# When modifying an object
# [1, 2], [1, 2], [1, 2, 8], [1, 2, 8], [1, 2, 8]

class Point():
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


def f(l: list) -> None:
    print(l)
    l.append(8)
    print(l)


if __name__ == "__main__":
    value = [1, 2]

    print(value)
    f(value)

    print(value)