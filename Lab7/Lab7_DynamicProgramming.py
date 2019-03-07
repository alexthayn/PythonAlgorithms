#Lab 7:Dynamic Programming
from collections import namedtuple

# With repeated items
def knapsack_unbounded(capacity, items):
    K = [0]*(capacity+1)

    for wt in range(1,len(K)):
        K[wt] = max([(K[wt-item.weight] + item.value) # list comprehension syntax is pretty cool
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
    print("For the knapsack problem with repeats the max value is: %d"%knapsack_unbounded(500,loot))

def test_knapsack_unbounded():
    loot = [
        Item(6,30),
        Item(3,14),
        Item(4,16),
        Item(2,9)
    ]
    assert knapsack_unbounded(0,loot) == 0
    assert knapsack_unbounded(1,loot) == 0
    assert knapsack_unbounded(2,loot) == 9
    assert knapsack_unbounded(3,loot) == 14
    assert knapsack_unbounded(4,loot) == 18
    assert knapsack_unbounded(10,loot) == 48
    assert knapsack_unbounded(50, loot) == 249
    assert knapsack_unbounded(1000000, loot) == 4999998 # 166666(Item1) + 2(Item4) = 166666*30 + 2*9