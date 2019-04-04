
def solution(max):
    if max < 2:
        return 0
    num1 = 1
    num2 = 2
    sum = 0

    i = 0
    while(num2 < max):
        if(num2 % 2 == 0):
            sum += num2
            print(sum)

        next = num1 + num2
        num1 = num2
        num2 = next
        i += 1

    return sum


# solution(2)
# solution(5)
# solution(100)


def binTreeSolution(arr):
    if(len(arr) == 0):
        return ""

    levels = []
    levels.append([arr[0]])

    levelNum = 1
    i = 1
    # populate each level with node values
    # Suppose you're given a binary tree represented as an array. For example, [3,6,2,9,-1,10] represents the following binary tree where -1 is a non-existent node):

    while i < len(arr):
        currLevel = []
        upperLevelIter = 0

        while len(currLevel) < 2**levelNum and i < len(arr):
            if levels[levelNum-1][upperLevelIter] == -1:
                currLevel.append(-1)
            else:
                currLevel.append(arr[i])
            i += 1
            if(i % 2 == 1):
                upperLevelIter += 1

        levelNum += 1
        levels.append(currLevel)

    print(levels)


binTreeSolution([3, 6, 2, 9, -1, 10])
binTreeSolution([3, 6, 2, 9, -1, 10, 2, 5, 6, 7,
                 8, 2, 4, 5, 4, 3, 56, 3, 6, 2])

# class Node:
#     def __init__(self, value, parent=None, leftChild=None, rightChild=None):
#         self.value = value
#         self.parent = parent
#         self.leftChild = leftChild
#         self.rightChild = rightChild


# class BinaryTree:
#     def __init__(self, root):
#         self.root = root
#         self.nextOpening = root.leftChild

#     def insertNode(node):
#         self.nextOpening = node
#         self.nextOpening = self.findNextOpening()

#     def findNextOpening()
#        # find if the current next opening value is a left or right child
#        if self.nextOpening == self.nextOpening.parent.rightChild:
#             self.nextOpening = self.nextOpening.parent.left

#         # move on to the next node in that level
#         self.nextOpening=
