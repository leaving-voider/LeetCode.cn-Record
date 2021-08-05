###############################################################################################
# 简单DFS
###########
# 时间复杂度：O(n*n!)，第一个n是最后一层要遍历一次path，n!是最后一层的节点数，上层的可以忽略
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, st, path = [], [0]*n, []
        def dfs(u):
            if u == n:
                res.append([per for per in path])
                return
            
            for i in range(n):
                if not st[i]:
                    st[i] = 1
                    path.append(nums[i])
                    dfs(u+1)
                    st[i] = 0
                    path.pop()
        
        dfs(0)
        return res
