class Solution(object):
    def merge1(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        if nums1.count(0) == m+n:
            nums1 = nums2
        elif len(nums2) != 0:
            while i < m and j < n:
                if nums1[i] < nums2[j]:
                    nums3.append(nums1[i])
                    i += 1
                else:
                    nums3.append(nums2[j])
                    j += 1
            while i < m:
                nums3.append(nums1[i])
                i += 1
            while j < n:
                nums3.append(nums2[j])
                j += 1
            nums1 = nums3
        return

    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if m > 0 and nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m = m-1
            else:
                nums1[n+m-1] = nums2[n-1]
                n = n-1


if __name__  ==  "__main__" :
    nums1 = [1,2,3,5,7,9,0,0,0, 0, 0]
    m = 6
    nums2 = [2,5,6,10,12]
    n = 5
    nums3 = []
    Solution().merge1(nums1, m, nums2, n)
    print(nums1)

