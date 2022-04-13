class Solution:
    def minNumberDisappeared(self, nums):
        n = len(nums)   # nums中的正整数范围是1-n
        nums.append(-1)   # 原地哈希:使nums中取值为1-n的元素:元素与索引一一对应
        i = 0
        while i <= len(nums) - 1:
            # 使nums中取值为1-n的元素:元素与索引一一对应
            if nums[i] >= 1 and nums[i] <= n:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                if i == nums[i]:
                    i += 1
            # 非正整数忽略
            else:
                i += 1
        for j in range(1, len(nums)):
            if nums[j] < 1 or nums[j] > n:
                return j
        return len(nums)

if __name__ == '__main__':
    num = [4,5,6,8,9]
    rel = Solution().minNumberDisappeared(num)
    print(rel)