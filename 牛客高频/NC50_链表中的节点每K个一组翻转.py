# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # 将链表分为N/K组,每组分别进行反转,再链接到一起
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)   # 定义伪头结点指向链表头节点head
        dummy.next = head
        pre = dummy    # pre指向待反转链表的前驱(即已反转链表的最后一个元素)
        while head:
            end = pre   # end指向待反转链表的尾部元素
            for _ in range(k):
                end = end.next
                # 当最后剩余链表的长度不足k时
                if not end:
                    return dummy.next
            temp = end.next   # temp指向下一轮待反转链表的首个元素
            head, end = self.reverseK(head, end)  # 子链表反转,返回头部head和尾部end
            # 将反转链表与原链表拼接
            pre.next = head   # 前一轮的最后一个元素指向本轮已反转链表的头元素
            end.next = temp   # 本轮已反转链表的尾结点指向下一轮待反转链表的头结点
            pre = end   # 更新pre,使其指向已反转链表的尾部
            head = end.next  # head指向下一轮待反转链表的首个元素
        return dummy.next
    # 将链表中head-end区间的元素进行反转
    def reverseK(self, head, end):
        prev = end.next   # prev指向待反转链表的后继节点
        cur = head
        while prev != end:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return end, head