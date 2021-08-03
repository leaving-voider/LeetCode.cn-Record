###############################################################################################
# 深搜
###########
# 时间复杂度：O(m^n)，m表示每个数字对应的字母个数，此题m≈3, n表示数字个数，这个时间复杂度就是暴搜
# 空间复杂度：O(n + logn), 每个数字替换成字母所用的存储 + 递归消耗
###############################################################################################
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        len_ = len(digits)
        if len_ == 0:
            return []
        rep = ['']*5
        res = []
        dic = {
            '1': "",
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        def dfs(u):
            if u == len_:
                res.append(''.join(rep))
                return
            
            for ch in dic[digits[u]]:
                rep[u] = ch
                dfs(u+1)
        dfs(0)
        return res