class Solution(object):
    def permute(self, nums):
        res = []  # 用于存储所有路径
        track = []  # 用于当前每一条路径
        self.backtrack(nums, track, res)
        return res
    # 回溯函数   递归之前做选择，递归之后撤销选择
    def backtrack(self, nums, track, res):
        # 已选择一条完整路径  递归函数的base case
        if len(track) == len(nums):
            res.append(list(track))   # append方法添加的是track的内存地址
            return

        for item in nums:
            if item in track:
                continue
            track.append(item)  # 做选择
            self.backtrack(nums, track, res)  # 递归
            track.pop()   # 撤销选择

if __name__ == '__main__':
    nums = [1, 2, 3]
    rel = Solution().permute(nums)
    print(rel)




