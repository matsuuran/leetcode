#Definition for singly-linked list.
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
        l3 = ListNode(0)
        tempNode = l3
        carry = 0
        
        while l1.next != None or l2.next != None:
            temp = l1.val + l2.val + carry
            
            if l1.next == None:
                l1.next = ListNode(0)
            elif l2.next == None:
                l2.next = ListNode(0)
                
            l1 = l1.next
            l2 = l2.next
                
            tempNode.val = temp % 10
            
            if temp >= 10:
                carry = 1
            else:
                carry = 0

            tempNode.next = ListNode(0)
            tempNode = tempNode.next
        
        temp = l1.val + l2.val + carry
        tempNode.val = temp % 10
        
        if temp >= 10:
            tempNode.next = ListNode(0)
            tempNode = tempNode.next
            tempNode.val = 1

        return l3