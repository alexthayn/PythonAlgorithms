#Alex Thayn 2/10/19
# 1. Implement a function to check if a binary tree is balanced.

#Check if a binary tree is balanced such that the heights of the two subtress never differ by more than one.
def isTreeBalanced(root):
    leftHeight = 0 
    rightHeight = 0

    #base case 
    if root == None:
        return True
    
    #find height of left and right subtrees
    leftHeight = treeHeight(root.left)
    rightHeight = treeHeight(root.right)
    #check if left and right subtrees are balanced and differ by no more than one
    if(abs(leftHeight - rightHeight) <= 1) and isTreeBalanced(root.left) == True and isTreeBalanced(root.right) == True:
        return True

    #else tree is not balanced
    return False

#Determine height of binary tree
def treeHeight(root):
    #base case
    if root == None:
        return 0
    return max(treeHeight(root.left), treeHeight(root.right)) + 1


#Node class for binary tree
class Node:
    #constructor 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

#Main driver
if __name__ == "__main__":
    #create sample tree that is balanced
    balancedTree = Node(23)
    balancedTree.left = Node(50)
    balancedTree.left.left = Node(88)
    balancedTree.left.right = Node(90)
    balancedTree.right = Node(32)
    balancedTree.right.left = Node(96)
    balancedTree.right.right = Node(74)

    #check if tree is balanced
    isBalanced = isTreeBalanced(balancedTree)
    
    print("The balanced test tree returned: ") 
    print(isBalanced)

    #create unbalanced test tree

    unbalancedTree = Node(48)
    unbalancedTree.left = Node(12)
    unbalancedTree.left.right = Node(15)

    isBalanced = isTreeBalanced(unbalancedTree)
    print("The unbalanced test tree returned: ")
    print(isBalanced)


####################### Unit tests #######################

#test for isBalanced function
def test_isBalanced():
    #empty tree
    emptyTree = None
    assert isTreeBalanced(emptyTree) == True

    #tree with no sub-trees
    root = Node(100)
    assert isTreeBalanced(root) == True

    #balanced perfect binary tree
    balancedTree = Node(1)
    balancedTree.left = Node(12)
    balancedTree.right = Node(3)
    assert isTreeBalanced(balancedTree) == True

    #balanced tree that differs by one
    balancedTreeDiffer1 = Node(34)
    balancedTreeDiffer1.left = Node(12)
    assert isTreeBalanced(balancedTreeDiffer1) == True

    #unbalanced tree
    unbalancedTree = Node(2)
    unbalancedTree.right = Node(12)
    unbalancedTree.left = Node(15)
    unbalancedTree.right.right = Node(23)
    unbalancedTree.right.right.left = Node(21)
    assert isTreeBalanced(unbalancedTree) == False

#test for treeHeight function
def test_treeHeight():
    #create a tree with height of 0
    root0 = None
    assert treeHeight(root0) == 0

    #create a tree with height of 1
    root = Node(12)
    assert treeHeight(root) == 1

    #create tree with height of 2
    root2 = Node(1)
    root2.left = Node(3)
    assert treeHeight(root2) == 2

    #create tree with height of 8
    root8 = Node(1)
    root8.left = Node(2)
    root8.left.left = Node(3)
    root8.left.left.left = Node(4)
    root8.left.left.left.left = Node(5)
    root8.left.left.left.left.left = Node(6)
    root8.left.left.left.left.left.left = Node(7)
    root8.left.left.left.left.left.left.left = Node(8)
    assert treeHeight(root8) == 8
    
##################### End Unit tests #####################
