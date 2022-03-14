class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []   # 存储所有排列结果
        path = []   # 存储当前排列结果
        vis = [0 for _ in range(len(s))]  # 标记
        S = sorted(list(s))   # 排序
        # 固定第cur个位置的元素
        def recur(cur):
            if cur == len(S):
                res.append(''.join(path))
            for i in range(len(S)):
                if vis[i] == 1 or i > 0 and not vis[i-1] and S[i] == S[i-1]:
                    continue
                vis[i] = 1
                path.append(S[i])
                # 递归处理第cur+1位置
                recur(cur+1)
                # 撤销选择
                vis[i] = 0
                path.pop()
        recur(0)
        return res

if __name__ == '__main__':
    s = 'aab'
    rel = Solution().permutation(s)
    print(rel)