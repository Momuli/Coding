import heapq
class Solution(object):
    # 堆排序
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        list = []
        for item in nums:
            heapq.heappush(list, item)
            if len(list) > k:
                heapq.heappop(list)
        return heapq.heappop(list)

    # 快速排序
    def findKthLargest2(self, nums, k):
        res = self.Quicksort(nums)
        return res[-k]

    def Quicksort(self, nums):
        if len(nums) < 2:
            return nums
        # 以nums的中间元素作为基准
        pivot = nums[len(nums)//2]
        del nums[len(nums)//2]
        nums_left = []   # 存放比pivot小的元素
        nums_right = []  # 存放比pivot大的元素
        for item in nums:
            if item >= pivot:
                nums_right.append(item)
            else:
                nums_left.append(item)
        return self.Quicksort(nums_left) + [pivot] + self.Quicksort(nums_right)
if __name__ == '__main__':
    nums = [4, 9, 6, 3, 8, 5]
    k = 2
    rel = Solution().findKthLargest2(nums, k)
    print(rel)