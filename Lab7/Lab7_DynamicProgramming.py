#Lab 7:Dynamic Programming
from collections import namedtuple

# Knapsack with repeated items
def knapsack_unbounded(capacity, items):
    if(capacity < 1):
        return 0
    K = [0]*(capacity+1)

    for wt in range(1,len(K)):
        K[wt] = max([(K[wt-item.weight] + item.value) # list comprehension syntax is pretty cool
        for item in items if item.weight <= wt]+[0])
    return K[capacity]

# Knapsack with zero or one items allowed
def knapsack_0_1(capacity, items):
    if(capacity < 1):
        return 0
    K = [[0 for x in range(capacity+1)] for y in range(len(items))]
    
    for i in range(len(items)):
        for c in range(1,capacity+1):
            if(c < items[i].weight):
                K[i][c] = K[i-1][c]
            else:
                K[i][c] = max(
                    K[i-1][c-items[i].weight] + items[i].value,
                    K[i-1][c]
                )
    print(K)
    return K[len(items)-1][capacity]

# loot item for knapsack
Item = namedtuple('Item', ['weight', 'value'])
loot = [
        Item(6,30),
        Item(3,14),
        Item(4,16),
        Item(2,9)
    ]

if __name__ == "__main__":
    #print("For the knapsack problem with repeats the max value is: %d"%knapsack_unbounded(500,loot))
    print(knapsack_0_1(10,loot))

def test_knapsack_unbounded():    
    assert knapsack_unbounded(0,loot) == 0
    assert knapsack_unbounded(1,loot) == 0
    assert knapsack_unbounded(2,loot) == 9
    assert knapsack_unbounded(3,loot) == 14
    assert knapsack_unbounded(4,loot) == 18
    assert knapsack_unbounded(10,loot) == 48
    assert knapsack_unbounded(50, loot) == 249
    assert knapsack_unbounded(1000000, loot) == 4999998 # 166666(Item1) + 2(Item4) = 166666*30 + 2*9

def test_knapsack_0_1():
    assert knapsack_0_1(-100,loot) == 0
    assert knapsack_0_1(0,loot) == 0
    assert knapsack_0_1(1,loot) == 0
    assert knapsack_0_1(2,loot) == 9
    assert knapsack_0_1(10,loot) == 46
    assert knapsack_0_1(20,loot) == 69
    assert knapsack_0_1(1000,loot) == sum(item.value for item in loot)