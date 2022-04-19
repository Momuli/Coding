class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head ):
        if not head or not head.next:
            return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        temp = self.reverse(temp)
        dummy = ListNode(0)
        dummy.next = head
        while head and temp:
            tmp1 = head.next
            tmp2 = temp.next
            head.next = temp
            temp.next = tmp1
            head = tmp1
            temp = tmp2
        return dummy.next

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre