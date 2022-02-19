# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 如果是空链表或者链表中只含一个元素,那么一定不存在环
        if not head or not head.next:
            return
        slow = fast = head  # 定义快慢指针
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next   # 这里是为什么while判断时要加fast.next的原因
            if slow == fast:   # 到达相遇点
                break
        # 当因为fast or fast.next 为空退出循换时,证明链表无环
        if not fast or not fast.next:
            return
        # 否则，因为 slow == fast 退出循换, 此时到达相遇点
        else:
            slow = head   # 将slow重新直向head, fast和slow指针同时前进k-m步到达环起点
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

