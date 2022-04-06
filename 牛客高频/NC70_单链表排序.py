class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
class Solution:
    # 归并排序
    def sortInList(self, head):
        if not head or not head.next:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next   # 右子链表的头结点
        slow.next = None  # 左子链表的尾结点
        left_list = self.sortInList(head)
        right_list = self.sortInList(mid)
        res = self.Merge(left_list, right_list)
        return res
    def Merge(self, l1, l2):
        dummy = p = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return dummy.next

