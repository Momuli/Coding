class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 定义滑动窗口的左右边界
        left = right = 0
        needs = dict()
        windows = dict()
        valid = 0   # 表示滑动窗口是否包含needs中的所有字符
        for item in s1:
            windows[item] = 0
            if item in needs:
                needs[item] += 1
            else:
                needs[item] = 1
        while right < len(s2):
            cur = s2[right]  # 当前元素
            right += 1
            if cur in needs:
                windows[cur] += 1
                if windows[cur] == needs[cur]:
                    valid += 1
            else:
                if cur in windows:
                    windows[cur] += 1
                else:
                    windows[cur] = 1
            while valid == len(needs):
                if windows == needs:
                    return True
                pop_item = s2[left]
                left += 1
                if pop_item in needs:
                    windows[pop_item] -= 1
                    if windows[pop_item] < needs[pop_item]:
                        valid -= 1
                else:
                    windows[pop_item] -= 1
                    if windows[pop_item] == 0:
                        del windows[pop_item]
        return False

if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    rel = Solution().checkInclusion(s1, s2)
    print(rel)