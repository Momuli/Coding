class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rel1 = rel2 = 0
        x = 0
        m = 1  # m用于找出rel1^rel2中为1的位置
        for item in nums:
            x ^= item  # 最终的 x= rel ^ rel2
        while x & m == 0:
            m <<= 1    # m左移一位
        for item in nums:
            if item & m ==0:
                rel1 ^= item
            else:
                rel2 ^= item
        return [rel1, rel2]

if __name__ == '__main__':
    nums = [4, 1, 4, 6]
    rel = Solution().singleNumbers(nums)
    print(rel)
