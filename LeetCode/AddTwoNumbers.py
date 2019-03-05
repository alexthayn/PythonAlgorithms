# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sumList = ListNode(0)
        nextNode = sumList
        node1 = l1
        node2 = l2
        carry = 0
        
        while node1 is not None and node2 is not None:
            if node1.val + node2.val + carry > 9:
                nextNode.val = (node1.val + node2.val + carry) - 10 
                carry = 1
            else: 
                nextNode.val = node1.val + node2.val + carry
                carry = 0                   
    
            node1 = node1.next
            node2 = node2.next
            if node1 is not None and node2 is not None:
                nextNode.next = ListNode(0)
                nextNode = nextNode.next

        while node1 is not None:  
            nextNode.next = ListNode(0)
            nextNode = nextNode.next 
            print("hello")
            if node1.val + carry > 9:
                nextNode.val =(node1.val + carry) - 10
                carry = 1
            else:                 
                nextNode.val = node1.val + carry
                carry = 0
            node1 = node1.next   
            
                    
        while node2 is not None: 
            nextNode.next = ListNode(0)
            nextNode = nextNode.next 
            print(node2.val)
            if node2.val + carry > 9:
                nextNode.val = (node2.val + carry) - 10
                carry = 1
            else: 
                nextNode.val = node2.val + carry  
                carry = 0
            node2 = node2.next
        
        if carry > 0:
            nextNode.next = ListNode(1)

        return sumList

if __name__ == "__main__":
    solution = Solution()
    first = ListNode(4)
    first.next = ListNode(5)
    first.next.next = ListNode(6)
    second = ListNode(3)
    second.next = ListNode(8)
    second.next.next = ListNode(5)
    answer = solution.addTwoNumbers(first, second)

    curr = answer
    while curr is not None:
        print(curr.val)
        curr = curr.next