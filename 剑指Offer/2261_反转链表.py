# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 需要遍历两遍:将head链表中的元素放入数组res,再将res元素倒叙弹出,重组成链表
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 定义伪头结点
        dummy = ListNode(0)
        res = []
        while head:
            res.append(head.val)
            head = head.next
        q = dummy
        while res:
            q.next = ListNode(res.pop())
            q = q.next
        return dummy.next

    def reverseList2(self, head):
        # 只包含一个节点
        if not head or not head.next:
            return head
        # 函数的作用是返回反转链表的头结点
        last = self.reverseList2(head.next)    # 处理除去头结点的子链表,返回反转后的子链表的头结点
        head.next.next = head   # 将头结点加在反转子链表的最后一个元素后面
        head.next = None  # 尾结点指向空指针
        return last   # 返回子链表的头结点last