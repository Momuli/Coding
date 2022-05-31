# 记录出现最多次的任务的次数max_val
# 需要的最少时间为:(max_val-1)*(n+1)
# 如果最多的任务次数出现不止一次，再加上最多任务出现的次数
# T = （max_val-1)*(n+1)+count
class Solution:
    def leastInterval(self, tasks, n):
        # 记录每个任务出现的总次数
        hash_dict = {}
        for item in tasks:
            if item in hash_dict:
                hash_dict[item] += 1
            else:
                hash_dict[item] = 1
        val = list(hash_dict.values())
        max_val = max(val)
        # 时间
        T = (max_val - 1) * (n + 1) + val.count(max_val)
        if T > len(tasks):
            return T
        else:
            return len(tasks)