###############################################################################################
# 暴搜
###########
# 时间复杂度：O((m*n)*(3^L))，每个点为起点进行暴搜,L是字符串的长度，到达每个点，除了不能往回走，有3个方向可走
# 空间复杂度：O(m*n)，每个点都可能存入steped
###############################################################################################
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, len_ = len(board), len(board[0]), len(word)
        steped = set()
        def dfs(i, j, u):
            steped.add((i,j))
            if board[i][j] != word[u]:
                return False
            if u == len_-1:
                return True
            ret = 0
            if i - 1 >= 0 and (i-1, j) not in steped:
                ret |= dfs(i-1, j, u+1)
                steped.remove((i-1, j))
            if i + 1 < m and (i+1,j) not in steped:
                ret |= dfs(i+1, j, u+1)
                steped.remove((i+1, j))
            if j - 1 >= 0 and (i, j-1) not in steped:
                ret |= dfs(i, j-1, u+1)
                steped.remove((i, j-1))
            if j + 1 < n and (i, j+1) not in steped:
                ret |= dfs(i, j+1, u+1)
                steped.remove((i, j+1))
            return ret
        
        for i in range(m):
            for j in range(n):
                steped = set()
                if dfs(i, j, 0):
                    return True
        return False