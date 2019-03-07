#Lab 7:Dynamic Programming
from collections import namedtuple
# loot item for knapsack
Item = namedtuple('Item', ['weight', 'value'])

#############################################
# Knapsack with repeated items
#############################################
def knapsack_unbounded(capacity, items):
    if(capacity < 1):
        return 0
    K = [0]*(capacity+1)

    for wt in range(1,len(K)):
        K[wt] = max([(K[wt-item.weight] + item.value) # list comprehension syntax is pretty cool
        for item in items if item.weight <= wt]+[0])
    return K[capacity]

#############################################
# Knapsack with zero or one of each item allowed
#############################################
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
    return K[len(items)-1][capacity]

#############################################
# Minimum edit-distance
#############################################
def edit_distance(str1, str2):
    T = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    #initialize 2d array with correct start values
    for i in range(len(str1)+1):
        T[0][i] = i
    for j in range(len(str2)+1):
        T[j][0] = j
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if(str1[i-1] == str2[j-1]):
                T[j][i] = T[j-1][i-1] # get the diagonal value because these two chars are the same
            else:
                T[j][i] = 1 + min(T[j-1][i],T[j-1][i-1],T[j][i-1]) # 1 + min(top,left,diagonal)
    return T[len(str2)][len(str1)]

#############################################
# Length of longest increasing subsequence
#############################################
def longest_subsequence(seq):
    if len(seq) < 1:
        return 0

    L = [1]*len(seq)

    for i in range(1,len(seq)):
        j = 0
        while  j < i:
            if seq[i] > seq[j]:
                if L[j] + 1 > L[i]:
                    L[i] = 1 + L[j]
            j+= 1
    return max(L)

#############################################
# Length of shortest s, t path through a dag
#############################################

loot = [
        Item(6,30),
        Item(3,14),
        Item(4,16),
        Item(2,9)
    ]

#############################################
# MAIN
#############################################
if __name__ == "__main__":
    print("The knapsack with capacity 500 and repeats allowed the max value is: %d"%knapsack_unbounded(500,loot))
    print("The knapsack with capacity 10 and no repeats the max value is: %d"% knapsack_0_1(10,loot))
    print("The minimum edit distance between abcdef and azced is: %d"% edit_distance("abcdef","azced"))
    print("The longest increasing subsequence of 2,5,1,8,3 is: %d"%longest_subsequence([2,5,1,8,3]))

#############################################
# TESTS
#############################################
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
    assert knapsack_0_1(75,loot) == sum(item.value for item in loot)

def test_edit_distance():
    assert edit_distance("","") == 0
    assert edit_distance("Blue","Blue") == 0
    assert edit_distance("Hello", "Jello") == 1
    assert edit_distance("blue", "bear") == 3
    assert edit_distance("abcdef", "azced") == 3
    assert edit_distance("exponential", "polynomial") == 6

def test_longest_subsequence():
    assert longest_subsequence([]) == 0
    assert longest_subsequence([1]) == 1
    assert longest_subsequence([0,1,2,3,4,6,7,8,9,10,11,12,13]) == 13
    assert longest_subsequence([3,4,-1,0,6,2,3]) == 4
    assert longest_subsequence([2,5,1,8,3]) == 3
    assert longest_subsequence([5,2,8,6,3,6,9,7]) == 4