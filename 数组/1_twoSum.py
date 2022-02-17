class Solution(object):
    # 枚举法:O(n^2) 双层循环（类似于冒泡)
    def twoSum1(self, nums, target):
        re_idx = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):

                if nums[i]+nums[j] == target:
                    re_idx.append(i)
                    re_idx.append(j)
        return re_idx
    #
    def twoSum2(self, nums, target):
        re_idx = []
        diff_dict = []
        for i in range(len(nums)):
            # diff_dict[str(target-nums[i])] = i
            if ((nums[i] in diff_dict)):
                re_idx.append(diff_dict.index(nums[i]))
                re_idx.append(i)
            diff_dict.append(target - nums[i])
        return re_idx



if __name__  ==  "__main__" :
    nums = [2,5,5,11]
    target = 10
    rel = Solution().twoSum2(nums, target)
    print(rel)