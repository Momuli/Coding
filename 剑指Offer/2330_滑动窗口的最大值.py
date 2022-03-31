import collections
class Solution(object):
    def maxSlidingWindow1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return []
        res = []  # 存储结果
        max_deque = collections.deque()   # 存储最大值(降序排列)
        # 右边界right:[0,n-1]  左边界left:[0-k+1, n-1-k+1]=[1-k, n-k]
        # 若窗口右索引为j,则窗口左索引为[j-k+1]
        # 未形成完整窗口
        for i in range(k):
            while max_deque and max_deque[-1] < nums[i]:
                max_deque.pop()
            max_deque.append(nums[i])
        # 此时刚形成第一个窗口
        res.append(max_deque[0])
        for i in range(k, len(nums)):
            if max_deque[0] == nums[i-k]:   # nums[i-k]为刚弹出的元素  窗口范围:[i-k+1, i]
                max_deque.popleft()
            while max_deque and max_deque[-1] < nums[i]:
                max_deque.pop()
            max_deque.append(nums[i])
            res.append(max_deque[0])
        return res

    def maxSlidingWindow2(self, nums, k):
        if not nums or len(nums) == 0:
            return []
        res = []
        for i in range(0, len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res
if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    rel = Solution().maxSlidingWindow2(nums, k)
    print(rel)