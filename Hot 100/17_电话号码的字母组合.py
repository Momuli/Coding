# 首先定义电话号码对应的字母列表
# 相当于从每个字符串取出一个数字进行组合，求总的组合数
# 回溯树的每一层都是一个新的选择列表
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        res = []
        cur = []
        temp = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        # start表示digits的索引,用于控制当前回溯树的层数，每一层都在一个新的字符串中选择一个元素
        def recur(start, l):
            if start == l:
                res.append(''.join(cur))
                return
            # 当前的选择列表
            strs = temp[int(digits[start])]
            for item in strs:
                cur.append(item)
                # 选择下一层的字母
                recur(start+1, l)
                cur.pop()
        recur(0, len(digits))
        return res

digit = '23'
rel = Solution().letterCombinations(digit)
print(rel)