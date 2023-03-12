# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        values = []
        for l in lists:
            print(l)
            while l:
                values.append(l.val)
                l = l.next
        values.sort()
        res = None
        for m in values[::-1]:
            res = ListNode(m, res)
        return res


# [ 1->4->5, 1->3->4, 2->6 ]

