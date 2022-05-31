# 前缀和
# 用哈希表记录和为sum的子数组的个数
# temp表示以第一个元素到当前元素的和
# 如果temp-K在哈希表中，那么表示存在一个中间子数组的和为K
# a0-ai的累和为temp-K,a0-aj的累和为temp,那么ai+1-aj的和为K
class Solution:
    def subarraySum(self, nums, k):
        # hash_dict[item]=val:累计和为item的子数组出现过val次
        hash_dict = {}
        temp = 0
        res = 0
        hash_dict[0] = 1
        for i in range(len(nums)):
            temp += nums[i]
            if temp - k in hash_dict:
                res += hash_dict[temp - k]
            if temp in hash_dict:
                hash_dict[temp] += 1
            else:
                hash_dict[temp] = 1
        return res

nums = [1, 1, 1]
k = 2
rel = Solution().subarraySum(nums, k)
print(rel)
