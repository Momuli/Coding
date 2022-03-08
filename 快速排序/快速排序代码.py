# 快速排序
class Solution(object):
    # 主函数
    def Quicksort1(self, nums):
        self.Qsort(nums, 0, len(nums)-1)
        return nums

    # 核心函数
    # 对数组nums[low, high]进行快速排序
    def Qsort(self, nums, low, high):
        if low >= high:
            return
        # 通过交换元素构造分界点索引
        pivot = self.Partition(nums, low, high)
        # 现在nums[low, pivot-1]都小于nums[pivot]
        # nums[pivot+1, high]都大于nums[pivot]
        self.Qsort(nums, low, pivot-1)
        self.Qsort(nums, pivot+1, high)

    # 交换元素获得分界点索引pivot
    def Partition(self, nums, low, high):
        if low == high:
            return low
        p = nums[low]
        while low < high:
            while low < high and nums[high] >= p:
                high -= 1
            self.swap(nums, low, high)
            while low < high and nums[low] < p:
                low += 1
            # 因为p不在low的位置就在high的位置
            self.swap(nums, low, high)
        return low

    # 将nums[i]和nums[j]的顺序交换
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


    def Quicksort2(self, nums):
        # 当nums中只有一个元素,不用排序
        if len(nums) < 2:
            return nums
        # nums的中间元素作为基准
        pivot = nums[len(nums)//2]
        del nums[len(nums)//2]
        nums_left = []  # 记录比pivot小的元素
        nums_right = []  # 记录比pivot大的元素
        for item in nums:
            if item > pivot:
                nums_right.append(item)
            elif item <= pivot:
                nums_left.append(item)
        return self.Quicksort2(nums_left) + [pivot] + self.Quicksort2(nums_right)

if __name__ == '__main__':
    nums = [4, 9, 6, 3, 8, 5]
    rel = Solution().Quicksort2(nums)
    print(rel)