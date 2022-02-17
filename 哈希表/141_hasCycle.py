# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        else:
            fast = head.next  # 快指针
            slow = head  # 慢指针
            while slow != fast:
                if fast == None or fast.next == None:
                    return False
                else:
                    fast = fast.next.next
                    slow = slow.next
        return True

    def hasCycle2(self, head):
        if head == None or head.next == None:
            return False
        hash_l = []
        p = head
        while p:
            if p not in hash_l:
                hash_l.append(p)
                p = p.next
            else:
                return True
        return False




