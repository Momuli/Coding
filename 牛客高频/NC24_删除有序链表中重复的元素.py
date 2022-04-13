class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self , head):
        dummy = ListNode(0)   # 伪头结点
        dummy.next = head
        pre = dummy   # 当前节点的前驱结点
        cur = head  # 当前节点
        while cur and cur.next:
            if cur.val != cur.next.val:
                pre = cur
                cur = cur.next
            else:
                while cur.val == cur.next.val:
                    cur = cur.next
                    if not cur.next:
                        break
                pre.next = cur.next
                cur = cur.next
        return dummy.next

