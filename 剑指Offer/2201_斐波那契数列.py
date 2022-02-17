class Solution(object):
    def fib1(self, n):
        """
        :type n: int
        :rtype: int
        """
        fibb = [0, 1]
        mod = 10**9+7
        for i in range(2, n+1):
            fibb.extend([fibb[i-1]+fibb[i-2]])
        return (fibb[n] % mod)

    def fib2(self, n):
        if n < 2:
            return n
        mod = 10**9+7
        p = 0
        q = 0
        r = 1
        for i in range(2, n+1):
            p = q
            q = r
            r = p+q
        return r % mod

    def fib3(self, n):
        mod = 10 ** 9 + 7
        # 矩阵乘法
        def Multi_matirx(A, B, s):
            rel_c = [[]]*s
            for i in range(len(rel_c)):
                rel_c[i] = [0]*s    # 初始化结果矩阵
            for i in range(s):
                for j in range(s):
                    for k in range(s):
                        rel_c[i][j] += A[i][k]*B[k][j]
                    rel_c[i][j] = rel_c[i][j] % mod
            return rel_c
        # 计算矩阵快速幂
        def matrix_pow(A, S, n):
            # 定义单位矩阵
            ans = [[]] * S
            for i in range(S):
                ans[i] = [0] * S
            for i in range(S):
                for j in range(S):
                    if i == j:
                        ans[i][j] = 1
            # 计算矩阵的幂
            while n:
                if n & 1:
                    ans = Multi_matirx(ans, A, 2)
                A = Multi_matirx(A, A, 2)
                n >>= 1   # 右移一位，当做二进制计算
            return ans

        if n < 2:
            return n
        else:
            M = [[1, 1], [1, 0]]
            res = matrix_pow(M, 2, n-1)
            print(res)
            return res[0][0]

if __name__ == "__main__":
    n = 5
    rel = Solution().fib3(n)
    print(rel)