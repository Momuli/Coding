class Solution(object):
    def replaceSpace1(self, s):
        return s.replace(' ', '%20')

    def replaceSpace2(self, s):
        l = list(s)
        for i in range(len(l)):
            if l[i] == ' ':
                l[i] = '%20'
        return ''.join(l)

if __name__ == '__main__':
    s = "We are happy."
    rel = Solution().replaceSpace2(s)
    print(rel)