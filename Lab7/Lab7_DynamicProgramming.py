#Lab 7:Dynamic Programming
from collections import namedTuple

def knapval_rep(capacity, items):
    """return the maximum value acheivable in `capacity`
    weight using `items` when repeated items are allowed"""
    options = list(
        item.value + knapval_rep(capacity - item.weight, items)
        for item in items if item.weight <= capacity)
    if len(options):
        return max(options)
    else:
        return 0

    #for item in items:
        #choose to use item.weight and get item.value + optimal from what's left
        #this_option_value = item.value + knapval_rep(capacity - item.weight, items)

# loot item for knapsack
Item = namedTuple('Item', ['weight', 'value'])

def test_knapval_rep():
    loot = [
        Item(6,30),
        Item(3,14),
        Item(4,16),
        Item(2,9)
    ]
    assert knapval_rep(10,loot) == 48