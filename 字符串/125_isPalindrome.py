class Solution(object):
    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_new = ''
        for i in range(len(s)):
            if s[i].isalnum():
                s_new = s_new + s[i].lower()
        j = 0   # 首指针
        k = len(s_new)-1  # 尾指针
        flag = True
        while j < k:
            if s_new[j] == s_new[k]:
                j += 1
                k -= 1
            else:
                flag = False
                break
        return flag

    def isPalindrome2(self, s):
        s_new = ''
        for i in range(len(s)):
            if s[i].isalnum():
                s_new += s[i].lower()
        mid = len(s_new) // 2
        if len(s_new) % 2:
            s1 = s_new[:mid]
            s2 = s_new[mid+1:]
        else:
            s1 = s_new[:mid]
            s2 = s_new[mid:]
        flag = True
        for i in range(mid):
            if ord(s1[i]) - ord(s2[mid-1-i]) != 0:
                flag = False
                break
        return flag


if __name__ == '__main__':
    s = ""
    rel = Solution().isPalindrome1(s)
    print(rel)