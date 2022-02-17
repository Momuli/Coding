# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reversePrint1(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res = []
        while head:
            res.extend([head.val])
            head = head.next
        return res[::-1]

    def reversePrint2(self, head):
        if not head:
            return []
        return self.reversePrint2(head.next)+[head.val]
