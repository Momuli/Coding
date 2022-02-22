class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str    s = "ADOBECODEBANC"
        :type t: str    t = "ABC"
        :rtype: str
        """
        windows = dict()   # 记录滑动窗口中指定元素的个数
        needs = dict()   # 记录模板子串中每个字符的个数
        # needs:{'A':1, 'B':1, 'C':1}
        for item in t:
            windows[item] = 0
            if item in needs:
                needs[item] += 1
            else:
                needs[item] = 1
        # 定义滑动窗口的左右指针
        left = right = 0
        valid = 0   # 标识windows与needs中已经满足匹配条件的字符个数
        start = 0   # 最终结果的开始索引
        end = len(s)+6  # 最终结果的结束索引
        # 滑动窗口算法
        # 增大窗口
        while right < len(s):
            cur = s[right]   # right当前指示的元素
            right += 1
            if cur in needs:
                windows[cur] += 1
                # 当windows中cur的个数与needs中要求的cur的个数相等时,valid+1
                if needs[cur] == windows[cur]:
                    valid += 1

            # 当滑动窗口中已经包含模板子串t的所有字符时,已经得到一个可行解,对该可行解进行优化
            while valid == len(needs):
                # 更新最终结果的索引位置
                if right - left <= end - start:
                    end = right
                    start = left
                pop_item = s[left]   # 缩小窗口弹出的元素
                left += 1
                # 如果弹出的是模板子串t中的字符
                if pop_item in needs:
                    if pop_item in windows:
                        windows[pop_item] -= 1
                        if windows[pop_item] < needs[pop_item]:
                            valid -= 1
        return '' if end == len(s)+6 else s[start:end]

if __name__ == '__main__':
    s = "A"
    t = "AQ"
    rel = Solution().minWindow(s, t)
    print(rel)