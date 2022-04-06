class Solution:
    def topKstrings(self , strings , k ):
        hash = {}
        for item in strings:
            if item in hash:
                hash[item] += 1
            else:
                hash[item] = 1
        # 按照key进行排序
        # hash.items(): [(key1:val1), (key2, val2)...]
        hash = sorted(hash.items(), key=lambda x:x[0])
        # 按照val降序排序
        hash = sorted(hash, key=lambda x:x[1], reverse=True)
        if len(hash) > k:
            return hash[:k]
        else:
            return hash

if __name__ == '__main__':
    ss = ["a", "b", "c", "b"]
    k = 2
    rel = Solution().topKstrings(ss, k)
    print(rel)
