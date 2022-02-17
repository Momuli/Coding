class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_str = ""
        if strs == []:
            return common_str
        else:
            min_str = strs[0]
            for i in range(len(strs)):   # 找最短字符串
                if len(strs[i]) < len(min_str):
                    min_str = strs[i]
            flag = True    # 判断依据，flag=false时结束
            for j in range(len(min_str)):
                for k in range(len(strs)):
                    if strs[k][j] != min_str[j]:
                        flag = False
                        break
                if flag:
                    common_str += min_str[j]
        return common_str


if __name__ == '__main__':
    strs = ['', 'b']
    rel = Solution().longestCommonPrefix(strs)
    print(rel)

