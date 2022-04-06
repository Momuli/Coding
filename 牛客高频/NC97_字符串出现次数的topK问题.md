## def topKstrings(self , strings , k ):
### 哈希表

**思路:**
1. 利用哈希表`hash`记录各个字符串出现次数
2. 对字符串`hash[key]`按照`ASCII`码升序排列
3. 再对`hash`中的各元素按照`hash[value]`值降序排列

**代码:**
```
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
```