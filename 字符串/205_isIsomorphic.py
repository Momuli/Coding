class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        flag = True
        if len(s) != len(t):
            flag = False
        else:
            hash_dict_s = {}
            hash_dict_t = {}
            for i in range(len(s)):
                if s[i] not in hash_dict_s:
                    hash_dict_s[s[i]] = t[i]
                if t[i] not in hash_dict_t:
                    hash_dict_t[t[i]] = s[i]
                if hash_dict_s[s[i]] != t[i] or hash_dict_t[t[i]] != s[i]:
                    flag = False
                    break
        return flag

if __name__ == '__main__':
    s = 'paper'
    t = 'title'
    rel = Solution().isIsomorphic(s, t)
    print(rel)