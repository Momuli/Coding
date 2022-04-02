import bisect
class Solution:
    def LIS(self , arr ):
        # write code here
        vec = []   # vex[i]表示长度为i的递增子序列的最后一个元素的最小值
        dp = [1] * len(arr)  # dp[i]表示以arr[i]结尾的最长递增子序列的长度
        for i in range(len(arr)):
            # 寻找元素arr[i]在vec中的位置
            # 如果vec中没有元素比arr[i]大,那么将arr[i]添加到vec的尾部
            # 如果vec中存在比arr[i]大的元素,利用arr[i]替换第一个比它大的元素
            # arr[i]对应的索引idx也就是以arr[i]结尾的最长上升子序列的长度
            # 如果arr[i]存在，返回arr[i]左侧的位置,若arr[i]不存在,返回arr[i]应该插入的位置
            idx = bisect.bisect_left(vec, arr[i])
            if idx >= len(vec):
                vec.append(arr[i])    # 如果vec中没有元素比arr[i]大,那么将arr[i]添加到vec的尾部
            else:
                vec[idx] = arr[i]  # 如果vec中存在比arr[i]大的元素,利用arr[i]替换第一个比它大的元素
            dp[i] = idx + 1
        max_len = max(dp)
        res = []
        for i in range(len(arr)-1, -1, -1):
            if dp[i] == max_len:
                res.append(arr[i])
                max_len -= 1
        return res[::-1]

if __name__ == '__main__':
    arr = [2,1,5,3,6,4,8,9,7]
    rel = Solution().LIS(arr)
    print(rel)