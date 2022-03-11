import collections
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # 定义栈
        stack = collections.deque()
        j = 0  # 指向popped索引
        for item in pushed:
            # 栈中压入元素
            stack.append(item)
            # 判断栈头元素是不是popped的首元素
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1   # 元素匹配成功,索引后移一位
        return j == len(popped)

if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 1, 2]
    rel = Solution().validateStackSequences(pushed, popped)
    print(rel)
