class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        sort_num = self.Qsort(nums)
        return ''.join(sort_num)

    def Qsort(self, nums):
        str_nums = [str(item) for item in nums]
        self.Quicksort(str_nums, 0, len(str_nums)-1)
        return str_nums

    def Quicksort(self, nums, low, high):
        if low >= high:
            return
        pivot = self.Partation(nums, low, high)
        self.Quicksort(nums, low, pivot-1)
        self.Quicksort(nums, pivot+1, high)

    def Partation(self, nums, low, high):
        if low == high:
            return low
        cur = nums[low]
        while low < high:
            while low < high and nums[high] + cur >= cur + nums[high]:
                high -= 1
            self.swap(nums, low, high)
            while low < high and nums[low] + cur < cur + nums[low]:
                low += 1
            self.swap(nums, low, high)
        return low
    def swap(self, nums, i, j):
        nums[i],nums[j] = nums[j], nums[i]

if __name__ == '__main__':
    nums = [3,30,34,5,9]
    rel = Solution().minNumber(nums)
    print(rel)