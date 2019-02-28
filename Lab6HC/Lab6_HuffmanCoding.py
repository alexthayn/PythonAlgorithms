# Alex Thayn
# Lab 6: Huffman Coding
from boltons.queueutils import PriorityQueue

# Binary Tree Node Class
class BinTreeNode:
    def __init__(self, freq, data = None,  parent = None, leftChild = None, rightChild = None):
        self.freq = freq
        self.data = data
        self.parent  = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.codeValue = None

    
# Tree Codec class
class TreeCodec:
    def __init__(self, rootNode):
        self.root = rootNode
        self.leaves = None

    def encode(self, symbols):
        #find matching leaf node for symbol follow it up until we reach root
        encoding = ''
        for symbol in symbols:
            symbolNode = None
            for index, item in enumerate(self.leaves):
                if item.data == symbol:
                    symbolNode = item
                else:
                    print("The symbol %s is not in the current huffman tree", symbol)
            while(symbolNode.parent != None):
                encoding += symbolNode.codeValue
                symbolNode = symbol.Parent

    def decode(self, bits):
        pass

# I decided to have this return a tree codec instead of just a bintreenode, this way I could still maintain references to the leaves of the tree
def huffmanTree(dict):
    #Fill priority queue with frequency of symbols (ordered from lowest to higest frequency)
    pq = PriorityQueue()
    leafNodes = []*len(dict)
    for symbol, freq in dict.items():
        node = BinTreeNode(freq, symbol)
        leafNodes.append(node)
        pq.add(node, -freq)
    root = BinTreeNode(1)
    #Build huffman tree
    while len(pq) > 1:
        #take the two lowest frequency values and connect them
        #lowest frequency on the right
        rightNode = pq.pop()
        rightNode.codeValue = '1'
        #next lowest frequency on the left
        leftNode = pq.pop()
        leftNode.codeValue = '0'

        # Create a parent node that combines the two lowest frequency nodes
        parent = BinTreeNode(rightNode.freq + leftNode.freq, leftNode.data + rightNode.data)
        parent.leftChild = leftNode
        parent.rightChild = rightNode
        pq.add(parent)

        leftNode.parent = rightNode.parent = parent
        root = parent
        
        #create a tree codec to store the tree and its leaves
        treeCodec = TreeCodec(root)
        treeCodec.leaves = leafNodes
    return treeCodec    

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

    while tree.root.rightChild != None:
        print(tree.root.rightChild.data)
        tree.root = tree.root.rightChild


def test_HuffmanTree():
    simpleDict = {
        "a": 3,
        "b": 1
    }

    simpleTree = BinTreeNode(4,'ab', 'a', 'b')
    result =  huffmanTree(simpleDict)
    print(result.root.rightChild.data)
    print(result.root.leftChild.data)
    tree = huffmanTree(simpleDict)

    assert tree.root.data == simpleTree.data
    assert tree.root.freq == simpleTree.freq


def test_HuffmanTreeMoreNodes():
    huffmanDict = {
        "a": 4,
        "b": 5,
        "c": 18,
        "x": 30,
        "y": 2,
        "z": 1,
    }

    tree = huffmanTree(huffmanDict)
    
    assert tree.root.freq == sum(huffmanDict.values())
    assert tree.root.data == 'xcbayz'
    assert tree.root.leftChild.data == 'x'
    assert tree.root.rightChild.leftChild.data == 'c'
    assert tree.root.rightChild.rightChild.rightChild.leftChild.data == 'a'
    assert tree.root.rightChild.rightChild.data == 'bayz'