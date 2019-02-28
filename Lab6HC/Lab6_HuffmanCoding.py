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
        message = ''
        treeIter = self.root
        for bit in bits:
            if bit == '1':
                if treeIter.rightChild == None:
                    message += treeIter.data
                    print(treeIter.data)
                    treeIter = self.root                
                else: treeIter = treeIter.rightChild
            else:
                if treeIter.leftChild == None:
                    message += treeIter.data
                    print(treeIter.data)
                    treeIter = self.root
                else: treeIter = treeIter.leftChild
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

    root = None
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

    tree = huffmanTree(huffmanDict)
    

    eMessage = tree.encode("abc")
    print(eMessage)

    print("Decoding: ")
    print(tree.decode(eMessage))


#################################################################
############################# TESTS #############################
################################################################# 
huffmanTestDict = {
    "a": 4,
    "b": 5,
    "c": 18,
    "x": 30,
    "y": 2,
    "z": 1,
}

testTree = huffmanTree(huffmanTestDict)

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
    assert testTree.decode('0011111110') == None