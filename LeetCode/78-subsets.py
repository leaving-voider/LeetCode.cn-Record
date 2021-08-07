###############################################################################################
# 数据小，直接暴搜
###########
# 时间复杂度：O(n*(2^n))，每个数都有选或不选两种，每种可能最后还要加入res，又是O(n)
# 空间复杂度：O(n)，存当前选择
###############################################################################################
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        len_ = len(nums)
        res, path = [], []
        def dfs(u):
            if u == len_:
                res.append([per for per in path])
                return
            
            path.append(nums[u])
            dfs(u+1) # 选
            path.pop()
            dfs(u+1) # 不选
        
        dfs(0)
        return res