#!/usr/bin/env python3
# Class with iterator
class IterTest:
    def __init__(self, *values):
        self.values = values
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == len(self.values):
            raise StopIteration

        elem = self.values[self.index]
        self.index += 1
        return elem
    
# Generator function
def test_gen(*values):
    for index in range(0, len(values)):
        yield values[index]
    
if __name__ == "__main__":
    test = IterTest(1, 2, 3, 4, 5)
    it = iter(test)
    
    for elem in it:
        print(elem)

    gen = test_gen(1, 2, 3)
    
    for elem in gen:
        print(elem)

    for elem in test_gen("a", "b", "c"):
        print(elem)