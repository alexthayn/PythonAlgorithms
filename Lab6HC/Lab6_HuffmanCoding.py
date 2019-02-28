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

    #find matching leaf node for symbol follow it up until we reach root
    def encode(self, symbols):
        if symbols == '' or None:    
            return None

        #iterate through message passed in
        encoding = ''        
        for symbol in symbols:
            encodedSymbol = ''
            symbolNode = None
            for index, item in enumerate(self.leaves):
                if item.data == symbol:
                    symbolNode = self.leaves[index]
                
            if symbolNode == None: 
                print("The symbol %s was not found" %(symbol))
                return None

            while(symbolNode.parent != None):
                encodedSymbol += symbolNode.codeValue
                symbolNode = symbolNode.parent

            #reverse encoded value because we started at the root
            encoding += encodedSymbol[::-1]

        return encoding

    def decode(self, bits):
        if bits == '':
            return None
        message = ''
        treeIter = self.root
        for bit in bits:
            if treeIter.leftChild == None:
                message += treeIter.data
                treeIter = self.root
            if bit == '1':
                treeIter = treeIter.rightChild
            else:
                treeIter = treeIter.leftChild
        # get last symbol
        if treeIter.leftChild == None:
            message += treeIter.data
        else:
            message = "Unable to decode message."
        return message


# I decided to have this return a tree codec instead of just a bintreenode, this way I could still maintain references to the leaves of the tree
def huffmanTree(dict):
    #Fill priority queue with frequency of symbols (ordered from lowest to higest frequency)
    pq = PriorityQueue()
    leafNodes = []*len(dict)
    for symbol, freq in dict.items():
        node = BinTreeNode(freq, symbol)
        leafNodes.append(node)
        pq.add(node, -freq)

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
        
        #create a tree codec to store the tree and its leaves
    treeCodec = TreeCodec(pq.pop())
    treeCodec.leaves = leafNodes
    return treeCodec    

#################################################################
############################# MAIN ##############################
#################################################################
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

    print(  """
    Symbol frequencies:
        "a": z
        "b": 5
        "c": 18
        "x": 30
        "y": 2
        "z": 1

    Encoded values:
        a: 1110
        b: 110
        c: 10 
        x: 0
        y: 11110
        z: 11111
    """)
    tree = huffmanTree(huffmanDict)
    message = 'abc'
    print("Encoding: %s"%(message))
    eMessage = tree.encode(message)
    print("   Result: %s" %eMessage)

    print("Decoding: %s"%(eMessage))
    print("    Result: %s"%tree.decode(eMessage))

    message = 'Hello'
    print("\nEncoding: %s"%(message))
    print("   Result: %s" %tree.encode(message))

    message = 'xxxyyyzzz'
    print("\nEncoding: %s"%(message))
    eMessage = tree.encode(message)
    print("   Result: %s" %eMessage)

    print("Decoding: %s"%(eMessage))
    print("    Result: %s"%tree.decode(eMessage))

    eMessage = '111111'
    print("\nDecoding: %s"%eMessage)
    print("    Result: %s"%tree.decode(eMessage))

#################################################################
############################# TESTS #############################
################################################################# 
#Setup dictionary and tree to use for tests
huffmanTestDict = {
    "a": 4,
    "b": 5,
    "c": 18,
    "x": 30,
    "y": 2,
    "z": 1,
}
testTree = huffmanTree(huffmanTestDict)

def test_BinTreeNode():
    testNode = BinTreeNode(2, 'a')
    assert testNode.data == 'a'
    assert testNode.freq == 2
    assert testNode.codeValue == None
    assert testNode.parent == None
    assert testNode.rightChild == testNode.leftChild == None


def test_HuffmanTree():
    simpleDict = {
        "a": 3,
        "b": 1
    }

    simpleTree = BinTreeNode(4,'ab', 'a', 'b')
    result =  huffmanTree(simpleDict)
    print(result.root.rightChild.data)
    print(result.root.leftChild.data)
    sTree = huffmanTree(simpleDict)

    assert sTree.root.data == simpleTree.data
    assert sTree.root.freq == simpleTree.freq


def test_HuffmanTreeMoreNodes():    
    assert testTree.root.freq == sum(huffmanTestDict.values())
    assert testTree.root.data == 'xcbayz'
    assert testTree.root.leftChild.data == 'x'
    assert testTree.root.rightChild.leftChild.data == 'c'
    assert testTree.root.rightChild.rightChild.rightChild.leftChild.data == 'a'
    assert testTree.root.rightChild.rightChild.data == 'bayz'

def test_treeCodec_Encode():
    assert testTree.encode('abc') == '111011010'
    assert testTree.encode('xyx') == '0111100'
    assert testTree.encode('zzzabc') == '111111111111111111011010'
    assert testTree.encode('hello') == None

def test_treeCodec_Decode():
    """
    Encoded values
    a: 1110
    b: 110
    c: 10 
    x: 0
    y: 11110
    z: 11111
    """
    assert testTree.decode('1110') == 'a'
    assert testTree.decode('110') == 'b'
    assert testTree.decode('10') == 'c'
    assert testTree.decode('0') == 'x'
    assert testTree.decode('11110') == 'y'
    assert testTree.decode('11111') == 'z'
    assert testTree.decode('111011010') == 'abc'
    assert testTree.decode('111111111111111111011010') == 'zzzabc'
    assert testTree.decode('') == None
    assert testTree.decode('0011111111') == "Unable to decode message."