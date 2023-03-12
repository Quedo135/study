# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        a, b = [], []
        while l1:
            a.append(l1.val)
            l1 = l1.next         
        while l2:
            b.append(l2.val)
            l2 = l2.next         
        while  :
                                


        res = sum( for i in range())        
        

        # [ 1->4->5, 1->3->4, 2->6 ]
