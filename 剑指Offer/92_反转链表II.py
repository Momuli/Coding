class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # 从head开始,也就是以head为下标1,反转[left,right]区间的节点,返回反转链表的头结点
    def reverseBetween(self, head, left, right):
        # base case:当left等于1是相当于从头节点head开始,反转前right个节点
        if left == 1:
            return self.reverseN(head, right)
        # 递归处理:以head.next为下标1开始,反转从left-1到right-1区间的链表,返回反转链表的头结点
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head

    # 从head节点开始,反转n个节点,返回旋转链表的头结点
    def reverseN(self, head, n):
        # behind指针用于记录第n+1个节点,也就是第n个节点的后驱节点,链表反转后需要将其与反转链表链接
        self.behind = None
        # base case:当只有一个元素时,不需要反转
        if n == 1:
            self.behind = head.next
            return head
        # 递归操作:反转从head.next开始的n-1个元素
        last = self.reverseN(head.next, n-1)
        # 将head节点连接到子反转节点的尾部
        head.next.next = head
        # 将head.next指向没有反转的节点的头部，即第n+1个节点
        head.next = self.behind
        return last