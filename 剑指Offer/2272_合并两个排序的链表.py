class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        dummy = q = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                q.next = l1
                l1 = l1.next
            else:
                q.next = l2
                l2 = l2.next
            q = q.next
        q.next = l1 if not l1 else l2
        return dummy.next