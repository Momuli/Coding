class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self , head):
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        while cur:
            if cur.val != pre.val:
                pre = pre.next
                cur = cur.next
            else:
                pre.next = cur.next
                cur = cur.next
        return head