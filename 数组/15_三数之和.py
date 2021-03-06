class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 数组排序
        nums = sorted(nums)
        res = []    # 保存最终结果
        i = 0
        while i < len(nums):
            cur_num = nums[i]
            two_res = self.twoSum(nums, -cur_num, i+1)
            # 如果two_res不为空
            if two_res:
                for item in two_res:
                    item.append(nums[i])
                    res.append(item)
            # 去除重复的第一个元素
            while i < len(nums) and nums[i] == cur_num:
                i += 1
        return res

    # 返回和为target的两个数组成的元祖,不能重复
    def twoSum(self, nums, target, start):
        # 要除去第一个元素,因此左指针从start开始
        # 定义左右指针
        left = start
        right = len(nums)-1
        res = []
        while left < right:
            sum = nums[left] + nums[right]
            cur_left = nums[left]
            cur_right = nums[right]
            if sum < target:
                # 去除重复元素
                while left < right and nums[left] == cur_left:
                    left += 1
            elif sum > target:
                while left < right and nums[right] == cur_right:
                    right -= 1
            elif sum == target:
                res.append([nums[left], nums[right]])
                while left < right and nums[right] == cur_right:
                    right -= 1
                while left < right and nums[left] == cur_left:
                    left += 1
        return res

if __name__ == '__main__':
    num = [-1,0,1,2,-1,-4]
    target = 0
    rel = Solution().threeSum(num)
    print(rel)