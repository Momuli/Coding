class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return
        dummy = ListNode()  # 定义虚拟节点,以防删除的是最后一个元素时,出现slow.next.next不存在的问题
        dummy.next = head
        slow = fast = dummy
        # 让fast先走n步
        for _ in range(n):
            if fast:
                fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
