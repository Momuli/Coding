class Solution:
    def minmumNumberOfHost(self , n , startEnd ):
        start = []
        end = []
        for item in startEnd:
            start.append(item[0])
            end.append(item[1])
        start.sort()
        end.sort()
        res = 0   # 主持人个数
        idx = 0  # 当前最小结束时间的索引
        for i in range(len(start)):
            if start[i] >= end[idx]:
                idx += 1
            else:
                res += 1
        return res