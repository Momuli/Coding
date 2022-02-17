class Solution(object):
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_l_r = list(str(x))
        x_l_r.reverse()
        x_l = list(str(x))
        return x_l == x_l_r

    def isPalindrome2(self, x):
        return str(x) == str(x)[::-1]

    def isPalindrome3(self, x):
        l = len(str(x))
        mid = l // 2
        return str(x)[:mid] == str(x)[-1:-mid-1:-1]

    def isPalindrome4(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        r_num = 0
        while x > r_num:
            r_num = r_num * 10 + x % 10
            x = x // 10

        return x == r_num or x == r_num // 10

if __name__ == '__main__':
    n = 12321
    rel = Solution().isPalindrome4(n)
    print(rel)