class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 分治法:归并排序
    def mergeKLists1(self, lists):
        # base case
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left_list = self.mergeKLists1(lists[:mid])
        right_list = self.mergeKLists1(lists[mid:])
        rel = self.Mergesort(left_list, right_list)
        return rel
    def Mergesort(selfself, left, right):
        if not left:
            return right
        if not right:
            return left
        dummy = temp = ListNode(0)
        while left and right:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        temp.next = left if left else right
        return dummy.next
    # 枚举
    def mergeKLists2(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        temp = []
        for item in lists:
            while item:
                temp.append(item.val)
                item = item.next
        temp = sorted(temp)
        dummy = p = ListNode(0)
        for i in range(len(temp)):
            p.next = ListNode(temp[i])
            p = p.next
        return dummy.next
