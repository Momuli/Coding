import heapq
class Solution(object):
    def getLeastNumbers1(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        sort_arr = self.Qsort(arr)
        return sort_arr[:k]
    def Qsort(self, nums):
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        cur = nums[mid]
        del nums[mid]
        left = []
        right = []
        for item in nums:
            if item > cur:
                right.append(item)
            else:
                left.append(item)
        return self.Qsort(left) + [cur] + self.Qsort(right)

if __name__ == '__main__':
    arr = [3, 2, 1]
    k = 2
    rel = Solution().getLeastNumbers1(arr, k)
    print(rel)