#!/usr/bin/env python3

import math

# How does Python pass these types:
# - For an int:
# 10, 10, 20, 10 (like pass-by-value)
# - for a str:
# "Bye", "Bye", "Hello", "Bye" (like pass-by-value)
# - for a custom class Point
# -> behaves like pass-by-value if a new point is assigned in the
#    function
# -> behaves like pass-by-reference when an attribute is used to change
#    the Point object
# - for a list 
# -> when assigning a new list pass-by-value
# -> When modifying the list using its methods -> pass-by-reference
# => Python uses pass-by-assignment

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


def modify_using_method(l: list) -> None:
    print(l)
    l.append(8)
    print(l)


def modify_using_attr(p: Point) -> None:
    print(p)
    p.x = 20
    print(p)


def modify_using_assignment(p: Point) -> None:
    print(p)
    p = Point(20, 2)
    print(p)

if __name__ == "__main__":
    # for a list
    list = [1, 2]
    print(list)
    modify_using_method(list)
    print(list)

    # for a custom class using an attribute
    cls = Point(10, 2)
    print(cls)
    modify_using_attr(cls)
    print(cls)

    # for a custom class when assigning a new point
    cls = Point(10, 2)
    print(cls)
    modify_using_assignment(cls)
    print(cls)