class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 递归函数
        def board_find(i, j, k):
            # base case
            # 索引越界
            if i < 0 or i >= len(board):
                return False
            if j < 0 or j >= len(board[0]):
                return False
            if board[i][j] != word[k]:
                return False
            # 此时board[i][j]==word[k],并且word[k]是word中的最后一个元素
            if k == len(word) - 1:
                return True
            board[i][j] = ' '   # 防止重复遍历
            # 递归操作:匹配word的下一个字符
            res = board_find(i-1, j, k+1) or board_find(i+1, j, k+1) or \
                  board_find(i, j+1, k+1) or board_find(i, j-1, k+1)
            # 撤销选择
            board[i][j] = word[k]
            return res
        # 遍历矩阵中的元素,寻找到与word[0]匹配的元素,再递归处理word中的其他字符
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board_find(i, j, 0):
                    return True
        return False

if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    rel = Solution().exist(board, word)
    print(rel)




