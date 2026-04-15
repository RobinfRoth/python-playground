#!/usr/bin/eny python
import pprint

from typing import NamedTuple 

class Item(NamedTuple):
    name: str
    weight: float
    value: float

def sum_field(items: list[Item], field: str) -> int | float:
    '''Sum the value for `field` from every item in `items`.''' 
    return sum([getattr(i, field, 0.0) for i in items])
    

# O(C*N), where C is the number of different capacities and N is the number
# of items.
def knapsack(items: list[Item], max_capacity: int) -> list[Item]:
    '''Find the items that fit in the knapsack and have the maximum value possible.'''
    table: list[list[float]] = [[0.0 for _ in range(len(items) + 1)]
        for _ in range(max_capacity + 1)
    ]

    for capacity in range(1, max_capacity + 1): 
        for i, item in enumerate(items):
            previous_items_value: float = table[capacity][i]
            if item.weight <= capacity:
                value_freeing_weight_for_item: float = table[capacity - item.weight][i]
                # only take the new item if its more valuable than the previous
                table[capacity][i + 1] = max(
                    value_freeing_weight_for_item + item.value,
                    previous_items_value,
                )
            else: # no space for item
                table[capacity][i + 1] = previous_items_value;
        
    # find the solution in the table
    solution: list[Item] = []
    capacity = max_capacity
    for i in range(len(items), 0, -1):
        # check if item was used
        if table[capacity][i] != table[capacity][i - 1]:
            solution.append(items[i - 1])
            # subtract weight of the used item
            capacity -= items[i - 1].weight
    return solution


if __name__ == '__main__':
    items: list[Item] = [
        Item('TV', 50, 500), Item('Candleholder', 2, 300), 
        Item('Stereo', 35, 400), Item('Notebook', 3, 1000),
        Item('Food', 15, 50), Item('Clothes', 20, 800), 
        Item('Jewellery', 1, 4000), Item('Books', 100, 300),
        Item('Printer', 18, 30), Item('Fridge', 200, 700),
        Item('Painting', 10, 1000),
    ]
    max_capacity: int = 75

    result: list[Item] = knapsack(items, max_capacity)
    print('\n'.join([str(i) for i in result]))
    print(f'Total weight = {sum_field(result, "weight")}')
    print(f'Total value = {sum_field(result, "value")}')
