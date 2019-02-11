#Alex Thayn 2/10/19

# 2. Implement an algorithm to find the kth to last element of a singly linked list
# Given a list: 1 -> 23 -> 59 -> 2  
# The 2nd to last element would be 23, the 0th to last element would be 2, etc.

#Find the kth to last element
#Return None if there is no element at that location
def kthToLastElement(list, k):
    if list == None:
        return None
    
    i = 0
    kthFromLastValue = list

    #traverse k element into the list
    while i < k:
        if list.next != None:
            list = list.next
            i+= 1
        else:
            return None

    #traverse to end of list, update kth from last value with each iteration
    while list.next != None:
        list = list.next
        kthFromLastValue = kthFromLastValue.next

    return kthFromLastValue.value



#Linked list structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    list = Node(1)
    list.next = Node(23)
    list.next.next = Node(59)
    list.next.next.next = Node(2)
    print("Given a list with values: 1 -> 23 -> 59 -> 2  we will find the kth value")
    print("0th from last value is: " + str(kthToLastElement(list,0)))
    print("2nd from last value is: " + str(kthToLastElement(list, 2)))
    print("3rd from last value is: " + str(kthToLastElement(list,3)))
    print("4th from last value is: " + str(kthToLastElement(list, 4)))


####################### Unit tests #######################
def test_kthTolastElement():
    #test empty list
    list0 = None
    assert kthToLastElement(list0, 12) == None

    list4 = Node(1)
    list4.next = Node(2)
    list4.next.next = Node(3)
    list4.next.next.next = Node(4)
    assert kthToLastElement(list4, 2) == 2
    assert kthToLastElement(list4, 1) == 3
    assert kthToLastElement(list4, 4) == None
    assert kthToLastElement(list4, 3) == 1
    assert kthToLastElement(list4, 0) == 4

    list2 = Node(45)
    list2.next = Node(45)
    assert kthToLastElement(list2, 2 ) == None
    assert kthToLastElement(list2, 1) == 45
    assert kthToLastElement(list2, 0) == 45
    assert kthToLastElement(list2,1000) == None

    list6 = Node(0)
    list6.next = Node(423)
    list6.next.next = Node(8)
    list6.next.next.next = Node(234)
    list6.next.next.next.next = Node(569)
    list6.next.next.next.next.next = Node(1)
    assert kthToLastElement(list6,0) == 1
    assert kthToLastElement(list6,100) ==None
    assert kthToLastElement(list6,2) == 234

##################### End Unit tests #####################
