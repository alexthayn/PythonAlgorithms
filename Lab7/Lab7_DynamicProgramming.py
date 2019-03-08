#Lab 7:Dynamic Programming
from collections import namedtuple
from functools import lru_cache, reduce

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

class GraphNode:
    def __init__(self,data, parents = None):
        self.data = data
        self.parentNodes = parents
        self.children = []
        self.numPaths = None
        self.maxPath = None
        self.minPath = None

    def addChild(self, child):
        self.children.append(child)


#############################################
# Number of s, t paths through a dag
#############################################
@lru_cache(maxsize=None)
def numOfPaths(s, t):
    if s == t:
        return 1
    else:
        if not s.numPaths:
            s.numPaths = sum(numOfPaths(child, t) for child in s.children)
    return s.numPaths

#############################################
# Length of longest s, t path through a dag
#############################################
@lru_cache(maxsize=None)
def longestPath(s,t):
    if s == t:
        return 0
    else:
        if not s.maxPath:
            s.maxPath = max(longestPath(child, t)+1 for child in s.children)
    return s.maxPath

#############################################
# Length of shortest s, t path through a dag
#############################################
@lru_cache(maxsize=None)
def shortestPath(s,t):
    if s == t:
        return 0
    else:
        if not s.minPath:
            s.minPath = min(longestPath(child, t)+1 for child in s.children)
    return s.minPath

loot = [
        Item(6,30),
        Item(3,14),
        Item(4,16),
        Item(2,9)
    ]

# DAG creation
s = GraphNode('S')
b = GraphNode('B',[s])
a = GraphNode('A',[s,b])
c = GraphNode('C',[b])
d = GraphNode('D',[c])
t = GraphNode('T',[a,c,d])
s.addChild(a)
s.addChild(b)
a.addChild(t)
b.addChild(a)
b.addChild(c)
c.addChild(t)
c.addChild(d)
d.addChild(t)
#############################################
# MAIN
#############################################
if __name__ == "__main__":
    print("The knapsack with capacity 500 and repeats allowed the max value is: %d"%knapsack_unbounded(500,loot))
    print("The knapsack with capacity 10 and no repeats the max value is: %d"% knapsack_0_1(10,loot))
    print("The minimum edit distance between abcdef and azced is: %d"% edit_distance("abcdef","azced"))
    print("The longest increasing subsequence of 2,5,1,8,3 is: %d"%longest_subsequence([2,5,1,8,3]))
    print("""   
    DAG Adjacency List: 
    S: A, B
    A: T
    B: A, C
    C: D, T
    D: T
    T: None""")
    print("The number of paths from S to T is: %d"%numOfPaths(s,t))
    print("The longest path from S to T is: %d"%longestPath(s,t))
    print("The shortest path from S to T is: %d"%shortestPath(s,t))
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

def test_numberOfPaths():
    assert numOfPaths(s,t) == 4
    assert numOfPaths(c,t) == 2
    assert numOfPaths(t,t) == 1
    assert numOfPaths(a,t) == 1
    assert numOfPaths(b,t) == 3

def test_longestPath():
    assert longestPath(s,t) == 4
    assert longestPath(a,t) == 1
    assert longestPath(b,t) == 3
    assert longestPath(c,t) == 2
    assert longestPath(d,t) == 1
    assert longestPath(b,d) == 3
    
def test_shortestPath():
    assert shortestPath(s,t) == 2
    assert shortestPath(a,t) == 1
    assert shortestPath(b,t) == 2
    assert shortestPath(c,t) == 1
    assert shortestPath(d,t) == 1