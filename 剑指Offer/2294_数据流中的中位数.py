from heapq import *
class MedianFinder1(object):
    # 使用一个小顶堆
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []   # 存储元素

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.A, num)

    def findMedian(self):
        """
        :rtype: float
        """
        len_A = len(self.A)   # 计算A的长度
        mid = len_A // 2 + 1
        # 如果为奇数
        if len_A % 2 == 1:
            return float(self.A[mid])
        # 如果为偶数
        if len_A % 2 == 0:
            return (self.A[mid] + self.A[mid-1]) / 2.0

class MedianFinder2(object):
    # 双堆
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []   # 存储较大的一半元素,小顶堆, m = n+1 (奇数)
        self.B = []     # 存储较小的一半元素,大顶堆
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.A) == len(self.B):
            heappush(self.A, -heappushpop(self.B, -num))
        else:
            heappush(self.B, -heappushpop(self.A, num))
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.A) == len(self.B):
            return float(self.A[0])
        else:
            return (self.A[0]-self.B[0]) / 2.0
