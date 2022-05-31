# 将数组中的字符串升序排序重新,升序排序结果相同的为一组
class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return [['']]
        hash_dict = {}
        for item in strs:
            temp = ''.join(sorted(item))
            if temp in hash_dict:
                hash_dict[temp].append(item)
            else:
                hash_dict[temp] = [item]
        return list(hash_dict.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
rel = Solution().groupAnagrams(strs)
print(rel)
