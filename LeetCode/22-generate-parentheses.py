###############################################################################################
# 简单dfs应用
###########
# 时间复杂度：O(2^n)，最多不超过2^n，实际上达不到，n是有多少对括号
# 空间复杂度：O(n)，记录一种组合就得消耗n
###############################################################################################
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        conb, res = [], []
        def dfs(l, r):
            if l == 0 and r == 0:
                res.append(''.join(conb))
                return
            
            if l:
                l -= 1
                conb.append('(')
                dfs(l, r)
                l += 1
                conb.pop()
            
            if r and r > l: # 避免 ) 放前面了
                r -= 1
                conb.append(')')
                dfs(l, r)
                r += 1
                conb.pop()
        
        dfs(n, n)
        return res