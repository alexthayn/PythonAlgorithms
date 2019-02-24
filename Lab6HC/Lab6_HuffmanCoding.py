# Alex Thayn
# Lab 6: Huffman Coding
from boltons.queueutils import PriorityQueue

# Binary Tree Node Class
class BinTreeNode:
    def __init__(self, data = None,  parent = None, leftChild = None, rightChild = None):
        self.data = data
        self.parent  = parent
        self.leftChild = leftChild
        self.rightChild = rightChild


# Tree Codec class
class TreeCodec:
    def __init__(self, rootNode):
        self.root = rootNode
        self.leaves = None

    def encode(self, symbols):
        pass

    def decode(self, bits):
        pass


def huffmanTree(dict):
    #Fill priority queue with frequency of symbols (ordered from lowest to higest frequency)
    pq = PriorityQueue()
    for symbol, freq in dict.items():
        pq.add(symbol, -freq)
    root = BinTreeNode()
    #Build huffman tree
    while len(pq) > 1:
        #take the two lowest frequency values and connect them
        parent = BinTreeNode()
        #lowest frequency on the right
        rightNode = BinTreeNode(pq.pop(), parent)
        #next lowest frequency on the left
        leftNode = BinTreeNode(pq.pop(), parent)
        parent.leftChild = leftNode
        parent.rightChild = rightNode
        root = parent

    return root

    

if __name__ == "__main__":
    #construct a dictionary for which we want to build a huffman tree
    huffmanDict = {
        "a": 4,
        "b": 5,
        "c": 18,
        "x": 30,
        "y": 2,
        "z": 1,
    }

    tree = huffmanTree(huffmanDict)

    while tree.rightChild != None:
        print(tree.rightChild.data)
        tree = tree.rightChild


def test_HuffmanTree():
    simpleDict = {
        "a": 3,
        "b": 1
    }

    simpleTree = BinTreeNode(None,None, "a", "b")
    result =  huffmanTree(simpleDict)
    print(result.rightChild.data)
    print(result.leftChild.data)
