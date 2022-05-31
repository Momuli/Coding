# 逆序遍历+维护降序单调栈
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = [0] * len(nums1)
        que = []
        for i in range(len(nums2)-1, -1, -1):
            while que and que[-1] < nums2[i]:
                que.pop()
            if nums2[i] in nums1:
                if que:
                    res[nums1.index(nums2[i])] = que[-1]
                else:
                    res[nums1.index(nums2[i])] = -1
            que.append(nums2[i])
        return res