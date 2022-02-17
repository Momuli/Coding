class Solution(object):
    def generate1(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        Total = []
        Total.append([1])
        if numRows == 1:
            return Total
        else:
            for i in range(1, numRows):
                arr_r = []
                arr_r.extend([1])
                j = 1
                while j < i:
                    arr_r.extend([Total[i-1][j-1]+Total[i-1][j]])
                    j += 1
                arr_r.extend([1])
                Total.append(arr_r)
            return Total

    def generate2(self, numRows):
        Total = []
        Total.append([1])
        for i in range(1, numRows):
            # arr_r = list(zip([0]+Total[i-1], Total[i-1]+[0]))
            # for j in range(len(arr_r)):
            #     arr_r[j] = arr_r[j][0]+arr_r[j][1]
            arr_r = [a+b for a, b in zip([0]+Total[i-1], Total[i-1]+[0])]
            Total.append(arr_r)
        return Total






if __name__ == '__main__':
    num = 10
    rel = Solution().generate2(num)
    print(rel)
