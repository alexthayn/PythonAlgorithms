#Lab 7:Dynamic Programming
from collections import namedtuple

# With repeated items
def knapval_rep(capacity, items):
    K = [0]*(capacity+1)

    for wt in range(1,len(K)):
        K[wt] = max([(K[wt-item.weight] + item.value) #list comprehension syntax
        for item in items if item.weight <= wt]+[0])
    return K[capacity]

# loot item for knapsack
Item = namedtuple('Item', ['weight', 'value'])

if __name__ == "__main__":
    loot = [
        Item(6,30),
        Item(3,14),
        Item(4,16),
        Item(2,9)
    ]
    print("For the knapsack problem with repets the max value is: %d"%knapval_rep(10,loot))

def test_knapval_rep():
    loot = [
        Item(6,30),
        Item(3,14),
        Item(4,16),
        Item(2,9)
    ]
    assert knapval_rep(10,loot) == 48