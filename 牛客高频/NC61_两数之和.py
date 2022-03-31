class Solution(object):
    def twoSum(self, numbers, target):
        diff_dict = {}    # {'差值':索引}
        for i in range(len(numbers)):
            if numbers[i] in diff_dict:
                return [diff_dict[numbers[i]]+1, i+1]
            else:
                diff = target - numbers[i]
                diff_dict[diff] = i    # numbers[i]与target的差值为diff
        return []