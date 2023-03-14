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

        a, b, res = [], [], []
        while l1:
            a.append(l1.val)
            l1 = l1.next         
        while l2:
            b.append(l2.val)
            l2 = l2.next         
        s = 0
        while a or b :
            s = a.pop() + b.pop() + next_digit
            next_digit = s//10
            res.append(s%10)
        if next_digit: 
            res.append(next_digit)
        print(res)
        return res
            




        

        # [ 1->4->5, 1->3->4, 2->6 ]
