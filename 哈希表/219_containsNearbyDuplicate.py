class Solution(object):
    def containsNearbyDuplicate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_dict = {}
        for i in range(len(nums)):
            if nums[i] not in hash_dict.keys():
                hash_dict.update({nums[i]:i})
            else:
                if i-hash_dict.get(nums[i])<=k:
                    return True
                else:
                    hash_dict[nums[i]] = i
        return False

    def containsNearbyDuplicate2(self, nums, k):
        hash_l = []
        for i in range(len(nums)):
            if nums[i] not in hash_l:
                if len(hash_l) < k:
                    hash_l.extend([nums[i]])
                else:
                    del hash_l[0]
                    hash_l.extend([nums[i]])
            else:
                return True
        return False



if __name__ == '__main__':
    nums = [1,2,3,1]
    k = 3
    rel = Solution().containsNearbyDuplicate2(nums,k)
    print(rel)

