###############################################################################################
# 暴搜
###########
# 时间复杂度：O(p^q)，p是平均每个数出现的个数,q是数字种类
# 空间复杂度：O(q + logq), 存每种数字的个数 + 深搜栈消耗
###############################################################################################
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N, len_ = 35, len(candidates)
        
        res = []
        nums = [0]*N # 表示当前的选择，每个数对应的数量
        sums = 0 # 表示当前的选择之和

        def dfs(u):
            nonlocal sums
            if u == len_:
                if sums == target:
                    res.append([candidates[i] for i in range(len_) for _ in range(nums[i])]) # 高级列表生成式
                return
            
            for i in range(target//candidates[u]+1):
                if i*candidates[u] + sums <= target:
                    sums += i*candidates[u]
                    nums[u] = i 
                    dfs(u+1)
                    sums -= i*candidates[u]
                else: # 下一个更大，更不行（剪枝1）
                    break

        dfs(0)
        return res