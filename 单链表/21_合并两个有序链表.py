# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = res = ListNode()   # 合并链表的伪头结点
        q1 = list1
        q2 = list2
        while q1 and q2:
            if q1.val <= q2.val:
                cur.next = q1
                q1 = q1.next
            else:
                cur.next = q2
                q2 = q2.next
            cur = cur.next
        cur.next = q1 if q1 else q2
        return res.next

