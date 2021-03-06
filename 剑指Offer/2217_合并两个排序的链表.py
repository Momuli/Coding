class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = res = ListNode(0)   # res:伪头结点  cur:当前节点
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = l2
                l2 = l2.next
            elif l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return res.next

    def mergeTwoLists2(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        else:
            if l1.val >= l2.val:
                l2.next = self.mergeTwoLists2(l1, l2.next)
                return l2
            else:
                l1.next = self.mergeTwoLists2(l1.next,l2)
                return l1
