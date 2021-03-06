class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 定义滑动窗口的左右指针
        left = right = 0
        # 当前字符串长度
        cur_len = 0
        # 最大字符串长度
        max_len = 0
        # 扩大窗口
        while right < len(s):
            cur = s[right]
            # right指向的元素不在s[left,right-1]子串中
            if cur not in s[left:right]:
                cur_len += 1
                right += 1
            else:
                # 缩小窗口,知道s[left:right]中不包含cur
                while cur in s[left:right]:
                    left += 1
                    cur_len -= 1
            max_len = max(max_len, cur_len)
        return max_len

    # 利用字典存储子串中不同字符法的个数
    def lengthOfLongestSubstring2(self, s):
        # 定义左右指针
        left = right = 0
        # 字典
        hash_table = dict()
        # 子串最大长度
        max_len = 0
        while right < len(s):
            cur = s[right]
            right += 1
            # cur不在字典中,即cur首次出现
            if cur not in hash_table:
                hash_table[cur] = 0
                max_len = max(max_len, right-left)
            else:
                # cur已经在字典中,cur重复出现
                hash_table[cur] += 1
                # 当子字符串中还包含cur时
                while hash_table[cur]:
                    if s[left] == cur:
                        hash_table[cur] -= 1
                    left += 1
        return max_len




if __name__ == '__main__':
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    rel = Solution().lengthOfLongestSubstring2(s1)
    print(rel)