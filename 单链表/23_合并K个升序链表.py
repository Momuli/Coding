import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        cur = res = ListNode()  # 合并列表的伪头结点
        min_heap = []    # 定义优先级列表  最小堆
        # 将所有单链表的所有节点元素的值压入min_heap
        for item in lists:   # item是链表头结点
            if item:
                heapq.heappush(min_heap, item.val)  # 将节点的值压入队列
                item = item.next
        while min_heap:
            cur.next = ListNode(heapq.heappop(min_heap))  # 每次弹出最小值
            cur = cur.next
        return res




