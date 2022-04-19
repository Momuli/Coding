from collections import defaultdict, OrderedDict
class Solution:
    def LFU(self , operators, k):
        # write code here
        self.capacity = k
        # {频率1:{key:value, ...}， 频率2:{key:value, ...}}
        self.freq_to_kv = defaultdict(OrderedDict)
        # {key1:频率1, key2:频率2, ...}
        self.key_to_freq = {}
        self.min_freq = 0
        self.res = []
        for opt in operators:
            if opt[0] == 1:
                self.set(opt[1], opt[2])
            else:
                value = self.get(opt[1])
                self.res.append(value)
        return self.res
    def set(self, key, value):
        if self.capacity == 0:
            return
        # key已经存在
        if key in self.key_to_freq:
            key_freq = self.key_to_freq[key]  # key当前被使用的频率
            self.freq_to_kv[key_freq].pop(key)   # 将key从原本的freq对应的dict中删除
            # 如果当前key的使用频率是使用频率为key_freq的dict中的最后一个元素
            # 并且key_freq == self.min_freq,那么self.min_freq+1
            if not self.freq_to_kv[key_freq] and key_freq == self.min_freq:
                self.min_freq += 1
            # 将(key.value)的使用频率+1并存放在key_freq+1对应的dict中
            self.freq_to_kv[key_freq+1][key] = value
            # key的使用频率+1
            self.key_to_freq[key] = key_freq + 1
        # key不存在
        else:
            # 超出容量需要删除
            if len(self.key_to_freq) == self.capacity:
                # 弹出使用频率最少的且最久没有被使用的(key, value)
                item, v = self.freq_to_kv[self.min_freq].popitem(last=False)
                del self.key_to_freq[item]
            self.key_to_freq[key] = 1
            self.freq_to_kv[1][key] = value
            self.min_freq = 1
    def get(self, key):
        if key not in self.key_to_freq:
            return -1
        key_freq = self.key_to_freq[key]
        value = self.freq_to_kv[key_freq][key]
        self.freq_to_kv[key_freq].pop(key)
        if not self.freq_to_kv[key_freq] and key_freq == self.min_freq:
            self.min_freq += 1
        self.freq_to_kv[key_freq+1][key] = value
        self.key_to_freq[key] = key_freq+1
        return value


if __name__ == '__main__':
    num = [[1,1,1],[1,2,2],[1,3,2],[1,2,4],[1,3,5],[2,2],[1,4,4],[2,1]]
    k = 3
    rel = Solution().LFU(num, k)
    print(rel)