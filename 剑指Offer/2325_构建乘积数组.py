class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        left = [1 for _ in range(len(a))]   # 存储a[i]左边的乘积
        right = [1 for _ in range(len(a))]  # 存储a[i]右边的乘积
        # 计算left:下三角
        for i in range(1, len(left)):
            left[i] = left[i-1] * a[i-1]
        # 计算right:上三角
        for j in range(len(right)-2, -1, -1):
            right[j] = right[j+1] * a[j+1]
        # left * right
        res = []
        for k in range(len(a)):
            res.append(left[k] * right[k])
        return res

if __name__ == '__main__':
    a =  [1,2,3,4,5]
    rel = Solution().constructArr(a)
    print(rel)

