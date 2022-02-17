# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        hash_l = []
        while headA:
            hash_l.append(headA)
            headA = headA.next
        while headB:
            if headB not in hash_l:
                headB = headB.next
            else:
                return headB
        return None

    def getIntersectionNode2(self, headA, headB):
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            if pa:
                pa = pa.next
            else:
                pa = headB
            if pb:
                pb = pb.next
            else:
                pb = headA
        return pa

