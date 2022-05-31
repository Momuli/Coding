# 从后向前遍历,找到第一个相邻的升序数对(i,j)
# 在子数组[j:end]中逆序遍历，找到第一个比nums[i]大的数字nums[k]
# 将nums[k]与num[i]进行调换
# 将子数组[j:end]进行升序排列
# 返回整个数组

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        right = len(nums) - 1
        while right > 0:
            if nums[right] <= nums[right-1]:
                right -= 1
                continue
            else:
                cur = right-1
                temp = right
                for i in range(len(nums)-1, right, -1):
                    temp = i
                    if nums[i] > nums[cur]:
                        break
                nums[temp], nums[cur] = nums[cur], nums[temp]
                nums[:] = nums[:right] + nums[right:][::-1]
                return nums
        nums[:] = nums[::-1]
        return nums

nums = [1, 2, 3, 4, 6, 5]
rel = Solution().nextPermutation(nums)
print(rel)
