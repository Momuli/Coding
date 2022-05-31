# 定义前缀树结构Node
# 前缀树包括:一个标记(是否是结束字符)+指向子节点位置的列表
# 前缀树结构
class Node():
    def __init__(self):
        # 是否是结束字符
        self.isEnd = False
        # 保存26个英文字母
        self.child = [None for _ in range(26)]
    # 是否包含key
    def contain_key(self, key):
        return self.child[ord(key)-ord('a')]
    # 返回key的值
    def get(self, key):
        return self.child[ord(key)-ord('a')]
    # 插入key
    def put(self, key):
        self.child[ord(key)-ord('a')] = Node()

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        p = self.root
        # 从word的第一个字符开始匹配
        for item in word:
            if not p.contain_key(item):
                p.put(item)
            p = p.get(item)
        # 表示一个单词插入结束
        p.isEnd = True

    def search(self, word: str) -> bool:
        p = self.root
        for item in word:
            if not p.contain_key(item):
                return False
            else:
                p = p.get(item)
        # 查找单词需要检查最后一个字符是否是结束符
        return p.isEnd

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for item in prefix:
            if not p.contain_key(item):
                return False
            else:
                p = p.get(item)
        # 检查前缀不需要
        return True