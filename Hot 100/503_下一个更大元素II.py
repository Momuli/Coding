# 环形数组+数组扩展为2倍+取余
# 逆序遍历+维护降序单调栈
class Solution:
    def nextGreaterElements(self, nums):
        l = len(nums)
        res = [0] * l
        que = []
        for i in range(2*l-1, -1, -1):
            while que and que[-1] <= nums[i % l]:
                que.pop()
            res[i % l] = que[-1] if que else -1
            que.append(nums[i%l])
        return res