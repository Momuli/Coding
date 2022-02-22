class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0  # 记录最大长度
        windows = dict()
        left = right = 0
        while right < len(s):
            cur = s[right]
            right += 1
            # windows中不存在cur时
            if not cur in windows:
                windows[cur] = 1
                res = max(res, len(windows))
            # windows中已经存在cur
            else:
                windows[cur] += 1
            # 当存在重复字符时,缩小窗口
            while windows[cur] > 1:
                pop_item = s[left]
                left += 1
                windows[pop_item] -= 1
                if windows[pop_item] == 0:
                    del windows[pop_item]
        return res

if __name__ == '__main__':
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    rel = Solution().lengthOfLongestSubstring(s1)
    print(rel)