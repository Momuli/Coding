# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        slow = fast = head
        # 当fast走到终点时，slow到达终点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow