class Solution:
    def isPalindrome(self , x):
        if x < 0:
            return False
        if x == 0:
            return True
        reverse = 0
        while x > reverse:
            tmp = x % 10
            reverse = reverse * 10 + tmp
            x = x // 10
        return x == reverse or x == reverse // 10

if __name__ == '__main__':
    num = 122
    rel = Solution().isPalindrome(num)
    print(rel)