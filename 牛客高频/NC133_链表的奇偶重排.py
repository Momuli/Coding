class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self , head):
        if not head or not head.next:
            return head
        evenHead = head.next  # 偶链表的头结点, head作为奇链表的头结点
        odd = head   # 指向奇链表的指针
        even = evenHead  # 指向偶链表的指针
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead   # 将偶链表添加到奇链表的尾部
        return head

