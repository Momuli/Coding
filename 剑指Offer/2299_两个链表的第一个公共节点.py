# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        q1 = headA
        q2 = headB
        while q1 != q2:
            if q1:
                q1 = q1.next
            else:
                q1 = headB
            if q2:
                q2 = q2.next
            else:
                q2 = headA
        return q1

