class Solution:
    def restoreIpAddresses(self, s):
        res = []
        self.recur(s, 0, 0, '', res)
        return res
    def recur(self, s, start_idx, depth, path, res):
        if depth == 3 and self.isValidIP(s[start_idx:]):
            res.append(path+s[start_idx:])
            return
        elif depth == 3:
            return
        for i in range(start_idx+1, start_idx+4):
            cur_range = s[start_idx:i]
            if not self.isValidIP(cur_range):
                continue
            if i > len(s):
                continue
            new_path = path + cur_range + '.'
            self.recur(s, i, depth+1, new_path, res)
    def isValidIP(self, stri):
        if not stri:
            return False
        flag = True
        if int(stri) > 255:
            flag = False
        if len(stri) > 1 and stri[0] == '0':
            flag = False
        return flag

if __name__ == '__main__':
    s = "25525522135"
    rel = Solution().restoreIpAddresses(s)
    print(rel)