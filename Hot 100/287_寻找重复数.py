# 题目已知一定存在重复数
# 相当于链表中一定存在环，需要找到换入口
# 根据索引->值的映射，就可以得到一条链表
# 思想与求链表环入口一致
class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0
        # slow走一步
        slow = nums[slow]
        # fast走两步
        fast = nums[nums[fast]]
        # 寻找相遇点
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # 退回链表头部
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

nums = [3, 1, 3, 4, 2]
rel = Solution().findDuplicate(nums)
print(rel)
