# 贪心算法+先确定一个维度+再确定另一个维度
# 先按照身高降序排列+遇到身高相同的按照个数k升序排列
# 遍历一遍已排序好的people+以k为索引进行插入
class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x:(-x[0], x[1]))
        res = []
        for item in people:
            res.insert(item[1], item)
        return res

people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
rel = Solution().reconstructQueue(people)
print(rel)