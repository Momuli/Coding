class Solution(object):
    # 摩尔消除法
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vote = 0
        for item in nums:
            if vote == 0:
                x = item
            if item == x:
                vote += 1
            else:
                vote -= 1
        return x
    # 快速排序法
    def majorityElement2(self, nums):
        sort_num = self.Qsort(nums)
        return sort_num[len(sort_num)//2]
    def Qsort(self, nums):
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        cur = nums[mid]
        del nums[mid]
        left = []
        right = []
        for item in nums:
            if item < cur:
                left.append(item)
            else:
                right.append(item)
        return self.Qsort(left) + [cur] + self.Qsort(right)


if __name__ == '__main__':
    nums = [4, 9, 6, 3, 8, 5, 4, 4, 4, 4]
    rel = Solution().majorityElement2(nums)
    print(rel)