# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 如果链表为空
        if not head:
            return
        # 如果链表的首元素是val
        if head.val == val:
            return head.next
        # pre是当前节点cur的前驱节点
        pre = head
        cur = head.next
        while cur:
            if cur.val == val:
                pre.next = cur.next
                break
            else:
                cur = cur.next
                pre = pre.next
        return head
