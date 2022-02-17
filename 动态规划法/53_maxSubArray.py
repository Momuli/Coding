class Solution(object):
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        pre_sum = 0
        for i in range(len(nums)):
            if pre_sum <= 0:
                now_sum = nums[i]
            else:
                now_sum = pre_sum + nums[i]
            if max_sum < now_sum:
                max_sum = now_sum
            pre_sum = now_sum
        return max_sum

    def maxSubArray2(self, nums):
        sum_list = [nums[0]]
        for i in range(1, len(nums)):
            if sum_list[-1] <= 0:
                sum_list.extend([nums[i]])
            else:
                sum_list.extend([nums[i] + sum_list[-1]])
        return max(sum_list)



if __name__ == '__main__':
    nums = [-1]
    rel = Solution().maxSubArray2(nums)
    print(rel)