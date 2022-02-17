class Solution(object):
    def minAarry1(self, numbers):
        i = len(numbers)-1
        while i > 0:
            if numbers[i] - numbers[i-1] >= 0:
                i -= 1
            else:
                return numbers[i]
        return numbers[i]

    def minAarry2(self, numbers):
        i = 0
        j = len(numbers)-1
        while i < j:
            mid = (i + j) // 2
            if numbers[mid] > numbers[j]:
                i = mid + 1
            if numbers[mid] < numbers[j]:
                j = mid
            else:
                j -= 1
        return numbers[i]

if __name__ == '__main__':
    l = [3,4,5,2,3]
    rel = Solution().minAarry2(l)
    print(rel)