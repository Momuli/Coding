class Solution(object):
    # 哈希表
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}
        for item in nums:
            if item in hash_map:
                hash_map[item] += 1
            else:
                hash_map[item] = 1
        for item in nums:
            if hash_map[item] == 1:
                return item
            else:
                continue

    # 状态机
    def singleNumber2(self, nums):
        twos = 0
        ones = 0
        for item in nums:
            ones = ones ^ item & ~twos
            twos = twos ^ item & ~ones
        return ones

    # 按二进制位对3取余,不为0的位组成rel
    def singleNumber3(self, nums):
        temp = [0 for _ in range(32)]
        for item in nums:
            for i in range(len(temp)):
                temp[i] += item & 1
                item >>= 1
        for i in range(len(temp)):
            temp[i] = str(temp[i] % 3)
        return int(''.join(temp)[::-1], 2)


if __name__ == '__main__':
    nums = [3, 4, 3, 3]
    rel = Solution().singleNumber3(nums)
    print(rel)